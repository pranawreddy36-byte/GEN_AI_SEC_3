WEEK 3 - LLM MONITORING

Install:
  python -m pip install -r requirements.txt

Ensure MongoDB is running locally at mongodb://localhost:27017/

Gemini:
  Copy .env.example to .env, add your Gemini API key.
  Run python main.py and select 1.

Ollama:
  Install/start Ollama; run ollama pull llama3.2.
  Run python main.py and select 2.

The cost rates in cost_calculator.py are sample estimates, not verified live
pricing. Update them using official current pricing before relying on estimates.
