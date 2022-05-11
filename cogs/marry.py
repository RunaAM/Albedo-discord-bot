import discord
import random
import time
import json
from discord.ui import Button,View
from discord.ext import commands
character_names=["freddy fazbear","bonnie the bunny","foxy the pirate fox","chica the chicken","golden freddy","toy freddy","toy chica","toy bonnnie","mangle","withered freddy","withered chica","withered bonnie","withered foxy","puppet","shadow bonnie","shadow freddy","springtrap","phantom freddy","phantom foxy","phantom chica","phantom puppet","nightmare freddy","nightmare bonnie","nightmare chica"]
character_photos=["https://cdn.discordapp.com/attachments/972583052708552737/972583267880554556/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972583795574308915/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972583910921879624/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972583977481281536/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972584439811026955/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972584696586330112/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972585228373737502/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972585336934907946/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972585725226799114/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972585944987357214/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972586979705389117/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972587083581497354/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972588657838002186/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972588964248686662/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972589572418596904/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972589635538673684/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972589966033059860/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972590064062312458/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972590188251471942/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972590348993974322/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972590542376542208/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972590834241405008/unknown.png","https://cdn.discordapp.com/attachments/972583052708552737/972591033894469672/unknown.png","https://media.discordapp.net/attachments/972583052708552737/973658998853230592/unknown.png?width=434&height=665"]
class Marry(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids=[968887343119482940],name="rebuild", description="fnaf tinder")
	async def rebuild(self,ctx):
		length = len(character_names)
		if ctx.author.id == 858521685435088916:
			with open('/home/runner/Albedo-bot/data/characters.json', 'r') as f:
				users = json.load(f)
			for i in range(0,length):
				if not character_names[i] in users:
					users[f'{character_names[i]}'] = {}
					users[f'{character_names[i]}']['owner'] = 0
					users[f'{character_names[i]}']['game'] = "fnaf"
			with open('/home/runner/Albedo-bot/data/characters.json', 'w') as f:
				json.dump(users, f)
			await ctx.respond("json built succesfully")
		else:
			await ctx.respond("you dont have permissions to mess with me")
	@commands.slash_command(guild_ids=[968887343119482940],name="roll", description="fnaf tinder")
	async def roll(self,ctx):
		length = len(character_names)
		roll_limit = 5
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
		if not 'marry' in users[f'{ctx.author.id}']:
			users[f'{ctx.author.id}']['marry'] = {}
		if not 'time' in users[f'{ctx.author.id}']['marry']:
			users[f'{ctx.author.id}']['marry']["time"] = time.time()
		if not 'rolls' in users[f'{ctx.author.id}']['marry']:
			users[f'{ctx.author.id}']['marry']["rolls"] = roll_limit
			
		if(time.time() - users[f'{ctx.author.id}']['marry']["time"] >=3600):
			users[f'{ctx.author.id}']['marry']["rolls"] = roll_limit
			users[f'{ctx.author.id}']['marry']["time"] = time.time()
		
		if(users[f'{ctx.author.id}']['marry']["rolls"] >0  ):
			number = random.randint(0,length-1)
			users[f'{ctx.author.id}']['marry']["rolls"] -=1
			embed=discord.Embed(title="Albedo's tinder", color=0xd24b4b)
			embed.set_image(url=character_photos[number])
			embed.add_field(name=character_names[number], 				value="wow", inline=True)
			length = len(character_names)
			button = Button(label="Claim = 10 coins",style=discord.ButtonStyle.green)
			async def button_callback(interaction):
				with open('/home/runner/Albedo-bot/data/characters.json', 'r') as f:
					chars = json.load(f)
				if ctx.author.id == interaction.user.id and users[f'{ctx.author.id}']['money'] >=10:
					chars[f"{character_names[number]}"]['owner'] = ctx.author.id
					users[f'{ctx.author.id}']['money'] -=10
					with open('/home/runner/Albedo-bot/data/users.json', 'w') as f:
						json.dump(users, f)
					await interaction.response.send_message("Claimed")
				elif ctx.author.id != interaction.user.id:
					await interaction.response.send_message("No stealing fmm")
				else:
					await interaction.response.send_message("Not enough money for claiming")
				with open('/home/runner/Albedo-bot/data/characters.json', 'w') as f:
					json.dump(chars, f)
				
			with open('/home/runner/Albedo-bot/data/characters.json', 'r') as f:
					chars = json.load(f)
			if chars[f"{character_names[number]}"]['owner']== 0:
				button.callback = button_callback
				view = View()
				view.add_item(button)
				await ctx.respond(embed=embed,view = view)
			else:
				embed.set_footer(text=f"Owned by {ctx.bot.get_user(int(chars[f'{character_names[number]}']['owner']))}")
				await ctx.respond(embed=embed)
		else:
			seconds = int(3600-(time.time()-users[f'{ctx.author.id}']['marry']['time']))
			minutes = int(seconds/60)
			seconds = seconds - minutes*60
			await ctx.respond(f"wait for {minutes} minutes and {seconds} seconds")
		with open('data/users.json', 'w') as f:
			json.dump(users, f)
	@commands.slash_command(guild_ids=[968887343119482940],name="harem", description="your character collection")
	async def harem(self,ctx):
		with open('/home/runner/Albedo-bot/data/characters.json', 'r') as f:
			chars = json.load(f)
		embed = discord.Embed(colour=discord.Color.purple())
		embed.set_author(name= f"{ctx.author.name}'s harem")
		for char in chars:
			if chars[char]['owner'] == ctx.author.id:
				embed.add_field(name = str(char),value='wow')
		await ctx.respond(embed=embed)
		
def setup(client):
	client.add_cog(Marry(client))