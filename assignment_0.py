import json

def validate_username(username):
    string_check = '[@_!#$%^&*()<>?/\|}{~:]'
    if "@." in username:
        print("Invalid input @ should not precede .")
        main()
    elif "@" not in username or "." not in username or "com" not in username:
        print("Please enter username in format name@domain.com")
        main()
    elif username[0] in string_check:
        print("Invalid input, email should not start with special characters")
        main()
    else:
        return True

def validate_password(passwd):
    digit_found = 0
    sc_found = 0
    uc_found = 0
    lc_found =0
    string_check = '[@_!#$%^&*()<>?/\|}{~:]'
    if len(passwd) < 5 or len(passwd) > 16:
        print("Invalid length, password should be > 5 and < 16")
        main()
    for char in string_check:
        if char in passwd:
            sc_found = 1
    for char in passwd:
        if str(char).isupper():
            uc_found = 1
        if str(char).islower():
            lc_found = 1
        if str(char).isdigit():
            digit_found = 1
    if digit_found == 0:
        print ("Password should have at-least one digit")
        main()
    elif sc_found == 0:
        print ("Password should have at-least one special character")
        main()
    elif uc_found == 0:
        print("Password should have at-least one upper case character")
        main()
    elif lc_found == 0:
        print("Password should have at-least one lower case character")
        main()
    else:
        return True

def register():
    username = input("Enter the username in the following format name@domain.com \n").strip()
    passwd = input("Please enter the password \n").strip()
    validate_username(username)
    validate_password(passwd)
    f1 = open("users.txt", "r")
    data = json.load(f1)
    data['users'].append({
        'username': username,
        'passwd': passwd
    })
    f1.close()
    with open('users.txt', 'w') as outfile:
        json.dump(data, outfile)

def login():
    username = input("Enter the username in the following format name@domain.com \n").strip()
    forgot_passwd = input("Forgot password input [Y/N]").strip()
    if forgot_passwd.lower() == "n":
        passwd = input("Please enter the password \n").strip()
        return username, forgot_passwd, passwd
    elif forgot_passwd.lower() == "y":
        passwd = ""
        return username, forgot_passwd, passwd
    else:
        print("Invalid Input for Forgot Password")
        main()



def main():
    username, forgot_passwd, passwd = login()
    user_found = 0
    passwd_correct = 0
    with open('users.txt', 'r') as json_file:
        data = json.load(json_file)
        for p in data['users']:
            if username == p["username"]:
                user_found = 1
                if forgot_passwd.lower() == "y":
                    print("Your password is {}".format(p["passwd"]))
                    print("Please use your credentials to login again")
                    main()
                elif passwd == p["passwd"] and forgot_passwd.lower() == "n":
                    passwd_correct = 1
                    print("Login successful")
                    exit(0)
        if user_found == 0:
            print("Your username is not found, please register as a user")
            register()
            print("Registration complete, please use your credentials to login again")
            main()
        elif user_found == 1 and passwd_correct == 0:
            print("Incorrect password please try to login again")
            main()
main()


