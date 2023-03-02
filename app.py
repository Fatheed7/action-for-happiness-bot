import os

import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from datetime import datetime

if os.path.exists("env.py"):
    import env

# Get Discord Token
TOKEN = os.getenv('DISCORD_TOKEN')
# Set Intents
intents = nextcord.Intents.all()
# Set Bot
bot = commands.Bot()
# Set Server ID
servers = [int(os.getenv('SERVER_ID'))]

# Confirm successful Discord connection
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Action for Happiness Slash Command /action #
@bot.slash_command(guild_ids=servers,
                   description="Get the daily Action for Happiness")
async def action(interaction: Interaction):
    # Get current date
    now = datetime.now()
    # Return current day
    day = now.strftime("%d")
    # Return current month (short form)
    month = now.strftime("%b").upper()
    # Return current month name in full
    month_name = now.strftime("%B")
    # Return current month number
    month_number = now.strftime("%m")
    # Return current year
    year = now.strftime("%Y")
    # Set image URL
    image_url = (
        "https://actionforhappiness.org/sites/default/files/styles/"
        "daily_message_convo_overlay/public/AFH_ACTION_"
        + year + "_" + month_number + "_" + month + "_" + day + ".png")
    # Trying Sending Image in Embed
    try:
        embed = nextcord.Embed(
            title="Daily Action for " + month_name + " " + day + ", " + year,
            color=nextcord.Color.blue()
        )
        embed.set_image(
            url=image_url)
        await interaction.response.send_message(embed=embed)
    # If Image Not Found, Send Error Message
    except Exception:
        await interaction.send((
            "```Sorry, I couldn't find the Action for Happiness image for today.```"))
        
# Run Bot
bot.run(TOKEN)