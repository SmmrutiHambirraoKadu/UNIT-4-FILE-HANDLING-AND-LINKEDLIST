# Writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.close()

# Reading from file
file = open("sample.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# Appending to file
file = open("sample.txt", "a")
file.write("This is an appended line.\n")
file.close()

# Reading again
file = open("sample.txt", "r")
print("Updated Content:\n", file.read())
file.close()
