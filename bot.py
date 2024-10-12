import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(intents = intents,command_prefix='!')

# Dictionary to store customer vouches
vouches = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='vouch', help='Vouch for a customer')
async def vouch(ctx, customer: discord.Member):
    if customer.id not in vouches:
        vouches[customer.id] = 1
    else:
        vouches[customer.id] += 1
    await ctx.send(f'Vouch added for {customer.mention}! They now have {vouches[customer.id]} vouches.')

@bot.command(name='vouches', help='Get vouches for a customer')
async def get_vouches(ctx, customer: discord.Member):
    if customer.id in vouches:
        await ctx.send(f'{customer.mention} has {vouches[customer.id]} vouches.')
    else:
        await ctx.send(f'{customer.mention} has no vouches.')

bot.run('')
