import discord
from discord.ext import commands
from datetime import datetime
import asyncio


class modcommands(commands.Cog):

    
    def __init__(self,bot):
        self.bot = bot
    #moderation roles
    #mass delete messages
    @commands.command(aliases = ['purge','clean','delete','pochha','saaf'] )
    @commands.has_any_role('papa','homiez')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)
    #error handler of clear
    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error, commands.BadArgument):
            problem = discord.Embed(
                title = '❌ Please give a number of message to purge',
                colour = discord.Colour.red()
            )
            await ctx.send(embed=problem)
            await ctx.message.add_reaction('❌')
            raise error
            
    #kicks a member
    @commands.command(aliases = ['Kick','getout','nikal','nikalmc'])
    @commands.has_any_role('papa')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if member == ctx.guild.owner:
            kickowner = discord.Embed(
            colour = discord.Colour.green(),
            )
        
            kickowner.set_author(name = f'❌ {member.name}#{member.discriminator} is the owner of this server')
            await ctx.message.add_reaction('❌') 
            await ctx.send(embed = kickowner)
        else:
            await member.kick(reason=reason)
            kick = discord.Embed(
            colour = discord.Colour.green(),
            )
        
            kick.set_author(name = f'✅ {member.name}#{member.discriminator} was kicked')
            await ctx.send(embed=kick)
            await ctx.message.add_reaction('✅')  
            await member.send(f'**you have been kicked out from {member.guild} by {ctx.author} Reason: {reason}**')

    #kick missing argument error
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            kick = discord.Embed(

                title = 'Command: ?kick',
                colour = discord.Colour.from_rgb(0,0,0)
            )
            kick.add_field(name= 'Description:', value= 'Kick a member')
            kick.add_field(name= 'Usage:', value ='?kick [user] [reason]')
            kick.add_field(name='Example:', value= '?kick @robin spam')
            await ctx.send(embed=kick)
            raise error
    #ban a member
    @commands.command()
    @commands.has_any_role('papa')
    async def ban(self,ctx, member : discord.Member, *,reason=None):
        if member == ctx.guild.owner:
            banowner = discord.Embed(
            colour = discord.Colour.green(),
            )
        
            banowner.set_author(name = f'❌ {member.name}#{member.discriminator} is the owner of this server')
            await ctx.message.add_reaction('❌') 
            await ctx.send(embed = banowner)
        else: 

            await member.ban(reason=reason)
            ban = discord.Embed(
            colour = discord.Colour.green(),
            )
        
            ban.set_author(name = f'✅ {member.name}#{member.discriminator} has been banned')
            await ctx.send(embed=ban)
            await ctx.message.add_reaction('✅')  
            await member.send(f'**you have been Banned from {member.guild} by {ctx.author} Reason: {reason}**')
    #ban missingargument error
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ban = discord.Embed(

                title = 'Command: ?ban',
                colour = discord.Colour.from_rgb(0,0,0)
            )
            ban.add_field(name= 'Description:', value= 'ban a member')
            ban.add_field(name= 'Usage:', value ='?ban [user] [reason]')
            ban.add_field(name='Example:', value= '?ban @robin spam')
            await ctx.send(embed=ban)
            raise error
    #unban a banned member
    @commands.command(aliases = ['Unban', 'Aaja','aja'])
    @commands.has_any_role('papa','homiez')
    async def unban(self, ctx, *,member):
        Banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in Banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                unban = discord.Embed(
                colour = discord.Colour.green()
                )
        
                unban.set_author(name = f'✅ {user.name}#{user.discriminator} was unbanned ')
                await ctx.send(embed=unban)
                await ctx.message.add_reaction('✅')  

            else:
                e = discord.Embed(
                    colour = discord.Colour.red()
                )
                e.set_author(name = '❌ that user is not banned')
                await ctx.send(embed=e)

    @unban.error
    async def unban_error(self, ctx, error):
            unban = discord.Embed(

                title = 'Command: ?unban',
                colour = discord.Colour.from_rgb(0,0,0)
            )
            unban.add_field(name= 'Description:', value= 'unban a user')
            unban.add_field(name= 'Usage:', value ='?unban [user]')
            unban.add_field(name='Example:', value= '?unban robin#1193')
            await ctx.send(embed=unban)
    
    @commands.command()
    @commands.has_any_role('papa','homiez')
    async def mute(self, ctx,member: discord.Member, *, reason=None):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                 if member == ctx.guild.owner:
                    muteowner = discord.Embed(
                    colour = discord.Colour.green(),
                    )
                    muteowner.set_author(name = f'❌ {member.name}#{member.discriminator} is the owner of this server')
                    await ctx.message.add_reaction('❌') 
                    await ctx.send(embed = muteowner)
                 else:
                    await member.add_roles(role)
                    mute = discord.Embed(
                    colour = discord.Colour.green(),
                    )
                    mute.set_author(name = f'✅ {member.name}#{member.discriminator} has been muted')


                    await ctx.send(embed=mute)
                    await ctx.message.add_reaction('✅')  
                    await member.send(f'**you have been muted from {member.guild} by {ctx.author} Reason: {reason}**')
                    return

            
        for channel in guild.text_channels:
            await channel.set_permissions(await guild.create_role(name='Muted'), overwrite=discord.PermissionOverwrite(send_message=False))

            await member.add_roles('Muted')
    #Unmutes a member
    @commands.command()
    @commands.has_any_role('papa','homiez')
    async def unmute(self, ctx, member: discord.Member):

        guild = ctx.guild

        for role in guild.roles:
            if role.name == 'Muted':
                await member.remove_roles(role)
                unmute = discord.Embed(
                colour = discord.Colour.green(),
                )
        
                unmute.set_author(name = f'✅ {member.name}#{member.discriminator} has been unmuted')
                await ctx.send(embed=unmute)
                await ctx.message.add_reaction('✅')  
                await member.send(f'**you have been unmuted from {member.guild} by {ctx.author}**')
         
    @commands.command()
    async def av(self, ctx, member: discord.Member):
        
        embed = discord.Embed(
            colour = discord.Colour.from_rgb(0,0,0),
            title = f"{member.username}'s avatar"
        )
        embed.set_author(icon_url= member.avatar_url, name = f'{member.username}#{member.discriminator}')
        embed.set_image(url = member.avatar_url)
        ctx.send(enmbed=embed)
def setup(bot):
    bot.add_cog(modcommands(bot))