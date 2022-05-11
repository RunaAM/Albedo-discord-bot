import discord
from discord.ext import commands
import json
#from discord.commands import Option
#=Option(str, "Enter help page", default = "help")
import random
import time
class Money(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids =[968887343119482940],name="balance", description="shows balance")
	async def balance(self,ctx):
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
			if "money" in users[f'{ctx.author.id}']:
				
				embed=discord.Embed(title="Balance", color=0x44882b)
				embed.set_author(name=f"{ctx.author.name}'s wallet",icon_url="https://cdn.discordapp.com/attachments/860869456846782487/970358117768503386/unknown.png")
				embed.add_field(name="Coins", value=f"{users[f'{ctx.author.id}']['money']}", inline=True)
				embed.add_field(name="Level",value = f"{users[f'{ctx.author.id}']['level']}",inline=True)
				embed.add_field(name="XP",value = f"{users[f'{ctx.author.id}']['experience']}",inline=True)
				await ctx.respond(embed=embed)
			else:
				users[f'{ctx.author.id}']["money"] = 0
				await ctx.respond("Balance created")


				
		with open('/home/runner/Albedo-bot/data/users.json', 'w') as f:
			json.dump(users, f)

	@commands.slash_command(guild_ids=[968887343119482940],name="inventory", description="shows inventory")
	async def inventory(self,ctx):
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
		embed=discord.Embed(title="Inventory", color=0x44882b)
		embed.set_author(name=f"{ctx.author.name}'s items",icon_url="https://cdn.discordapp.com/attachments/860869456846782487/970358117768503386/unknown.png")
		for key in users[f'{ctx.author.id}']['Inventory']:
			embed.add_field(name=f'{key}', value=f"{users[f'{ctx.author.id}']['Inventory'][f'{key}']}", inline=True)
		await ctx.respond(embed=embed)
	@commands.slash_command(guild_ids=[968887343119482940],name="daily", description="get daily coins")
	async def daily(self,ctx):
		amount = random.randint(50,100)
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
		if not 'daily' in users[f'{ctx.author.id}']:
			users[f'{ctx.author.id}']['daily'] = time.time()
			users[f'{ctx.author.id}']['money'] += amount
			embed = discord.Embed(colour=discord.Color.green())
			embed.add_field(name='Coins added',value=f' +{amount}',inline=True)
			embed.set_author(name="Albedo's purse")
			await ctx.respond( embed=embed)
		else:
			if int((time.time()-users[f'{ctx.author.id}']['daily'] )>=3600*12  ):
				users[f'{ctx.author.id}']['daily'] = time.time()
				users[f'{ctx.author.id}']['money'] += amount
				embed = discord.Embed(colour=discord.Color.green())
				embed.add_field(name='Coins added',value=f' +{amount}',inline=True)
				embed.set_author(name="Albedo's purse")
				await ctx.respond( embed=embed)
			else:
				seconds=int(3600*12 -(time.time()-users[f'{ctx.author.id}']['daily']))
				hours = int(seconds/3600)
				seconds = seconds-hours*3600
				minutes = int(seconds/60)
				seconds = seconds-minutes*60
				embed = discord.Embed(colour=discord.Color.red())
				embed.add_field(name='Wait for',value=f' {hours} hours {minutes} minutes and {seconds} seconds',inline=True)
				embed.set_author(name="Albedo's purse")
				await ctx.respond( embed=embed)
		with open('/home/runner/Albedo-bot/data/users.json', 'w') as f:
			json.dump(users, f)
def setup(client):
    client.add_cog(Money(client))