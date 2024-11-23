# test_setup.py
from langchain import hub
from transformers import pipeline

def test_imports():
    print("Testing LangChain import...")
    # Test LangChain
    prompt = hub.pull("rlm/text-question-answer")
    print("LangChain import successful!")

    print("\nTesting Hugging Face Transformers import...")
    # Test Transformers
    classifier = pipeline("sentiment-analysis")
    result = classifier("Hello, world!")
    print("Transformers import successful!")
    print(f"Test classification result: {result}")

if __name__ == "__main__":
    test_imports()