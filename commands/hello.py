import discord
from discord.ext import commands
from discord import app_commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hi", description="Hi mesajı gönderir.")
    async def selam_slash(self, interaction: discord.Interaction):
        await interaction.response.send_message("hi!")

async def setup(bot):
    await bot.add_cog(Hi(bot))
