from nodes import *
from values import Number


class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return NumberNode(node.value)

    def visit_VariableNode(self, node):
        return NumberNode(node.value)

    def visit_AdditionNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error!")
        
    def visit_ExponentNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
    
    # def visit_ModulusNode(self, node):
    #     return self.visit(node.node)

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
