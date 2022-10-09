from lib2to3.pgen2 import token
import gspread
import discord

#updates the list of roles and discord ids
def update():
    global roles
    global discord_ids

    #uses the json file with the passwords and shit
    gc = gspread.service_account(filename='google_token.json')

    #opens page 1 of the spread sheet
    sh = gc.open("SPAC")

    #gets all the roles from the collombs as a list of lists
    roles = sh.sheet1.get("B3:B35")
    discord_ids = sh.sheet1.get("C3:C35")


#starts the discord bot
client = discord.Client()


#gives you a lovley message to let you know the bot has logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    #changes what the bot displays as doing
    await client.change_presence(activity = discord.Activity(name="vietnam war ASMR", type=2))


#makes it so the bot doesnt respond to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return


    #This checks for the message below and then executes the code below
    if message.content.startswith('!roles'):

        #gets an updated list of the roles and discord ids
        update()

        #uses the json file with the passwords and shit
        gc = gspread.service_account(filename='sex.json')

        #opens page 1 of the spread sheet
        sh = gc.open("SPAC")

        #gets all the roles from the collombs as a list of lists
        squads = sh.sheet1.get("E4:E36")
        
        #this sets an embed for the roles
        embed=discord.Embed(title="__**Roles avaliable:**__", color=0x0088ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752557777037164626/764934074460274778/arma_3_unit_logo.png")

        #puts all the squads into a nicely formatted list
        counter = 0

        #runs the loop once for every squad
        for i in range(0, int(sh.sheet1.get("E3")[0][0])):
            
            #this remembers the numbering from the old squad
            current_num = counter

            #clears the message to add as an embed
            msg_send = ""

            #runs the code below for every slot in a squad
            for x in range(0, int(squads[i][0])):
                msg_send += "\n" + str(x+current_num+1) + ": " + roles[x+current_num][0] + ": **" + discord_ids[x+current_num][0] + "**"
                counter += 1

            #adds to the embed    
            embed.add_field(name="__**Squad " + str(i+1) + ":**__", value=msg_send, inline=False)

        await message.channel.send(embed=embed)


    #This checks for the message below and then executes the code below
    elif message.content.startswith('!take'):
    
        update()

        role_number = message.content[6:len(message.content)]

        #checks to see if your command is correct
        if role_number.isdigit() == True:
            
            #checks wether the role is valid or not
            if len(roles)+1 > int(role_number) and int(role_number) > 0:

                #checks if the role is free
                if discord_ids[int(role_number)-1][0] == "Vacant":

                    #checks to see if you have allready taken a role
                    if [str(message.author)] not in discord_ids:
                    
                        #uses the json file with the 
                        gc = gspread.service_account(filename='sex.json')

                        #opens page 1 of the spread sheet
                        sh = gc.open("SPAC")

                        #updates the sheet with the discord id of the person who signed up
                        sh.sheet1.update("C" + str(int(role_number)+2), str(message.author))
                        sh.sheet1.update("D" + str(int(role_number)+2), str(message.author.id))
                        await message.channel.send('Thanks for signing up!')

                    else:
                        await message.channel.send('You allready have a role!')

                else:
                    await message.channel.send('That role is allready taken!')
            else:
                await message.channel.send('Bruh that aint even a role...')
        else:
            await message.channel.send('Bruh can you even format the command properly?')


    #This checks for the message below and then executes the code below
    elif message.content.startswith('!leave'):
        
        update()

        role_number = message.content[7:len(message.content)]

        #checks to see if your command is correct
        if role_number.isdigit() == True:

            #checks wether the role is valid or not
            if len(roles)+1 > int(role_number) and int(role_number) > 0:

                #checks if the role is occupied by you
                if discord_ids[int(role_number)-1][0] == str(message.author):

                    #uses the json file with the passwords and shiz
                    gc = gspread.service_account(filename='sex.json')

                    #opens page 1 of the spread sheet
                    sh = gc.open("SPAC")

                    #leaves the role and writes vacant to it
                    sh.sheet1.update("C" + str(int(role_number)+2), "Vacant")
                    sh.sheet1.update("D" + str(int(role_number)+2), "Vacant")
                    await message.channel.send('The role has been left')

                else:
                    await message.channel.send('That role isnt yours...')
            else:
                await message.channel.send('Bruh that aint even a role...')
        else:
            await message.channel.send('Bruh can you even format the command properly?')


    #adds the help command
    elif message.content.startswith('!help'):
        embed=discord.Embed(title="Help:", color=0x0088ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752557777037164626/764934074460274778/arma_3_unit_logo.png")
        embed.add_field(name="!roles", value="Shows you all the roles which are avaliable and their associated numbers", inline=False)
        embed.add_field(name="!take (number)", value="Takes the role associated with the number you entered", inline=False)
        embed.add_field(name="!leave (number)", value="Leaves the role associated with the number you entered", inline=False)
        embed.add_field(name="!about", value="Displays information about the bot such as its version", inline=False)
        await message.channel.send(embed=embed)

    #adds the about command
    elif message.content.startswith('!about'):
        embed=discord.Embed(color=0x0088ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/752557777037164626/764934074460274778/arma_3_unit_logo.png")
        embed.add_field(name="About:", value="This bot is currently at version 1.2 (last updated 18/12/2020) and was coded by kittycat959 of the spac unit, you can check out his website here: https://kittyhosting.net", inline=False)
        await message.channel.send(embed=embed)

    #the command which lets jacob ping everyone
    elif message.content.startswith('!start') and str(message.author) in ["Kraken.434#5974","kittycat959#4886"]:
        update()

        #uses the json file with the passwords and shit
        gc = gspread.service_account(filename='sex.json')

        #opens page 1 of the spread sheet
        sh = gc.open("SPAC")

        #gets all the roles from the collombs as a list of lists
        user_ids = sh.sheet1.get("D3:D28")

        #this sets an embed for the roles
        to_ping = "Event starting soon, get on teamspeak!\n"
        
        for x in range (0, len(discord_ids)):

            user_to_mention = user_ids[x][0]

            if user_to_mention != "Vacant":
                to_ping += "<@!"+user_to_mention+">\n"
                #embed.add_field(name=roles[x][0]+":",value="<@"+user_to_mention+">", inline=False)

        await message.channel.send(to_ping)
        #await message.channel.send(embed=embed)

token_file = open("demofile.txt", "r")
discord_token = token_file.read()
token_file.close()
client.run(discord_token)
