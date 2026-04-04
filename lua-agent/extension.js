const vscode = require('vscode');
const axios = require('axios');

const API_URL = 'http://localhost:5000';

function activate(context) {
    console.log('LUA-AGENT VSCode extension activated');

    // Command 1: Generate Code
    let generateCode = vscode.commands.registerCommand('lua-agent.generateCode', async () => {
        const prompt = await vscode.window.showInputBox({
            prompt: 'Describe the Lua code you want',
            placeHolder: 'e.g., Create a function to read CSV files'
        });

        if (!prompt) return;

        vscode.window.showInformationMessage('Generating code with LUA-AGENT...');

        try {
            const response = await axios.post(`${API_URL}/generate`, {
                prompt: prompt,
                use_rag: true
            });

            if (response.data.status === 'success') {
                const code = response.data.code;
                
                const editor = vscode.window.activeTextEditor;
                if (editor) {
                    await editor.edit(editBuilder => {
                        editBuilder.insert(editor.selection.active, code + '\n');
                    });
                }
                
                vscode.window.showInformationMessage('✓ Code generated successfully!');
            } else {
                vscode.window.showErrorMessage(`Error: ${response.data.error}`);
            }

        } catch (error) {
            vscode.window.showErrorMessage(`Connection Error: Make sure backend is running on ${API_URL}\n${error.message}`);
        }
    });

    // Command 2: Search Libraries
    let searchLibraries = vscode.commands.registerCommand('lua-agent.searchLibraries', async () => {
        const query = await vscode.window.showInputBox({
            prompt: 'Search Lua libraries',
            placeHolder: 'e.g., CSV parsing, HTTP requests'
        });

        if (!query) return;

        try {
            const response = await axios.post(`${API_URL}/search`, {
                query: query,
                k: 5
            });

            if (response.data.status === 'success') {
                const results = response.data.results;
                
                const items = results.map(r => ({
                    label: `${r.library_name} (${r.similarity_score})`,
                    description: r.description.substring(0, 60) + '...',
                    detail: r.description
                }));

                const selected = await vscode.window.showQuickPick(items, {
                    placeHolder: 'Select a library'
                });

                if (selected) {
                    vscode.window.showInformationMessage(`Selected: ${selected.label}`);
                }
            }

        } catch (error) {
            vscode.window.showErrorMessage(`Error: ${error.message}`);
        }
    });

    // Command 3: Validate Code
    let validateCode = vscode.commands.registerCommand('lua-agent.validateCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No file is open');
            return;
        }

        try {
            const code = editor.document.getText();
            
            const response = await axios.post(`${API_URL}/validate`, {
                code: code
            });

            if (response.data.valid) {
                vscode.window.showInformationMessage('✓ Lua syntax is valid!');
                
                if (response.data.clean_code) {
                    await editor.edit(editBuilder => {
                        const fullRange = new vscode.Range(
                            editor.document.positionAt(0),
                            editor.document.positionAt(code.length)
                        );
                        editBuilder.replace(fullRange, response.data.clean_code);
                    });
                }
            } else {
                vscode.window.showErrorMessage('Lua syntax error!');
            }

        } catch (error) {
            vscode.window.showErrorMessage(`Error: ${error.message}`);
        }
    });

    context.subscriptions.push(generateCode, searchLibraries, validateCode);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};