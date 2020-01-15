def get_passwords(file):
    passwords = []
    with open(file) as f:
        for line in f:
            passwords.append(line)
    return passwords
