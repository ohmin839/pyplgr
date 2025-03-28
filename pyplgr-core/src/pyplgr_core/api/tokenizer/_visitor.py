from parsimonious.nodes import NodeVisitor

class Visitor(NodeVisitor):
    def visit_tokens(self, node, visited_children):
        return [v for v, *_ in visited_children if v]

    def visit_word(self, node, visited_children):
        alphabet_node, apos_node = node.children

        alphabet = ''.join([n.text for n in alphabet_node])
        if apos_node.children:
            apostroph = apos_node.children[0].text
            return alphabet + apostroph
        else:
            return alphabet

    def visit_white_space(self, node, visited_children):
        return node.text.strip()

    def visit_any_char(self, node, visited_children):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node
