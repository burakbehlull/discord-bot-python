import discord
from discord.ext import commands
import json

with open('./config.json') as f:
    config = json.load(f)
    
intents = discord.Intents.all()

class BurakBehlul(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config["prefix"], intents=intents)
        self.initial_extensions = []

    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)
            
bot = BurakBehlul()

for filename in os.listdir('./commands'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.initial_extensions.append(f'commands.{filename[:-3]}')

for filename in os.listdir('./events'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.initial_extensions.append(f'events.{filename[:-3]}')
        
for filename in os.listdir('./prefixCommands'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.initial_extensions.append(f'prefixCommands.{filename[:-3]}')
 
bot.run(config["token"])
