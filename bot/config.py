import os

# Fetch individual tokens from environment variables
bot_token1 = os.getenv('bot_token1', 'default_bot_token1')
bot_token2 = os.getenv('bot_token2', 'default_bot_token2')
bot_token3 = os.getenv('bot_token3', 'default_bot_token3')
bot_token4 = os.getenv('bot_token4', 'default_bot_token4')
bot_token5 = os.getenv('bot_token5', 'default_bot_token5')
bot_token6 = os.getenv('bot_token6', 'default_bot_token6')

# Construct lists from individual environment variables
UPLOADER_BOTS_1 = [bot_token1, bot_token2, bot_token3]
UPLOADER_BOTS_2 = [bot_token4, bot_token5, bot_token6]

# Other configurations
API_ID = os.getenv('API_ID', 'default_api_id')
API_HASH = os.getenv('API_HASH', 'default_api_hash')
MAIN_BOT_TOKEN = os.getenv('MAIN_BOT_TOKEN', 'default_main_bot_token')
LOGGER_BOT_TOKEN = os.getenv('LOGGER_BOT_TOKEN', 'default_logger_bot_token')
MONGO_DB_URL = os.getenv('MONGO_DB_URL', 'default_mongo_db_url')
WEBSITE_DOMAIN = os.getenv('WEBSITE_DOMAIN', 'default_website_domain')
PLAYERX_API_KEY = os.getenv('PLAYERX_API_KEY', 'default_playerx_api_key')
PLAYERX_EMAIL = os.getenv('PLAYERX_EMAIL', 'default_playerx_email')
PLAYERX_PASSWORD = os.getenv('PLAYERX_PASSWORD', 'default_playerx_password')
