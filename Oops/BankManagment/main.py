import json
import random
import string
from pathlib import Path



class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")

    except Exception as err:
        print("an exception occured as {err} ")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def createAccount(self):
        info = {
            "name" : input("tell your name:- "),
            "age" : int(input("tell your age:-")),
            "email" : input("tell your email:- "),
            "pin" : int(input("tell your 4 number pin:- ")),
            "accountNo" : Bank.__accountGenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully ")
            for i in info:
                print(f"{i} : {info[i]} ")
            print("plese note down your account number")

            Bank .data.append(info)
            Bank.__update()

    def depositMoney(self):
        accnumber = input("Please tell your account number:- ")
        pin = int(input("Please tell your pin aswell:- "))
        # print(Bank.data)
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if not userdata:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to depositL:- "))
            if amount > 10000 and amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0 .")
            else:
                # print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")


    def withdrawMoney(self):
        accnumber = input("Please tell your account number:- ")
        pin = int(input("Please tell your pin aswell:- "))
        # print(Bank.data)
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if not userdata:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to withdraw:- "))
            if userdata[0]['balance'] < amount:
                print("sorry you don't have that much money .")
            else:
                # print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully ")

    def showDetails(self):
        accnumber = input("Please tell your account number:- ")
        pin = int(input("Please tell your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No such user found")
            return
        
        # print(userdata)
        print("Your information are \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updateDetails(self):
        accnumber = input("Please tell your account number:- ")
        pin = int(input("Please tell your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("no such user found ")
        else:
            print("You can't change the age, account number, balance ")
            print("Fill the details for change or leave it empty if no change ")

            newdata = {
                "name": input("please tell new name or press enter: "),
                "email": input("please tell your new email or press enter to skip: "),
                "pin": input("Please new Pin or press enter to skip: ")
            }
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            else:
                newdata['pin'] = int(newdata['pin'])

            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")

    def userDelete(self):
        accnumber = input("Please tell your account number:- ")
        pin = int(input("Please tell your pin aswell:- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No such user found ")
        else:
            check = input("press y if you actuaally want to delete the account or press n:- ")
            if(check == 'n' or check == 'N'):
                print("btpassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.__update()



user = Bank()
print("press 1 for creating an account ")
print("press 2 for Depositing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details ")
print("press 6 for deleting your account ")

check = int(input("tell your response :-"))

if check == 1:
    user.createAccount()
if check == 2:
    user.depositMoney()
if check == 3:
    user.withdrawMoney()
if check == 4:
    user.showDetails()
if check == 5:
    user.updateDetails()
if check == 6:
    user.userDelete()


