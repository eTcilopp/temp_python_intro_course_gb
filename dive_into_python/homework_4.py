"""
Напишите функцию для транспонирования матрицы
"""


def transpond(matrix):
    return list(map(list, zip(*matrix)))

assert transpond([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert transpond([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
assert transpond([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def make_dict(**kwargs):
    return dict((value, key) for key, value in kwargs.items())


assert make_dict(a=1, b=2, c=3) == {1: 'a', 2: 'b', 3: 'c'}
assert make_dict(a=1, b=2, c=3, d=1) == {1: 'd', 2: 'b', 3: 'c'}


"""
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сума пополнения и снятия кратны 50 у.е.
Процент за снятие 1.5% от сумны снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляется проценты 3%
Нельзя снять больше, чем на счете
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""

from decimal import Decimal


class ATM:
    def __init__(self,
                 multiplicity=50,
                 withdraw_percent=0.015,
                 min_withdraw_comission=30,
                 max_withdraw_comission=600,
                 interest=0.03,
                 interest_counter=3,
                 rich_tax=0.1, rich_tax_treshold=5_000_000):
        self.balance = Decimal(0)
        self.operation_counter = 0
        self.multiplicity = Decimal(multiplicity)
        self.withdraw_percent = Decimal(withdraw_percent)
        self.min_withdraw_comission = Decimal(min_withdraw_comission)
        self.max_withdraw_comission = Decimal(max_withdraw_comission)
        self.interest = Decimal(interest)
        self.interest_counter = interest_counter
        self.rich_tax = Decimal(rich_tax)
        self.rich_tax_treshold = Decimal(rich_tax_treshold)

    def get_withdraw_comission(self, amount: Decimal):
        comission = amount * self.withdraw_percent
        if comission < self.min_withdraw_comission:
            return self.min_withdraw_comission
        if comission > self.max_withdraw_comission:
            return self.max_withdraw_comission
        return comission

    def check_if_deposit_is_multiple_of_multiplicity(self, amount: Decimal):
        return amount % self.multiplicity == 0

    @property
    def counter_comission(self):
        self.operation_counter += 1
        print(f'{self.operation_counter = }')
        if self.operation_counter % self.interest_counter == 0:
            return self.balance * self.interest
        return 0

    @property
    def rich_tax_amount(self):
        if self.balance > self.rich_tax_treshold:
            return self.balance * self.rich_tax
        return 0

    @property
    def rounded_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount: Decimal):
        self.balance -= self.rich_tax_amount
        if not self.check_if_deposit_is_multiple_of_multiplicity(amount):
            return f'Rejected. Amount must be multiple of {self.multiplicity}. Balance: {self.rounded_balance}.'
        self.balance += amount
        self.balance += self.counter_comission
        self.balance -= self.get_withdraw_comission(amount)
        return f'Deposited {amount}. Balance: {self.rounded_balance}.'

    def withdraw(self, amount: Decimal):
        self.balance -= self.rich_tax_amount
        if self.balance - amount < 0:
            return f'Not enough money. Balance: {self.rounded_balance}.'
        if not self.check_if_deposit_is_multiple_of_multiplicity(amount):
            return f'Rejected. Amount must be multiple of {self.multiplicity}. Balance: {self.rounded_balance}.'
        self.balance -= amount
        self.balance += self.counter_comission
        self.balance -= self.get_withdraw_comission(amount)
        return f'Withdrawn {amount}. Balance: {self.rounded_balance}.'

    def exit(self):
        return f'Goodbye!. Balance: {self.rounded_balance}.'


def main():
    atm_client = ATM()
    while True:
        action = input('Enter action: 1 - deposit, 2 - withdraw, 3 - exit\n')
        if action == '1':
            amount = Decimal(input('Enter amount: '))
            print(atm_client.deposit(amount))
        elif action == '2':
            amount = Decimal(input('Enter amount: '))
            print(atm_client.withdraw(amount))
        elif action == '3':
            print(atm_client.exit())
            break
        else:
            print('Unknown action. Try again.')


if __name__ == '__main__':
    main()
