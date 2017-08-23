invites = {}
options = ["add","list","approve","delete", "quit"]
prompt = "pick any of the options (%s):" % ", ".join(options)
status_1 = "approved"
status_2 = "unapproved"

while True:
    inp = input(prompt)
    if inp not in options:
        continue
    if inp=="add":
        name = input("enter name: ")
        if not name:
            continue
        invites[name] = status_2
    
    elif inp =="list":
        for name, staus in invites.items():
            print("%s (%s)" % (name,staus))
    elif inp =="approve":
        for name in invites:
            if invites[name] == status_2:
                break
        else:
            print("choose a %s name,cos word is %s" % (status_2,status_1))
            continue
        while True:
            print("please enter a valid name fom the list")
            unapproved = []
            for name in invites:
                if invites[name] == status_2:
                    unapproved.append(name)
            print(", ".join(unapproved))
            name = input("input name")
            if not name:
                break
            if name in unapproved:
                invites[name] = status_1
                print('%s(%s)' % (name,status_1))
                break

    elif inp =='delete':
        if not invites:
            print('there must be invites before you delete')
            continue
        while True: 
            print('please enter a valid name from the list below')
            for name ,status in invites.items():
                print('%s (%s)' % (name, status))
            name = input('enter name: ')
            if not name:
                break
            if name in invites:
                del invites[name]
                print('%s deleted' % name)
                break
    elif inp == 'quit':
        print('Quiting program..')
        print('final program follows')

        for name, status in invites.items():
            print('%s(%s)' % (name, status))
        break

