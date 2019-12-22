import discord
from discord.ext import commands

token = "NjU3MTg5NzY4ODE5NTA3MjEx.Xftl1g.qEJ_LNTvKMS9I2hMGybVNM5xS4Y"
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready")

# improper way

# @client.event
# async def on_message(message):
# 	# author = message.author
# 	# content = message.content
# 	# print("{} : {}".format(author,content))
# 	#channel = message.channel
# 	if message.content.startswith('.ping'):
# 		await client.message.channel.send("Pong!")

# 	if message.content.startswith('.echo'):
# 		msg = message.content.split()
# 		output = " "
# 		for word in msg[1:]:
# 			output += word
# 			output += ' '
# 		await client.message.channel.send(output)

# # @client.event
# # async def on_message_delete(message):
# # 	author = message.author
# # 	content = message.content
# # 	channel = message.channel
# # 	await channel.send("{} : {}".format(author,content))

# Proper way

@client.command()
async def ping():
	await client.say('Pong')  #It can only be used in commands


client.run(token)