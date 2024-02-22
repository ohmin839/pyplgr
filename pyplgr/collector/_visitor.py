from parsimonious.nodes import NodeVisitor

class Visitor(NodeVisitor):
    def visit_words(self, node, visited_children):
        return [v for v, *_ in visited_children if isinstance(v, str)]

    def visit_word(self, node, visited_children):
        alphabet_node, apos_node = node.children

        alphabet = ''.join([n.text for n in alphabet_node])
        if apos_node.children:
            apostroph = apos_node.children[0].text
            return alphabet + apostroph
        else:
            return alphabet

    def generic_visit(self, node, visited_children):
        return visited_children or node
