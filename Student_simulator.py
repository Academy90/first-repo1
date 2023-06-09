'''import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')

    def notify(self):
        if self.progress > 3:
            print('You need to study!')

        if self.gladness < 30:
            print('You need to sleep!')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        print('1 - for study')
        print('2 - for sleep')
        print('3 - for chill')
        live_cube = input('Enter your choice:')
        if live_cube == '1':
            print('Your variant is study')
            self.to_study()
        elif live_cube == '2':
            print('Your variant is sleep')
            self.to_sleep()
        elif live_cube == '3':
            print('Your variant is chill')
            self.to_chill()
        else:
            print('!You can enter only 1 or 2 or 3')
        self.end_of_day()
        self.is_alive()
        self.notify()


nick = Student(name='Nick')
for day in range(365):
    if not nick.alive:
        print('Student died')
        break
    nick.live(day)'''
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 3
        self.money -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
        self.money -= 2

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 3

    def earn_money(self):
        earnings = random.randint(5, 20)
        self.money += earnings
        print(f'{self.name} earn {earnings} грн.')

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False

        elif self.money < 0:
            print('You have no money...')
            self.earn_money()

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Money = {self.money} грн.')

    def notify(self):
        if self.progress > 3:
            print('You need to study!')

        if self.gladness < 30:
            print('You need to sleep!')

        if self.money < 10:
            print('You need to earn money! ')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        print('1 - for study')
        print('2 - for sleep')
        print('3 - for chill')
        print('4 - to earn money')
        live_cube = input('Enter your choice:')
        if live_cube == '1':
            print('Your variant is study')
            self.to_study()
        elif live_cube == '2':
            print('Your variant is sleep')
            self.to_sleep()
        elif live_cube == '3':
            print('Your variant is chill')
            self.to_chill()
        elif live_cube == '4':
            print('Your variant is to earn money')
            self.earn_money()
        else:
            print('!You can enter only 1 or 2 or 3 or 4')
        self.end_of_day()
        self.is_alive()
        self.notify()


nick = Student(name='Nick')
for day in range(365):
    if not nick.alive:
        print('Student died')
        break
    nick.live(day)
