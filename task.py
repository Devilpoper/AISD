class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

def solve(root:Node) -> bool:
    if root is None:
        return True
    if compare_high(root) is False:
        return False
    return solve(root.left) and solve(root.right)

def diff(root: Node):
    if root.right is None and root.left is None:
        return 99999999
    left_m, right_m = 9999999, 9999999
    if root.left is not None:
        left_m = min(abs(root.val - root.left.val), diff(root.left))

    if root.right is not None:
        right_m = min(abs(root.val - root.right.val), diff(root.right))

    return min(left_m, right_m)