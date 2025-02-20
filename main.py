import sys
from buttons import ButtonsGrid  # type: ignore
from display import Display  # type: ignore
from info import Info  # type: ignore
from main_window import MainWindow  # type: ignore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme  # type: ignore
from variables import WINDOW_ICON_PATH  # type: ignore

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.VLayout.addLayout(buttonsGrid)  # Correção do erro

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()