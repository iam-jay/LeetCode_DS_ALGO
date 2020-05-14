class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_in_order_tree(self, root):
        if not root:
            return
        if root.left:
            self.print_in_order_tree(root.left)
        print(root.data, end=" ")
        if root.right:
            self.print_in_order_tree(root.right)

    def print_pre_order_tree(self, root):
        if not root:
            return
        print(root.data, end=" ")
        if root.left:
            self.print_pre_order_tree(root.left)
        if root.right:
            self.print_pre_order_tree(root.right)

    def print_post_order_tree(self, root):
        if not root:
            return
        if root.left:
            self.print_post_order_tree(root.left)
        if root.right:
            self.print_post_order_tree(root.right)
        print(root.data, end=" ")

    def print_mirror_tree(self):
        pass

    def print_level_order_tree(self):
        pass

    def print_bottom_of_tree(self):
        pass

    def print_boundary_of_tree(self):
        pass

    def tree_height(self, root):
        if root is None:
            return 0
        lh = self.tree_height(root.left)
        rh = self.tree_height(root.right)
        height = max(lh, rh) + 1
        return height


def print_post_order_from_pre_and_in(in_order, pre_order, n):
    if pre_order[0] in in_order:
        root = in_order.index(pre_order[0])
    if root != 0:
        print_post_order_from_pre_and_in(in_order[:root],
                                         pre_order[1:root + 1],
                                         len(in_order[:root]))
    if root != n - 1:
        print_post_order_from_pre_and_in(in_order[root+1:],
                                         pre_order[root + 1:],
                                         len(in_order[root + 1:]))

    print(pre_order[0], end=' ')


def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        print(root.data)
        return root
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
    b_root = BinaryTree(1)
    b_root.left = BinaryTree(2)
    b_root.right = BinaryTree(3)
    b_root.left.left = BinaryTree(4)
    b_root.left.right = BinaryTree(5)
    b_root.right.left = BinaryTree(6)
    b_root.right.right = BinaryTree(7)
    print("\n--------IN ORDER---------")
    b_root.print_in_order_tree(b_root)
    print("\n--------PRE ORDER---------")
    b_root.print_pre_order_tree(b_root)
    print("\n--------POST ORDER---------")
    b_root.print_post_order_tree(b_root)
    print()
    print_post_order_from_pre_and_in([4, 2, 5, 1, 6, 3],
                                     [1, 2, 4, 5, 3, 6], 6)
    print()
    print(findLCA(b_root, 2, 4).data)
