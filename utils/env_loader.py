# utils/env_loader.py
import os
from dotenv import load_dotenv

def load_env_variables():
    """Load environment variables from .env file"""
    load_dotenv()
    
    required_vars = [
        'OPENAI_API_KEY',
        'HUGGINGFACE_API_KEY',
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}\n"
            "Please ensure these are set in your .env file"
        )

    return {var: os.getenv(var) for var in required_vars}