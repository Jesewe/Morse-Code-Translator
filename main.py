import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QMessageBox
from PyQt6.QtGui import QPalette, QColor, QFont
from PyQt6.QtCore import Qt

morse_code_dict_eng = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

morse_code_dict_rus = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

reverse_morse_code_dict_eng = {value: key for key, value in morse_code_dict_eng.items()}
reverse_morse_code_dict_rus = {value: key for key, value in morse_code_dict_rus.items()}

class MorseCodeTranslator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Morse Code Translator')
        self.setFixedSize(400, 350)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.language_label = QLabel('Select a language:')
        self.layout.addWidget(self.language_label)

        self.language_combo_box = QComboBox()
        self.language_combo_box.addItems(['eng', 'rus'])
        self.layout.addWidget(self.language_combo_box)

        self.input_label = QLabel('Enter text:')
        self.layout.addWidget(self.input_label)

        self.input_text_edit = QTextEdit()
        self.layout.addWidget(self.input_text_edit)

        self.translate_button = QPushButton('Translate')
        self.translate_button.clicked.connect(self.translate_text)
        self.layout.addWidget(self.translate_button)

        self.switch_mode_button = QPushButton('Switch Mode')
        self.switch_mode_button.clicked.connect(self.switch_mode)
        self.layout.addWidget(self.switch_mode_button)

        self.output_label = QLabel('Translated text:')
        self.layout.addWidget(self.output_label)

        self.output_text_edit = QTextEdit()
        self.output_text_edit.setReadOnly(True)
        self.layout.addWidget(self.output_text_edit)

        self.copy_button = QPushButton('Copy')
        self.copy_button.clicked.connect(self.copy_text)
        self.layout.addWidget(self.copy_button)

        self.theme_button = QPushButton('Toggle Theme')
        self.theme_button.clicked.connect(self.toggle_theme)
        self.layout.addWidget(self.theme_button)

        self.light_theme = True
        self.set_light_theme()

        self.mode_morse_to_text = True
        
    def toggle_theme(self):
        if self.light_theme:
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def set_light_theme(self):
        self.light_theme = True
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.ColorRole.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
        self.setPalette(palette)

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }

            QPushButton {
                background-color: #4784DF;
                color: #000000;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            
            QComboBox {
                background-color: #f0f0f0;
                color: #000000;
                padding: 5px;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
            }
            
            QTextEdit {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
            }
        """)

    def set_dark_theme(self):
        self.light_theme = False
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(45, 45, 45))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(35, 35, 35))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
        self.setPalette(palette)

        self.setStyleSheet("""
            QPushButton {
                background-color: #353535;
                color: #ffffff;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            
            QComboBox {
                background-color: #353535;
                color: #ffffff;
                padding: 5px;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
            }
            
            QTextEdit {
                background-color: #454545;
                color: #ffffff;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
            }
        """)

    def switch_mode(self):
        self.mode_morse_to_text = not self.mode_morse_to_text

        if self.mode_morse_to_text:
            self.translate_button.setText('Translate')
            self.switch_mode_button.setText('Switch Mode (Morse to Text)')
            self.input_label.setText('Enter Morse code:')
            self.output_label.setText('Translated text:')
        else:
            self.translate_button.setText('Translate')
            self.switch_mode_button.setText('Switch Mode (Text to Morse)')
            self.input_label.setText('Enter text:')
            self.output_label.setText('Translated Morse code:')

        self.input_text_edit.clear()
        self.output_text_edit.clear()

    def translate_text(self):
        if self.mode_morse_to_text:
            self.translate_morse_to_text()
        else:
            self.translate_text_to_morse()

    def copy_text(self):
        translated_text = self.output_text_edit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(translated_text)

        QMessageBox.information(self, 'Copy', 'Translated text has been copied to the clipboard.')

    def translate_morse_to_text(self):
        language = self.language_combo_box.currentText()
        morse_code = self.input_text_edit.toPlainText()
        translated_text = ''

        if language == 'rus':
            reverse_morse_code_dict = reverse_morse_code_dict_rus
        else:
            reverse_morse_code_dict = reverse_morse_code_dict_eng

        words = morse_code.split(' / ')
        translated_words = []

        for word in words:
            letters = word.split(' ')
            translated_letters = []

            for letter in letters:
                if letter in reverse_morse_code_dict:
                    translated_letters.append(reverse_morse_code_dict[letter])

            translated_word = ''.join(translated_letters)
            translated_words.append(translated_word)

        translated_text = ' '.join(translated_words)
        self.output_text_edit.setPlainText(translated_text)

    def translate_text_to_morse(self):
        language = self.language_combo_box.currentText()
        text = self.input_text_edit.toPlainText().upper()
        translated_text = ''

        if language == 'rus':
            morse_code_dict = morse_code_dict_rus
        else:
            morse_code_dict = morse_code_dict_eng

        translated_text = []

        for char in text:
            if char in morse_code_dict:
                translated_text.append(morse_code_dict[char])

        translated_text = ' / '.join(translated_text)
        self.output_text_edit.setPlainText(translated_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = MorseCodeTranslator()
    translator.show()
    sys.exit(app.exec())