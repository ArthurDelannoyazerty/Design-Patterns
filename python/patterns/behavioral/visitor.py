from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class Node(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Visitor(ABC):
    @abstractmethod
    def visit_number_node(self, node):
        pass

    @abstractmethod
    def visit_add_node(self, node):
        pass

    @abstractmethod
    def visit_multiply_node(self, node):
        pass



# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# ----------------------------------- Data ----------------------------------- #
class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor:Visitor):
        return visitor.visit_number_node(self)

class AddNode(Node):
    def __init__(self, left:NumberNode, right:NumberNode):
        self.left = left
        self.right = right

    def accept(self, visitor:Visitor):
        return visitor.visit_add_node(self)

class MultiplyNode(Node):
    def __init__(self, left:NumberNode, right:NumberNode):
        self.left = left
        self.right = right

    def accept(self, visitor:Visitor):
        return visitor.visit_multiply_node(self)
    

# ---------------------------------- Visitor --------------------------------- #
class PythonCodeGenerator(Visitor):
    """
    A concrete visitor that generates Python code from the AST.
    """
    def visit_number_node(self, node:NumberNode):
        return str(node.value)

    def visit_add_node(self, node:AddNode):
        left_code = node.left.accept(self)
        right_code = node.right.accept(self)
        return f"({left_code} + {right_code})"

    def visit_multiply_node(self, node:MultiplyNode):
        left_code = node.left.accept(self)
        right_code = node.right.accept(self)
        return f"{left_code} * {right_code}"


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Let's represent the expression: (1 + 2) * 3
    ast = MultiplyNode(
        AddNode(NumberNode(1), NumberNode(2)),
        NumberNode(3)
    )

    python_visitor = PythonCodeGenerator()
    python_code = ast.accept(python_visitor)

    print(f"The generated Python code is: {python_code}")

    # We can even execute the generated code to verify it
    result = eval(python_code)
    print(f"The result of executing the code is: {result}")


# ---------------------------------- Output ---------------------------------- #
# The generated Python code is: (1 + 2) * 3
# The result of executing the code is: 9