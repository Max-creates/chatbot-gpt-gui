from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        
        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700, 500)
        
        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        
        # Add the input field
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter a message...")
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)
        
        # Add the send button
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setGeometry(500, 340, 100, 40)
        
        # Add the clear button
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_chat)
        self.clear_button.setGeometry(500, 290, 100, 40)
        
        # Add the exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.exit)
        self.exit_button.setGeometry(500, 240, 100, 40)
        
        
        
        self.show()
        
    def send_message(self):
        message = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {message}</p>")
        self.input_field.clear()
        
        thread = threading.Thread(target=self.get_bot_response, args=(message, ))
        thread.start()

    def get_bot_response(self, message):
        response = self.chatbot.get_response(message)
        self.chat_area.append(
            f"<p style='color:#333333; background-color: #E9E9E9'>Chatbot: {response}</p>")
    
    def clear_chat(self):
        self.chat_area.clear()
        
    def exit(self):
        self.close()


app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())