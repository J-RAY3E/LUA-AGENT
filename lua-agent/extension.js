const vscode = require('vscode');
const axios = require('axios');
const path = require('path');
const fs = require('fs');

const API_URL = 'http://127.0.0.1:5000';

function activate(context) {
    console.log('LUA-AGENT activated');

    let openPanel = vscode.commands.registerCommand('lua-agent.openPanel', () => {
        const panel = vscode.window.createWebviewPanel(
            'lua-agent',
            'LUA-AGENT',
            vscode.ViewColumn.Beside,
            { enableScripts: true, retainContextWhenHidden: true }
        );

        const webviewPath = path.join(context.extensionPath, 'webview.html');
        const html = fs.readFileSync(webviewPath, 'utf8');
        panel.webview.html = html;

        panel.webview.onDidReceiveMessage(async message => {
            switch(message.command) {
                case 'generate':
                    await handleGenerate(message.prompt, panel);
                    break;
                case 'search':
                    await handleSearch(message.query, panel);
                    break;
                case 'validate':
                    await handleValidate(message.code, panel);
                    break;
                case 'insertCode':
                    insertCodeToEditor(message.code);
                    break;
            }
        });
    });

    let quickGenerate = vscode.commands.registerCommand('lua-agent.generateCode', async () => {
        const prompt = await vscode.window.showInputBox({
            prompt: 'Describe the Lua code you want',
            placeHolder: 'e.g., Create a function to read CSV files'
        });

        if (!prompt) return;

        vscode.window.showInformationMessage('Generating code...');
        
        try {
            const response = await axios.post(`${API_URL}/generate`, {
                prompt: prompt,
                use_rag: true
            });

            insertCodeToEditor(response.data.code);
            vscode.window.showInformationMessage('✓ Code generated!');
        } catch (error) {
            vscode.window.showErrorMessage(`Error: ${error.message}`);
        }
    });

    context.subscriptions.push(openPanel, quickGenerate);
}

async function handleGenerate(prompt, panel) {
    try {
        const response = await axios.post(`${API_URL}/generate`, {
            prompt: prompt,
            use_rag: true
        });

        panel.webview.postMessage({
            type: 'showCode',
            code: response.data.code,
            libraries: response.data.libraries
        });

    } catch (error) {
        panel.webview.postMessage({
            type: 'showError',
            error: error.message
        });
    }
}

async function handleSearch(query, panel) {
    try {
        const response = await axios.post(`${API_URL}/search`, {
            query: query,
            k: 5
        });

        panel.webview.postMessage({
            type: 'showResults',
            results: response.data.results
        });

    } catch (error) {
        panel.webview.postMessage({
            type: 'showError',
            error: error.message
        });
    }
}

async function handleValidate(code, panel) {
    try {
        const response = await axios.post(`${API_URL}/validate`, {
            code: code
        });

        panel.webview.postMessage({
            type: 'validationResult',
            valid: response.data.valid,
            cleanCode: response.data.clean_code
        });

    } catch (error) {
        panel.webview.postMessage({
            type: 'showError',
            error: error.message
        });
    }
}

function insertCodeToEditor(code) {
    const editor = vscode.window.activeTextEditor;
    if (editor) {
        editor.edit(editBuilder => {
            editBuilder.insert(editor.selection.active, code + '\n');
        });
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};