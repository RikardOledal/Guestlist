import json
# display intro
def intro () :
    title = ' ** PhoneBook **'
    print ('*' * len(title))
    print (title)
    print ('*' * len(title))
intro ()
# PhoneBook operaions
def save_contacts (contacts, filename):
    with open (filename, 'w') as f:
        json.dump(contacts, f)
def print_contact (contact_info):
    print ()
def create_contact(name=None):
    if name is None:
        name = input ('Enter name:')
        phone = input ('Enter phone number:')
        email = input ('Enter email:').lower()
        while True:
            if len(phone) != 10:
                print("A phonenumber must be 10 digits")
                phone = input ('Enter phone number:')
            else:
                break
        return {'name':name, 'phone': phone, 'emai':email}
def phonebook (filename):
    with open(filename) as f:
        contacts = json.loads(f)
    while True:
        print (
'1. Add new entries',
'2. Search by first name',
'3. Search by second name',
'4. Search by full name',
'5. Search by telephone number',
'6. Search by city or state',
'7. Delete',
'8. Update',
'9. Exit'
)
# display_separator
print ('-' * 24)
# user input
choice = int(input('Please enter your choice:'))
while not choice.isdigit():
    print ('Invalid menu option.')
    choice = input('Please try again:')
choice = int(choice)
while choice > 8 or choice < 1 :
    print ('Invalid menu option.')
    choice = int(input('Please try again:'))
if choice == '1' :
    try:
        new_contact = create_contact()
    except:
        print('The phone numer entered is invalid')
    else:
        contacts[new_contact ['name']]= new_contact
        save_contacts (contacts, filename)
elif choice == '2':
    print_contact ({'name': 'NAME','phone':'PHONE','email': 'EMAIL'})
    for contacts in contacts.values():
        print_contact (contact)
elif choice == '3':
    search = input ('Please enter name:')
    try:
        print_contact(contacts[search])
    except KeyError:
        print ('Contact not found')
elif choice == '4':
    search = input ('please enter name:')
    try:
        print_contact(contacts[search])
    except KeyError:
        print ('Contact not found')
    else:
        try:
            contacts [search] = create_contact(search)
        except:
            print("wrong")
        else:
            save_contacts(contacts, filename)
elif choice =='5':
    search =input ('Please enter name:')
    try:
        contacts.pop (search)
    except KeyError:
        print ('Contact not found')
    else:
        save_contacts (constacts, filename)
elif choice == '6':
    print ('Ending PhoneBook. /nHave a nice day!')
else:
    print('Invalid Input! Try again.')