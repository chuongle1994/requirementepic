import ast
def send_message(usersName):
    recipient = input("\nEnter the username of the person you want to send a message to: ")
    with open("membership.txt", "r") as file:
        for line in file:
            data = ast.literal_eval(line)
    with open("friendList.txt", "r") as f:
        for FriendLine in f:
            FriendData = ast.literal_eval(FriendLine)
    with open("profile.txt", "r") as file1:                                  
        for data1 in file1:
            lines = ast.literal_eval(data1)    
            if data["Membership_Type"] == "Standard" and data["Username"] == usersName:
                if FriendData["Friend Lists"] == recipient and FriendData["Username"] != usersName:
                        message = input("\nPlease enter your message: ")
                        #store_message(sender, recipient, message)
                        print("\nMessage Has Been Sent.\n")
                        return
                else: 
                        print("I'm sorry, you are not friends with that person.")
            if data["Membership_Type"] == "Plus" and data["Username"] == usersName:   
                if lines["Username"] == recipient and lines["Username"] != usersName:
                    message = input("\nPlease enter your message: ")
                    #store_message(sender, recipient, message)
                    print("\nMessage Has Been Sent.\n")
                    return
                else:
                    print("I'm sorry, This person is not in the system yet.")
                    return
         
        
            
        
                            
    
                
            
            
            
    