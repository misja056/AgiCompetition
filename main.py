import challenges

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# Import the os module.
import os

# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

# Loads the .env file that resides on the same level as the script.
load_dotenv('token.env')

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
#bot = discord.Client()
bot = commands.Bot(command_prefix='*')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
#@bot.event
#async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "*challenge1".
	#if message.content == "*challenge122":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		#member = message.author
		#role = get(member.guild.roles, name="Admin") 
		#if role in member.roles:
			#await message.channel.send("Catch 10 Starter Pokémon of a specific type (grass/water/fire)")
			#await message.channel.send(file=discord.File('C:/Users/groen/Documents/AgiCompetition/img/pokemon-tired.mp4'))
		#await bot.process_commands(message)

@bot.command()
async def challenge(ctx, number:int):
	if (number == 1) and (get(ctx.guild.roles, name="Rookie Trainer")) in ctx.author.roles:
		await challenges.challenge1(ctx)
	elif (number == 2) and (get(ctx.guild.roles, name="Starter Trainer")) in ctx.author.roles:
		await challenges.challenge2(ctx)
	elif (number == 3) and (get(ctx.guild.roles, name="Mint Badge")) in ctx.author.roles:
		await challenges.challenge3(ctx)
	elif (number == 4) and (get(ctx.guild.roles, name="Snorlax Player")) in ctx.author.roles:
		await challenges.challenge4(ctx)
	elif (number == 5) and (get(ctx.guild.roles, name="Herbal Badge")) in ctx.author.roles:
		await challenges.challenge5(ctx)
	elif (number == 6) and (get(ctx.guild.roles, name="Kanto Master")) in ctx.author.roles:
		await challenges.challenge6(ctx)
	elif (number == 7) and (get(ctx.guild.roles, name="Citrus Badge")) in ctx.author.roles:
		await challenges.challenge7(ctx)
	elif (number == 8) and (get(ctx.guild.roles, name="Helping Hand")) in ctx.author.roles:
		await challenges.challenge8(ctx)
	elif (number == 9) and (get(ctx.guild.roles, name="Helping Hand")) in ctx.author.roles:
		await challenges.challenge9(ctx)
	elif (number == 10) and (get(ctx.guild.roles, name="Light in the Dark")) in ctx.author.roles:
		await challenges.challenge10(ctx)
	elif (number == 11) and (get(ctx.guild.roles, name="Chai Badge")) in ctx.author.roles:
		await challenges.challenge11(ctx)
	elif (number == 12) and (get(ctx.guild.roles, name="Surfer")) in ctx.author.roles:
		await challenges.challenge12(ctx)
	elif (number == 13) and (get(ctx.guild.roles, name="Haunted")) in ctx.author.roles:
		await challenges.challenge13(ctx)
	elif (number == 14) and (get(ctx.guild.roles, name="Cozy Badge")) in ctx.author.roles:
		await challenges.challenge14(ctx)
	elif (number == 15) and (get(ctx.guild.roles, name="Malt Badge")) in ctx.author.roles:
		await challenges.challenge15(ctx)
	elif (number == 16) and (get(ctx.guild.roles, name="Cup of Tea")) in ctx.author.roles:
		await challenges.challenge16(ctx)
	elif (number == 17) and (get(ctx.guild.roles, name="Bergamot Badge")) in ctx.author.roles:
		await challenges.challenge17(ctx)
	elif (number == 18) and (get(ctx.guild.roles, name="Riddlemaster")) in ctx.author.roles:
		await challenges.challenge18(ctx)
	elif (number == 19) and (get(ctx.guild.roles, name="Survivor")) in ctx.author.roles:
		await challenges.challenge19(ctx)
	elif (number == 20) and (get(ctx.guild.roles, name="Survivor")) in ctx.author.roles:
		await challenges.challenge20(ctx)
	elif (number == 21) and (get(ctx.guild.roles, name="Smoke Badge")) in ctx.author.roles:
		await challenges.challenge21(ctx)
	elif (number == 22) and (get(ctx.guild.roles, name="Safari Zone")) in ctx.author.roles:
		await challenges.challenge22(ctx)
	elif (number == 23) and (get(ctx.guild.roles, name="Bulked Up")) in ctx.author.roles:
		await challenges.challenge23(ctx)
	elif (number == 24) and (get(ctx.guild.roles, name="Almost There")) in ctx.author.roles:
		await challenges.challenge24(ctx)
	elif (number == 25) and (get(ctx.guild.roles, name="Almost There")) in ctx.author.roles:
		await challenges.challenge25(ctx)
	elif (number == 26) and (get(ctx.guild.roles, name="Almost There")) in ctx.author.roles:
		await challenges.challenge26(ctx)
	elif (number == 27) and (get(ctx.guild.roles, name="Almost There")) in ctx.author.roles:
		await challenges.challenge27(ctx)
	elif (number == 28) and (get(ctx.guild.roles, name="Almost There")) in ctx.author.roles:
		await challenges.challenge28(ctx)
	elif (number == 29) and (get(ctx.guild.roles, name="Professors Legacy")) in ctx.author.roles:
		await challenges.challenge29(ctx)
	elif (number == 30) and (get(ctx.guild.roles, name="The Moment You Waited For")) in ctx.author.roles:
		await challenges.challenge30(ctx)


@bot.command()
async def hey(ctx, arg):
	await ctx.send("Hey hoer " + arg)
	await ctx.send(file=discord.File('C:/Users/groen/Documents/AgiCompetition/img/middelvinger.jpg'))

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)

