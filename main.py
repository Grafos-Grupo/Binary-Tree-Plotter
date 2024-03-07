from treenode import TreeNode, delete_node, search_node


with open("entrada_arvore/arvore1.txt") as file:
    entry = [int(i.replace("\n", "")) for i in file.readlines()]


tree = TreeNode(entry[0])

for i in entry[1:]:
    tree.insert(i)

delete_node(root=tree, key=1)

tree.print_in_order()
print("\n")
tree.print_pre_order()
print("\n")
tree.print_post_order()
print("\n")


