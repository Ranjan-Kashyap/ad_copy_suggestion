from langchain.llms import OpenAI
import logging

logging.basicConfig(filename='logs/std.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def generate_ads(prompt,apiKey):
    try:
        llm = OpenAI(openai_api_key=apiKey,model_name="text-davinci-003")
        # llm = OpenAI(openai_api_key=apiKey, temperature=0.9)
        content = llm(prompt)
    except Exception as e:
        logging.warning(f"Error in {e}")
        content = "Having traffic this time try sometime later."
    return content
