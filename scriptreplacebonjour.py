search_text = "hello"
replace_text = "bonjour"
with open(r'patate.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
with open(r'patate.txt', 'w') as file:
    file.write(data)
print("Text replaced")