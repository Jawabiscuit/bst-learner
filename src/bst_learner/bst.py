"""
"""
from typing import Optional

from graphviz import Digraph

from bst_learner.node import TreeNode


class BST:
    """Binary Search Tree"""

    def __init__(self):
        """Constructor"""
        self.root = None

    def insert(self, key):
        """Insert a node with the given key"""
        node = TreeNode(key)
        if self.root is None:
            self.root = node
        else:
            self.insert_node(self.root, node)

    def insert_node(self, root, node):
        """Insert a node into the tree"""
        while root is not None:
            if root.key > node.key:
                if root.left is None:
                    root.left = node
                    node.parent = root
                    return
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = node
                    node.parent = root
                    return
                else:
                    root = root.right

    def search(self, root, key):
        """Search for a node with the given key starting at the given root node"""
        if root is None or root.key == key:
            root.color = "red"
            return root
        elif root.key > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find(self, key):
        """Find a node with the given key, searching from root"""
        return self.search(self.root, key)

    def transplant(self, src, dest):
        """Replace subtree rooted at dest with subtree rooted at src. Used when deleting a node"""
        pass

    def delete(self, key):
        """Delete a node with the given key"""
        pass


def add_nodes_edges(node: Optional[TreeNode], dot: Digraph, parent_name: str = None) -> None:
    """Constructs a graphviz Digraph object from the given node

    Args:
        node (Optional[TreeNode]): The root node of the tree.
        graph (Digraph): The graphviz Digraph object to add nodes and edges to.
        parent_name (str, optional): The name of the parent node. Defaults to None.
    """
    if node is None:
        return
    node_name = str(node.key)
    dot.node(name=node_name, color=node.color, shape="circle")
    if parent_name:
        dot.edge(tail_name=parent_name, head_name=node_name)
    add_nodes_edges(node.left, dot, node_name)
    add_nodes_edges(node.right, dot, node_name)


def render_graph(filename: str, root: TreeNode, dot: Digraph) -> None:
    add_nodes_edges(root, dot)
    png = dot.pipe(format="png")
    with open(f"{filename}.png", "wb") as f:
        f.write(png)


if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(6)
    bst.insert(12)
    bst.insert(17)
    bst.insert(1)
    bst.insert(3)
    bst.insert(7)
    bst.insert(13)
    bst.insert(18)
    bst.insert(4)
    bst.insert(8)
    bst.insert(14)
    bst.insert(19)
    bst.insert(0)
    bst.insert(9)
    bst.insert(11)
    bst.insert(16)
    bst.insert(100)
    bst.insert(50)
    bst.insert(150)
    bst.insert(200)
    bst.insert(60)
    bst.insert(120)
    bst.insert(170)
    bst.insert(1000)
    bst.insert(500)

    dot = Digraph(comment="Binary Search Tree", strict=True)
    render_graph("bst", bst.root, dot)

    node = bst.find(100)
    if node is not None:
        print(f"Found node {node.key}")
        dot = Digraph(comment="Binary Search Tree Search Result", strict=True)
        render_graph("bst_search_result", node.parent, dot)
