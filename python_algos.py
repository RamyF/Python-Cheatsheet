import collections


def binary_search(list, target):
    l, r = 0, len(list) - 1

    while l <= r:
        mid = (r - l) // 2
        mid += l

        if list[mid] < target:
            l = mid + 1
        elif list[mid] > target:
            r = mid - 1
        else:
            return mid
    return None

# print(binary_search([0, 2, 5, 10, 11, 22, 31, 42, 50, 55, 61], 100))

# graphs / nodes

class BinaryNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def iterative_binary_tree_dfs(node):
    stack = [node]
    visited = set()
    
    while stack:
        visited.add(stack[-1])
        n = stack.pop()
        # process node
        print(n.val)
        stack.append(n.left) if n.left is not None else None
        stack.append(n.right) if n.right is not None else None

def iterative_binary_tree_bfs(node):
    q = collections.deque([node])
    visited = set()
    
    while q:
        visited.add(q[0])
        n = q.popleft()
        # process node
        print(n.val)
        q.append(n.left) if n.left is not None else None
        q.append(n.right) if n.right is not None else None

node3 = BinaryNode(10)
node4 = BinaryNode(21)
node1 = BinaryNode(20, node3, node4)
node5 = BinaryNode(27)
node6 = BinaryNode(40)
node2 = BinaryNode(30, node5, node6)
root = BinaryNode(25, node1, node2)

#             25
#     20              30
# 10      21      27      40


# iterative_binary_tree_dfs(root)
# iterative_binary_tree_bfs(root)

def recursive_dfs(node):
    if not node:    
        return
    
    print(node.val)
    recursive_dfs(node.left)
    recursive_dfs(node.right)

# recursive_dfs(root)

class Node:
    def __init__(self, val):
        self.val = val

single_node3 = Node(10)
single_node4 = Node(21)
single_node1 = Node(20)
single_node5 = Node(27)
single_node6 = Node(40)
single_node2 = Node(30)
root2 = Node(25)

# adjeceny list
graph = {
    
}