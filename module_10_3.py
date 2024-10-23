from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):
    def __init__(self, balance=0):
        super().__init__()
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            num = randint(50, 500)
            self.balance += num
            print(f'Пополнение: {num}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            num = randint(50, 100)
            print(f'Запрос на {num}')
            if num <= self.balance:
                self.balance -= num
                print(f'Снятие: {num}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
