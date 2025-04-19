Yago Assistant – AI Chatbot using Google PaLM

This is a simple Python chatbot powered by Google PaLM (text-bison-001) that works via command line, and can be extended to work with Streamlit or Flask UI.

---

## Features

- Uses Google PaLM's text generation API
- Interactive CLI chatbot interface
- Easily extendable to Streamlit or Flask with HTML frontends

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yago-assistant.git
cd yago-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

Replace `"enter your api key"` in `main.py` with your actual API key from [Google Generative AI](https://makersuite.google.com/).

---

## Run the App

```bash
python main.py
```

You can type prompts directly in the terminal.

---

## Web UI Options

### Streamlit

You can build a Streamlit interface for chat interaction:

```bash
streamlit run streamlit_app.py
```

### Flask

Use a basic HTML form (e.g., `index.html`) and backend Flask server (`app.py`):

```bash
python app.py
```

Then visit: http://localhost:5000

---

## Troubleshooting

See [problem_solving.md](./problem_solving.md)

---

## Model Info

- Model: `text-bison-001`
- Temperature: `0.99` (random/creative responses)
- Max Output Tokens: `800`

---

## License

MIT License