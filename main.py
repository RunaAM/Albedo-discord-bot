import discord, os
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from keep_alive import keep_alive
import json
os.system("pip install -U git+https://github.com/Pycord-Development/pycord")
intents = discord.Intents(messages=True,guilds = True,reactions=True,members=True,presences = True)


status = cycle(['Made by runa#3672','a! will no longer be used'])

icon = " "

client = commands.Bot(command_prefix = "a!",intents = discord.Intents.all())
client.remove_command('help')
with open('data/users.json', 'r') as f:
  users = json.load(f)
players = {}
@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		await ctx.send("I do not understand what your message is.")
@client.event
async def on_message(message):
	if message.author.bot == False:
		with open('data/users.json', 'r') as f:
			users = json.load(f)
		await add_experience(users, message.author)
		await level_up(users, message.author, message)
		if "money" in users[f'{message.author.id}']:
			users[f'{message.author.id}']["money"] +=1
		else:
			users[f'{message.author.id}']["money"] = 0
		with open('data/users.json', 'w') as f:
			json.dump(users, f)
			await client.process_commands(message)
					 	

	await client.process_commands(message)
async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 6
  
 
async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.channel.send(f':tada: {user.mention} has reached level {lvl_end}. Congrats! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@client.slash_command(name='ping',description="pinging")
async def newping(ctx):
	embed = discord.Embed(colour=discord.Color.green())
	embed.add_field(name='Ping',value=f' {round(client.latency * 1000)}ms',inline=True)
	embed.set_author(name='Albedo')
	embed.timestamp = datetime.utcnow()
	await ctx.respond( embed=embed)
@client.event
async def on_ready():
	change_status.start()
	print("Albedo is ready")


@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(os.environ['Token'])
