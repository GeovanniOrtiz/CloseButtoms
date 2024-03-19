import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Barra de Botones")
        self.setGeometry(100, 100, 400, 300)

        # Crear una barra de herramientas
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Botón para minimizar
        minimize_action = QAction(QIcon("icons/minimize.png"), "Minimizar", self)
        minimize_action.triggered.connect(self.minimize_window)
        toolbar.addAction(minimize_action)

        # Botón para cerrar
        close_action = QAction(QIcon("icons/close.png"), "Cerrar", self)
        close_action.triggered.connect(self.close_window)
        toolbar.addAction(close_action)

        # Botón para redimensionar
        resize_action = QAction(QIcon("icons/resize.png"), "Redimensionar", self)
        resize_action.triggered.connect(self.resize_window)
        toolbar.addAction(resize_action)

        # Botón para pantalla completa
        fullscreen_action = QAction(QIcon("icons/fullscreen.png"), "Pantalla Completa", self)
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        toolbar.addAction(fullscreen_action)

    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        self.close()

    def resize_window(self):
        self.resize(600, 400)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
