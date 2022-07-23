text = "I am learning Python. Becoming Python Pro"
count = 0
if len(text) > 0:
    count = 1
for char in text:
    if char == ' ':
        count = count + 1
print("Your total number of words is", count)