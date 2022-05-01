import discord
from discord.ext import commands
from datetime import datetime


class Meme(commands.Cog):
	guilds_id=[860869454878736384,968887343119482940]
	def __init__(self, client):
		self.client = client

	@commands.slash_command( name="nsfw",description="ok")
	async def nsfw(self,ctx):
		await ctx.respond("I see a lot of... questionable stuff here")


	@commands.slash_command( name="runa",description="runa runa runa runa")
	async def andrei(self,ctx):
		await ctx.respond("<:emoji_1:871794698887499776>")


	@commands.slash_command( name="pride",description="BEE WHO YOU ARE")
	async def pride(self,ctx):
		embed = discord.Embed(title='I,Albedo the chief alchemist, have to say "happy pride month!!"',
                          colour=discord.Color.orange())
		embed.set_author(
        name='Albedo'
    )
		
		embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/846783543694721087/848931596609912862/200w.gif'
    )
		embed.timestamp = datetime.utcnow()
		await ctx.respond( embed=embed)
	
def setup(client):
    client.add_cog(Meme(client))