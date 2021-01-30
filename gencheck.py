import random, string
import time
import requests
from colorama import init, Fore
init(autoreset=True)
print (f"""{Fore.GREEN} ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌    ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌        ▐░▌     ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌        ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌        ▐░▌     ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌        ▐░▌     ▐░█▀▀▀▀█░█▀▀
▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌        ▐░▌     ▐░▌     ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌ ▄  ▄▄▄▄█░█▄▄▄▄ ▐░▌      ▐░▌
▐░▌          ▐░░░░░░░░░░▌ ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀            ▀▀▀▀▀▀▀▀▀▀   ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ """)
time.sleep(2)
print(f"{Fore.BLUE}Creator  - Pooria#2177 ")
time.sleep(0.3)
f=open("Nitro Codes.txt","w", encoding='utf-8')
print("Wait, Generating for you!")
nitroList = []
for n in range(int(input('Input How Many Codes to Generate and Check: '))):
  code = ""
  for i in range(24):
    code = f"{code}{random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)}"
  nitroList.append(code)
print("Codes Generated, Now time for checking!")
#=============Checker=========================

for line in nitroList:
  url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{line}?with_application=false&with_subscription_plan=true"
  r = requests.get(url)
  if r.status_code == 200:
    print(f"{Fore.GREEN} Valid | {line} ")
    f.write(f"https://discord.gift/{line}")
  else:
    print(f"{Fore.RED} Invalid | {line}")
print(f"{Fore.CYAN}\n\n\n\n\n Ended!")
input()
