class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height: int = 1


def height(root: Node) -> int:
    if root is None:
        return 0
    return root.height

def balance_factor(root: Node) -> int:
    return height(root.right) - height(root.left)

def fix_height(root: Node):
    root.height = max(height(root.left), height(root.right)) + 1

def right_rotate(root: Node) -> Node:
    tmp = root.left
    root.left = tmp.right
    tmp.right = root
    fix_height(root)
    fix_height(tmp)
    return tmp

def left_rotate(root: Node) -> Node:
    tmp = root.right
    root.right = tmp.left
    tmp.left = root
    fix_height(root)
    fix_height(tmp)
    return tmp

def balance(root: Node) -> Node:
    fix_height(root)
    if balance_factor(root) == -2:
        if balance_factor(root.left) > 0:
            root.left = left_rotate(root.left)
        return right_rotate(root)

    elif balance_factor(root) == 2:
        if balance_factor(root.right) < 0:
            root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def insert(val: int, root: Node) -> Node:
    if root is None:
        return Node(val)
    elif val < root.val:
        root.left = insert(val, root.left)
    else:
        root.right = insert(val, root.right)
    return balance(root)

def find_min(root):
    if root.left is None:
        return root
    return find_min(root.left)

def delete_min(root):
    if root.left is None:
        return root.right
    root.left = delete_min(root.left)
    return balance(root)

def delete_max(root):
    if root.right is None:
        return root.left
    root.right = delete_max(root.right)
    return balance(root)

def delete_value(val, root):
    if root is None:
        return None
    if val < root.val:
        root.left = delete_value(val, root.left)
    elif val > root.val:
        root.right = delete_value(val, root.right)
    else:
        l = root.left
        r = root.right
        if r is not None:
            min_node = find_min(r)
            min_node.right = delete_min(r)
            min_node.left = l
            return balance(min_node)
        else:
            return l
    return balance(root)

def get_high(root:Node):
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return 1
    high_l, high_r = 0, 0

    if root.left is not None:
        high_l = get_high(root.left)

    if root.right is not None:
        high_r = get_high(root.right)

    return max(high_r, high_l) + 1


def compare_high(root):
    if abs(get_high(root.left) - get_high(root.right)) > 1:
        return False
    return True

def check(root:Node) -> bool:
    if root is None:
        return True
    if compare_high(root) is False:
        return False
    return check(root.left) and check(root.right)

def print_tree(root: Node):
    if root is None:
        return
    print(f"root: {root.val}, ", end=" ")
    if root.left is not None:
        print(f"left_child - {root.left.val}")
    else:
        print(f"left_child - None")
    if root.right is not None:
        print(f"    right_child - {root.right.val}\n")
    else:
        print(f"    right_child - None\n")
    print_tree(root.left)
    print_tree(root.right)
