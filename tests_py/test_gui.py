import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog


class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.label = QLabel("Selected file path will be displayed here")
        layout.addWidget(self.label)

        self.button = QPushButton("Open File")
        self.button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)

        self.setWindowTitle("File Dialog Example")
        self.show()

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        if file_path:
            self.label.setText(f"Selected file: {file_path}")
        else:
            self.label.setText("No file selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialogExample()
    sys.exit(app.exec_())