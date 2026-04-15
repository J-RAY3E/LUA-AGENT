import sys
import os

# --- PATH CONFIGURATION ---
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from agents.coder import generate_code
from agents.validator import validate_and_reconstruct_lua
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.traceback import install

install(show_locals=False)

console = Console()

def main():
    # Header
    console.print("\n" + "=" * 60)
    console.print("[bold blue]🚀 LUA CODING AGENT - STARTUP SEQUENCE[/bold blue]")
    console.print("=" * 60)
    user_request = console.input("\n[bold yellow]Enter your request in English or Russian:[/bold yellow] ")
    
    if not user_request:
        console.print("[red]❌ Error: Request cannot be empty.[/red]")
        return

    console.print(f"\n[green]📝 Processing request:[/green] {user_request}")
    console.print("[dim]⏳ Agent is extracting keywords, searching local Wiki, and generating code...[/dim]")
    console.print("-" * 60)
    
    try:
        final_code = generate_code(user_request, plan_result=None, context_docs=None)
        
        if not final_code:
            console.print("\n[bold red]❌ Failed to generate code after multiple attempts.[/bold red]")
            return

        code_text = Text(final_code, style="white on black")
        panel = Panel(code_text, title="[bold green]✅ GENERATED CODE", border_style="green")
        console.print(panel)

        is_valid, error_msg =  validate_and_reconstruct_lua(final_code)
        
        if is_valid:
            console.print("\n[bold green]✅ FINAL VALIDATION SUCCESSFUL! Lua code is clean.[/bold green]")
            # Opsional: Simpan file
            # filename = f"output_{len(final_code)}.lua"
            # from agents.coder import save_code
            # path = save_code(final_code, filename)
            # console.print(f"[dim]💾 Code saved to: {path}[/dim]")
        else:
            console.print(f"\n[yellow]⚠️ WARNING: External validation failed.[/yellow]")
            console.print(f"[dim]Error Message: {error_msg}[/dim]")
            console.print("Although the model attempted corrections, there might be logical edge cases.")

    except Exception as e:
        console.print(f"\n[bold red]💥 Critical system error occurred:[/bold red] {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[dim]⏹️ Program stopped by user.[/dim]")
    except SystemExit:
        pass