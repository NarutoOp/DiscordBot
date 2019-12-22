import discord
import random
from discord.ext import commands

token = "NjU4MTc0MzI4NzkzMzMzNzYw.Xf7-bw.e6GWc_8NtP6HzrJcR83GRD3Zj70"
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Bot is ready")

@client.event
async def on_member_join(member):
	print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left  server.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
	responses = ['It is certain.',
				'It is decidedly so.',
				'Without a doubt.',
				'Yes definitely.',
				'You may rely on it.',
				'As I see it ,yes',
				'Most likely.',
				'Outlook good.',
				'Yes.',
				'Signs point to you.',
				'Reply hazy, try again.',
				'Ask again later.',
				'Better not tell you now.',
				'Cannot predict now.',
				'Concentrate and ask again.',
				'Dont count on it.',
				'My reply is no',
				'My sources say no',
				'Outlook not so good',
				'Very doubtful.']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx,amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member : discord.Member,*,reason=None):
	await member.kick(reason=reason)

@client.command()
async def ban(ctx,member : discord.Member,*,reason=None):
	await member.ban(reason=reason)

client.run(token)