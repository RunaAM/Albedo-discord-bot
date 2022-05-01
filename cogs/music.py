import discord
import youtube_dl
import pafy
from discord.ext import commands

class Player(commands.Cog):
	def __init__(self,client):
		self.client = client
		self.song_queue = {}
		self.setup=()
	def setup(self):
		for guild in self.client.guilds:
			self.song_queue[guild.id] =[]

	async def check_queue(self,ctx):
		if len(self.song_queue[ctx.guild.id]) >0:
			ctx.voice_client.stop()
			await self.play_song(ctx,self.song_queue[ctx.guild.id][0])
			self.song_queue[ctx.guild.id].pop(0)
	async def search_song(self,amount,song,get_url=False):
		info = await self.client.loop.run_in_executor(None,lambda:youtube_dl.YoutubeDL({'quiet': False,
    'default_search': 'ytsearch',
    'format': 'bestaudio/best',
    'youtube_include_dash_manifest': False,}).extract_info(f"ytsearch{amount}:{song}",download=False,ie_key="YoutubeSearch"))
		if len(info['entries']) ==0:return None

		return[entry["webpage_url"] for entry in info['entries']] if get_url else info

	async def play_song(self,ctx,song):
		url = pafy.new(song).getbestaudio().url
		ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)),after=lambda error:self.client.loop.create_task(self.check_queue(ctx)))
		ctx.voice_client.source.volume = 0.5
	@commands.command()
	async def join(self,ctx):
		if ctx.author.voice is None:
			return await ctx.send("You wanna listen to music but you are not in the voice channel, interesting... ")
		
		if ctx.voice_client is not None:
			await ctx.author.voice.channel.disconnect()
		await ctx.author.voice.channel.connect()
		self.song_queue[860869454878736384,968887343119482940] =[]
	
	@commands.command()
	async def leave(self,ctx):
		if ctx.voice_client is not None:
			return await ctx.voice_client.disconnect()
		await ctx.send("I am no longer in a voice channel.")

	@commands.command()
	async def play(self,ctx,*,song=None):
		if song is None:
			return await ctx.send("You wanna listen to what?")
		if ctx.voice_client is None:
			return await ctx.send("Dont you need me for you to listen?")

		#handle song where is not url
		if not("youtube.com/watch"in song or "https://youtu.be/" in song):
			await ctx.send("Searching for the song, it might take a while.")
			result = await self.search_song(1,song,get_url = True)
			if result is None:
				return await ctx.send("I apologise but i could not find the song, maybe next time.")
				song = result[0]
		if ctx.voice_client.source is not None:
			queue_len = len(self.song_queue[ctx.guild.id])

			if queue_len < 100:
				self.song_queue[ctx.guild.id].append(song)
				return await ctx.send(f"This song has been queued at the position {queue_len+1}." )
			else:
				return await ctx.send("I understand you have no life but i have my limits")
		await self.play_song(ctx,song)
		await ctx.send(f"Now playing: {song}")

	@commands.command()
	async def search(self,ctx,*,song=None):
		if song is None: return await ctx.send("You forgot to include the song.")
		await ctx.send("Searching for the song, it might take a while")
		info = await self.search_song(5,song)
		embed = discord.Embed(title = f"results for '{song}'",description="Use these urls to play what you want")
		amount = 0
		for entry in info['entries']:
			embed.description+=f"[{entry['title']}]({entry['webpage_url']})\n"
			amount +=1

		embed.set_footer(text=f'Displaying the first {amount}results')
		await ctx.send(embed = embed)

	@commands.command()
	async def queue(self, ctx):
		if len(self.song_queue[ctx.guild.id]) == 0:
			return await ctx.send("There are no songs in the queue")
		embed = discord.Embed(title='Song queue',description="",colour=discord.Colour.dark_gold())
		i = 1
		for url in self.song_queue[ctx.guild.id]:
			embed.description += f"{i}) {url}\n"
			i+=1

		embed.set_footer(text="Thanks for using me!")
		await ctx.send(embed=embed)

	@commands.command()
	async def skip(self,ctx):
		if ctx.voice_client is None:
			return await ctx.send("I am not playing any song")
		if ctx.author.voice is None:
			return await ctx.send("You are not connected to a voice channel")
		if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
			return await ctx.send("I am not playing any song")

		ctx.voice_client.stop()
		await self.check_queue(ctx)
	@commands.command()
	async def pause(self,ctx):
		await ctx.voice_client.pause()
		await ctx.send("Paused")
	@commands.command()
	async def resume(self,ctx):
		await ctx.voice_client.resume()
		await ctx.send("Resumed")

def setup(client):
	client.add_cog(Player(client))