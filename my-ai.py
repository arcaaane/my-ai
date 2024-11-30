import discord
from discord.ext import commands
from g4f.client import Client
bot = commands.Bot(command_prefix="?")
client = Client()
@bot.command()
async def robo(ctx, *, question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
    )
    answer = response.choices[0].message.content
    await ctx.send(answer)
bot.run(token)