from random import sample

def get_password(n=8) -> str:
    hub = '0123456789ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return "".join(sample(hub, n))


print(get_password())
