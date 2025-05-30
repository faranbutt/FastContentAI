# utils/llm.py

import os
from config import LLM_TYPE, OPENAI_API_KEY, LLAMA_MODEL_NAME,GROQ_API_KEY
from groq import Groq

print(LLM_TYPE)

if LLM_TYPE.lower() == "openai":
    import openai
    openai.api_key = OPENAI_API_KEY
else:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    # Using a placeholder Llama model; adjust MODEL_NAME as needed.
    # tokenizer = AutoTokenizer.from_pretrained(LLAMA_MODEL_NAME)
    # model = AutoModelForCausalLM.from_pretrained(LLAMA_MODEL_NAME)

def generate_article_content(prompt, max_length=200):
    """
    Generate article content based on a prompt using the selected LLM.
    
    :param prompt: Text prompt for content generation.
    :param max_length: Maximum length of generated content.
    :return: Generated text as a string.
    """
    if LLM_TYPE.lower() == "openai":
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_length,
                temperature=0.7,
            )
            text = response["choices"][0]["message"]["content"].strip()
            return text
        except Exception as e:
            return f"Error generating content: {e}"
    else:
        try:
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # or "gemma-7b-it"
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=max_length
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error using Groq API: {e}"
