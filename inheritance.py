class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, recipient, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Kes{amount} sent to {recipient} successfully.")
        else:
            print("Insufficient balance")


class Personal_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"You have successfully bought Kes {amount} airtime from your account.")
        else:
            print("Insufficient balance to purchase airtime.")


class Business_Mpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"Kes{amount} received successfully.")


personal = Personal_Mpesa(5000, 768543934, 13424522)
personal.send_money(756830954, 1000)
personal.buy_airtime(5000)
Business_Mpesa = Business_Mpesa(550000, 769243444, "Furniture Palace Kenya")
Business_Mpesa.receive_money(240000)
Business_Mpesa.send_money(757957594, 70000)
