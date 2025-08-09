# Write a Python program to read a text file(servers.txt) and print its contents
with open('servers.txt', 'r') as file:
    contents = file.read()
    print(contents)