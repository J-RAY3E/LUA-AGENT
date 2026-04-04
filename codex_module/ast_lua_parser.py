from luaparser import ast

def validate_and_reconstruct_lua(lua_code: str) -> str:
    """
    Parses the raw Lua code string into an Abstract Syntax Tree (AST),
    validates that there are no syntax errors, and then reconstructing 
    back into a clean Lua string, discarding any informal syntax logic.
    """
    try:
        # Generate AST
        tree = ast.parse(lua_code)
        
        # In a more advanced implementation, we could manipulate the tree here.
        # e.g. mapping library calls, validating variable names, expanding structures.
        
        # Convert AST back to Lua string
        clean_code = ast.to_lua_source(tree)
        return clean_code
        
    except Exception as e:
        print(f"AST Parsing Error! The model generated invalid Lua Syntax:\n{e}")
        return None

if __name__ == "__main__":
    # Small test
    test_code = """
local my_lib = require("my_lib")
function sum(a, b)
    return a + b
end
    """
    
    print("Original Node:\n", test_code.strip())
    
    clean_lua_ast = validate_and_reconstruct_lua(test_code)
    print("\n--- Parsed Reconstructed AST String ---\n")
    if clean_lua_ast:
        print(clean_lua_ast)
