
class AVLTreeNode:
    def __init__(self, value: float):
        self.__value = value
        self.__right = None
        self.__left = None
        self.__height = 1

    def update_height(self):
        self.height = 1 + max(get_height(self.left), get_height(self.right))

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def value(self) -> float:
        return self.__value

    @property
    def left(self) -> 'AVLTreeNode':
        return self.__left

    @left.setter
    def left(self, node: 'AVLTreeNode'):
        self.__left = node

    @property
    def right(self) -> 'AVLTreeNode':
        return self.__right

    @right.setter
    def right(self, node: 'AVLTreeNode'):
        self.__right = node


def insert(root: AVLTreeNode, value: float) -> AVLTreeNode:
    if root is None:
        return AVLTreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    root.update_height()

    balance = get_height(root.left) - get_height(root.right)
    if balance > 1:
        if value > root.left.value:
            root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1:
        if value < root.right.value:
            root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def right_rotate(root: AVLTreeNode) -> AVLTreeNode:
    left_child = root.left
    right_of_left_child = left_child.right

    left_child.right = root
    root.left = right_of_left_child

    root.update_height()
    left_child.update_height()

    return left_child


def left_rotate(root: AVLTreeNode) -> AVLTreeNode:
    right_child = root.right
    left_of_right_child = right_child.left

    right_child.left = root
    root.right = left_of_right_child

    root.update_height()
    right_child.update_height()

    return right_child


def get_height(node: AVLTreeNode) -> int:
    return 0 if node is None else node.height


def print_tree(node: AVLTreeNode, depth=0) -> None:
    if node is None:
        return
    print(" " + str(node.value))
    if node.left is not None:
        print(" " * 3 * (depth+1) + "l", end="")
        print_tree(node.left, depth + 1)
    if node.right is not None:
        print(" " * 3 * (depth + 1) + "r", end="")
        print_tree(node.right, depth + 1)
