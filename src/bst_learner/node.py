from dataclasses import dataclass, field
from typing import Optional


@dataclass(slots=True)
class TreeNode:
    key: int = field(default=0)
    parent: Optional[int] = None
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    color: str = field(default="black", repr=False)


if __name__ == "__main__":
    t = TreeNode(1)
    print(t)
