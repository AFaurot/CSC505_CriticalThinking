def main():
    print("---DESCRIPTION OF UI ELEMENTS---")
    # Dictionary to associate page names with their descriptions
    pages = {"Home Menu" : "Displays shopping list and options menu UI elements.",
             "Shopping List": "Options to modify save or delete lists. Opens the add/edit item form.",
             "Add/Edit Item Form": "Opened from shopping menu and allows input of item details.",
             "Options Menu": "Options to register a user, modify user details, "
                             "accessibility settings, login, and logout."}
    # Loop to print the pages dictionary
    for page, description in pages.items():
        print("Page Name: {}\nDescription: {}\n".format(page, description))
    print("---PROCESS FLOW---:\nHome Page --> Shopping List or Home page --> Options Menu")
    print("Shopping List <--> Add/Edit Item Form")


if __name__== '__main__': main()
