from discord.ext import commands
import discord

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[BOT]: {self.bot.user} olarak giriş yaptı!')
        game = discord.Game("Bot aktif.")
        await self.bot.change_presence(status=discord.Status.idle, activity=game)
        
        try:
            synced = await self.bot.tree.sync()  # Access the bot's tree attribute directly
            print(f"{len(synced)} komut senkronize edildi")
        except Exception as e:
            print(f"Komutları senkronize ederken hata: {e}")

async def setup(bot):
    await bot.add_cog(OnReady(bot))
