filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    print("File opened successfully!")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied to read the file.")
