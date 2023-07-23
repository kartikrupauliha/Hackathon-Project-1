import json

# Read the JSON file
with open('new.json', 'r', encoding='utf-8') as file:
    json_content = file.read()

# Find the position of the extra closing bracket
position = json_content.rfind(']')

# Check if the closing bracket is inside a string
if json_content.count('"', 0, position) % 2 != 0:
    print("Extra closing bracket inside a string. Ignoring.")

else:
    if position != -1:
        # Remove the extra closing bracket
        corrected_json = json_content[:position] + json_content[position+1:]
        print("Extra closing bracket removed.")
    else:
        corrected_json = json_content
        print("No extra closing bracket found.")

    # Write the corrected JSON to a new file
    with open('corrected_file.json', 'w', encoding='utf-8') as file:
        file.write(corrected_json)

    print("Corrected JSON file created.")
