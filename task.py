class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_node(root: Node, value: int) -> list:
    cur = root
    roots_list = []
    while cur.left is not None and cur.right is not None:
        if cur.val == value:
            roots_list.append(cur.val)
            return roots_list
        elif cur.val > value:
            roots_list.append(cur.val)
            cur = cur.left
        else:
            roots_list.append(cur.val)
            cur = cur.right

    if cur.val == value:
        roots_list.append(cur.val)
        return roots_list
    elif cur.val > value and cur.left is not None:
        roots_list.append(cur.val)
    elif cur.val < value and cur.right is not None:
        roots_list.append(cur.val)
    return roots_list

def solve(root: Node, p: int, q: int) -> int:
    p_roots = find_node(root, p)
    q_roots = find_node(root, q)
    roots_set = list(set(p_roots) & set(q_roots))
    return min(roots_set)


t1 = Node(14)
t2 = Node(48, left=t1)
t3 = Node(51)
t4 = Node(50, left=t2, right=t3)
t7 = Node(63)
t8 = Node(78)
t6 = Node(68, left=t7, right=t8)
t5 = Node(55, left = t4, right=t6)

print(solve(t5, 68, 51))