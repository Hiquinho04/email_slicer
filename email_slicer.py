email = input("Add your best email: ").strip()
user = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f'your user email is {user}')
print(f'your email domain is {domain}')