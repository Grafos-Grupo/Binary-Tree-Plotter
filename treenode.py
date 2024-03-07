class TreeNode:

    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)

    def print_in_order(self):
        result = []
        if self.left:
            result.extend(self.left.print_in_order())
        result.append(str(self.key))
        if self.right:
            result.extend(self.right.print_in_order())
        return result

    def print_pre_order(self):
        result = [str(self.key)]
        if self.left:
            result.extend(self.left.print_pre_order())
        if self.right:
            result.extend(self.right.print_pre_order())
        return result

    def print_post_order(self):
        result = []
        if self.left:
            result.extend(self.left.print_post_order())
        if self.right:
            result.extend(self.right.print_post_order())
        result.append(str(self.key))
        return result


def search_node(root: TreeNode, key: int):
    if root.key == key or root is None:
        return root
    if root.key > key: return search_node(root.left, key)
    else: return search_node(root.right, key)


def delete_node(root: TreeNode, key: int):
    if not root: return None
    if root.key == key:
        if not root.left and not root.right: return None
        if not root.left and root.right: return root.right
        if not root.right and root.left: return root.left

        pointer = root.right
        while pointer.left: pointer = pointer.left
        root.key = pointer.key
        root.right = delete_node(root.right, root.key)
    elif root.key > key:
        root.left = delete_node(root.left, key)
    else:
        root.right = delete_node(root.right, key)
    return root

