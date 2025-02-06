# PyQt Chatbot with DeepSeek (Ollama) (Please Read the important points at last)

## 📌 Overview
This is a PyQt-based chatbot GUI that interacts with a locally installed DeepSeek model(or any other model which you can download via the Ollama). The chatbot allows users to send messages and receive AI-generated responses in a user-friendly interface.

## 🛠 Features
- ✅ User-friendly chat interface using PyQt5
- ✅ Asynchronous API requests via `QThread`
- ✅ Uses Ollama's local API to generate AI responses
- ✅ Markdown support for formatted AI responses
- ✅ Scrollable chat window

## 📂 Project Structure
-LocalGpt.py (**Main File**)
-README.md (**Steps and Intro File**)
      


## 🚀 Installation

### 1️⃣ Install Python (if not installed)
Make sure you have Python 3.8+ installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Install Dependencies

### 3️⃣ Install and Run Ollama
  1. **Install Ollama** (if not installed):
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```
  2. **Start Ollama**:
   ```bash
   ollama serve
   ```
  3. **Download the DeepSeek model**:
   ```bash
   ollama pull deepseek-r1:8b
   ```

## 🏃‍♂️ Running the Chatbot
Run the script:
```bash
python LocalGpt.py
```
This will launch the PyQt chatbot window.

## 🛠 Debugging
### 1️⃣ Verify Ollama API
Test if Ollama is running properly by making a manual API request:
```bash
curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{
  "model": "deepseek-r1:8b",
  "prompt": "Hello"
}'
```
Expected response:
```json
{
  "response": "Hello! How can I assist you?"
}
```
If this fails, check if Ollama is running with:
```bash
ollama serve
```

### 2️⃣ Check Console Logs
Run the chatbot script in a terminal and look for any errors. Use `print()` statements to debug if necessary.

### 3️⃣ Verify Model Name
Run:
```bash
ollama list
```
Ensure that `deepseek-r1:8b` appears in the list. If not, install it again:
```bash
ollama pull deepseek-r1:8b
```

## IMPORTANT POINTS
- **Don't** forget to install all the modules or dependencies before running the python script.
- In some cases you will need to run the **llm modal in background through terminal**.
- Also, if you install any other model of llm **don't forget to change the model name in LocalGpt file in line number 22**. If, you forget to do so you may encounter problem and it will wont work.
- This code is only for running **llm which are stored locally and downloaded only throught ollama**. If you download it from any other platform feel free to change the url in the file Localgpt line number 17.  

## 📜 License
This project is open-source. You can modify and distribute it as needed.
