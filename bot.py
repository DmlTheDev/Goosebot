from urllib import response
import discord
import os 
from neuralintents import GenericAssistant
from art import *
import platform
from dotenv import load_dotenv

load_dotenv()
TOKEN = (os.getenv('TOKEN'))

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

def start_message():
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
    
    if message.content.startswith("goosebot"):
        response = chatbot.request(message.content[9:])
        await message.channel.send(response)

# def token():
#     global TOKEN
#     f=open(TOKEN_FILE, 'r')
#     data = f.readline()
#     TOKEN = data
#     print(TOKEN)
#     f.close()
    


#Main Program
start_message() 


#Discord Program Start (BOTTOM!)  

client.run(TOKEN)
