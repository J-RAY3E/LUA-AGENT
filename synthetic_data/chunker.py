import re

try:
    from luaparser import ast as lua_ast
    from luaparser import astnodes
    HAVE_LUAPARSER = True
except ImportError:
    HAVE_LUAPARSER = False
    print("Warning: luaparser is not installed. Using Regex Fallback only.")

def chunk_lua_code(lua_code):
    """
    Takes a raw Lua code string and chunks it into meaningful blocks (functions).
    If luaparser fails (e.g., Luau specific syntax like static typing which breaks standard Lua AST),
    it falls back to basic regex heuristics.
    """
    if HAVE_LUAPARSER:
        try:
            tree = lua_ast.parse(lua_code)
            chunks = []
            
            # luaparser doesn't provide exact source slices easily,
            # but we can extract line blocks
            lines = lua_code.split('\n')
            
            for node in lua_ast.walk(tree):
                if isinstance(node, (astnodes.Function, astnodes.LocalFunction)):
                    start_line = getattr(node, 'line', None)
                    end_line = getattr(node, 'last_line', None)
                    
                    if start_line is not None and end_line is not None:
                        # lua line numbers are 1-indexed
                        chunk_text = "\n".join(lines[start_line-1:end_line])
                        if len(chunk_text.strip()) > 10:
                            chunks.append(chunk_text)
            
            if chunks:
                return chunks
        except Exception:
            # Fallback to regex if parsing fails (common for Luau)
            pass
            
    return fallback_chunker(lua_code)

def fallback_chunker(lua_code):
    """Fallback chunker using Regex for basic blocks."""
    chunks = []
    # Match function ... end blocks roughly (not perfect for nested, but decent heuristic)
    pattern = re.compile(r'((?:local\s+)?function\s+(?:[a-zA-Z0-9_\.:]+)\s*\([^)]*\).*?^end)', re.MULTILINE | re.DOTALL)
    matches = pattern.findall(lua_code)
    for match in matches:
        if len(match.strip()) > 10:
            chunks.append(match.strip())
    
    # If no functions and small enough, consider the whole file a chunk
    if not chunks and len(lua_code) > 10 and len(lua_code) < 3000:
        return [lua_code.strip()]
        
    return chunks
