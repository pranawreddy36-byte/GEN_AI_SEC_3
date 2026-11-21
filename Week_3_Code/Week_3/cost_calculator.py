# Example rates per 1 million tokens; update using current official model pricing.
PRICING = {
    "gemini-3-flash-pro": {"input": 0.50, "output": 2.00}
}

def calculate_cost(provider, model, input_tokens, output_tokens):
    if provider == "OllamaProvider":
        return 0.0
    rates = PRICING.get(model)
    if rates is None:
        return None
    input_cost = input_tokens * rates["input"] / 1_000_000
    output_cost = output_tokens * rates["output"] / 1_000_000
    return round(input_cost + output_cost, 10)
