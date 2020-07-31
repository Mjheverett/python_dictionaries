phonebook = {}

def phonebook_update():
    keep_updating = "Y"
    while keep_updating == "Y":
        print("")
        print("Electronic Phone Book")
        print("=====================")
        print("1. Look up an entry")
        print("2. Set an entry")
        print("3. Delete an entry")
        print("4. List all entries")
        print("5. Quit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            search_name = input("Name?: ")
            search_number = phonebook[search_name]
            print("Found entry for %s: %s" % (search_name, search_number))
        elif selection == 2:
            add_name = input("Name: ")
            add_phone = input("Phone Number: ")
            phonebook[add_name] = add_phone
            print("Entry stored for %s" % add_name)
        elif selection == 3:
            search_name = input("Name?: ")
            del phonebook[search_name]
            print("Deleted entry for %s" % search_name)
        elif selection == 4:
            for key, value in phonebook:
                print("Found entry for %s: %s" % (key, value))
        elif selection == 5:
            keep_updating = "N"
            print("Bye.")
        else:
            print("Please select a valid option (1-5)")

phonebook_update()