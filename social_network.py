#Various import Statements can go here
from  social_network_classes import SocialNetwork, Person
import social_network_ui
import random



#Create instance of main social network object
ai_social_network = SocialNetwork()
reload = input("Enter y to retrieve a previously saved account: ")
create1 = False
if reload == "y":
    ai_social_network.reload_social_media()
x = None
if len(ai_social_network.get_people()) >= 1:
    create1 = True
    x = ai_social_network.get_people()[random.ranint(0, len(ai_social_network.get_people()) - 1)]
    print("Currently accessing the account of " + x.get_name() + ".")

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            name = input("Enter the account name: ")
            age = input("Enter the account age: ")
            if create1:
                ai_social_network.save_social_media()
                ai_social_network.reload_social_media()
            x = ai_social_network.create_account(name, age, True)
            create1 = True

        elif choice == "2" and create1:
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    name = input("Enter the new name: ")
                    x.change_name(name)
                    age = input("Enter the new age: ")
                    x.change_age(age)
                    print("Name and age changed.")
                
                elif inner_menu_choice == "2":
                    z = x.quickadd()
                    if (z != 0):
                        x.add_friend(z)
                        print(z.get_name(), "was added to your list of friends.")
                    search = input("Search for an account? Enter y to continue: ")
                    if search == "y":
                        name = input("Enter the name of the friend that will be added: ")
                        age = input("Enter the age of the friend that will be added: ")
                        y = ai_social_network.create_account(name, age)
                        x.add_friend(y)
                        print(name + " was added to your list of friends.")
            
                elif inner_menu_choice == "3":
                    x.view_friends()

                elif inner_menu_choice == "4":
                    isnotfriend = True
                    friend = input("Enter the name of the friend you want to block: ")
                    for i in range (len(x.get_friendslist())):
                        if x.get_friendslist()[i].get_name() == friend:
                            isnotfriend = False
                            doubleblock = input("Blocking " + friend + " will remove your message history with them. To confirm blocking " + friend + ", enter y: ")
                            if (doubleblock == "y"):
                                x.block_friend(x.get_friendslist()[i])
                                print(friend + " was blocked.")
                                break
                            else:
                                print(friend + " was not blocked.")
                                break
                    if (isnotfriend):
                        print("You do not have a friend named " + friend + ".")
                
                elif inner_menu_choice == "5":
                    notsent = True
                    friend = input("Enter the name of the friend that will recieve the message: ")
                    for i in range (len(x.get_friendslist())):
                        if x.get_friendslist()[i].get_name() == friend:
                            message = input("Enter what you want to send: ")
                            x.send_message(x.get_friendslist()[i], message)
                            notsent = False
                            print("Message sent")
                            break
                    if (notsent):
                        print("You do not have a friend named " + friend + ".")
                
                elif inner_menu_choice == "6":
                    x.view_messages()

                elif inner_menu_choice == "7":
                    break

                else:
                    print("Your input is invalid. Try Again!")
                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            notaccount = True
            name = input("Enter the name of the account that will be switched to: ")
            for i in range(len(ai_social_network.get_people())):
                if ai_social_network.get_people()[i].get_name() == name:
                    ai_social_network.save_social_media()
                    ai_social_network.reload_social_media()
                    x = ai_social_network.switch_account(i)
                    print("Now accessing the account of " + name + ".")
                    notaccount = False
                    break
            if (notaccount):
                print("You do not own an account named " + name + ".")

        elif choice == "4":
            ai_social_network.save_social_media()
            print("Thank you for visiting. Goodbye.")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()