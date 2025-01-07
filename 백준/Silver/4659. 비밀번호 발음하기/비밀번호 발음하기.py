import sys
input = sys.stdin.readline
mo = ['a','e','i','o','u']
def check(password):

    if not any(ch in mo for ch in password):
        return False

    for i in range(len(password)-2):
        if (password[i] in mo and password[i + 1] in mo and password[i + 2] in mo) or \
                (password[i] not in mo and password[i + 1] not in mo and password[i + 2] not in mo):
            return False
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in ['e','o']:
            return False
    return True
while True:
    password = input().rstrip()
    if password=='end':
        break
    if check(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")