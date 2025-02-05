import re

# Read the file content
with open('1_1Data Cleaning Car_drop_model.ipynb', 'r') as file:
    content = file.read()

# Replace all instances of distplot with histplot and add kde=True
content = re.sub(r'sns\.distplot\(([^)]+)\)', r'sns.histplot(\1, kde=True)', content)

# Write the modified content back to the file
with open('1_1Data Cleaning Car_drop_model.ipynb', 'w') as file:
    file.write(content)