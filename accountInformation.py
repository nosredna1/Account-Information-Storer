# Empty list of accounts
accounts = []

# Store information into accounts
storing = True

print("Type DONE for username when finished.")
while storing:
    # Take user input for username, password, and site used
    username = input("Enter your username: ")

    # Checks whether user is done inputing accounts
    if username.upper() == 'DONE':
        storing = False
    else:
        password = input("Enter your password: ")
        site = input("Enter the site for this account: ")
        account = {'username': username,
            'password': password,
            'site': site,
            }
        accounts.append(account)

# Extract corresponding usernames, passwords, and sites in separate lists
username = [i['username'] for i in accounts]
password = [i['password'] for i in accounts]
site = [i['site'] for i in accounts]

# File I/O
f = open('Account List.txt', 'w')
for i in range(len(username)):
    f.write("Username: " + username[i] + "\n")
    f.write("Password: " + password[i] + "\n")
    f.write("Site: " + site[i] + "\n\n")
f.close()
