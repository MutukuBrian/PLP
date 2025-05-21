try:
    file = open("sample.txt", "r")
    data = file.read()
    print("File found")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()