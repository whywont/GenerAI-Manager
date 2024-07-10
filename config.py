import json
import os

def load_config():
  config_path = os.path.join(os.path.dirname(__file__), 'config.json')
  try:
    with open(config_path, 'r') as config_file:
      config = json.load(config_file)
    return config
  except FileNotFoundError:
    print(f"Configuration file not found. Please create a config.json file in {os.path.dirname(__file__)}")
    return {}
  except json.JSONDecodeError:
    print("Error reading the configuration file. Please make sure it's valid JSON.")
    return {}

def validate_config(config):
  required_keys = ['TAVILY_API_KEY', 'OPENAI_API_KEY']

  for key in required_keys:
    if key not in config or not config[key] or config[key].startswith("REPLACE_WITH_YOUR_"):
      print(f"Invalid or missing {key}. Please update in config.json.")
      return False

  return True

config = load_config()

if not validate_config(config):
  exit(1)

TAVILY_API_KEY = config['TAVILY_API_KEY']
OPENAI_API_KEY = config['OPENAI_API_KEY']

print("Configuration Successful")