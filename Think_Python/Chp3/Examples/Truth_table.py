import ttg



"""
print(ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r']))
print(ttg.Truths(['p', 'q'], ['p and q', 'p or q', '(p or (~q)) => (~p)'], ints=False))

Operators and their representations:
negation: 'not', '-', '~'
logical disjunction: 'or'
logical nor: 'nor'
exclusive disjunction: 'xor', '!='
logical conjunction: 'and'
logical NAND: 'nand'
material implication: '=>', 'implies'
logical biconditional: '='
Note: Use parentheses! Especially with the negation operator.
(not(p and q))or r
"""

print(ttg.Truths(['p', 'q', 'r'],['(~(p and q))','(~(p and q))' ' or  r'],ints=False))
print(ttg.Truths(['p', 'q', 'r'],['(~(p and q))''or r'],ints=False))

