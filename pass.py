#! /usr/bin/python3
# pass.py - Saves and loads secure passwords to the clipboard.
# Usage: ./pass.py save <keyword> - Save a new password from the clipboard.
#        ./pass.py list - Loads all keywords to clipboard.
#        ./pass.py <keyword> - Loads password to clipboard.
#        ./pass.py validate - Validate the strong of a password.
#        ./pass.py delete <keyword> - Delete a saved password.
#        ./pass.py deleteall - Delete all the saved passowrds.
#        ./pass.py help - print this comment on the console.

import shelve, pyperclip, sys, re

passShelf = shelve.open('pass')

strongPwdRegex = re.compile(r'''(
    ^(?=.*?[A-Z])           # At least one upper case
    (?=.*?[a-z])            # At least one lower case
    (?=.*?[0-9])            # At least one digit
    (?=.*?[#?!@$%^&*-])     # At least one special character
    .{8,}                   # Minimum eight in lenght
    $
)''', re.VERBOSE)


if len(sys.argv) == 3:
    # Verify password, and save clipboard content.
    if sys.argv[1].lower() == 'save':
        mo = str(strongPwdRegex.search(sys.argv[2]))
        if not mo:
            print('Not strong, bling blong')
        else:
            print('Long, Strong, and down to get the crypto on')
            passShelf[sys.argv[2]] = pyperclip.paste()
            print('The clipboard is not a safe option, do not forget',
            'to copy something different once you finish to use this script.')

    # Delete one element
    elif sys.argv[1].lower() == 'delete':
        verification = input('you want to delete %s? (Y/N): ' %sys.argv[2])
        if verification.lower() == 'y':
            del passShelf[sys.argv[2]]


elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(passShelf.keys())))


    # Return a password from a keyword
    elif sys.argv[1] in passShelf:
        pyperclip.copy(passShelf[sys.argv[1]])
        print('The clipboard is not a safe option, do not forget to copy something different once you finish to use this script.')


    # Validate strong of a password
    elif sys.argv[1].lower() == 'validate':
        mo = str(strongPwdRegex.search(sys.argv[2]))
        if not mo:
            print('Not strong, bling blong')
        else:
            print('Long, Strong, and down to get the crypto on')


    # Remove all the passwords saved
    elif sys.argv[1].lower() == 'deleteall':
        verification = input('you want to delete everything? (Y/N): ')
        if verification.lower() == 'y':
            passShelf.clear()

    elif sys.argv[1].lower() == 'help':
        # Help keyword
        print('''
        pass.py - Saves and loads secure passwords to the clipboard.
        Usage: ./pass.py save <keyword> - Save a new password from the clipboard.
               ./pass.py list - Loads all keywords to clipboard.
               ./pass.py <keyword> - Loads password to clipboard.
               ./pass.py validate - Validate the strong of a password.
               ./pass.py delete <keyword> - Delete a saved password.
               ./pass.py deleteall - Delete all the saved passowrds.
               ./pass.py help - print this comment on the console.
        ''')
