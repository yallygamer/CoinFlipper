import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "$")
viplist = ("246993761673019394", "361888183505649664")
allowlist = ("kop","munt")
isresetting = False
with open("coins.txt") as obj:
    coins = obj.read().splitlines()

with open("date.txt") as obj:
    date = obj.read().splitlines()

@client.event
async def on_ready():
    print("Bot is online en heeft tot nu toe geen foutmeldingen")
    await client.change_presence(game=discord.Game(name="$info"))

@client.event
async def on_message(message):
    if message.content == "$Removecoins":
        isresetting = True
        await client.send_message(message.channel, "Zeker weten? Zeg `COINSREMOVE` om door te gaan! Of zeg `STOP` om te stoppen!")
        UserID = message.author.id
    if message.content == "COINSREMOVE":
        if isresetting:
                 await client.send_message(message.channel, "ok")
                 isresetting = False

    
    if message.content == "$info":
     userID = message.author.id
     await client.send_message(message.channel, "Hey <@%s>! Ik ben Coin Flipper! Ik ben een bot waarmee je geld kan verdienen (En verliezen!) door te tossen! Om alle commands te zien, gebruik ``$Commands!``\nCoin Flipper is gemaakt met de progammeertaal **Python 3.6 IDLE.**\nDe maker van de bot is **@Stanlin#8449** op Discord!" % (userID))

    if message.content == "$commands":
     await client.send_message(message.channel, "**LET OP: Coin Flipper is gevoelig voor caps lock!**\nDit zijn mijn commands:\n**$commands** *Deze command heb jij net gebruikt, om alle commands te zien!*\n**$coinflip <jouw keuze van kant> [aantal munten]** *Gebruik dit om te tossen! Kies tussen 'munt' en 'kop' en vul een aantal coins in waarmee je wil gokken! Voorbeeld: $coinflip kop 10*\n**$info** *Gebruik deze command om de informatie van de bot te zien!*\n **$daily** *Met deze command kan je je dagelijkse 250 coins claimen!*\n**$coins** *Deze command vertelt jou hoeveel coins jij in je portemonnee hebt zitten!* *")
    if message.content == "$coins":
        try:
            userID = message.author.id
            user_coins = coins[coins.index(userID)+1]
            await client.send_message(message.channel, "<@%s>, jij hebt op dit moment %s coins in je portemonnee!" % (userID, user_coins))
        except ValueError:
            await client.send_message(message.channel, "<@%s>, jij hebt op dit moment 0 coins in je portemonnee!" % (userID))
 
    if message.content.startswith("$coinflip"):
                userID = message.author.id
                args = message.content.split(" ")
                guess = args[1].upper
                answer = random.choice(["Kop", "Munt", "Kop", "Munt"])
                money = int(args[2])
                user_coins = coins[coins.index(userID)+1]
                if int(user_coins) < int(money):
                        await client.send_message(message.channel, "<@%s>, je hebt niet genoeg coins in je portemonnee om deze actie uit te voeren!" % (userID))
                else:
                        if userID in coins:
                            if args[1].upper() == answer.upper():
                                    moneynew = int(args[2]) + int(args[2])
                                    await client.send_message(message.channel, "<@%s>, je hebt gewonnen! %s was het antwoord! Je hebt %s coins gewonnen, die zijn nu toegevoegd aan jouw portemonnee! :money_mouth:" % (userID, answer, money))
                                    user_coins = coins[coins.index(userID)+1]
                                    newcoins = int(user_coins) + money 
                                    start = coins.index(userID) 
                                    coins.pop(start)
                                    coins.pop(start)
                                    coins.append(userID)
                                    coins.append(newcoins)
                                    update_coins()
                            elif args[1].upper() is not answer.upper():
                                    await client.send_message(message.channel, "<@%s>, je hebt verloren! %s was het antwoord. Je hebt %s coins verloren! :slight_frown:" % (userID, answer, money))
                                    user_coins = coins[coins.index(userID)+1]
                                    newcoinsl = int(user_coins) - money
                                    start = coins.index(userID) 
                                    coins.pop(start)
                                    coins.pop(start)
                                    coins.append(userID)
                                    coins.append(int(newcoinsl))
                                    update_coins()

                        else:
                            userID = message.author.id
                            await client.send_message(message.channel, "<@%s>, jij hebt geen coins! Gebruik **$daily** om je dagelijkse coins te krijgen!" % (userID))
    if message.content.startswith("$givememoney"):
        userID = message.author.id
        if userID in viplist:
            args = message.content.split(" ")
            password = args[1]
            if password == "tryhard":
                await client.send_message(message.channel, "Jij gold digger... Je hebt zojuist 10000 coins ontvangen, omdat ik je speciaal vind!")
                if userID in coins:

                                user_coins = coins[coins.index(userID)+1]
                                newcoins = int(user_coins) + int(10000)
                                start = coins.index(userID) 
                                coins.pop(start)
                                coins.pop(start)
                                coins.append(userID)
                                coins.append(int(newcoins))
                                update_coins()
                else:
                    coins.append(userID)
                    coins.append(int(10000))
                    update_coins()
            else:
                await client.send_message(message.channel, "verkeerd wachtwoord!")
    if message.content.startswith("$transfer"):
        args = message.content.split(" ")
        usernewID = int(args[2])
        userID = message.author.id
        moneytransfer = int(args[1])
        correctformat =(str("@") + str(args[2])
        
        if usernewID is not correctformat:
            await client.send_message(message.channel, "<@%s>, dat was geen persoon! Zeker weten dat je de ID goed had?" % (userID))
        else:
                             
            userID = message.author.id
            if userID in coins:
                user_coins = coins[coins.index(userID)+1]
                if user_coins < int(args[2]):
                    await client.send_message(message.channel, "@<%s>, je hebt hier niet genoeg coins voor!" % (userID))
                else:
                        newcoinsl = int(user_coins) - moneytransfer
                        start = coins.index(userID) 
                        coins.pop(start)
                        coins.pop(start)
                        coins.append(userID)
                        coins.append(int(newcoinsl))
                        update_coins()
            else:
                await client.send_message(message.channel
                
        
        
        
                              
                            
                
        else:
            await client.send_message(message.channel,"<@%s>, mooi geprobeerd! Jij staat niet op mijn VIP lijst :wink:" % (userID))

    if message.content == "$daily":
        import datetime
        
        today = datetime.date.today()
        userID = message.author.id
        if userID in date:
                userdate = date[date.index(userID)+1]
                if str(userdate) == str(today):
                    await client.send_message(message.channel, "<@%s>, je hebt je dagelijkse 250 coins voor vandaag algeclaimed! Kom morgen terug!" % (userID))
                    
                elif str(userdate) is not str(today):
                    if userID in coins:

                        user_coins = coins[coins.index(userID)+1]
                        newcoins = int(user_coins) + int(250)
                        start = coins.index(userID) 
                        coins.pop(start)
                        coins.pop(start)
                        coins.append(userID)
                        coins.append(int(newcoins))
                        update_coins()
                        await client.send_message(message.channel, "<@%s>, je hebt je dagelijkse 250 coins geclaimed!" % (userID))
                        date.pop(start)
                        date.pop(start)
                        date.append(userID)
                        date.append(str(today))
                        update_date()
                    
                    else:
                        coins.append(userID)
                        coins.append(int(250))
                        update_coins()
                        await client.send_message(message.channel, "<@%s>, je hebt je dagelijkse 250 coins geclaimed!" % (userID))
                        date.pop(start)
                        date.pop(start)
                        date.append(userID)
                        date.append(str(today))
                        update_date()

        else:
                    if userID in coins:

                        user_coins = coins[coins.index(userID)+1]
                        newcoins = int(user_coins) + int(250)
                        start = coins.index(userID) 
                        coins.pop(start)
                        coins.pop(start)
                        coins.append(userID)
                        coins.append(int(newcoins))
                        update_coins()
                        await client.send_message(message.channel, "<@%s>, je hebt je dagelijkse 250 coins geclaimed!" % (userID))
                        date.append(userID)
                        date.append(str(today))
                        update_date()
                    
                    else:
                        coins.append(userID)
                        coins.append(int(250))
                        update_coins()
                        await client.send_message(message.channel, "<@%s>, je hebt je dagelijkse 250 coins geclaimed!" % (userID))
                        date.append(userID)
                        date.append(str(today))
                        update_date()


        
def update_coins():
    with open("coins.txt", "w") as f:
        for each in coins:
             f.write(str(each)) 
             f.write("\n")
def update_date():
    with open("date.txt", "w") as f:
        for each in date:
                f.write(str(each)) 
                f.write("\n")


client.login(process.env.BOT_TOKEN);
