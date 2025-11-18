class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """Bu metod keyingi klaslarda qayta aniqlanadi (polimorfizm)"""
        raise NotImplementedError("withdraw metodi subclasslarda aniqlanishi kerak")

    def get_balance(self):
        return self.__balance

    
    def _change_balance(self, amount):
        """Balansni o‘zgartirish (musbat yoki manfiy)"""
        self.__balance += amount


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        fee = amount * 0.01
        total = amount + fee

        if self.get_balance() >= total:
            self._change_balance(-total)
            print(f"SavingsAccount: {amount} yechildi (+{fee} foiz).")
        else:
            print("SavingsAccount: Mablag‘ yetarli emas.")


class CheckingAccount(BankAccount):
    def __init__(self, initial_balance=0, overdraft_limit=100):
        super().__init__(initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() + self.overdraft_limit >= amount:
            self._change_balance(-amount)
            print(f"CheckingAccount: {amount} yechildi (overdraft mumkin).")
        else:
            print("CheckingAccount: Limitdan oshib ketdi.")



sa = SavingsAccount(500)     
ca = CheckingAccount(100, 50)  

accounts = [sa, ca]

for acc in accounts:
    acc.withdraw(120)


for acc in accounts:
    print("Final balans:", acc.get_balance())
