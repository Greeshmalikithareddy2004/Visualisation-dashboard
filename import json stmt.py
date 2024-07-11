import json

# Load JSON data with the correct encoding
with open("data.json", encoding='utf-8') as f:
    mee = json.load(f)

# Print JSON data
print(mee)
