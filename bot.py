# Needed imports from various sources
# If error try installing then though python3
from urllib import response
import discord
import os 
from neuralintents import GenericAssistant
from art import * # Not needed just looks good for Start message!
import platform
from dotenv import load_dotenv

load_dotenv()
TOKEN = (os.getenv('TOKEN')) # Token ENV path 

chatbot = GenericAssistant('intents.json') # Tells the bot to look at intents.json for further responses ect ect...
chatbot.train_model()
chatbot.save_model()

def start_message():  # Start message which will be sent if the bot is put online successfully!
    my_system = platform.uname()
    msg = text2art("goose bot",font='Colossal')
    print(msg)
    print("[+] goosebot ready!")
    print(f"[+] running on: {my_system.system} {my_system.release} {my_system.machine}")


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("goosebot"): # if message starts with "goosebot" then reply...
        response = chatbot.request(message.content[9:])
        await message.channel.send(response)


#Main Program
start_message() 


#Discord Program Start {bottom}

client.run(TOKEN)
