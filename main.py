import discord
from discord.ext import commands

intents = discord.Intents.all()

class BurakBehlul(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
        self.initial_extensions = []

    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            
bot = BurakBehlul()

bot.run("TOKEN HERE")
