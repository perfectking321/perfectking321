import requests
import re

# Fetch a random quote from ZenQuotes API
try:
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    if response.status_code == 200:
        quote_data = response.json()
        # Escape any quotes in the text to prevent formatting issues
        quote_text = quote_data[0]["q"].replace('"', '\\"')
        quote_author = quote_data[0]["a"]
        quote = f'"{quote_text}" – {quote_author}'
    else:
        quote = '"Keep pushing forward, no matter what!" – Unknown'
except Exception as e:
    print(f"Failed to fetch quote from API: {e}")
    quote = '"Keep pushing forward, no matter what!" – Unknown'

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

print("Quote updated successfully!")
