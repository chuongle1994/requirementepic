import createAccountFunctions, friendList
def test_pending():
    friendList.createFriendList("Dinhle")
    createAccountFunctions.storeData("trile", "Abcdef1!", "tri", "le", "tri le") # making an account defaults sms to 1 or "on"
    createAccountFunctions.storeData("danhle", "Abcdef1!", "danh", "le", "danh le") # making an account defaults sms to 1 or "on"
    assert friendList.requestFriend("trile", "Dinhle") == (1,0,0)
