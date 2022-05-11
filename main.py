import discord, os
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from keep_alive import keep_alive
import json
import wavelink
os.system("pip install -U git+https://github.com/Pycord-Development/pycord")

intents = discord.Intents(messages=True,guilds = True,reactions=True,members=True,presences = True)


status = cycle(['Made by runa#3672','Yes, i am inside fnaf universe','every day i am closer to my goals'])

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
  users[f'{user.id}']['experience'] += 3
  
 
async def level_up(users, user, message):
	experience = users[f'{user.id}']["experience"]
	lvl = users[f'{user.id}']["level"]
	if(experience >=100*lvl):
		lvl+=1
		users[f'{user.id}']["level"] = lvl
		await message.channel.send(f':tada: {user.mention} has reached level {lvl}. Congrats! :tada:')
		users[f'{user.id}']["experience"] -=100*lvl
		users[f'{user.id}']['money'] +=50
 
@client.slash_command(name='ping',description="pinging")
async def ping(ctx):
	latency = round(client.latency*1000)
	if(latency <=40):
		color = discord.Color.green()
	elif latency <=80:
		color = discord.Color.yellow()
	else:
		color = discord.Color.red()
	embed = discord.Embed(colour=color)
	embed.add_field(name='Ping',value=f' {round(client.latency * 1000)}ms',inline=True)
	embed.set_author(name='Albedo')
	embed.timestamp = datetime.utcnow()
	await ctx.respond( embed=embed)
@client.event
async def on_ready():
	change_status.start()
	client.loop.create_task(node_connect())
	print("Albedo is ready")
	
async def node_connect():
	await client.wait_until_ready()
	await wavelink.NodePool.create_node(bot=client,host = 'lavalinkinc.ml',port=443, password='incognito',https=True)
@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
	print(f'Node {node.identifier}is ready!')
@client.slash_command(guild_ids=[968887343119482940],name = 'test', description='Play song')
async def test(ctx,test):
	print(test)
@client.slash_command(guild_ids=[968887343119482940],name = 'play', description='Play song')	
async def play(ctx:commands.Context, *,search: wavelink.YouTubeTrack):
	if not ctx.voice_client:
		vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
	elif not ctx.author.voice.client:
		await ctx.respond("first join a voice channel")
	else:
		vc: wavelink.Player = ctx.voice_client
	vc.play(search)
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
