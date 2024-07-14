import json
import os
import logging
from dotenv import load_dotenv

load_dotenv()

def load_config():
  try:
    config = {
      'TAVILY_API_KEY': os.environ['TAVILY_API_KEY'],
      'OPENAI_API_KEY': os.environ['OPENAI_API_KEY']
    }

    return config
  
  except KeyError as e:
    logging.error(f"Missing environment variable: {e}")
    return {}

TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

logging.info("Configuration Successful")