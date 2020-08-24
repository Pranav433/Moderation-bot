import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
status = ["I'm still being made,dont use me", "Ur mom Gay", "mridul gay"]


@bot.command()
async def enable(ctx, extension):
   bot.load_extension(f'modules.{extension}')
   await ctx.send(f'{extension} enabled')


@bot.command()
async def disable(ctx,extension):
    bot.unload_extension(f'modules.{extension}')
    await ctx.send(f'{extension} disabled')

modules = ['modules.casual','modules.modcommands']

if __name__ == '__main__':
    for module in modules:
        bot.load_extension(module)

#replace with your bot's token
bot.run('YOUR BOT's token here')
