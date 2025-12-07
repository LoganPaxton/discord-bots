# Setup Instructions:
# 1. Create a file named ".env"
# 2. Create a variable inside of the .env file named "BOT_TOKEN" with the content of your bot's token.
# You set .env variables by doing var_name=var_content (e.g., BOT_TOKEN=iahsfoihwe8hberboha23f32f_2f39hdfsSDF)
# 3. Install requirements.txt running "pip install -r requirements.txt"

# This is a very basic ticket system, and I do plan on updating it to make it more modern, and robust.

import os
import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import PermissionOverwrite
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["BOT_TOKEN"] # Do NOT hardcode your token, it is very insecure.

# Be sure to configure the variables below to match what is actually in your server.
TICKET_CATEGORY_ID = 1447121124109451335
STAFF_ROLE_ID = 1447122100937560155

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Bot Latency: {round(bot.latency * 1000)}ms')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

class CloseButton(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, button: Button):
        if not interaction.channel.name.startswith("ticket-"):
            return await interaction.response.send_message(
                "This isn't a ticket channel.", ephemeral=True
            )

        await interaction.response.send_message("Closing ticket...", ephemeral=True)
        await interaction.channel.delete(reason="Ticket closed")

@bot.tree.command(name="ticket", description="Open a support ticket.")
async def ticket(interaction: discord.Interaction):
    category = interaction.guild.get_channel(TICKET_CATEGORY_ID)
    if category is None:
        return await interaction.response.send_message(
            "Ticket category not found.", ephemeral=True
        )

    for channel in category.channels:
        if channel.name == f"ticket-{interaction.user.id}":
            return await interaction.response.send_message(
                "You already have a ticket open.", ephemeral=True
            )

    overwrites = {
        interaction.guild.default_role: PermissionOverwrite(view_channel=False),
        interaction.user: PermissionOverwrite(view_channel=True, send_messages=True),
        interaction.guild.get_role(STAFF_ROLE_ID): PermissionOverwrite(
            view_channel=True, send_messages=True
        ),
    }

    channel = await category.create_text_channel(
        name=f"ticket-{interaction.user.name}",
        overwrites=overwrites,
        reason="New Ticket",
    )

    await channel.send(
        f"{interaction.user.mention} Your ticket has been created.",
        view=CloseButton()
    )

    await interaction.response.send_message(
        f"Your ticket has been created: {channel.mention}", ephemeral=True
    )


bot.run(TOKEN)