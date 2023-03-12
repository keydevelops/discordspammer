import discord
from discord.ext import commands
import time
import os
from colorama import init, Fore, Style
import time
import sime_library
sime_library.set_window_title("Спамер")
init()
print(f'''{Fore.BLUE}{Style.BRIGHT}
╔══╗          ╔╗╔═╗         ╔═══╗                           ╔╗    ╔═══╗       ╔╗        
║╔╗║          ║║║╔╝         ╚╗╔╗║                           ║║    ╚╗╔╗║      ╔╝╚╗       
║╚╝╚╗╔╗ ╔╗    ║╚╝╝ ╔══╗╔╗ ╔╗ ║║║║╔══╗╔╗╔╗╔══╗    ╔══╗ ╔═╗ ╔═╝║     ║║║║╔╗╔╗╔╗╚╗╔╝╔═╗╔══╗
║╔═╗║║║ ║║    ║╔╗║ ║╔╗║║║ ║║ ║║║║║╔╗║║╚╝║║══╣    ╚ ╗║ ║╔╗╗║╔╗║     ║║║║║╚╝║╠╣ ║║ ║╔╝║╔╗║
║╚═╝║║╚═╝║    ║║║╚╗║║═╣║╚═╝║╔╝╚╝║║║═╣╚╗╔╝╠══║    ║╚╝╚╗║║║║║╚╝║    ╔╝╚╝║║║║║║║ ║╚╗║║ ║╚╝║
╚═══╝╚═╗╔╝    ╚╝╚═╝╚══╝╚═╗╔╝╚═══╝╚══╝ ╚╝ ╚══╝    ╚═══╝╚╝╚╝╚══╝    ╚═══╝╚╩╩╝╚╝ ╚═╝╚╝ ╚══╝
     ╔═╝║              ╔═╝║                                                             
     ╚══╝              ╚══╝                                                             
''')
print(Style.RESET_ALL)
time.sleep(4)
os.system('cls')
print(Fore.GREEN)
tkn = input('[ >> ] Введите ваш токен: ')
print(Style.RESET_ALL)
os.system('cls')
print(Fore.YELLOW)
msgg = input('[ >> ] Введите сообщение для спама: ')
print(Style.RESET_ALL)
os.system('cls')
while True:
    print(Fore.CYAN)
    count = input("[ >> ] Введите количество сообщений: ")
    print(Style.RESET_ALL)
    number = False
    for x in count:
        if x.isdigit():
            number = True
        else:
            number = False
            break
    if number:
        break
    elif not number:
        print(f'[ {Fore.RED}-{Style.RESET_ALL} ] {Fore.LIGHTRED_EX}Впишите число!')
        print(Style.RESET_ALL)
        continue
try:
    client = commands.Bot(command_prefix = '.', self_bot = True)
except Exception as e:
    print(f'[{Fore.RED} - {Style.RESET_ALL}] {Fore.LIGHTMAGENTA_EX}Не удалось запустить клиент{Style.RESET_ALL}\n {Fore.RED}{e}{Style.RESET_ALL}')
    print(Style.RESET_ALL)
    time.sleep(10)
    exit()
@client.event
async def on_ready():
    print(f'[{Fore.GREEN} + {Style.RESET_ALL}] {Fore.LIGHTGREEN_EX}Запустил селф-бота {client.user.name}\n\n[{Fore.GREEN} INFO {Style.RESET_ALL}] Для запуска спама напиши команду .spam')
@client.command()
async def spam(ctx):
    msgs = 0
    for x in range(int(count)):
        try:
            msgs += 1
            await ctx.send(msgg)
            print(f'[{Fore.GREEN} + {Style.RESET_ALL}] Отправил сообщение №{msgs} в канал {ctx.channel}')
        except Exception as e:
            print(f'[{Fore.RED} - {Style.RESET_ALL}] Не удалось отправить сообщение в канал {ctx.channel}\n\nОшибка: {e}')
try:
    client.run(tkn, bot = False)
except Exception as e:
    print(f'[{Fore.RED} - {Style.RESET_ALL}] Не смог загрузить селф-бота')
    time.sleep(10)
    exit()