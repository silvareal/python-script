#password regex
#regex for authentication of password
#must contain atleast a lower and uppercase
#must contain a character(#$$%^)
#must be longer than eight
import re
passwordRegex = re.compile(r'''(
    ^(?=.*[a-z].*[a-z])       #must contain atleast two lower case
    (?=.*[@#$%^&*])                #atleast one character
    (?=.*[A-Z].*[A-Z]*[A-Z])   #must cotain atleast three uppercase
    (?=.*[0-9].*[0-9])             #atleast three digits
    .{10,}
    $
    )''',re.VERBOSE)

def authenticate():
    text = input('input your password: ')
    search = passwordRegex.search(text)
    if not text:
        print('input text')
    elif search == None:
        print('password not strong enough...')
    else:
        print('you passed the password cipher test..')

authenticate()