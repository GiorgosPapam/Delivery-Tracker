import datetime #Tool to create date
import csv     #Tool to make csv readable

# Create an empty dictonary
Client = {}
#A global variable that counts how many money customers has spent
total_amount=0
#A global variable that count how many orders customers have made
orders = 0
# These three is a counter that count how many orders each user has made
tom=0
george=0
nick=0

#A fanction that runs the main prpgram
def main():
    print("Please Login to your Account")
    user = login() # Call login function and save the loged user in user variable for future actions
    print("Welcome ",user)
    print("")
    print("Do you want to make an Order or check the System ?")
    choose = input("Choose: ")
    start = True
    while (start == True):
        while (choose != "Order" and choose != "System"):
            print("Please enter the correct choise! ( Order or System )")
            choose = input("Choose: ")
        if (choose == "Order" or choose == "order"):
            Order(user) # Call Order function for current user
        elif ( choose == "System" or choose == "system"):
            System() #Call System function
        answer = input("Do you want to change user? y/n? : ")
        while ( answer !="y" and answer != "n" ):
            print("Error!")
            answer = input("Do you want to change user? y/n? : ")
        if ( answer == "n" ):
            again=input("Do you want to order again ? y/n :")
            while ( again !="y" and again != "n" ):
                print("Error!")
                again = input("Do you want to order again? y/n? : ")
            if (again == "y"):
                choose = "Order"
            elif (again == "n"):
                print("Do you want to check the system or exit ?")
                select = input("System or Exit? : ")
                while ( select !="System" and select != "Exit" ):
                    print("Error!")
                    select = input("System or Exit? y/n? : ")
                if ( select == "System" or select == "system"):
                    choose = "System"
                elif (select == "Exit" or select == "exit"):
                        start = False
        elif ( answer == "y" ):
            main()
        
        
        
                
            
    




def System():
    date =  datetime.date.today().strftime("%d-%m-%Y") #Create a date
    print("System Menu")
    print("")
    print("Please select one of the above")
    print("1) Numbers of order placed by one specific customer")
    print("2) Number of orders in one specific day")
    print("3) Total amount of all orders delivered")
    print("4) Total amount of the orders placed by a specific customer")
    print("5) Total amount of the orders placed by a specific day")
    print("6) Export the Customers names in .txt")
    print("7) Export the orders entered per userin .txt")
    print("8) Export all data in .csv")
    choose=int(input("Choose from 1 to 8: "))
    while ( choose < 1 or choose > 8): # Validity check for options 1-8 
        print("Error!")
        choose=int(input("Choose from 1 to 8: "))
    
    
    
    if ( choose == 1):
        print("The customers that we has were: ")
        for i in Client:
            print("ID:", i , Client[i]['Name'], Client[i]['Address'])
        c_id = input("Enter the ID of the Customer: ")
        found = False
        copy_Clients = Client.copy()
        while (found == False):
            for x in Client:
                if ( c_id == copy_Clients[x]['ID']):
                    found = True
                    i = x
                    break
                elif (int(c_id) > int(len(Client))):
                    print("ID not found!!")
                    c_id = input("Enter the correct ID: ")         
        print("The Customer ",Client[i]['Name']," with ID: ",i," has made ",Client[i]['Orders']," orders" )

    
    if (choose == 2):
        print("The number of orders in the date", date," is: ",orders)

    if (choose == 3):
        print("The total amount of the orders is : ",total_amount)
    
    
    if (choose == 4):
        y = 0
        print("The customers that we has were: ")
        for i in Client:
            print("ID:", y , Client[y]['Name'], Client[y]['Address'])
            y += 1
        c_id = input("Enter the ID of the Customer: ")
        found = False
        copy_Clients = Client.copy()
        while (found == False):
            for x in Client:
                if ( c_id == copy_Clients[x]['ID']):
                    found = True
                    i = x
                    break
                elif (int(c_id) > int(len(Client))):
                    print("ID not found!!")
                    c_id = input("Enter the correct ID: ")         
        print("The Customer ",Client[i]['Name']," with ID: ",i," has paid ",Client[i]['Amount']," euros." )
        
    if(choose == 5 ):
        print("In the date ",date," a total of ",total_amount,"€ has been made")
        
    if (choose == 6):# Saving the names of the clients into a txt document
            for i in Client:
                with open('ClientNames.txt', 'a') as Names:    # Saving the names of the clients into a txt document
                    Names.write("ID: "+ Client[i]['ID'] +" Name: "+Client[i]['Name']+"\n")
            print("Export done!")
    
    if (choose == 7):    # Saving the names of the clients into a txt document
        with open('Orders_Per_User.txt', 'a') as Orders_Per_User:    # Saving the names of the clients into a txt document
            Orders_Per_User.write("The user Tom has made "+ str(tom) +" orders.\n")
            Orders_Per_User.write("The user George has made "+ str(george) +" orders.\n")
            Orders_Per_User.write("The user Nick has made "+ str(nick) +" orders.")
        print("Export done!")

    if(choose == 8):
        with open('alldata.csv', 'w') as Alldata:
            writer = csv.writer(Alldata)
            writer.writerow(["ID", "Name", "Address", "Orders", "Amount", "Date"])
            for i in Client:
                writer.writerow([Client[i]['ID'] ,Client[i]['Name'] ,Client[i]['Address'], Client[i]['Orders'], Client[i]['Amount'], Client[i]['Date']])
        print("Export done!")
        
    
    














def Order(user):
    date = datetime.date.today().strftime("%d-%m-%Y") # Create date
    c_name = input("Enter the customer's name: ")
    c_address = input("Enter the customer's address: ")
    amount = int(input("Enter the order's amount: "))
    
    if (len(Client)==0):    # Check if Dictionary is empty. If is empy it creates a new Client
        New_Client = {}
        New_Client['Name'] = c_name
        New_Client['Address'] = c_address
        New_Client['Amount'] = amount
        New_Client['Date'] = date
        New_Client['Orders'] = 1
        new_client_id = len(Client) # Creates an id for each Client (first client will have ID 0 )
        New_Client['ID'] = str(new_client_id) # Saves the Client id 
        Client[new_client_id]= New_Client # Saves all the information for the Client 
    else:
        copy_Clients = Client.copy() # Copy the dict Client becouse it change size so i can scan it 
        
        for x in copy_Clients: #Repetition for scanning if the name and address we entered was already inside Client
            if (c_name == copy_Clients[x]['Name'] and c_address == copy_Clients[x]['Address']):
                found = True # if it find it it set to true
                i = x #It saves the line that name and address are located
                break #Stop the search becouse the if is true
            else:
                found = False
        
        if (found == True ): # If found = true we update the information for each customer. The thinks we update are the amount and the total orders per client 
            Client[i]['Amount'] = Client[i]['Amount'] + amount 
            Client[i]['Orders'] = Client[i]['Orders'] + 1
        else: # if found = false then create a new Client
            New_Client = {}
            New_Client['Name'] = c_name
            New_Client['Address'] = c_address
            New_Client['Amount'] = amount
            New_Client['Date'] = date
            New_Client['Orders'] = 1
            new_client_id = len(Client)
            New_Client['ID'] = str(new_client_id)
            Client[new_client_id]= New_Client
            
    global orders # Call the global variable orders to count the orders per day
    orders = orders +1
    
        
    global total_amount # Call the global variable total_amount to count how many money was made 
    total_amount = total_amount + amount
    
    global tom #Call a global variant tom to count how many orders did he made
    global george
    global nick
    
    if user=="Tom":    
        tom = tom +1    
    elif user=="George":
        george= george + 1
    elif user=="Nick":
       nick = nick + 1 

            
    

                    
    
    
    
    









#Login function
def login():
    accounts={ 
        "Tom":"tom",
        "George":"george",
        "Nick":"nick"
        } 
    print("Choose your username: Tom , George , Nick")
    username = input("Username: ")
    while ( username != "Tom" and username != "George" and username != "Nick"):   #Validited check for username
        print("Please enter the correct Username!")
        username = input("Username: ")
    print("Please enter the password for ",username)
    password = input("Password: ")
    while (password!=accounts[username]): #Validited check for password
        print("Wrong password! Try again!")
        password = input("Please enter the password for ",username,": ")
    return username # retuen to main the username
        

        


# without this the main function will not run / it calls the main function
if __name__=="__main__":
    main()