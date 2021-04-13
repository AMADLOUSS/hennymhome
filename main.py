import discord
from discord.ext import commands
import requests
import os

bot = commands.Bot(command_prefix ="!", descripton = "Bot hennymhome")
client = discord.Client()



@client.event
async def on_ready():
	print("ready !")
	
@client.command()
async def talk(ctx, args):
	await ctx.send(args)
	
@client.command()
async def manual():
	await ctx.send(args)


@client.command()
async def d(ctx, *, args=''):
	url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+args
	R = requests.get(url)
	if R.status_code !=200:
		await ctx.send("GET method returned:", status_code)
	elif R is None:
		await ctx.send("response is null")
	else :
		drinks=R.json()['drinks']
		if drinks != None:
			for items in drinks:
				await ctx.send(items['strDrink'])
		else :
			await ctx.send("The drink you are looking for "+args+" is very rare, I can't find it!")
			
			
	
@client.command()
async def c(ctx, *, args=''):
	url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+args
	R = requests.get(url)
	if R.status_code !=200:
		await ctx.send("GET method returned:", status_code)
	elif R is None:
		await ctx.send("response is null")
	else :
		drinks=R.json()['drinks']
		if drinks != None:
			for items in drinks:
				if items['strDrink'].lower() == args.lower():
					await ctx.send(items['strDrink']+ " " + items['strDrinkThumb'])
		else :
			await ctx.send("The drink you are looking for "+args+" is very rare, I can't find it!")	
			
@client.command()
async def r(ctx, *, args=''):
	url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+args
	R = requests.get(url)
	if R.status_code !=200:
		await ctx.send("GET method returned:", status_code)
	elif R is None:
		await ctx.send("response is null")
	else :
		drinks=R.json()['drinks']
		if drinks != None:
			for items in drinks:
				print(args, items['strDrink'])
				if items['strDrink'].lower() == args.lower():
					await ctx.send(items['strInstructions'])
		else :
			await ctx.send("The drink you are looking for "+args+" is very rare, I can't find it!")
			
			

	

client.run(os.environ['DISCORD_BOT_TOKEN'])