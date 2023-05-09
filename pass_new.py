import secrets
def create_new(len,chars):
    return "".join(secrets.choice(chars)for _ in range(len))