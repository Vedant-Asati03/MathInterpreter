from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class AdditionNode:
    node_a: any  # type: ignore
    node_b: any  # type: ignore

    def __repr__(self) -> str:
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any  # type: ignore
    node_b: any  # type: ignore

    def __repr__(self) -> str:
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any  # type: ignore
    node_b: any  # type: ignore

    def __repr__(self) -> str:
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any  # type: ignore
    node_b: any  # type: ignore

    def __repr__(self) -> str:
        return f"({self.node_a}/{self.node_b})"


@dataclass
class ExponentNode:
    node_a: any  # type: ignore
    node_b: any  # type: ignore

    def __repr__(self) -> str:
        return f"({self.node_a}**{self.node_b})"


# @dataclass
# class ModulusNode:
#     node: any

#     def __repr__(self) -> str:
#         return f"(|{self.node}|)"


@dataclass
class PlusNode:
    node: any  # type: ignore

    def __repr__(self) -> str:
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any  # type: ignore

    def __repr__(self) -> str:
        return f"(-{self.node})"
