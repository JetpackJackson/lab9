# Bailey Watkins
def encode(password):
    encoded_password = ""
    for char in password:
        newchar = str(int(char) + 3)
        encoded_password += str(int(newchar) % 10)
    return encoded_password
