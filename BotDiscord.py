#!/usr/bin/env python -B
#export PYTHONDONTWRITEBYTECODE=1
#-*- coding: utf-8 -*-
#---------------######## ----------------------<<
import sys
sys.dont_write_bytecode = True
import colorama
import os, stat
import yaml
import requests
import json
import cursor
import aiohttp
import random
import ctypes
import time
import asyncio
import discord, discord.utils
#-------######## -------------<<
from decimal import Decimal as D
from datetime import date, timedelta, datetime, timezone 
from time import sleep
from discord import Embed, guild, message, Game, Color, Status, ChannelType
from discord.client import Client
from random import shuffle, randrange
from discord.guild import Guild
from getch import pause
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import MemberConverter, MissingPermissions, CommandNotFound, MissingRequiredArgument
from discord.ext.commands.errors import CheckFailure
from os import listdir, system, name, walk
from os.path import isfile, isdir, join
from colorama import init, Fore, Back, Style, Cursor
#-------######## -------------<<
init()
intents = discord.Intents.all()
#-------######## -------------<<
def route_resolved(rout_resolved):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rout_resolved)
    return os.path.join(os.path.abspath('.'), rout_resolved)
configuration_resolved = route_resolved("Configuration")
sys.path.append(configuration_resolved)
#---------------######## ########-----------------------------------------------------<<


#---------------######## ----------------------<<
BOT_VERSION = "0.0.1"
CUSTOMER = "luisfernande929"
DEVELOPER = "xTrokxs#4444"

#-------######## -------------<<
if os.path.isfile(f"version.dat"):
    pass
else:
    version_file = open(f"version.dat", "a", encoding="utf-8", errors="ignore")
    version_file.write(f"{BOT_VERSION}")
    version_file.close()

#-------######## -------------<<
FIVERR_1 = r"""   ______ __  __   ________  ______  ______    """
FIVERR_2 = r"""  /\  ___/\ \/\ \ / /\  ___\/\  == \/\  == \   """
FIVERR_3 = r"""  \ \  __\ \ \ \ \'/\ \  __\\ \  __<\ \  __<   """
FIVERR_4 = r"""   \ \_\  \ \_\ \__| \ \_____\ \_\ \_\ \_\ \_\ """ + Style.RESET_ALL + f"v{BOT_VERSION}"
FIVERR_5 = r"""    \/_/   \/_/\/_/   \/_____/\/_/ /_/\/_/ /_/ """ + Style.RESET_ALL + f"Created by {DEVELOPER}"

#-------######## -------------<<
def clear():
    if os.name in ("nt", "dos"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Fiverr [v{BOT_VERSION}] - Created by {DEVELOPER}")
        cursor.hide()
        os.system("cls")
    elif os.name in ("linux", "osx", "posix"):
        os.system("clear")
    else:
        print("\n") * 100
def fiverr_good():
    if os.name in ("nt", "dos"):
        FIVERR_GOOD = Style.RESET_ALL + "\n" + Fore.GREEN + Style.BRIGHT + str(FIVERR_1) + "\n" + Fore.GREEN + Style.BRIGHT + str(FIVERR_2) + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_3 + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_4 + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_5 + Style.RESET_ALL + "\n"
    else:
        FIVERR_GOOD = Style.RESET_ALL + "\n" + Fore.GREEN + Style.BRIGHT + str(FIVERR_1) + "\n" + Fore.GREEN + Style.BRIGHT + str(FIVERR_2) + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_3 + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_4 + "\n" + Fore.GREEN + Style.BRIGHT + FIVERR_5 + Style.RESET_ALL + "\n"
    print(FIVERR_GOOD)
def fiverr_error():
    if os.name in ("nt", "dos"):
        FIVERR_ERROR = Style.RESET_ALL + "\n" + Fore.RED + Style.BRIGHT + str(FIVERR_1) + "\n" + Fore.RED + Style.BRIGHT + str(FIVERR_2) + "\n" + Fore.RED + Style.BRIGHT + FIVERR_3 + "\n" + Fore.RED + Style.BRIGHT + FIVERR_4 + "\n" + Fore.RED + Style.BRIGHT + FIVERR_5 + Style.RESET_ALL + "\n"
    else:
        FIVERR_ERROR = Style.RESET_ALL + "\n" + Fore.RED + Style.BRIGHT + str(FIVERR_1) + "\n" + Fore.RED + Style.BRIGHT + str(FIVERR_2) + "\n" + Fore.RED + Style.BRIGHT + FIVERR_3 + "\n" + Fore.RED + Style.BRIGHT + FIVERR_4 + "\n" + Fore.RED + Style.BRIGHT + FIVERR_5 + Style.RESET_ALL + "\n"
    print(FIVERR_ERROR)

#-------######## -------------<<
clear()
fiverr_good()
#---------------######## ########-----------------------------------------------------<<


#---------------######## ----------------------<<
if os.path.isdir("Configuration"):
    pass
else:
    os.mkdir("Configuration")
if os.path.isdir("Data"):
    pass
else:
    os.mkdir("Data")
if os.path.isdir("Configuration/Bot"):
    pass
else:
    os.mkdir("Configuration/Bot")

#-------######## -------------<<
try:
    config_file = open("Configuration/Bot/Config.yml")
    config_file.close()
    with open("Configuration/Bot/Config.yml") as config_ymal:
        config_ymal_json = yaml.safe_load(config_ymal)
    config_ymal.close()

    presence_file = open("Configuration/Bot/Presence.yml")
    presence_file.close()
    with open("Configuration/Bot/Presence.yml") as presence_ymal:
        presence_ymal_json = yaml.safe_load(presence_ymal)
    presence_ymal.close()

    server_file = open("Configuration/Bot/Server.yml")
    server_file.close()
    with open("Configuration/Bot/Server.yml") as server_ymal:
        server_ymal_json = yaml.safe_load(server_ymal)
    server_ymal.close()

    jsonlvel_file = open("Data/Data.json")
    jsonlvel_file.close()
    jsonlvel_file2 = open("Data/DataOld.json")
    jsonlvel_file2.close()

    pass
except Exception as e:
    clear()
    fiverr_error()
    e = str(e).split("'")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Wow!")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" Reason: The '{e[1]}' file has not been detected!""" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Press any key to exit..." + Style.RESET_ALL)
    pause(" ")
    os._exit(0)

#-------######## -------------<<
jsons_listlvel = sum(1 for line in open("Data/Data.json", encoding="utf-8", errors="ignore"))
jsons_listlvel2 = sum(1 for line in open("Data/DataOld.json", encoding="utf-8", errors="ignore"))
if jsons_listlvel == 0:
    file_level = open("Data/Data.json", "a", encoding="utf-8", errors="ignore")
    file_level.write(r"{}")
    file_level.close()
if jsons_listlvel2 == 0:
    file_level = open("Data/DataOld.json", "a", encoding="utf-8", errors="ignore")
    file_level.write(r"{}")
    file_level.close()

#-------######## -------------<<
try:
    config_ymal_json["Prefix"]
    config_ymal_json["Token"]

    presence_ymal_json["Option"]
    presence_ymal_json["Settings"]
    presence_ymal_json["Settings"]["Time"]
    presence_ymal_json["Settings"]["Messages"]
    presence_ymal_json["Settings"]["Type"]
    presence_ymal_json["Settings"]["Url"]

    server_ymal_json["Color"]

    pass
except Exception as e:
    clear()
    fiverr_error()
    e = str(e).split("'")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Wow!")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" Reason: The variable '{e[1]}' was not detected!""" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Press any key to exit..." + Style.RESET_ALL)
    pause(" ")
    os._exit(0)
#---------------######## ########-----------------------------------------------------<<


#---------------######## ----------------------<<
bot = commands.Bot(command_prefix=f"""{str(config_ymal_json["Prefix"])}""", case_insensitive=True, intents=intents, help_command=None)
#---------------######## ########-----------------------------------------------------<<


#---------------######## ----------------------<<
def role_staff(user):
    author_roles = user.roles
    has_right_role = False
    for role in author_roles:
        try:
            if str(role.id) in server_ymal_json["Roles"]["Staff"]:
                has_right_role = True
        except Exception:
            return has_right_role
    return has_right_role

#-------######## -------------<<
async def status_update():
    await bot.wait_until_ready()
    await asyncio.sleep(10)
    while not bot.is_closed():
        if presence_ymal_json["Option"] == True:
            pass
        else:
            break
        try:
            messages_status = random.choice(presence_ymal_json["Settings"]["Messages"]).strip()
            cycle_status = presence_ymal_json["Settings"]["Type"]
            url_status = presence_ymal_json["Settings"]["Url"]
            time_status = int(presence_ymal_json["Settings"]["Time"])
            if "watching" == str(cycle_status).lower():
                await bot.change_presence(activity = discord.Activity(name=messages_status, type=discord.ActivityType.watching), status = None, afk = False)
            elif "game" == str(cycle_status).lower():
                await bot.change_presence(activity = discord.Game(name=messages_status), status = None, afk = False)
            elif "listening" == str(cycle_status).lower():
                await bot.change_presence(activity = discord.Activity(name=messages_status, type=discord.ActivityType.listening), status = None, afk = False)
            elif "streaming" == str(cycle_status).lower():
                await bot.change_presence(activity = discord.Activity(name=messages_status, url=url_status, type=discord.ActivityType.streaming), status = None, afk = False)
        except Exception:
            pass
        try:
            await asyncio.sleep(time_status)
        except Exception:
            await asyncio.sleep(50)

async def print_update():
    await bot.wait_until_ready()
    await asyncio.sleep(500)
    while not bot.is_closed():
        clear()
        fiverr_good()
        print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + " STATUS " + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" ONLINE!""" + "\n")
        await asyncio.sleep(2000)

#-------######## -------------<<
@bot.event 
async def on_ready():
    clear()
    fiverr_good()
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + " STATUS " + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" ONLINE!""" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ID " + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]:" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" {bot.user.id}""")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " USER " + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]:" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" {bot.user}""")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " PREFIX " + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]:" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" {bot.command_prefix}help""" + Style.RESET_ALL + Fore.WHITE)
#---------------######## ########-----------------------------------------------------<<












#---------------######## ----------------------<<
headers = {"Authorization": f"""Bearer {server_ymal_json["Sellix-API"]}"""}

#-------######## -------------<<
@bot.command(pass_context=True, aliases=["h"])
async def help(message, command):
    try:
        await message.message.delete()
    except discord.errors.Forbidden:
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
        return
    if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
        if role_staff(message.author):
            pass
        else:
            return
    
    if role_staff(message.author):
        if str(command).lower() in ["comprar", "buy", "buyer", "compra"]:
            try:
                embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
            except Exception:
                embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=0x0049FF)
            embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
            embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}comprar"""), inline=True)
            embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `buy`, `buyer`, `compra`"""), inline=True)
            embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}buy <ID> <BOLETOS>` - Compra un boleto de un Anuncio."""), inline=False)
        elif str(command).lower() in ["anuncio", "anunciar", "vender"]:
            try:
                embed = discord.Embed(title=f"""{bot.user.name} • Anuncios""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
            except Exception:
                embed = discord.Embed(title=f"""{bot.user.name} • Anuncios""", timestamp=datetime.utcnow(), color=0x0049FF)
            embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
            embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}anuncio"""), inline=True)
            embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `anunciar`, `vender`"""), inline=True)
            embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}vender <@Vendedor> <#channel>` - Crea un anuncio para vender boletos."""), inline=False)
    else:
        if str(command).lower() in ["comprar", "buy", "buyer", "compra"]:
            try:
                embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
            except Exception:
                embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=0x0049FF)
            embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
            embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}comprar"""), inline=True)
            embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `buy`, `buyer`, `compra`"""), inline=True)
            embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}buy <ID> <BOLETOS>` - Compra un boleto de un Anuncio."""), inline=False)
    
    try:
        await message.channel.send(embed=embed)
    except Exception:
        pass
    return
@help.error
async def help_error(message, error):
    if isinstance(error, MissingRequiredArgument):
        try:
            await message.message.delete()
        except discord.errors.Forbidden:
            try:
                await message.channel.send("No tengo permiso para hacer eso.")
            except Exception:
                pass
            return
        if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
            if role_staff(message.author):
                pass
            else:
                return

        try:
            embed = discord.Embed(title=f"""{bot.user.name} • Lista de comandos""", description=f"""• Utilice `{bot.command_prefix}help <command>` para obtener más información sobre un comando.""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
        except Exception:
            embed = discord.Embed(title=f"""{bot.user.name} • Lista de comandos""", description=f"""• Utilice `{bot.command_prefix}help <command>` para obtener más información sobre un comando.""", timestamp=datetime.utcnow(), color=0x0049FF)
        embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
        
        if role_staff(message.author):
            embed.add_field(name=("• General"), value=(f"""➭ `{bot.command_prefix}comprar`, `{bot.command_prefix}vender`"""), inline=False)
        else:
            embed.add_field(name=("• General"), value=(f"""➭ `{bot.command_prefix}comprar`"""), inline=False)
        await message.channel.send(embed=embed)
    elif discord.errors.Forbidden:
        try:
            await message.message.delete()
        except discord.errors.Forbidden:
            try:
                await message.channel.send("No tengo permiso para hacer eso.")
            except Exception:
                pass
            return
        if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
            if role_staff(message.author):
                pass
            else:
                return
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass 
    return

#-------######## -------------<<
@bot.command(pass_context=True, aliases=["buy", "buyer", "compra"])
async def comprar(message, idcompra = None, idboletos: int = None):
    try:
        await message.message.delete()
    except discord.errors.Forbidden:
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
        return
    if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
        if role_staff(message.author):
            pass
        else:
            return
    
    if not idcompra or not idboletos:
        try:
            embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
        except Exception:
            embed = discord.Embed(title=f"""{bot.user.name} • Compra""", timestamp=datetime.utcnow(), color=0x0049FF)
        embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
        embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}comprar"""), inline=True)
        embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `buy`, `buyer`, `compra`"""), inline=True)
        embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}buy <ID> <BOLETOS>` - Compra un boleto de un Anuncio."""), inline=False)
        await message.channel.send(embed=embed)
        return
    else:
        with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
            idcompracheck = json.load(idcomprc)
        idcomprc.close()
        if not f"{str(idcompra)}" in idcompracheck:
            await message.channel.send(f"""**{message.author.mention}, la id `{str(idcompra)}` no esta registrada.**""")
            return
        else:
            channelcheck = bot.get_channel(int(idcompracheck[f"{str(idcompra)}"][f"channel"]))
            if str(channelcheck) == "None":
                del idcompracheck[f"{str(idcompra)}"]
                await message.channel.send(f"""**{message.author.mention}, la id `{str(idcompra)}` no esta registrada.**""")
                with open("Data/Data.json", "w") as idcomprc:
                    json.dump(idcompracheck, idcomprc)
                idcomprc.close()
                return
            else:
                try:
                    messageanounce2 = await channelcheck.fetch_message(int(idcompra))
                except Exception:
                    del idcompracheck[f"{str(idcompra)}"]
                    await message.channel.send(f"""**{message.author.mention}, la id `{str(idcompra)}` no esta registrada.**""")
                    with open("Data/Data.json", "w") as idcomprc:
                        json.dump(idcompracheck, idcomprc)
                    idcomprc.close()
                    return
                
                idboletoscheck = int(idcompracheck[f"{str(idcompra)}"][f"buy"]) + idboletos
                if idboletos > int(idcompracheck[f"{str(idcompra)}"][f"min"]):
                    if int(idcompracheck[f"{str(idcompra)}"][f"min"]) == 1:
                        correctone = "boleto"
                    else:
                        correctone = "boletos"
                    await message.channel.send(f"""**{message.author.mention}, solo se puede comprar {int(idcompracheck[f"{str(idcompra)}"][f"min"])} {correctone} por persona.**""")
                    return
                elif int(idcompracheck[f"{str(idcompra)}"][f"buy"]) >= int(idcompracheck[f"{str(idcompra)}"][f"max"]):
                    await message.channel.send(f"""**{message.author.mention}, este anuncio ya vendio todos sus boletos.**""")
                    return
                elif idboletoscheck > int(idcompracheck[f"{str(idcompra)}"][f"max"]):
                    idboletosrest = int(idcompracheck[f"{str(idcompra)}"][f"max"]) - int(idcompracheck[f"{str(idcompra)}"][f"buy"])
                    if idboletosrest == 1:
                        correctone = f"queda disponible {idboletosrest} boleto"
                    elif idboletosrest == 0:
                        await message.channel.send(f"""**{message.author.mention}, este anuncio ya vendio todos sus boletos.**""")
                        return
                    else:
                        correctone = f"quedan disponibles {idboletosrest} boletos"
                    await message.channel.send(f"""**{message.author.mention}, solo {correctone}.**""")
                    return

                with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                    idcompracheck = json.load(idcomprc)
                idcomprc.close()
                if not f"{message.author.id}" in idcompracheck[f"{idcompra}"]["purchased"]:
                    idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"] = {}
                    idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["shop"] = 0
                    idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["shopping"] = 0
                    idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["additional"] = 0
                    with open("Data/Data.json", "w") as idcomprc:
                        json.dump(idcompracheck, idcomprc)
                    idcomprc.close()
                with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                    idcompracheck = json.load(idcomprc)
                idcomprc.close()

                idboletoscheckuser = int(idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["shopping"]) + idboletos
                if idboletoscheckuser > int(idcompracheck[f"{str(idcompra)}"][f"min"]):
                    idboletoscheckuserdel = int(idcompracheck[f"{str(idcompra)}"][f"min"]) - int(idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["shopping"])
                    if idboletoscheckuserdel == 1:
                        correctone = f"{idboletoscheckuserdel} boleto"
                    elif idboletoscheckuserdel == 0:
                        await message.channel.send(f"""**{message.author.mention}, ya llegaste al tope de boletos.**""")
                        return
                    else:
                        correctone = f"{idboletoscheckuserdel} boletos"
                    await message.channel.send(f"""**{message.author.mention}, solo puedes comprar {correctone} mas.**""")
                    return
                else:
                    idcompracheck[f"{idcompra}"]["purchased"][f"{message.author.id}"]["shopping"] += idboletos
                    idcompracheck[f"{idcompra}"]["buy"] += idboletos
                    with open("Data/Data.json", "w") as idcomprc:
                        json.dump(idcompracheck, idcomprc)
                    idcomprc.close()
                with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                    idcompracheck = json.load(idcomprc)
                idcomprc.close()

                try:
                    if idboletos == 1:
                        correctone = f"boleto"
                    else:
                        correctone = f"boletos"
                    testuiservemde = await bot.fetch_user(int(idcompracheck[f"{idcompra}"]["seller"]))
                    await message.author.send(f":label: **Solicitaste comprar {idboletos} {correctone} a {testuiservemde.mention}!**\n:shopping_bags: **ID:** `{idcompra}`\n:bookmark_tabs: **Se enviara un enlace para el pago cuando se vendan todos los boletos.**")
                except Exception:
                    await message.channel.send(f"""**{message.author.mention}, debes tener abierto tu DM para comprar un boleto.**""")
                    return
                with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                    idcompracheck = json.load(idcomprc)
                idcomprc.close()
                cjecltptal = int(idcompracheck[f"{str(idcompra)}"][f"max"])
                cjeclbuye = int(idcompracheck[f"{str(idcompra)}"][f"buy"])
                trletobte = idcompracheck[f"{idcompra}"]["title"]

                if int(idcompracheck[f"{str(idcompra)}"][f"buy"]) >= int(idcompracheck[f"{str(idcompra)}"][f"max"]):
                    embed = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idcompra)}"][f"price"]}\n:label: **Boletos**: 0/{cjecltptal}\n:purple_circle: **Estado**: Pagando...\n\n:shopping_bags: **ID:** {idcompra}""", color=0x305CC1)
                    await messageanounce2.edit(embed=embed)
                    URL = "https://dev.sellix.io/v1/products"
                    Jsoncheck = {"title": f"{idcompra}", "price": idcompracheck[f"{str(idcompra)}"][f"price"], "currency": "USD", "description": f"**Vendedor**: {testuiservemde}\n**Boletos**: {cjecltptal}\n**ID:** {idcompra}", "gateways": ["PAYPAL"], "quantity": {"min": 1, "max": int(idcompracheck[f"{str(idcompra)}"][f"min"])}, "type": "service", "stock_delimiter": "\n", "delivery_text": "Gracias por comprar los Boletos!", "service_text": f"Vendedor: {testuiservemde}\nBoletos: {cjecltptal}\nID: {idcompra}", "custom_fields": [{"name": "• DISCORD", "type": "text", "placeholder": "Test#0000", "required": True}, {"name": "• CLAVE SECRETA", "type": "text", "placeholder": "00000000", "required": True}], "crypto_confirmations_needed": 1, "max_risk_level": 85, "block_vpn_proxies": False, "sort_priority": 1, "unlisted": True, "stock": int(idcompracheck[f"{str(idcompra)}"][f"max"])}
                    httpResp = requests.post(URL, headers=headers, json=Jsoncheck)
                    httpJson = httpResp.json()
                    httpResp.close()
                    estado = httpJson["status"]
                    if estado == 200:
                        pass
                    else:
                        print(Style.RESET_ALL + Fore.RED + Style.BRIGHT + f"""  -[ ERROR | {idcompra} | {estado} | {httpJson["error"]} ]-""" + Style.RESET_ALL)
                        return
                    idcompracheck[f"{idcompra}"]["uniqid"] = f"""{httpJson["data"]["uniqid"]}"""
                    idcompracheck[f"{idcompra}"]["status"] = f"""wait"""
                    with open("Data/Data.json", "w") as idcomprc:
                        json.dump(idcompracheck, idcomprc)
                    idcomprc.close()
                    with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                        idcompracheck = json.load(idcomprc)
                    idcomprc.close()

                    for checkusersendmd in idcompracheck[f"{idcompra}"]["purchased"]:
                        testuiservemde2 = await bot.fetch_user(int(checkusersendmd))
                        testuiservemdestaff = await bot.fetch_user(int(idcompracheck[f"{idcompra}"]["staff"]))
                        try:
                            testcomprado = idcompracheck[f"{idcompra}"]["purchased"][f"{checkusersendmd}"]["shopping"]
                            if int(testcomprado) == 1:
                                otravesmesg = f"{testcomprado} boleto"
                            else:
                                otravesmesg = f"{testcomprado} boletos"
                            await testuiservemde2.send(f"""**:label: Todos los boletos de {testuiservemde.mention} se han vendido!**\n:sparkling_heart: **Debes comprar {otravesmesg} en este enlace.**\n:closed_lock_with_key: **CLAVE SECRETA:** `{checkusersendmd}`\n:shopping_cart: **Producto: <https://sellix.io/product/{idcompracheck[f"{idcompra}"]["uniqid"]}>**\n:shopping_bags: **ID:** `{idcompra}`\n:bookmark_tabs: **Al momento de finalizar la compra te dara una __ID__ unica, esa __ID__ la debes colocar en este chat de esta forma: `{bot.command_prefix}pay {idcompra} <ID>`**""")
                        except Exception:
                            try:
                                if int(testcomprado) == 1:
                                    otravesmesg = f"{testcomprado} boleto"
                                else:
                                    otravesmesg = f"{testcomprado} boletos"
                                await testuiservemdestaff.send(f"""**:warning: {testuiservemde2.mention} no puede recibir el enlace del producto porque no tiene abierto los DM!**\n:closed_lock_with_key: **CLAVE SECRETA:** `{checkusersendmd}`\n:sparkling_heart: **Él debe comprar {otravesmesg} en este enlace.**\n:shopping_cart: **Producto: <https://sellix.io/product/{idcompracheck[f"{idcompra}"]["uniqid"]}>**\n:shopping_bags: **ID:** `{idcompra}`""")
                            except Exception:
                                pass
                    return
                else:
                    embed = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idcompra)}"][f"price"]}\n:label: **Boletos**: {cjeclbuye}/{cjecltptal}\n:green_circle: **Estado**: Activo!\n\n:shopping_bags: **ID:** {idcompra}""", color=0x62D727)
                    await messageanounce2.edit(embed=embed)
                return
    return
@comprar.error
async def comprar_error(message, error):
    if discord.errors.Forbidden:
        if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
            if role_staff(message.author):
                pass
            else:
                return
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
    return

#-------######## -------------<<
@bot.command(pass_context=True, aliases=["anunciar", "vender"])
async def anuncio(message, memb: discord.Member = None, chann: discord.TextChannel = None):
    try:
        await message.message.delete()
    except discord.errors.Forbidden:
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
        return
    if role_staff(message.author):
        pass
    else:
        return

    if not memb or not chann:
        try:
            embed = discord.Embed(title=f"""{bot.user.name} • Anuncios""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
        except Exception:
            embed = discord.Embed(title=f"""{bot.user.name} • Anuncios""", timestamp=datetime.utcnow(), color=0x0049FF)
        embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
        embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}anuncio"""), inline=True)
        embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `anunciar`, `vender`"""), inline=True)
        embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}vender <@Vendedor> <#channel>` - Crea un anuncio para vender boletos."""), inline=False)
        await message.channel.send(embed=embed)
        return
    else:
        contador_anuncio = 4
        channel = message.channel
        def check(m):
            return m.author == message.author and m.channel == channel

        anuncio_inicio = await message.channel.send(f"""Escriba el nombre que desea para el anuncio. **`(1/{contador_anuncio})`**""")
        formato_orden = await bot.wait_for("message", check=check)
        formato_orden_encontrado = await channel.fetch_message(formato_orden.id)
        await formato_orden_encontrado.delete()
        tipo_obtenido = str(formato_orden.content).strip()

        await anuncio_inicio.edit(content=f"""Por favor, especifique el precio del boleto. **`(2/{contador_anuncio})`**\n➭ Ejemplo: `2.0`, `1`, `5.02`""")
        formato_orden = await bot.wait_for("message", check=check)
        formato_orden_encontrado = await channel.fetch_message(formato_orden.id)
        await formato_orden_encontrado.delete()
        try:
            tipo_obtenido2 = int(float(formato_orden.content))
            tipo_obtenido22 = str(formato_orden.content).strip()
        except Exception:
            embed = discord.Embed(description=f"""**Precio incorrecto.**\n➭ **Ejemplo: `2.0`, `1`, `5.02`**""", color=0xD40E1D)
            await anuncio_inicio.edit(embed=embed, content="")
            return

        await anuncio_inicio.edit(content=f"""Por favor, especifique el maximo de boletos que se pueden vender. **`(3/{contador_anuncio})`**""")
        formato_orden = await bot.wait_for("message", check=check)
        formato_orden_encontrado = await channel.fetch_message(formato_orden.id)
        await formato_orden_encontrado.delete()
        try:
            tipo_obtenido3 = int(float(formato_orden.content))
        except Exception:
            embed = discord.Embed(description=f"""**El numero maximo de boletos es incorrecto.**""", color=0xD40E1D)
            await anuncio_inicio.edit(embed=embed, content="")
            return

        await anuncio_inicio.edit(content=f"""Por favor, especifique el maximo de boletos que se pueden comprar. **`(4/{contador_anuncio})`**""")
        formato_orden = await bot.wait_for("message", check=check)
        formato_orden_encontrado = await channel.fetch_message(formato_orden.id)
        await formato_orden_encontrado.delete()
        try:
            tipo_obtenido4 = int(float(formato_orden.content))
            if tipo_obtenido4 >= tipo_obtenido3:
                embed = discord.Embed(description=f"""**El numero de compra no puede ser mayor al numero de ventas.**""", color=0xD40E1D)
                await anuncio_inicio.edit(embed=embed, content="")
                return
            else:
                pass
        except Exception:
            embed = discord.Embed(description=f"""**El numero maximo de boletos es incorrecto.**""", color=0xD40E1D)
            await anuncio_inicio.edit(embed=embed, content="")
            return
        
        embed = discord.Embed(description=f"""{tipo_obtenido}\n\n:star2: **Vendedor**: {memb.mention}\n:moneybag: **Precio:** ${tipo_obtenido22}\n:label: **Boletos**: 0/{tipo_obtenido3}\n:green_circle: **Estado**: Activo!\n\n:shopping_bags: **ID:** """, color=0x62D727)
        ididentificator = await chann.send(embed=embed)
        await anuncio_inicio.edit(content=f":pencil: Anuncio creado en {chann.mention} con un identificador de `{ididentificator.id}`.")
        embed.description = f"""{tipo_obtenido}\n\n:star2: **Vendedor**: {memb.mention}\n:moneybag: **Precio:** ${tipo_obtenido22}\n:label: **Boletos**: 0/{tipo_obtenido3}\n:green_circle: **Estado**: Activo!\n\n:shopping_bags: **ID:** {ididentificator.id}"""
        await ididentificator.edit(embed=embed)
        with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
            idcompracheck = json.load(idcomprc)
        idcomprc.close()
        idcompracheck[f"{ididentificator.id}"] = {}
        idcompracheck[f"{ididentificator.id}"]["status"] = "on"
        idcompracheck[f"{ididentificator.id}"]["winner"] = ""
        idcompracheck[f"{ididentificator.id}"]["buy"] = 0
        idcompracheck[f"{ididentificator.id}"]["sellix"] = 0
        idcompracheck[f"{ididentificator.id}"]["max"] = tipo_obtenido3
        idcompracheck[f"{ididentificator.id}"]["min"] = tipo_obtenido4
        idcompracheck[f"{ididentificator.id}"]["price"] = f"{tipo_obtenido22}"
        idcompracheck[f"{ididentificator.id}"]["channel"] = f"{chann.id}"
        idcompracheck[f"{ididentificator.id}"]["staff"] = f"{message.author.id}"
        idcompracheck[f"{ididentificator.id}"]["seller"] = f"{memb.id}"
        idcompracheck[f"{ididentificator.id}"]["title"] = f"{tipo_obtenido}"
        idcompracheck[f"{ididentificator.id}"]["purchased"] = {}
        with open("Data/Data.json", "w") as idcomprc:
            json.dump(idcompracheck, idcomprc)
        idcomprc.close()
    return
@anuncio.error
async def anuncio_error(message, error):
    if discord.errors.Forbidden:
        if role_staff(message.author):
            pass
        else:
            return
        
        try:
            await message.channel.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
    return

#-------######## -------------<<
@bot.command(pass_context=True, aliases=["pagar", "pago"])
async def pay(message, idunidrop = None, uidshop = None):
    if isinstance(message.channel, discord.channel.DMChannel):
        if not idunidrop or not uidshop:
            try:
                embed = discord.Embed(title=f"""{bot.user.name} • Pagos""", timestamp=datetime.utcnow(), color=server_ymal_json["Color"])
            except Exception:
                embed = discord.Embed(title=f"""{bot.user.name} • Pagos""", timestamp=datetime.utcnow(), color=0x0049FF)
            embed.set_footer(text=f"""Solicitado por {message.author}""", icon_url=f"""{message.author.avatar_url}""")
            embed.add_field(name=(f"""• NOMBRE"""), value=(f"""➭ {bot.command_prefix}pay"""), inline=True)
            embed.add_field(name=(f"""• ALIAS"""), value=(f"""➭ `pagar`, `pago`"""), inline=True)
            embed.add_field(name=(f"""• SUB-COMANDOS"""), value=(f"""➭ `{bot.command_prefix}pay <ANUNCIO-ID> <ID>` - Te agrega a la verificacion de los boletos."""), inline=False)
            try:
                await message.author.send(embed=embed)
            except Exception:
                pass
            return
        else:
            with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                idcompracheck = json.load(idcomprc)
            idcomprc.close()
            if not f"{str(idunidrop)}" in idcompracheck:
                try:
                    await message.author.send(f"""**{message.author.mention}, la id `{str(idunidrop)}` no esta registrada.**""")
                except Exception:
                    pass
                return
            else:
                if str(idcompracheck[f"{idunidrop}"]["status"]) == "wait":
                    pass
                else:
                    try:
                        await message.author.send(f"""**{message.author.mention}, el anuncio aun sigue en espera.**""")
                    except Exception:
                        pass
                    return

                if not f"{message.author.id}" in idcompracheck[f"{idunidrop}"]["purchased"]:
                    try:
                        await message.author.send(f"""**{message.author.mention}, este anuncio ya vendio todos sus boletos.**""")
                    except Exception:
                        pass
                    return
                
                channelcheck = bot.get_channel(int(idcompracheck[f"{str(idunidrop)}"][f"channel"]))
                if str(channelcheck) == "None":
                    del idcompracheck[f"{str(idunidrop)}"]
                    await message.channel.send(f"""**{message.author.mention}, la id `{str(idunidrop)}` no esta registrada.**""")
                    with open("Data/Data.json", "w") as idcomprc:
                        json.dump(idcompracheck, idcomprc)
                    idcomprc.close()
                    return
                else:
                    try:
                        messageanounce2 = await channelcheck.fetch_message(int(idunidrop))
                    except Exception:
                        del idcompracheck[f"{str(idunidrop)}"]
                        await message.channel.send(f"""**{message.author.mention}, la id `{str(idunidrop)}` no esta registrada.**""")
                        with open("Data/Data.json", "w") as idcomprc:
                            json.dump(idcompracheck, idcomprc)
                        idcomprc.close()
                        return
                    
                    if int(idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["shop"]) >= int(idcompracheck[f"{idunidrop}"]["min"]):
                        try:
                            await message.author.send(f"""**{message.author.mention}, ya llegaste al tope de boletos.**""")
                        except Exception:
                            pass
                        return
                    else:
                        URL = f"""https://dev.sellix.io/v1/orders/{str(uidshop).strip().replace(" ", "")}"""
                        httpResp = requests.get(URL, headers=headers)
                        httpJson = httpResp.json()
                        httpResp.close()
                        estado = httpJson["status"]
                        if estado == 200:
                            pass
                        elif estado == 404:
                            try:
                                await message.author.send(f""":warning: **{message.author.mention}, la ID `{uidshop}` no esta registrada como compra.**""")
                            except Exception:
                                pass
                            return
                        else:
                            print(Style.RESET_ALL + Fore.RED + Style.BRIGHT + f"""  -[ ERROR | {idcompra} | {estado} | {httpJson["error"]} ]-""" + Style.RESET_ALL)
                            return
                        
                        estadoidcheck = str(httpJson["data"]["order"]["status"])
                        uidshop = str(uidshop).strip().replace(" ", "")
                        obtenproducid = str(httpJson["data"]["order"]["product_id"])
                        if obtenproducid == str(idcompracheck[f"{idunidrop}"]["uniqid"]):
                            pass
                        else:
                            try:
                                await message.author.send(f""":warning: **{message.author.mention}, la compra no coincide con el producto.**""")
                            except Exception:
                                pass
                            return
                        clavsecertatest = str(httpJson["data"]["order"]["custom_fields"]["• CLAVE SECRETA"])
                        if str(message.author.id) == clavsecertatest:
                            pass
                        else:
                            try:
                                await message.author.send(f""":warning: **{message.author.mention}, la clave secreta no coincide con la compra.**""")
                            except Exception:
                                pass
                            return

                        if estadoidcheck == "VOIDED":
                            try:
                                await message.author.send(f""":warning: **{message.author.mention}, el pago fue cancelado.**\n:shopping_cart: **ID:** `{uidshop}`""")
                            except Exception:
                                pass
                            return
                        elif estadoidcheck == "PENDING":
                            try:
                                await message.author.send(f""":warning: **{message.author.mention}, el pago aun no se ha completado.**\n:shopping_cart: **ID:** `{uidshop}`\n:bookmark_tabs: **Vuelve a ejecutar este comando cuando este completo: `{bot.command_prefix}pay {idunidrop} {uidshop}`**""")
                            except Exception:
                                pass
                            return
                        elif estadoidcheck == "COMPLETED":
                            pass
                        else:
                            return
                        
                        cantidadcompradap = int(httpJson["data"]["order"]["quantity"])
                        with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                            idcompracheck = json.load(idcomprc)
                        idcomprc.close()
                        cantidadcompradapsum = int(idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["shop"]) + cantidadcompradap
                        if cantidadcompradapsum > int(idcompracheck[f"{idunidrop}"]["min"]):
                            cantidadcompradarest = cantidadcompradapsum - int(idcompracheck[f"{idunidrop}"]["min"])
                            cantidadcompradarest2 = int(cantidadcompradap - cantidadcompradarest)
                            cantidadctolasuim = int(idcompracheck[f"{idunidrop}"]["sellix"]) + cantidadcompradarest2
                            if cantidadctolasuim > int(idcompracheck[f"{idunidrop}"]["max"]):
                                passeselstotasl = cantidadctolasuim - int(idcompracheck[f"{idunidrop}"]["max"])
                                cantidadcompradarest += passeselstotasl
                                cantidadcompradarest2 -= passeselstotasl
                            else:
                                pass
                            idcompracheck[f"{idunidrop}"]["sellix"] += cantidadcompradarest2
                            idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["shop"] += cantidadcompradarest2
                            idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["additional"] += cantidadcompradarest
                            totalreset2 = int(idcompracheck[f"{idunidrop}"]["max"]) - int(idcompracheck[f"{idunidrop}"]["sellix"])
                            URL2 = f"""https://dev.sellix.io/v1/products/{str(idcompracheck[f"{idunidrop}"]["uniqid"])}"""
                            jsonentre2 = {"stock": totalreset2}
                            try:
                                httpResp2 = requests.put(URL2, headers=headers, json=jsonentre2)
                                httpJson2 = httpResp2.json()
                                httpResp2.close()
                            except Exception:
                                pass
                        else:
                            cantidadctolasuim = int(idcompracheck[f"{idunidrop}"]["sellix"]) + cantidadcompradap
                            if cantidadctolasuim > int(idcompracheck[f"{idunidrop}"]["max"]):
                                passeselstotasl = cantidadctolasuim - int(idcompracheck[f"{idunidrop}"]["max"])
                                cantidadcompradarest += passeselstotasl
                                cantidadcompradap -= passeselstotasl
                                idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["additional"] += cantidadcompradarest
                            else:
                                pass
                            
                            idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["shop"] += cantidadcompradap
                            idcompracheck[f"{idunidrop}"]["sellix"] += cantidadcompradap
                            totalreset2 = int(idcompracheck[f"{idunidrop}"]["max"]) - int(idcompracheck[f"{idunidrop}"]["sellix"])
                            URL2 = f"""https://dev.sellix.io/v1/products/{str(idcompracheck[f"{idunidrop}"]["uniqid"])}"""
                            jsonentre2 = {"stock": totalreset2}
                            try:
                                httpResp2 = requests.put(URL2, headers=headers, json=jsonentre2)
                                httpJson2 = httpResp2.json()
                                httpResp2.close()
                            except Exception:
                                pass
                        with open("Data/Data.json", "w") as idcomprc:
                            json.dump(idcompracheck, idcomprc)
                        idcomprc.close()
                        with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                            idcompracheck = json.load(idcomprc)
                        idcomprc.close()

                        trletobte = idcompracheck[f"{idunidrop}"]["title"]
                        testuiservemde = await bot.fetch_user(int(idcompracheck[f"{idunidrop}"]["seller"]))
                        embed = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idunidrop)}"][f"price"]}\n:label: **Boletos**: {int(idcompracheck[f"{idunidrop}"]["sellix"])}/{int(idcompracheck[f"{idunidrop}"]["max"])}\n:purple_circle: **Estado**: Pagando...\n\n:shopping_bags: **ID:** {idunidrop}""", color=0x305CC1)
                        await messageanounce2.edit(embed=embed)
                        totalusercomprad = int(idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["shop"]) + int(idcompracheck[f"{idunidrop}"]["purchased"][f"{message.author.id}"]["additional"])
                        if int(idcompracheck[f"{idunidrop}"]["sellix"]) >= int(idcompracheck[f"{idunidrop}"]["max"]):
                            try:
                                await message.author.send(f""":white_check_mark: **{message.author.mention}, tu compra ha sido verificada.**\n:label: **Boletos:** {totalusercomprad}/{int(idcompracheck[f"{idunidrop}"]["min"])}\n:shopping_bags: **ID:** `{idunidrop}`""")
                            except Exception:
                                pass
                            usersparticipando2 = idcompracheck[f"{idunidrop}"]["purchased"]
                            usersparticipando = []
                            for usersparticipando3 in usersparticipando2:
                                usersparticipando.append(usersparticipando3)
                            winner1 = random.choice(usersparticipando)
                            ganandorsearch = await bot.fetch_user(int(winner1))

                            idcompracheck[f"{idunidrop}"]["winner"] = int(winner1)
                            idcompracheck[f"{idunidrop}"]["status"] = "completed"
                            with open("Data/Data.json", "w") as idcomprc:
                                json.dump(idcompracheck, idcomprc)
                            idcomprc.close()
                            with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                                idcompracheck = json.load(idcomprc)
                            idcomprc.close()

                            tiempo_segundos = datetime.now()
                            tiempo_cadena = tiempo_segundos
                            tiempo_cadena2 = tiempo_cadena.strftime("%b %d, %Y %H:%M %p")
                            embed = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idunidrop)}"][f"price"]}\n\n:medal: {ganandorsearch.mention}\n\n:label: **Boletos**: {int(idcompracheck[f"{idunidrop}"]["sellix"])}/{int(idcompracheck[f"{idunidrop}"]["max"])}\n:red_circle: **Estado**: Finalizado!\n\n:shopping_bags: **ID:** {idunidrop}""", color=0xC2373D)
                            embed.set_footer(text=f"""Finalizó: {tiempo_cadena2}""")
                            await messageanounce2.edit(embed=embed)

                            staffsearch = await bot.fetch_user(int(idcompracheck[f"{idunidrop}"]["staff"]))
                            vendedorsearch = await bot.fetch_user(int(idcompracheck[f"{idunidrop}"]["seller"]))
                            try:
                                embed_winner = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idunidrop)}"][f"price"]}\n\n:tada: {ganandorsearch.mention}\n\n:label: **Boletos**: {totalusercomprad}/{int(idcompracheck[f"{idunidrop}"]["min"])}\n:red_circle: **Estado**: Finalizado!\n\n:shopping_bags: **ID:** {idunidrop}""", color=0xB9C62E)
                                embed_winner.set_footer(text=f"""Finalizó: {tiempo_cadena2}""")
                                await ganandorsearch.send(embed=embed_winner)
                            except Exception:
                                pass

                            totalprice = D(idcompracheck[f"{str(idunidrop)}"][f"price"]) * D(idcompracheck[f"{str(idunidrop)}"][f"max"])
                            try:
                                embed_winner = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idunidrop)}"][f"price"]}/${totalprice}\n\n:medal: {ganandorsearch.mention}\n\n:label: **Boletos**: {totalusercomprad}/{int(idcompracheck[f"{idunidrop}"]["min"])}\n:red_circle: **Estado**: Finalizado!\n\n:shield: **Staff:** {staffsearch.mention}\n:shopping_bags: **ID:** {idunidrop}""", color=0x29E3D0)
                                embed_winner.set_footer(text=f"""Finalizó: {tiempo_cadena2}""")
                                await vendedorsearch.send(embed=embed_winner)
                            except Exception:
                                pass

                            try:
                                embed_winner = discord.Embed(description=f"""{trletobte}\n\n:star2: **Vendedor**: {testuiservemde.mention}\n:moneybag: **Precio:** ${idcompracheck[f"{str(idunidrop)}"][f"price"]}/${totalprice}\n\n:medal: {ganandorsearch.mention}\n\n:label: **Boletos**: {totalusercomprad}/{int(idcompracheck[f"{idunidrop}"]["min"])}\n:red_circle: **Estado**: Finalizado!\n\n:shopping_bags: **ID:** {idunidrop}""", color=0x339EE8)
                                embed_winner.set_footer(text=f"""Finalizó: {tiempo_cadena2}""")
                                await staffsearch.send(embed=embed_winner)
                            except Exception:
                                pass
                            
                            URL3 = f"""https://dev.sellix.io/v1/products/{str(idcompracheck[f"{idunidrop}"]["uniqid"])}"""
                            try:
                                httpResp3 = requests.delete(URL3, headers=headers)
                                httpJson3 = httpResp3.json()
                                httpResp3.close()
                            except Exception:
                                pass
                            #-------######## -------------<<
                            with open("Data/Data.json", "r", encoding="utf-8", errors="ignore") as idcomprc:
                                idcompracheck = json.load(idcomprc)
                            idcomprc.close()
                            with open("Data/DataOld.json", "r", encoding="utf-8", errors="ignore") as idcomprc2:
                                idcompracheck2 = json.load(idcomprc2)
                            idcomprc2.close()
                            idcompracheck2[f"{idunidrop}"] = {}
                            idcompracheck2[f"{idunidrop}"] = idcompracheck[f"{idunidrop}"]
                            del idcompracheck[f"{idunidrop}"]

                            with open("Data/DataOld.json", "w") as idcomprc2:
                                json.dump(idcompracheck2, idcomprc2)
                            idcomprc2.close()
                            with open("Data/Data.json", "w") as idcomprc:
                                json.dump(idcompracheck, idcomprc)
                            idcomprc.close()
                            return
                        else:
                            try:
                                await message.author.send(f""":white_check_mark: **{message.author.mention}, tu compra ha sido verificada.**\n:label: **Boletos:** {totalusercomprad}/{int(idcompracheck[f"{idunidrop}"]["min"])}\n:shopping_bags: **ID:** `{idunidrop}`""")
                            except Exception:
                                pass
                            return
    else:
        try:
            await message.message.delete()
        except discord.errors.Forbidden:
            try:
                await message.channel.send("No tengo permiso para hacer eso.")
            except Exception:
                pass
            return
    return
@pay.error
async def pay_error(message, error):
    if discord.errors.Forbidden:
        if isinstance(message.channel, discord.channel.DMChannel):
            pass
        else:
            try:
                await message.message.delete()
            except discord.errors.Forbidden:
                try:
                    await message.channel.send("No tengo permiso para hacer eso.")
                except Exception:
                    pass
                return
        try:
            await message.author.send("No tengo permiso para hacer eso.")
        except Exception:
            pass
    return
#---------------######## ########-----------------------------------------------------<<












#---------------######## ----------------------<<
@bot.event
async def on_command_error(message, error):
    if isinstance(error, CommandNotFound):
        if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
            if role_staff(message.author):
                pass
            else:
                return
        
        try:
            await message.channel.send(f"""Comando desconocido. Escriba `{bot.command_prefix}help` para obtener una lista de comandos.""")
        except discord.errors.Forbidden:
            try:
                await message.channel.send("No tengo permiso para hacer eso.")
            except Exception:
                pass
    return

#-------######## -------------<<
@bot.event
async def on_message(message):
    bot_id = bot.user.id
    if message.mentions:
        for mention in message.mentions:
            if len(message.mentions) == 1:
                if mention.id == bot_id:
                    if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
                        if role_staff(message.author):
                            pass
                        else:
                            return
                    
                    try:
                        await message.channel.send(f"""Hola! Mi prefijo es: `{bot.command_prefix}`""")
                    except Exception:
                        pass
                    break
            else:
                break
    elif message.content.startswith(f"""{bot.command_prefix} """):
        if str(message.channel.id) in server_ymal_json["Channels"]["Excluded"]:
            if role_staff(message.author):
                pass
            else:
                return
            
        try:
            await message.channel.send(f"""Usa `{bot.command_prefix}help` para obtener más ayuda.""")
        except Exception:
            pass
    await bot.process_commands(message)
#---------------######## ########-----------------------------------------------------<<


#---------------######## ----------------------<<
try:
    bot.loop.create_task(status_update())
    bot.loop.create_task(print_update())

    bot.run(f"""{str(config_ymal_json["Token"])}""", reconnect=True)
except discord.errors.LoginFailure as e:
    clear()
    fiverr_error()
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Wow!")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + f""" Reason: The token is invalid!""" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Press any key to exit..." + Style.RESET_ALL)
    pause(" ")
    os._exit(0)
except discord.errors.PrivilegedIntentsRequired as e:
    clear()
    fiverr_error()
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Wow!")
    print(Fore.WHITE + Style.DIM + """  [""" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + """ERROR""" + Style.RESET_ALL + Fore.WHITE + Style.DIM + """]""" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + """ Reason: It is recommended to go to discord.com/developers/applications""" + "\n" + "  and enable privileged intents within the app page!" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Press any key to exit..." + Style.RESET_ALL)
    pause(" ")
    os._exit(0)
except aiohttp.client_exceptions.ClientConnectorError as e:
    clear()
    fiverr_error()
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Wow!")
    print(Fore.WHITE + Style.DIM + """  [""" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + """ERROR""" + Style.RESET_ALL + Fore.WHITE + Style.DIM + """]""" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + """ Reason: Unstable connection!""" + "\n")
    print(Fore.WHITE + Style.DIM + "  [" + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "ERROR" + Style.RESET_ALL + Fore.WHITE + Style.DIM + "]" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + " Press any key to exit..." + Style.RESET_ALL)
    pause(" ")
    os._exit(0)
#---------------######## ########-----------------------------------------------------<<
