WEEK 2 - PROVIDER-AGNOSTIC LLM APPLICATION

Install:
  python -m pip install -r requirements.txt

For Gemini:
  Copy .env.example to .env, add GEMINI_API_KEY, then run python main.py
  Choose: gemini

For Ollama:
  Install/start Ollama and run: ollama pull llama3.2
  Run python main.py and choose: ollama

Run unit test:
  python -m unittest test_client.py
