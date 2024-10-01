import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox
import os
import shutil

class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем главный layout
        main_layout = QHBoxLayout()

        # Создаем два виджета для отображения содержимого папок
        self.folder1_widget = QListWidget()
        self.folder2_widget = QListWidget()

        # Пути к папкам
        self.folder1_path = "first_folder"
        self.folder2_path = "second_folder"

        # Обновляем содержимое виджетов
        self.update_folder_contents()

        # Создаем кнопки
        create_button = QPushButton("Создать")
        delete_button = QPushButton("Удалить")
        transfer_button = QPushButton("Перенести")

        # Подключаем кнопки к функциям
        create_button.clicked.connect(self.create_file)
        delete_button.clicked.connect(self.delete_file)
        transfer_button.clicked.connect(self.transfer_file)

        # Создаем вертикальный layout для кнопок
        button_layout = QVBoxLayout()
        button_layout.addWidget(create_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(transfer_button)

        # Добавляем виджеты и кнопки в главный layout
        main_layout.addWidget(self.folder1_widget)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.folder2_widget)

        self.setLayout(main_layout)
        self.setWindowTitle('Файловый менеджер')
        self.setGeometry(300, 300, 600, 400)

    def update_folder_contents(self):
        # Обновляем содержимое виджетов
        self.folder1_widget.clear()
        self.folder2_widget.clear()
        self.folder1_widget.addItems(os.listdir(self.folder1_path))
        self.folder2_widget.addItems(os.listdir(self.folder2_path))

    def create_file(self):
        # Создание файла
        file_name, ok = QInputDialog.getText(self, 'Создать файл', 'Введите имя файла:')
        if ok and file_name:
            with open(os.path.join(self.folder1_path, file_name), 'w') as f:
                pass
            self.update_folder_contents()

    def delete_file(self):
        # Удаление файла
        selected_items = self.folder1_widget.selectedItems() + self.folder2_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'Ошибка', 'Выберите файл для удаления')
            return
        
        for item in selected_items:
            file_path = os.path.join(self.folder1_path if item in self.folder1_widget.selectedItems() else self.folder2_path, item.text())
            os.remove(file_path)
        
        self.update_folder_contents()

    def transfer_file(self):
        # Перенос файла
        selected_items = self.folder1_widget.selectedItems() + self.folder2_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'Ошибка', 'Выберите файл для переноса')
            return
        
        for item in selected_items:
            source_folder = self.folder1_path if item in self.folder1_widget.selectedItems() else self.folder2_path
            target_folder = self.folder2_path if source_folder == self.folder1_path else self.folder1_path
            
            source_path = os.path.join(source_folder, item.text())
            target_path = os.path.join(target_folder, item.text())
            
            shutil.move(source_path, target_path)
        
        self.update_folder_contents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileManager()
    ex.show()
    sys.exit(app.exec_())