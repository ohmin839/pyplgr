from ._grammar import grammar
from ._visitor import Visitor

def to_polytonic(text):
    tree = grammar.parse(text)
    visitor = Visitor()
    return visitor.visit(tree)