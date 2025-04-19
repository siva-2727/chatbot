#  Problem Solving – Yago Assistant

---

##  API Key Errors

**Error:**
```
google.auth.exceptions.DefaultCredentialsError
```

**Solution:**
- Replace `"enter your api key"` in `main.py` with your actual API key from Google.
- Ensure you’ve enabled access in your Google Cloud console or MakerSuite.

---

## 🔎No Response / Empty Output

**Symptoms:**
- The bot prints nothing or returns `None`.

**Fix:**
- Check API key and internet connectivity.
- Add logging or print `completion` object to debug.

---

## PaLM Model Doesn’t Exist

**Error:**
```
model "text-bison-001" not found
```

**Fix:**
- Double-check if the model name still exists: run `list_models()` to print all available models.
- Replace with the correct model ID.

---

##  Web Server Not Starting

**Symptoms:**
- Flask or Streamlit doesn't launch

**Fix:**
- Ensure port `8501` (Streamlit) or `5000` (Flask) is free.
- Run Streamlit with an alternative port:
```bash
streamlit run streamlit_app.py --server.port 8502
```

---

##  Chatbot Freezes or Delays

- Reduce `max_output_tokens` to 300 or 400.
- Lower `temperature` to reduce random long answers.

---

## Common Tips

- Keep API key secret – use environment variables in production.
- Use `try/except` to catch API exceptions.