"""
Configuration helper module for Budget Lens project.
Handles environment variable loading and retrieval.
"""

import os
from dotenv import load_dotenv


def load_env():
    """
    Load environment variables from .env file.
    
    Returns:
        bool: True if .env file was loaded successfully, False otherwise
    """
    return load_dotenv()


def get_key(key_name, default=None):
    """
    Retrieve an environment variable value.
    
    Args:
        key_name (str): Name of the environment variable
        default: Default value to return if key is not found
        
    Returns:
        str: Value of the environment variable or default value
    """
    return os.getenv(key_name, default)


# Load environment variables when module is imported
load_env()
