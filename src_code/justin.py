# This example requires the 'message_content' intent.
import requests
from bs4 import BeautifulSoup
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def runescapeupdate():

    response = requests.get('https://oldschool.runescape.com/l=2/')
    html_page = response.text
    soup = BeautifulSoup(html_page, 'html.parser')
    url = soup.find(id="news-article-fig-1")

    # Inside the webpage...
    response2 = requests.get(url.get("href"))
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    title = soup2.title

    return url.get("href")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if 'runescape' in message.content.lower() and 'justin' in message.content.lower() and 'update' in message.content.lower():
        await message.channel.send(runescapeupdate())


token = os.environ['TOKEN']

client.run(token)

