from text_patterns import menu_text
from treenode import TreeNode, delete_node, search_node


def menu(tree: TreeNode):
    choice = input(menu_text)
    match choice:
        case "1":
            node = int(input("Qual a chave do nó que será inserido? "))
            tree.insert(key=node)
        case "2":
            node = int(input("Qual a chave do nó que será deletado? "))
            delete_node(root=tree, key=node)
        case "3":
            return 0
        case "4":
            print("Em ordem (ERD")
            tree.print_in_order()
            print("\n")
            tree.print_pre_order("Pré ordem (RED)")
            print("\n")
            tree.print_post_order("Pós ordem (EDR)")
            print("\n")
        case "5":
            print("Programa fechando...")
            return -1
        case _:
            print("Essa opção não existe! Tente novamente.")
            menu(tree)
