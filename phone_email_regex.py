import pyperclip , re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s.*(ext|x|ext).s*(\d{2,5}))?
    )''',re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9$%&*]+
    @
    [a-zA=Z.-]+
    (\.[a-zA-Z]{2,8})
    )''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for group in phoneRegex.findall(text):
    phone = '-'.join([group[1],group[3],group[5]])
    if group[8] != '':
        phone += 'X' + group[8]
    matches.append(group[0])

for group in emailRegex.findall(text):
    matches.append(group[0])
    if len(matches) > 0:
        for lines in matches:
            pyperclip.copy(lines)
            print('\n'.join(lines))
    else:
        print('not copied to clipboard')

