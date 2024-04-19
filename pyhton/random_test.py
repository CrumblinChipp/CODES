import msvcrt, sys, os

accounts = {'librarian': {'password': 'librarian_admin','role': 'admin', 'books_burrowed': []},
            'student1': {'password': 'student1_pass', 'role': "student", 'books_burrowed': ['Biochemistry']}}

logged_in = None
role_key = None

def hidden_input(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = ''
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            sys.stdout.write('\n')
            break
        sys.stdout.write('*')
        sys.stdout.flush()
        password += char
    return password
def role(): # ALL FUNCTION ACCOUNTED FOR
    global logged_in, role_key
    while True:
        print("===========================================")
        username = input("Enter username: ")
        password = hidden_input("Enter password: ")
        if password == accounts[username]['password']:
            role_key = accounts[username]['role']
            print("Log in successful..")
            print("Press ENTER to continue..")
            input()
            if role_key == 'admin':
                print("admin goods")
            elif role_key == 'student':
                logged_in = username
        else:
            os.system('cls')
            print("WRONG PASSWORD")
                    
role()