# Simple Login System
# -------------------
# This program allows users to register and log in with a username and password.

# Account dictionary
Accounts = {'Ben': '1'}

# Function to display menu options
def Menu():
    print('\n Menu Options')
    print('''
    1) Register
    2) Login
    3) Exit
    ''')

# Function to log in a user
def Login(username, password):
    if username in Accounts and Accounts[username] == password:
        print('\n\nLogin successful')
        return True
    else:
        print("This account doesn't exist!")
        return False

# Function to register a new user
def Register(username, password):
    Accounts[username] = password
    if username in Accounts and Accounts[username] == password:
        print('Account Created!')
        return True
    else:
        print('Error while creating account')
        return False

# Test functions for pytest
def test_login_success():
    """Test successful login"""
    assert Login('Ben', '1') == True

def test_login_failure():
    """Test failed login with wrong password"""
    assert Login('Ben', 'wrong') == False

def test_register_new_user():
    """Test user registration"""
    initial_count = len(Accounts)
    Register('TestUser', 'pass123')
    assert 'TestUser' in Accounts
    assert Accounts['TestUser'] == 'pass123'

# Main loop - only runs when script is executed directly
if __name__ == '__main__':
    # Welcome message
    print('\033[1m' + 'Welcome to Login System' + '\033[0m')
    print('-------------------------------------------------')
    
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
