# Simple Login System
# -------------------
# This program allows users to register and log in with a username and password.

# Welcome message
print('\033[1m' + 'Welcome to Login System' + '\033[0m')
print('-------------------------------------------------')

# Function to display menu options
def Menu():
    print('\n Menu Options')
    print('''
    1) Register
    2) Login
    3) Exit
    ''')

# Account dictionary
Accounts = {'Ben': '1'}

# Function to log in a user
def Login(username, password):
    global Accounts
    if username in Accounts and Accounts[username] == password:
        print('\n\nLogin successful')
    else:
        print("This account doesn't exist!")

# Function to register a new user
def Register(username, password):
    global Accounts
    Accounts[username] = password
    if username in Accounts and Accounts[username] == password:
        print('Account Created!')
    else:
        print('Error while creating account')

# Main loop
while True:
    Menu()
    choice = int(input('\n\nChoose an option: '))

    if choice == 1:
        # Register
        print('\033[1m' + 'Register' + '\033[0m')
        print('---------------------------------')
        
        NewUser = input('\n\nUsername: ')
        
        if NewUser in Accounts:
            print('This username already exists')
        else:
            Pass = input('Password: ')
            Length = len(Pass)
            
            if Length < 4:
                print('Password must be at least 4 characters')
            else:
                Register(NewUser, Pass)

    elif choice == 2:
        # Login
        print('\033[1m' + '\n\nLogin' + '\033[0m')
        print('---------------------------------')
        
        User = input('\n\nUsername: ')
        Pass = input('Password: ')
        
        Login(User, Pass)

    elif choice == 3:
        # Exit program
        print('Exiting')
        break

    else:
        # Invalid menu choice
        print('Invalid Input')
