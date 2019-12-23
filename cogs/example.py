import discord 
from discord.ext import commands


class Example(commands.Cog):
	def __init__(self,client):
		self.client = client

	#events in cog
	@commands.Cog.listener()
	async def on_ready(self):#must pass self when defining in cogs
		print('Bot is online.')

	#commands in cog
	@commands.command()
	async def ping(self,ctx):
		await ctx.send(f'Pong!')


def setup(client):
	client.add_cog(Example(client))  