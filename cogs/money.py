import discord
from discord.ext import commands
import json
#from discord.commands import Option
#=Option(str, "Enter help page", default = "help")
class Money(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(name="balance", description="shows balance")
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

	@commands.slash_command(name="inventory", description="shows inventory")
	async def inventory(self,ctx):
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
		embed=discord.Embed(title="Inventory", color=0x44882b)
		embed.set_author(name=f"{ctx.author.name}'s items",icon_url="https://cdn.discordapp.com/attachments/860869456846782487/970358117768503386/unknown.png")
		for key in users[f'{ctx.author.id}']['Inventory']:
			embed.add_field(name=f'{key}', value=f"{users[f'{ctx.author.id}']['Inventory'][f'{key}']}", inline=True)
		await ctx.respond(embed=embed)
def setup(client):
    client.add_cog(Money(client))