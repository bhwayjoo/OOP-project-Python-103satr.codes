import datetime

class Bank:
    def __init__(self, client, Billing):
        self.__client = client
        self.__Billing = Billing

    def setClient(self):
        return self.__client

    def setBilling(self):
        return self.__Billing

    def TopUpTheBankBalance(self, Balance):
        self.__Billing += Balance
        return self.__Billing

    def WithdrawalTheBankBalance(self, Balance):
        if self.__Billing >= Balance:
            self.__Billing -= Balance
            return self.__Billing
        else:
            return -1  # Indicate insufficient balance

    def modifyBilling(self, newbilling):
        self.__Billing = newbilling

clients = []

while True:
    option = input('Enter your choice \n 1. add a new client \n 2. Billing\n 0. exit\n ')
    if option == "1":
        name = input('What\'s your name?\n')
        clt = Bank(name, 0)
        clients.append(clt)
    elif option == "2":
        cltName = input("Type your name: ")
        for client in clients:
            now = datetime.datetime.now()
            if cltName == client.setClient():
                op = input('Enter your choice\n 1. show your balance \n 2. Top up the bank balance\n 3. Withdrawal the bank balance\n')
                if op == '1':
                    print(f"Hi {client.setClient()}, your balance is {client.setBilling()}")

                elif op == '2':
                    value = int(input('Type the balance you want to add: '))
                    client.TopUpTheBankBalance(value)
                    print(f"Your balance was {client.setBilling() - value}$, and it has become {client.setBilling()}$")
                    dt_string = now.strftime(f"{value}$ were deposited to your bank balance on %A, %d %B at %Y %I:%M %p")
                    print("Date and time =", dt_string)
                elif op == '3':
                    value = int(input('Type the balance you want to withdraw: '))
                    new_balance = client.WithdrawalTheBankBalance(value)
                    if new_balance != -1:
                        print(f"Your balance was {client.setBilling() + value}$, and it has become {new_balance}$")
                        dt_string = now.strftime(
                            f"{value}$ were deducted from your bank balance on %A, %d %B at %Y %I:%M %p")
                        print("Date and time =", dt_string)
                    else:
                        print('Insufficient balance to perform the transaction.')
            else:
                print('Invalid name')

    elif option == "0":
        break
    else:
        print("Invalid option")

print('Thanks for joining!')
