import sys,requests,markdown
from PyQt5.QtCore import Qt
from PyQt5 . QtWidgets import(QApplication, QMainWindow, QLineEdit, QTextEdit,QSizePolicy,
QPushButton, QVBoxLayout, QWidget, QLabel, 
QScrollArea, QSizePolicy, QHBoxLayout)
from PyQt5.QtCore import QThread, pyqtSignal


class ChatbotWorker(QThread):
    response_received = pyqtSignal(str)

    def __init__(self, user_input, parent=None):
        super().__init__(parent)
        self.user_input = user_input
        self.api_url = "http://localhost:11434/api/generate"  # Ollama local API

    def run(self):
        headers = {"Content-Type": "application/json"}
        data = {
            "model": "deepseek-r1:8b",  # Make sure this matches your installed model name
            "prompt": self.user_input,
            "stream": False  # Disable streaming for simplicity
        }

        try:
            response = requests.post(self.api_url, json=data, headers=headers)
            if response.status_code == 200:
                bot_response = response.json().get("response", "Error: No response from DeepSeek")
            else:
                bot_response = f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            bot_response = f"Error: {str(e)}"

        self.response_received.emit(bot_response)


class MainWindow(QWidget):
    def __init__(self): 
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Chatbot")

     
    def init_ui(self):
        self.setGeometry(100,100,600,600)
        

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 10px;
                font-size: 14px;
                padding: 5px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                font-size: 14px;
                border: none;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #005ea7;
            }
            
        """)

        
        #CREATING A LAYOUT
        hbox = QVBoxLayout(self)
        
        
        #CREATING A DISPLAY AREA
        self.text_display = QWidget()
        self.text_display_layout = QVBoxLayout()
        self.text_display_layout.setSpacing(10)
        self.text_display.setLayout(self.text_display_layout)
        #CREATING SCROLL AREA
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.text_display)
        self.scroll_area.setWidgetResizable(True)
        hbox.addWidget(self.scroll_area)
        #CREATING INPUT SPACE   
        self.input_area = QLineEdit(self)
        self.input_area.returnPressed.connect(self.sendmes)
        self.input_area.setPlaceholderText("Enter your message here")
        hbox.addWidget(self.input_area)
        
        #CREATE SEND BUTTON
        self.send_button=QPushButton('send', self)
        self.send_button.clicked.connect(self.sendmes)
        hbox.addWidget(self.send_button)

    #CREATING THE BUTTON

    def sendmes(self):
        user_text = self.input_area.text()  #getting text
        if user_text:
            label = QLabel(user_text)           #creating label with input text
            label.setStyleSheet("""
            background-color: #128C7E;
            border: 1px solid #cccccc;
            border-radius: 10px;
            font-size: 14px;
            padding: 5px;
            """)
            label.setWordWrap(True) 
            label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
            label.adjustSize() 
            self.text_display_layout.addWidget(label)
            self.input_area.clear()
            self.worker = ChatbotWorker(user_text)
            self.worker.response_received.connect(self.display_response)
            self.worker.start()

    def display_response(self, response_text):



        html_response = markdown.markdown(response_text, extensions=["extra", "sane_lists", "smarty"])
        label = QLabel(html_response)
        label.setStyleSheet("""
            background-color: #34B7F1;
            color:-#FFFFFF                
            border: 1px solid #cccccc;
            border-radius: 10px;
            font-size: 14px;
            padding: 5px;
            """)
        label.setWordWrap(True) 
        label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        label.adjustSize()
        self.text_display_layout.addWidget(label)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())






























