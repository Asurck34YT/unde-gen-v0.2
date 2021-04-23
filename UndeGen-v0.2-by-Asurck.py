import random, string
from colorama import Fore, Style, init
from console.utils import set_title
init(convert=True)









set_title("Unde_Gen v0.2 | by Asurck")


print(Fore.LIGHTCYAN_EX + ''' 
 _____  __        _________         _________                         _______     ______ 
 __  / / /_______ ______  /_____    __  ____/_____ _______    ___   ____  __ \    __|__ \\
 _  / / / __  __ \_  __  / _  _ \   _  / __  _  _ \__  __ \   __ | / /_  / / /    ____/ /
 / /_/ /  _  / / // /_/ /  /  __/   / /_/ /  /  __/_  / / /   __ |/ / / /_/ / ___ _  __/ 
 \____/   /_/ /_/ \__,_/   \___/    \____/   \___/ /_/ /_/    _____/  \____/  _(_)/____/ 
                Created and Coded By ! Asurck 👑#0262 - ! Asurck 👑#2021



''' + Fore.LIGHTRED_EX + '''[?] ''' + Fore.LIGHTWHITE_EX + '''Los codigos se gurdaran en un archivo llamado: ''' + Fore.CYAN + '''Codes.txt

''' + Fore.LIGHTGREEN_EX + '''[!] ''' + Fore.LIGHTWHITE_EX + '''Escribe la cantidad de codigos a generas: ''')


amount = int(input(Fore.LIGHTWHITE_EX + "\nEscribelo aqui..."))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(Fore.LIGHTWHITE_EX +  f'{code}  |  ' + Fore.LIGHTGREEN_EX + 'Generado y Guardado - Unde Gen v0.2')
    value += 1


    