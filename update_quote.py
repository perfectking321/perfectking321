import requests
import re

# Fetch a random quote from ZenQuotes API
response = requests.get("https://zenquotes.io/api/random")
if response.status_code == 200:
    quote_data = response.json()
    quote = f"“{quote_data[0]['q']}” – {quote_data[0]['a']}"
else:
    quote = "“Keep pushing forward, no matter what!” – Unknown"

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
