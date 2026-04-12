import ast

code = """
#Is just a script
x = 10
import os
print(x);wer
2+1
import numpy as np
np.array([1,2])
"""

tree = ast.parse(code)
print(ast.dump(tree,indent=4))