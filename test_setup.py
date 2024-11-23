# test_setup.py
from langchain_huggingface import HuggingFaceEndpoint

# Set your Hugging Face API token 
huggingfacehub_api_token = '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'

def test_prompts():
    # Define the LLM
    llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

    # Predict the words following the text in question
    question = 'Whatever you do, take care of your shoes'
    output = llm.invoke(question)

    print(output)

if __name__ == "__main__":
    test_prompts()