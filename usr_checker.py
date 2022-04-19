'''
# Codeing by lord4tb , [ @ilord4tb ]
# github : 511j
# Free src in >> https://github.com/511j/usr.gg-checker
'''
import os,requests,threading,random
from discord_webhook import DiscordWebhook,DiscordEmbed
from colorama import Fore
os.system("cls")
webhhok = input(f"{Fore.WHITE}[ {Fore.CYAN}+{Fore.WHITE} ] Webhook :{Fore.CYAN} ")
leg = int(input(f'{Fore.WHITE}[ {Fore.CYAN}+{Fore.WHITE} ] Length : {Fore.CYAN}'))
th = input(f"{Fore.WHITE}[ {Fore.CYAN}+{Fore.WHITE} ] Treads :{Fore.CYAN} ")
print()
li = '.1234567890qwer.tyuioplkmjnhbgvfcdxzsa_'
while 1:
    user = ("".join(random.choice(li) for i in range(leg)))
    r = requests.get(f"https://usr.gg/{user}")
    if (r.status_code == 200):
        print(f"{Fore.RED}Unavailable >> {user}{Fore.WHITE}")
    if (r.status_code == 404):
        print(f"{Fore.GREEN}Available >> {user}{Fore.WHITE}")
        webhook = DiscordWebhook(url=f'{webhhok}')
        embed = DiscordEmbed(title='#Lord4tb usr.gg checker', color='a63028')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/962419141892009994/966089585157353484/anime.gif')
        embed.set_footer(text='#Lord4tb usr.gg checker')
        embed.add_embed_field(name='Usr.gg username : ', value=f"{user}")
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        print(f"{Fore.RED}Blocked{Fore.WHITE}")
for _ in range(th):
    threading.Thread(target=user).start()
