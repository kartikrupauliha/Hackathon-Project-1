import json

# Read the JSON file
with open('security.json', encoding='utf-8') as file:
    data = json.load(file)

# Filter data for "investments" category
investments_data = [item for item in data if 'investments' in item['tag']]

# Update the "tag" values for "investments" category
for i, item in enumerate(investments_data):
    item['tag'] = f"investments {i+1}"

# Filter data for "cards" category
cards_data = [item for item in data if 'cards' in item['tag']]

# Update the "tag" values for "cards" category and restart numbering
for i, item in enumerate(cards_data):
    item['tag'] = f"cards {i+1}"

# Combine the updated data for both categories
formatted_data = investments_data + cards_data

# Write the updated data to a new JSON file
with open('formatted_data.json', 'w', encoding='utf-8') as file:
    json.dump(formatted_data, file, indent=4, ensure_ascii=False)
