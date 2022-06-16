import discord
from discord import Colour as c
from discord import Embed as e

async def challenge1(self):
    await self.send("*Welcome Rookie Trainer,*")
    await self.send("```\n```")
    await self.send("I heard from your mom that you wanted a Pokémon to start your journey. However there is a slight problem, all the Pokémon have run away. So right now, I don’t have any Pokémon to give to you. I am so sorry, I already sent out Nos to catch them back again but that might take a while.")
    await self.send("```\n```")
    await self.send("**Uhm, I have one other solution..** Right here I have a Pokedex <:pokedex:975729785810595940> and in this there are different types of starter Pokémon. The three types being **grass, water and fire.** And in this tab here on your pokedex you can see all the available Pokémon. What if I give you 10 great balls and you’ll have to catch 10 starter Pokémon of either the **grass, fire or water type.**")
    embedGrass = e(title="Grass", description="Bulbasaur, Chikorita, Treecko, Turtwig, Snivy, Chespin, Rowlet & Grookey", color=0x2ecc71)
    await self.send(embed=embedGrass)
    embedWater = e(title="Water", description="Squirtle, Totodile, Mudkip, Piplup, Oshawott, Froakie, Popplio & Sobble", color=0x3498db)
    await self.send(embed=embedWater)
    embedFire = e(title="Fire", description="Charmander, Cyndaquil, Torchic, Chimchar, Tepig, Fennekin, Litten & Scorbunny", color=0xe74c3c)
    await self.send(embed=embedFire)
    embedChal1 = e(title="Challenge 1: Catch 10 Starter Pokémon of one specific type", description="Catch either 10 Grass, 10 Water or 10 Fire Starter Pokémon and post a screenshot of the caught Pokémon in the thread <#" + str(975752561179099146) + ">")
    await self.send(embed=embedChal1)

async def challenge2(self):
    await self.send(file=discord.File('img/mint gym.png'))
    await self.send("*Welcome to Mint City.*")
    await self.send("The First Pokémon Gym is located in this town and it's a **Rock Type Gym**.")
    await self.send("You can also go to <#" + str(985494646950084638) +"> here to catch some more Pokémon before challenging this gym.")
    embedChal2 = e(title="Challenge 2: Defeat the Mint Gym Leader", description="Ping & Battle <@" + str(228954580795392001) + "> in <#" + str(981485850858770503) + ">", color=0xa84300)
    await self.send(embed=embedChal2)

async def challenge3(self):
    await self.send("*Welcome Mint Badge Trainer,*")
    await self.send("On this route you encounter a **sleeping Snorlax** <:sleeping:986764892885356544>.")
    await self.send("You & your team cannot move it or awake it. However you remember that there is a Pokémon who is very **loud**. Maybe 3 of them can help wake him up")
    await self.send(file=discord.File('img/pokemon-tired.gif'))
    embedChal3 = e(title="Challenge 3: Catch 3 Pokémon that are loud", description="Send <@" + str(238353350964281344) + "> a Direct Message with the screenshots that you have caught it. There are 3 correct answers in this scenario")
    await self.send(embed=embedChal3)

async def challenge4(self):
    await self.send(file=discord.File('img/unknown.png'))
    await self.send("*Welcome to Herbal Town <:herb:986763418667208764>,*")
    await self.send("This town strikes you as weird, since no herbs are to be found anywhere anymore.. there are only dried landscapes and all the people seem to have moved out except for a few. You decide to ask around a few villagers, but get no definite answers except that they don't know any better and they never touched any herbs in their entire life. You find that strange, however it will be fine you guess..")
    await self.send("For now, you'll have to do what you came to do here, to fight the Herbal Town Gym. It's a **grass type gym**")
    await self.send("however, before going there you come across a certain figure dressed in white. You decide to approach him, however before you could he *vanished* into thin air.")
    embedChal4 = e(title="Challenge 4: Defeat the Herbal Gym Leader", description="Ping & Battle <@" + str(223940201502867457) + "> in <#" + str(981510120733310996) + ">")
    await self.send(embed=embedChal4)

async def challenge5(self):
    await self.send("*Welcome Herbal Badge Trainer,")
    await self.send("On this route something peculiar happened. You are only seeing Pokémon from the __Kanto Region__ in here, however this used to be a road filled with all kinds of different Pokémon and especially Budew was one that was roaming around a lot. However, determined to get to the cause of it, you bought 25 Pokéballs and are going to catch some of them. ")
    embedChal5 = e(title="Challenge 5: Catch 25 Pokémon from the Kanto Region", description="Send the screenshots (or the links) in <#" + str(985541291616112720) + "> Yes, Legendary and Shinies are allowed & yes you may catch 25 caterpies.")
    await self.send(embed=embedChal5)

async def challenge6(self):
    await self.send("Catch 5 Misjas")

async def challenge7(self):
    await self.send("Catch 5 Misjas")

async def challenge8(self):
    await self.send("Catch 5 Misjas")

async def challenge9(self):
    await self.send("Catch 5 Misjas")

async def challenge10(self):
    await self.send("Catch 5 Misjas")

async def challenge11(self):
    await self.send("Catch 5 Misjas")

async def challenge12(self):
    await self.send("Catch 5 Misjas")
async def challenge13(self):
    await self.send("Catch 5 Misjas")
async def challenge14(self):
    await self.send("Catch 5 Misjas")
async def challenge15(self):
    await self.send("Catch 5 Misjas")
async def challenge16(self):
    await self.send("Catch 5 Misjas")
async def challenge17(self):
    await self.send("Catch 5 Misjas")
async def challenge18(self):
    await self.send("Catch 5 Misjas")
async def challenge19(self):
    await self.send("Catch 5 Misjas")
async def challenge20(self):
    await self.send("Catch 5 Misjas")
async def challenge21(self):
    await self.send("Catch 5 Misjas")
async def challenge22(self):
    await self.send("Catch 5 Misjas")
async def challenge23(self):
    await self.send("Catch 5 Misjas")
async def challenge24(self):
    await self.send("Catch 5 Misjas")
async def challenge25(self):
    await self.send("Catch 5 Misjas")
async def challenge26(self):
    await self.send("Catch 5 Misjas")
async def challenge27(self):
    await self.send("Catch 5 Misjas")
async def challenge28(self):
    await self.send("Catch 5 Misjas")
async def challenge29(self):
    await self.send("Catch 5 Misjas")
async def challenge30(self):
    await self.send("Catch 5 Misjas")
