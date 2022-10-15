import createAccountFunctions, friendList, json
def test_pending():
    pendingFriend = {"Username": "username", "Friend Lists": [], "Pending Lists": ["chuong"]}
    with open('friendList.txt', 'w') as file:
        file.write(json.dumps(pendingFriend))
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    assert friendList.pendingData("username") == ["chuong"]
