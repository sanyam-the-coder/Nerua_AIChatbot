# 🧠 NERUA – AI Chatbot  

NERUA is a simple **command-line chatbot** powered by OpenAI’s API.  
It lets you chat with state-of-the-art language models like `gpt-4o` or `gpt-5`.  

---

## 🚀 Features
- Interactive chat loop in your terminal  
- Powered by OpenAI’s **latest models** (`gpt-4o`, `gpt-5`, `gpt-5-mini`, etc.)  
- Graceful exit with `exit`, `quit`, or `bye`  
- Easy to extend with custom system prompts  

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/nerua.git
   cd nerua
   ```

2. **Set up a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install openai
   ```

---

## 🔑 API Key Setup

For security, **don’t hardcode your key** in the script.  
Instead, store it in an environment variable:

**Windows PowerShell**  
```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

**macOS/Linux (bash/zsh)**  
```bash
export OPENAI_API_KEY="your_api_key_here"
```

Then in your code:
```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## ▶️ Usage

Run the chatbot:
```bash
python main.py
```

Sample session:
```
You: hi
NERUA: Hello! How are you today?
```

Exit anytime with:
```
You: exit
```

---

## ⚙️ Model Selection

In the code, you can change the model here:
```python
response = client.chat.completions.create(
    model="gpt-4o",   # try "gpt-5", "gpt-5-mini", or "gpt-5-nano"
    messages=[{"role": "user", "content": prompt}]
)
```

---

## 💰 Pricing Note
You’ll be billed **per token** based on the model you choose.  
See [OpenAI Pricing](https://openai.com/pricing) for details.  

---

## 🛠️ Future Improvements
- Add cost tracking per conversation  
- Build a simple GUI with Tkinter or a web UI with Flask/React  
- Support conversation history across turns
