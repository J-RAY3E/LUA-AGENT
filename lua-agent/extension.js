const vscode = require('vscode');
const axios = require('axios');
const path = require('path');
const fs = require('fs');

const API_URL = 'http://127.0.0.1:5000';

function activate(context) {
    let panelProvider = vscode.commands.registerCommand('lua-agent.openPanel', () => {
        const panel = vscode.window.createWebviewPanel(
            'lua-agent', 'LUA-AGENT Panel', vscode.ViewColumn.Beside,
            { enableScripts: true, retainContextWhenHidden: true }
        );

        const htmlPath = path.join(context.extensionPath, 'webview.html');
        panel.webview.html = fs.readFileSync(htmlPath, 'utf8');

        panel.webview.onDidReceiveMessage(async (msg) => {
            try {
                if (msg.command === 'generate') {
                    const res = await axios.post(`${API_URL}/generate`, { prompt: msg.prompt });
                    panel.webview.postMessage({ type: 'showCode', code: res.data.code });
                } 
                else if (msg.command === 'validate') {
                    const res = await axios.post(`${API_URL}/validate`, { code: msg.code });
                    panel.webview.postMessage({ type: 'validationResult', valid: res.data.valid, cleanCode: res.data.clean_code });
                }
                else if (msg.command === 'search') {
                    const res = await axios.post(`${API_URL}/search`, { query: msg.query });
                    panel.webview.postMessage({ type: 'showResults', results: res.data.results });
                }
                else if (msg.command === 'insertCode') {
                    const editor = vscode.window.activeTextEditor;
                    if (editor) {
                        editor.edit(editBuilder => editBuilder.insert(editor.selection.active, msg.code));
                    }
                }
            } catch (err) {
                panel.webview.postMessage({ type: 'showError', error: err.message });
            }
        });
    });

    context.subscriptions.push(panelProvider);
}

module.exports = { activate, deactivate: () => {} };