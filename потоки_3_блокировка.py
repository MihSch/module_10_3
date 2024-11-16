import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for i in range(100):
            r_num = randint(50, 500)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            self.balance += r_num
            print(f'Пополнение: {r_num}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):

        for i in range(100):
            r_num = randint(50, 500)
            print(f'Запрос на {r_num}')
            if r_num > self.balance:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств")
            else:
                self.balance -= r_num
                print(f'Снятие: {r_num}. Баланс: {self.balance}')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
