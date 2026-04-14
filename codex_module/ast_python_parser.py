import ast
import json

def validate_and_get_python_ast(python_code: str):
    """
    Parses raw Python code string into an Abstract Syntax Tree (AST),
    validates there are no syntax errors, and returns a dictionary/dump representation
    of the Python AST.
    """
    try:
        # Generate AST
        tree = ast.parse(python_code)
        
        # We can return the ast.dump which gives a string representation of the tree,
        # or we could construct a dict. For now, returning standard ast.dump.
        dumped_ast = ast.dump(tree, indent=2)
        return dumped_ast
        
    except SyntaxError as e:
        print(f"AST Parsing Error! The model generated invalid Python Syntax:\n{e}")
        return None
    except Exception as e:
        print(f"Unexpected AST Error:\n{e}")
        return None

if __name__ == "__main__":
    # Small test
    test_code = """
import csv
def load_data():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
"""
    
    print("Original Python Code:\n", test_code.strip())
    
    python_ast = validate_and_get_python_ast(test_code)
    print("\n--- Parsed Python AST ---\n")
    if python_ast:
        print(python_ast)
