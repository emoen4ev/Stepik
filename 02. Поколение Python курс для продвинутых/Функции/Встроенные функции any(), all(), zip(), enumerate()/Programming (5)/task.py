def is_good_password(password):
    if len(password) < 7:
        return False
    if not any(i.isdigit() for i in password):
        return False
    if not any(i.isupper() for i in password):
        return False
    if not any(i.islower() for i in password):
        return False
    return True


psw = input()

if is_good_password(psw):
    print("YES")
else:
    print("NO")