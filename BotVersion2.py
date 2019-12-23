import os, random, discord
from discord.ext import commands,tasks
from itertools import cycle
from dotenv import load_dotenv

#Storing API keys safely.
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = ".")
status = cycle(['Pubg PC','GTA VI','God of War 4'])

@client.event
async def on_ready():
	change_status.start()
	# await client.change_presence(status=discord.Status.idle,activity=discord.Game('Hello Boi !!'))
	print("Bot is ready")

@tasks.loop(seconds=10)
async def change_status():
	 await client.change_presence(activity=discord.Game(next(status)))


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

@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.CommandNotFound):
		await ctx.send('Invalid command for help use .help !!')


@client.command()
@commands.has_permissions(manage_messages=True)#check user has a permission to delete
async def clear(ctx,amount : int):
	await ctx.channel.purge(limit=amount)

def is_it_me(ctx):
	return ctx.author.id == 658199810410807336

#custom check
@client.command()
@commands.check(is_it_me)
async def example():
	await ctx.send(f'Hi I m {ctx.author}')

@clear.error
async def clear_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send('Abe argument to daal !!')


@client.command()
async def kick(ctx,member : discord.Member,*,reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx,member : discord.Member,*,reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name,user.discriminator) == (member_name,member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

@client.command()
async def load(ctx,extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

# for filename in os.listdir('./cogs'):
# 	if filename.endswith('.py'):
# 		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)