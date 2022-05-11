import discord
from discord.ext import commands

#from discord.commands import Option
#=Option(str, "Enter help page", default = "help")
class Help(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.slash_command(guild_ids=[968887343119482940],name="help",description="help page")
	async def help(self,ctx):

		embed = discord.Embed(title="Help menu",color= 0xcc30cf)
		embed.set_author(name = "Albedo's rules")
		embed.add_field(name="Misc and debug stuff", value ="`/rebuild` `/ping` `/runa` `/nsfw` `/pride`")
		embed.add_field(name = "Marry fnaf character", value = "`/roll` `/harem`")
		embed.add_field(name = "Wish simulator", value = "`/pull`")
		embed.add_field(name = "Currency", value ="`/balance` `/inventory` `/daily`")
		embed.set_footer(text = "Albedo-bot")
		embed.set_author(name = "Albedo")
		await ctx.respond(embed = embed)
		
def setup(client):
	client.add_cog(Help(client))