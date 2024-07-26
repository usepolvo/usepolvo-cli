import os
import configparser

CONFIG_FILE_PATH = os.path.expanduser("~/.usepolvo_cli_config")

config = configparser.ConfigParser()

def load_config():
    if os.path.exists(CONFIG_FILE_PATH):
        config.read(CONFIG_FILE_PATH)

def save_config(integration, api_key):
    load_config()
    if integration not in config:
        config[integration] = {}
    config[integration]['API_KEY'] = api_key
    with open(CONFIG_FILE_PATH, 'w') as configfile:
        config.write(configfile)

def get_api_key(integration):
    load_config()
    return config[integration].get('API_KEY', None) if integration in config else None