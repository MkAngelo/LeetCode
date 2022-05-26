import string
def alphanumeric(password):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    abc = list(string.ascii_lowercase)
    aBC = list(string.ascii_uppercase)
    alpnum = num + abc + aBC
    for l in password:
        if l not in alpnum:
            return False
    return True
if __name__ == "__main__":
    print(alphanumeric('PassW0rd'))