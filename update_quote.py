import requests
import re

# Constants
FALLBACK_QUOTE = '"Keep pushing forward, no matter what!"'
FALLBACK_AUTHOR = "Unknown"
QUOTE_INDENT = "\n" + " " * 36 + "– "

# Fetch a random quote from ZenQuotes API
try:
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    if response.status_code == 200:
        quote_data = response.json()
        quote = f'{quote_data[0]["q"]}{QUOTE_INDENT}{quote_data[0]["a"]}'
    else:
        quote = f'{FALLBACK_QUOTE}{QUOTE_INDENT}{FALLBACK_AUTHOR}'
except Exception:
    # Fallback quote if API fails
    quote = f'{FALLBACK_QUOTE}{QUOTE_INDENT}{FALLBACK_AUTHOR}'

# Read the current README file
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Replace the placeholder with the new quote
updated_content = re.sub(
    r"<!--STARTS_HERE_QUOTE_README-->.*?<!--ENDS_HERE_QUOTE_README-->",
    f"<!--STARTS_HERE_QUOTE_README-->\n{quote}\n<!--ENDS_HERE_QUOTE_README-->",
    content,
    flags=re.DOTALL,
)

# Write the updated content back to the README file
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_content)
