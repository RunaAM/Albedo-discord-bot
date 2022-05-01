import discord
from discord.ext import commands

#from discord.commands import Option
#=Option(str, "Enter help page", default = "help")
class Help(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(name="help",description="type all in page")
	async def help(self,ctx,page):
		if type == "all":
			embed=discord.Embed(title="Help menu", description="principal menu", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="music player", value="/help music", inline=True)
			embed.add_field(name="wish simulator", value="/help wish", inline=True)
			embed.add_field(name="misc", value="/help misc", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'music':
			embed=discord.Embed(title="Help menu", description="Music player", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="Not available", value="in construction", inline=True)
			
			
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'wish':
			embed=discord.Embed(title="Help menu", description="Wish simulator", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="a!pull", value="Uses the genshin like gacha system WITHOUT PITY", inline=True)
			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
		elif type == 'misc':
			embed=discord.Embed(title="Help menu", description="Misc", color=0xcc30cf)
			embed.set_author(name="Albedo's rules")
			embed.add_field(name="/pride", value="be who you are", inline=True)
			embed.add_field(name="/ping", value="ping pong", inline=True)
			embed.add_field(name="/nsfw", value="umm", inline=True)
			embed.add_field(name="/runa", value="runa", inline=True)

			embed.set_footer(text="Albedo-bot")
			await ctx.respond(embed=embed)
def setup(client):
	client.add_cog(Help(client))