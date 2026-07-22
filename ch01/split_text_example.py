import re
text = "Hello, world. Is this---a test? Let's see how it works!"
result = re.split(r'([,.:;?_!"()\']|-|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)
