from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from treenode import TreeNode, delete_node


class BinaryTreeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tree = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Árvore Binária de Pesquisa')
        self.setGeometry(100, 100, 600, 800)

        icon_path = 'icon.png'
        self.setWindowIcon(QIcon(icon_path))

        self.label = QLabel('Insira o valor do nó:', self)
        self.node_input = QLineEdit(self)

        self.insert_button = QPushButton('Insert', self)
        self.delete_button = QPushButton('Delete', self)
        self.clear_button = QPushButton('Clear', self)
        self.list_button = QPushButton('List', self)
        self.import_button = QPushButton('Import file', self)

        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.node_input)
        self.layout.addWidget(self.insert_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.list_button)
        self.layout.addWidget(self.import_button)
        self.layout.addWidget(self.text_output)
        self.setLayout(self.layout)

        self.insert_button.clicked.connect(self.insert_node_func)
        self.delete_button.clicked.connect(self.delete_node_func)
        self.clear_button.clicked.connect(self.clear_func)
        self.list_button.clicked.connect(self.list_tree)
        self.import_button.clicked.connect(self.import_tree)

        # Adiciona um widget do matplotlib para exibir o gráfico
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def clear_func(self):
        self.tree = None
        self.plot_tree()
        self.node_input.clear()
    
    def list_tree(self):
        if self.tree:
            self.text_output.clear()
            self.text_output.append('Em ordem:')
            self.text_output.append(', '.join(self.tree.print_in_order()))
            self.text_output.append('Pré ordem:')
            self.text_output.append(', '.join(self.tree.print_pre_order()))
            self.text_output.append('Pós ordem:')
            self.text_output.append(', '.join(self.tree.print_post_order()))

    def delete_node_func(self):
        if self.node_input.text().isdigit():
            key = int(self.node_input.text())
            if key:
                delete_node(root=self.tree, key=key)

        self.plot_tree()
        self.node_input.clear()

    def insert_node_func(self):
        # Insert node in tree
        if self.node_input.text().isdigit():
            key = int(self.node_input.text())

            if key is not None:
                if self.tree is None:
                    self.tree = TreeNode(key)
                else:
                    self.tree.insert(key)
        self.plot_tree()
        self.node_input.clear()

    def import_tree(self):
        # Imports the tree from the txt

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "",
                                                   "Arquivos de Texto (*.txt);;Todos os Arquivos (*)", options=options)

        if file_name:
            with open(file_name) as file:
                data = file.readlines()
                entry = [int(i.replace("\n", "")) for i in data if i.strip().isdigit()]

            if self.tree is None:
                self.tree = TreeNode(entry[0])
                for i in entry[1:]:
                    self.tree.insert(int(i))
            else:
                for i in entry:
                    self.tree.insert(int(i))

        self.plot_tree()

    def plot_tree(self):
        # Gera a representação da árvore e a exibe no widget do matplotlib
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        self.plot_tree_recursive(ax, self.tree)
        self.canvas.draw()

    def plot_tree_recursive(self, ax, node, x=0, y=0, horizontal_space=1, level=1):
        if node:
            ax.text(x, y, str(node.key), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
            if node.left:
                x_left = x - horizontal_space / 2 ** level
                y_left = y - 1
                ax.plot([x, x_left], [y, y_left], 'k-')
                self.plot_tree_recursive(ax, node.left, x_left, y_left, horizontal_space / 2, level + 1)
            if node.right:
                x_right = x + horizontal_space / 2 ** level
                y_right = y - 1
                ax.plot([x, x_right], [y, y_right], 'k-')
                self.plot_tree_recursive(ax, node.right, x_right, y_right, horizontal_space / 2, level + 1)
