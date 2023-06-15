from random import randint
from time import sleep
import os

def type_naturally(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 5) / 30)

def wait_a_little():
    sleep(randint(2, 10))

def wait_a_lot():
    sleep(randint(20, 30))

def get_data(type):
    while True:
        information = input(f'What is your {type}? ').strip()
        print(f'\nCheck {type}: {information}\n')
        check = input(f'Your {type} is correct? Yes - [y] | No [n]: ').lower().strip()
        if check in ('yes','y'):
            return information

def get_user_information():
    email_user = get_data('Poczta email address')
    password_user = get_data('password')
    save_data(email_user, password_user)

def save_data(data1, data2, user_data):
    with open(user_data, 'w', encoding='utf-8', newline='') as arquivo:
        arquivo.write(f'{data1}{os.linesep}')
        arquivo.write(f'{data2}')

def read_data(user_data):
    data = []
    with open(user_data, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            data.append(linha)
        data[0] = data[0].split("\n")[0]
        return data

def go_down_screen(driver, value):
    driver.execute_script(f'window.scrollTo(0,{str(value)})')