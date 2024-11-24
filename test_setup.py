# test_setup.py
from langchain_huggingface import HuggingFaceEndpoint
from utils.env_loader import load_env_variables


def test_prompts():
# Set Hugging Face API token
    env_vars = load_env_variables()
    huggingfacehub_api_token = env_vars['HUGGINGFACE_API_KEY']
    # Define the LLM
    llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

    # Predict the words following the text in question
    question = 'Whatever you do, take care of your shoes'
    output = llm.invoke(question)

    print(output)

if __name__ == "__main__":
    test_prompts()