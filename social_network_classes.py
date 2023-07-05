import json
import random
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        print("Saving...")
        y = []
        for i in range(len(self.list_of_people)):
            works = []
            for j in range(len(self.list_of_people[i].get_friendslist())):
                works.append(SocialNetwork.toJson(self.list_of_people[i].get_friendslist()[j]))
            please = []
            for k in range(len(self.list_of_people[i].get_blocklist())):
                please.append(SocialNetwork.toJson(self.list_of_people[i].get_blocklist()[k]))
            x = {"Name" : self.list_of_people[i].get_name(), "Age" : self.list_of_people[i].get_age(), "Friends" : works, "Blocked" : please, "Inbox" : self.list_of_people[i].get_inbox()}
            y.append(x)
        with open('mydata.json', 'w') as f:
            json.dump(y, f)
        
    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        print("Loading...")
        f = open('mydata.json')
        y = json.load(f)
        for a in range(len(y) - 1, -1, -1):
            for b in range(a-1, -1, -1):
                if y[a] == y[b]:
                    del y[a]
        for i in range(len(y)):
            works = []
            for j in range (len(y[i].get("Friends"))):
                z = json.loads(y[i].get("Friends")[j])
                works.append(Person(z.get("id"), z.get("year"), z.get("friendlist"), z.get("blocklist"), z.get("inbox")))
            please = []
            for k in range (len(y[i].get("Blocked"))):
                w = json.loads(y[i].get("Friends")[j])
                please.append(Person(w.get("id"), w.get("year"), w.get("friendlist"), w.get("blocklist"), w.get("inbox")))
            p = Person(y[i].get("Name"), y[i].get("Age"), works, please, y[i].get("Inbox"))
            self.list_of_people.append(p)
        f.close()

    def switch_account(self, order):
        return self.list_of_people[order]
    
    def create_account(self, name, age, user = False, friendlist = [], blocklist = [], inbox = []):
        #implement function that creates account here
        print("Creating ...")
        p = Person(name, age, friendlist, blocklist, inbox)
        if user:
            self.list_of_people.append(p)
        return p
    
    def get_people(self):
        return self.list_of_people

class Person:
    def __init__(self, name, age, friendlist, blocklist, inbox):
        self.id = name
        self.year = age
        self.friendlist = friendlist
        self.blocklist = blocklist
        self.inbox = inbox
        self.mess = False

    def get_name(self):
        return self.id
    
    def change_name(self, name):
        self.id = name
    
    def get_age(self):
        return self.year
    
    def change_age(self, age):
        self.year = age
    
    def get_friendslist(self):
        return self.friendlist

    def get_blocklist(self):
        return self.blocklist
    
    def get_inbox(self):
        return self.inbox
    
    def get_message(self):
        return self.mess
    
    def set_message(self, value):
        self.mess = value

    def quickadd(self):
        loop = True
        print("\nQuick Add:")
        firstnpc = ["Elisa", "Dusty", "Frances", "Amy", "Lakeisha", "Arlie", "Cecilia", "Nicholas", "Terrence", "Freddie", "Angelina", "Delmar", "Rudolph", "Roy", "Dylan", "John", "Dewey", "Elvis", "Richard", "Parker", "Camille", "Florentino", "Alexis", "Alma", "Desmond", "Olen", "Carrie", "Hannah", "Lilly", "Lauri", "Chelsea", "Mariana", "Rachelle", "Jan", "Prince", "Lane", "Virginia", "Eli", "Cory", "Doris", "Carole", "Luisa", "Darrell", "Morris", "Richie", "Sonja", "Joel", "Estela", "Malcolm", "Charlene"]
        lastnpc = ["Hayden", "Rodriguez", "Cowan", "Fay", "Schaefer", "Montgomery", "Hooper", "Bender", "Harding", "Curtis", "Middleton", "Caldwell", "Robertson", "Peck", "Richmond", "Fuentes", "Schmidt", "Blevins", "Hammond", "Flynn", "Boyd", "Patterson", "Hagan", "Joyce", "Hawkins", "Black", "Kane", "Terry", "Richards", "Riley", "Hampton", "Gifford", "Bean", "Sheridan", "Bolton", "Lang", "Louis", "Vazquez", "Sampson", "Rollins", "Duncan", "Buck", "Pitts", "Diaz", "York", "Kennedy", "Coleman", "Holloway", "McAllister", "Slaughter"]
        name1 = str(random.choice(firstnpc)) +  " " + str(random.choice(lastnpc))
        age1 = random.randint(12,72)
        name2 = str(random.choice(firstnpc)) + " " + str(random.choice(lastnpc))
        age2 = random.randint(12,72)
        name3 = str(random.choice(firstnpc)) + " " + str(random.choice(lastnpc))
        age3 = random.randint(12,72)
        name4 = str(random.choice(firstnpc)) + " " + str(random.choice(lastnpc))
        age4 = random.randint(12,72)
        name5 = str(random.choice(firstnpc)) + " " + str(random.choice(lastnpc))
        age5 = random.randint(12,72)
        print("1.", name1 + ",", age1)
        print("2.", name2 + ",", age2)
        print("3.", name3 + ",", age3)
        print("4.", name4 + ",", age4)
        print("5.", name5 + ",", age5)
        print("6. Skip")
        while (loop):
            choice = input("\nEnter the number of the name you want to quick add: ")
            if choice == "1":
                account = Person(name1, age1, friendlist = [], blocklist = [], inbox = [])
                loop = False
            elif choice == "2":
                account = Person(name2, age2, friendlist = [], blocklist = [], inbox = [])
                loop = False
            elif choice == "3":
                account = Person(name3, age3, friendlist = [], blocklist = [], inbox = [])
                loop = False
            elif choice == "4":
                account = Person(name4, age4, friendlist = [], blocklist = [], inbox = [])
                loop = False
            elif choice == "5":
                account = Person(name5, age5, friendlist = [], blocklist =[], inbox = [])
                loop = False
            elif choice == "6":
                account = 0
                loop = False
            else:
                print("Your input is invalid. Try Again!")
        return account

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        self.inbox.append(person_object.get_inbox())

    def view_friends(self):
        print("\nNames of friends: ", end = "")
        for i in range(len(self.friendlist)):
            if (i != len(self.friendlist) - 1):
                print(self.friendlist[i].get_name(), end = ", ")
            else:
                print(self.friendlist[i].get_name())
        print("Blocked friends: ", end = "")
        for j in range(len(self.blocklist)):
            if (j != len(self.blocklist) - 1):
                print(self.blocklist[j].get_name(), end = ", ")
            else:
                print(self.blocklist[j].get_name())
                print()

    def block_friend(self, person_object):
        self.blocklist.append(person_object)
        self.friendlist.remove(person_object)
        self.inbox.remove(person_object.get_inbox())

    def send_message(self, person_object, message):
        #implement sending message to friend here
        npc = ["Yes", "It depends", "Definitely", "That's a tough one", "Possibly", "There's a slim chance", "It could be", "I'm afraid so", "Ask me again", "I'm not convinced", "Not likely at all", "I doubt it strongly", "Ask me later", "I can't tell", "It's a remote possibility", "It's contrary to expectation", "Not a snowball's chance in hell", "Only time will tell", "No way", "It's not likely", "Ask me tomorrow", "Highly improbable", "I'm not taking any chances", "I don't have an answer", "It's undecided", "I'm not sure where to start", "I'm not sure how to react", "I need more data", "I need to investigate it", "I need to evaluate it", "I'm not confident enough to answer", "I'm in between", "I'm flip-flopping", "I'm uncertain of the outcome", "It's hard to deduce", "It's hard to imagine", "I'm in a quandary", "I'm baffled", "I'm confused", "I'm undecided", "I'm torn", "I'm in a state of uncertainty", "I'm vacillating", "I'm in two minds", "I'm in a state of paralysis", "I'm in a lost cause", "I'm in a quandary", "I'm in a jam", "I'm in a quagmire", "I'm in a catch-22"]
        person_object.get_inbox().append(message)
        if (random.randint(1,5) == 2):
            response = random.choice(npc)
            person_object.get_inbox().append(response)
            person_object.set_message(True)

    def view_messages(self):
        npc = ["Yes", "It depends", "Definitely", "That's a tough one", "Possibly", "There's a slim chance", "It could be", "I'm afraid so", "Ask me again", "I'm not convinced", "Not likely at all", "I doubt it strongly", "Ask me later", "I can't tell", "It's a remote possibility", "It's contrary to expectation", "Not a snowball's chance in hell", "Only time will tell", "No way", "It's not likely", "Ask me tomorrow", "Highly improbable", "I'm not taking any chances", "I don't have an answer", "It's undecided", "I'm not sure where to start", "I'm not sure how to react", "I need more data", "I need to investigate it", "I need to evaluate it", "I'm not confident enough to answer", "I'm in between", "I'm flip-flopping", "I'm uncertain of the outcome", "It's hard to deduce", "It's hard to imagine", "I'm in a quandary", "I'm baffled", "I'm confused", "I'm undecided", "I'm torn", "I'm in a state of uncertainty", "I'm vacillating", "I'm in two minds", "I'm in a state of paralysis", "I'm in a lost cause", "I'm in a quandary", "I'm in a jam", "I'm in a quagmire", "I'm in a catch-22"]
        for i in range(len(self.friendlist)):
            print("\nName: ", self.friendlist[i].get_name())
            print("Messages: ")
            if (random.randint(1,5) == 2) and (not(self.friendlist[i].get_message())) and (len(self.friendlist[i].get_inbox) % 2 == 1):
                response = random.choice(npc)
                self.friendlist[i].get_inbox().append(response)
                self.friendlist[i].set_message(True)
            if (self.friendlist[i].get_message()):
                print("\nYou have a new message from", self.friendlist[i].get_name(),"\n")
            for j in range(len(self.friendlist[i].get_inbox())):
                if (j % 2 == 0):
                    print("\t\t" + self.friendlist[i].get_inbox()[j])
                else:
                    print(self.friendlist[i].get_inbox()[j])
            if (self.friendlist[i].get_message()):
                decision = input("Do you want to respond to the message? Enter y to continue: ")
                self.friendlist[i].set_message(False)
                if decision == "y":
                    message = input("Enter the message: ")
                    self.send_message(self.friendlist[i], message)
                    print("Message sent.")