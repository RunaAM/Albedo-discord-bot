import discord
from discord.ext import commands
from datetime import datetime
import random
import time
import json
weaponstandard=["Cool Steel","Dark Iron Sword","Fillet Blade","Harbinger of Dawn","Skyrider Sword","Traveler's Handy Sword","Bloodtainted Greatsword","Debate Club","Ferrous Shadow","Skyrider Greatsword","White Iron Greatsword","Black Tassel","Halberd","White Tassel","Messenger","Raven Bow","Recurve Bow","Sharpshooter's Oath","Slingshot","Emerald Orb","Magic Guide","Otherworldly Story","Thrilling Tales of Dragon Slayers","Twin Nephrite"]
weaponstdicon=["https://img.game8.co/3314331/bc3a8da537f6f3a0abbde6c9d404be33.png/show","https://img.game8.co/3314950/ab54ff0cffb07b225b39bb1ea27472ff.png/show","https://img.game8.co/3314301/416956bf4dabc34a2ba5687fa116745d.png/show","https://img.game8.co/3314301/416956bf4dabc34a2ba5687fa116745d.png/show","https://img.game8.co/3314343/983a8e13a604d27e588dd545b75f5d3a.png/show","https://img.game8.co/3314334/3e7a9688b870daa36b195588b4b411b7.png/show","https://img.game8.co/3314342/b49a750d74914edbbb4e420b058e2dca.png/show","https://img.game8.co/3314341/ae6ff3c52bf84b55b5dfe8f85a831e62.png/show","https://img.game8.co/3314336/037d718439f32e228033c90264168486.png/show","https://img.game8.co/3314303/33c8280c8687394a20aa193d8d363d43.png/show","https://img.game8.co/3314345/8e2f78f19863fabb5e0271c70b6d6459.png/show","https://img.game8.co/3314339/db15531019b243e2d34a4a4ccbf1c9b0.png/show","https://img.game8.co/3314306/b9587ae2277a1d35eea3e9618d13d446.png/show","https://img.game8.co/3314340/fcb44b06187bfbca8c6dabcba06593d2.png/show","https://img.game8.co/3314302/6447976a83698ca7ab6d300502ef16c1.png/show","https://img.game8.co/3314951/6d21f379931c8b2c3deb4dc56fb23239.png/show","https://img.game8.co/3314952/f6c5ade03ce15b449f3fdba2f45bb722.png/show","https://img.game8.co/3314335/9acdab3299e0304475240aa0a0898c4b.png/show","https://img.game8.co/3332716/2acae10f27b7e48605d1f4e939bd1888.png/show","https://img.game8.co/3314333/025e3a73a44d007f4e973ef77e60bdd3.png/show","https://img.game8.co/3314307/83e8a61bde175f4b4c50bcc992be5f82.png/show"]
charstandard=['Amber',"Lisa","Kaeya","Barbara","Razor","Bennett","Noelle","Fischl","Sucrose","Beidou","Ningguang","Xiangling","Xingqiu","Chongyun","Diona","Xinyan","Rosaria","Yanfei",'Favonius Sword',"Lion's Roar","Royal Longsword","Sacrificial Sword","The Flute","Favonius Greatsword","Lithic Blade","Sacrificial Greatsword","The Bell","Favonius Lance","Lithic Spear","Favonius Warbow","Rust","The Stringless","Eye of Perception","Favonius Codex","Mappa Mare","Royal Grimoire","The Widsith","Sayu"]
charstdicon=['https://img.game8.co/3294971/3c86f28546a768018df49960a15652bf.png/show','https://img.game8.co/3294972/ee211ef041897cd2f129ef320e21a9f0.png/show',"https://img.game8.co/3294973/b2a3d5ca1d6d4cb47acedfa8a64375ca.png/show",'https://img.game8.co/3294974/5e203f4ca8c30907bae5ad23432d6047.png/show','https://img.game8.co/3294976/698d06f42b22301950f6eeda34cc9a37.png/show','https://img.game8.co/3294999/853d5357be63f501a600fc776eb27256.png/show','https://img.game8.co/3295000/c61fa6632aeb5564203541e9c59f15f1.png/show',"https://img.game8.co/3294982/edb5c8b98147514a9ce8d20888d689b6.png/show",'https://img.game8.co/3294983/a87fb8809f1abed3f0f01cb17cc6e791.png/show','https://img.game8.co/3294990/3269f50c780182e3fd1860d45189d742.png/show','https://img.game8.co/3294992/4409701c15b04ff1a597817eb2883544.png/show','https://img.game8.co/3294993/cade13884333f5388bf84bfb14f08deb.png/show','https://img.game8.co/3294994/78be634e3a6f78d37e12b16e572762ef.png/show','https://img.game8.co/3294995/fee596e42fda91cf32e9a7909a3d8f55.png/show','https://img.game8.co/3295326/9d64a28761fd5a9b03234493b690cfde.png/show','https://img.game8.co/3301616/50f3ae6dfc1a4aa34d9a80d1aef95027.png/show','https://img.game8.co/3341649/5d22208b443b074dfb35fdf393c8d62f.png/show','https://img.game8.co/3350233/8170b6a6fce6e95b547a16859c3a562e.png/show',
"https://img.game8.co/3314483/042ba3ca7e48cb6c7a8d3c8d5be805c6.png/show",'https://img.game8.co/3314480/604d2c85951b54ee14c8426aab08c908.png/show','https://img.game8.co/3314416/dec4a2bc6f8204b3749be93dd89c23bb.png/show','https://img.game8.co/3314479/f5992046e18934edf51385d836106243.png/show','https://img.game8.co/3314484/da0eb7a3ce075d51f970fda9644d6271.png/show','https://img.game8.co/3314476/0a40ecf6456acb15bd8ab7203f982a30.png/show','https://img.game8.co/3325102/0c8af0a07dccbef7613a86d89713dd0b.png/show',
'https://img.game8.co/3314475/e7435217637d18327507c1566a72c710.png/show',
'https://img.game8.co/3314478/58ceb4cfcb54e9dcceaeb8c99cf7116b.png/show',
'https://img.game8.co/3314486/a2a0db169836e941c9c7a42889c2f29d.png/show',
'https://img.game8.co/3325101/bb337551b885279cf3607f2b805bbe55.png/show',
'https://img.game8.co/3314488/27bf81c6948beeeb3cb72376f4df668e.png/show','https://img.game8.co/3314490/72c5ae525ba26d02d2b6c40b5569ad73.png/show','https://img.game8.co/3314487/79dd9495f5329d39595706ccc31cd8f6.png/show','https://img.game8.co/3314493/5346c2b9acc3860b631262eae454a9b9.png/show','https://img.game8.co/3314590/560132b7897a6642851d313d988d61a9.png/show','https://img.game8.co/3314436/77efad7021cc15aa9502a9881404ea5a.png/show',
'https://img.game8.co/3314400/98ffec5e834ec29e2d23d7892287739e.png/show','https://img.game8.co/3314591/3a9b07fded3dd45454a6d850ca203499.png/show',"https://img.game8.co/3401060/f6cef4da3d573ae064d253cf8bee1448.png/show"]
fourweaponstand=['Favonius Sword',"Lion's Roar","Royal Longsword","Sacrificial Sword","The Flute","Favonius Greatsword","Lithic Blade"]

fivestandard=["Diluc","Jean","Keqing","Mona","Qiqi"]
fiveweaponstand=["Aquila Favonia","Skyward Blade","Skyward Pride","The Unforged","Wolf's Gravestone","Primordial Jade Winged-Spear","Skyward Spine","Amos' Bow","Skyward Harp","Lost Prayer to the Sacred Winds","Memory of Dust","Skyward Atlas"]
fivewicon=["https://img.game8.co/3301810/1d9a5461f86363f32f0e377540eb4360.png/show","https://img.game8.co/3314375/be522987f46d874d5a1f1e0e45dfd43b.png/show","https://img.game8.co/3301809/49d0e32b13e22df7a2787f9e7ed24089.png/show","https://img.game8.co/3301791/2983bb1c36edb32b5e936f15973c82ab.png/show","https://img.game8.co/3331435/5f3b64340420c98dbe9506940177f266.png/show","https://img.game8.co/3314371/b69ff07b01658994f8567f638e6173a1.png/show","https://img.game8.co/3314372/9f2e6c60062269c38316327b39c7f16f.png/show","https://img.game8.co/3314370/6ffcc5b665c0c0cdcfc6a5307efb50fc.png/show","https://img.game8.co/3346261/9c2f66fddbb0cbe55f2e79b8ac8c25a0.png/show","https://img.game8.co/3346264/0e392bb85512e2abb709aa844b46eb77.png/show","https://img.game8.co/3314350/d958ab07423e73c246b074d4e8aa0e31.png/show","https://img.game8.co/3301806/a6095a397ed72ce54a8dd128b4e7089b.png/show"]
fivestdicon=["https://img.game8.co/3294975/7a7f2b46d26c4458250f8fcaca0ca94c.png/show","https://img.game8.co/3294970/8416650b93b606f33e2411387dabf550.png/show","https://img.game8.co/3294997/b30e3834cd4ed13eb7c48dbca7d1d2f1.png/show","https://img.game8.co/3294986/edda48bf6a0908f1f00fe3211da8fd09.png/show","https://img.game8.co/3294996/af8d32be60362056ffcfd333e1fab761.png/show"]
fourevent=["Sayu","Diona","Xinyan"]
foureicon=['https://img.game8.co/3401060/f6cef4da3d573ae064d253cf8bee1448.png/show','https://img.game8.co/3295326/9d64a28761fd5a9b03234493b690cfde.png/show','https://img.game8.co/3301616/50f3ae6dfc1a4aa34d9a80d1aef95027.png/show']
fiveevent=["Venti","Klee","Zhongli","Childe","Albedo","Ganyu","Xiao","Keqing","Hutao","Venti","Childe","Zhongli","Eula","Klee","Kazuha","Ayaka","Yoimiya"]
fiveeventicon=["https://img.game8.co/3294977/da7d112f0f9c44f8d123cc533a3317a8.png/show","https://img.game8.co/3294978/e0194d396700c3add4ec1b95ddce41f0.png/show","https://img.game8.co/3300497/33da5700d1749ceecbea9369809c706d.png/show","https://img.game8.co/3295009/47a42db3c2736ef309028ccbd3cfb5cf.png/show","https://img.game8.co/3310758/429ff8386dab8be2f4b1de43ac783f19.png/show","https://img.game8.co/3317298/8a6ff657aae195d782276029ad880c34.png/show","https://img.game8.co/3294989/397b1e9b2effcd2ec2dabbbc1ff6a068.png/show","https://img.game8.co/3294997/b30e3834cd4ed13eb7c48dbca7d1d2f1.png/show","https://img.game8.co/3332448/6a22c735ab5ab9db5cd251ecbf4ab2a4.png/show","https://img.game8.co/3294977/da7d112f0f9c44f8d123cc533a3317a8.png/show","https://img.game8.co/3295009/47a42db3c2736ef309028ccbd3cfb5cf.png/show","https://img.game8.co/3300497/33da5700d1749ceecbea9369809c706d.png/show","https://img.game8.co/3357399/0681a143deeb28601cffa5fee727dd3d.png/show","https://img.game8.co/3294978/e0194d396700c3add4ec1b95ddce41f0.png/show","https://img.game8.co/3378026/242362114b92f3e00ee1d72355e6870f.png/show","https://img.game8.co/3313080/2cae7dd671c21d14eff9fdd945e07da2.png/show","https://img.game8.co/3400792/b31e528518dfa732ab0f3e184ac364d3.png/show"]
class wish(commands.Cog):
	guilds_id=[860869454878736384,968887343119482940]
	def __init__(self, client):
		self.client = client
	@commands.slash_command(name = "pull",description = " wishing simulator")
	async def pull(self,ctx):
		pulled_name=["none"]
		pulled_id=[0]
		pulled_icon=["none"]
		weapon_rand = random.randint(0,len(weaponstandard)-1)
		char_rand = random.randint(0,len(charstandard)-1)
		fifty =0
		pulled_name.append(charstandard[char_rand])
		pulled_id.append("4")
		pulled_icon.append(charstdicon[char_rand])
		for i in range(1,10):
			chance = random.randint(1,90)
			if(chance%37==0):
				weapon = random.randint(1,8)
				if(fifty ==1):
					weapon =1
				if(weapon ==8):
					char_rand = random.randint(0,len(fiveweaponstand)-1)
					pulled_name.append(fiveweaponstand[char_rand])
					pulled_id.append(5)
					#pulled_icon.append(fivewicon[char_rand])
					thumb = fivewicon[char_rand]
					fifty=1
				elif(weapon <8 and weapon >5):
					char_rand = random.randint(0,len(fivestandard)-1)
					pulled_name.append(fivestandard[char_rand])
					pulled_id.append(5)
					#pulled_icon.append(fivestdicon[char_rand])
					thumb = fivestdicon[char_rand]
				else:
					pulled_name.append(fiveevent[-1])
					pulled_id.append(5)
					#pulled_icon.append(fiveeventicon[-1])
					thumb = fiveeventicon[-1]
					fifty=0
			elif(chance%10==0):
				character = random.randint(1,2)
				pulled_id.append(4)
				if(character ==1):
					char_rand = random.randint(0,len(charstandard)-1)
					pulled_name.append(charstandard[char_rand]) 
					#pulled_icon.append(charstdicon[char_rand])
				else:
					char_rand = random.randint(0,len(fourevent)-1)
					pulled_name.append(fourevent[char_rand]) 
					#pulled_icon.append(foureicon[char_rand])
			else:
				weapon_rand = random.randint(0,len(weaponstandard)-1)
				pulled_name.append(weaponstandard[weapon_rand])
				pulled_id.append(3)
				#pulled_icon.append(weaponstdicon[weapon_rand])
		color = 0
		for id in pulled_id:
			if(id == 5):
				color = 1
		if(color == 1):
			embed = discord.Embed(colour=discord.Color.gold())
			print("culoare galben")
		else:
			embed = discord.Embed(colour=discord.Color.purple())
			print("culoare mov")
		print(pulled_name)
		with open('/home/runner/Albedo-bot/data/users.json', 'r') as f:
			users = json.load(f)
		if not 'Inventory' in users[f'{ctx.author.id}']:
			users[f'{ctx.author.id}']['Inventory']={}
		for x in range(1,len(pulled_name)):
			embed.add_field(name=f'{pulled_id[x]} star',value=pulled_name[x],inline=True)
			if not f'{pulled_name[x]}' in users[f'{ctx.author.id}']['Inventory']:
				users[f'{ctx.author.id}']['Inventory'][f'{pulled_name[x]}'] =1
			else:
				users[f'{ctx.author.id}']['Inventory'][f'{pulled_name[x]}']+=1
			print("element adaugat")
		with open('data/users.json', 'w') as f:
			json.dump(users, f)

		if(color == 1):
			embed.set_thumbnail(url=thumb)
		embed.set_author(name='Albedo')
		embed.timestamp = datetime.utcnow()

		#for x in range(1,len(pulled_id)):
		#	if(x >3):
				#with open('data/users.json', 'r') as f:
				#	users = json.load(f)
		#		users[ctx.message.author.id][pulled_name[a]] +=1
				#with open('data/users.json', 'w') as f:
				#	json.dump(users, f)
		#	a+=1
		
		if(color ==1):
			await ctx.respond(file=discord.File(f'/home/runner/Albedo-bot/media/wish.mov'))

		else:
			await ctx.respond(file=discord.File(f'/home/runner/Albedo-bot/media/w1sh.mov'))
		time.sleep(10)
		await ctx.send( embed=embed)	
def setup(client):
	client.add_cog(wish(client))