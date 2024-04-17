from twitchio.ext import commands
import secrets

super_secret_password=secrets.super_secret_password


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=super_secret_password , prefix='?', initial_channels=['fiskenhero'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        print(message.author.name, ': ' , message.content)
        await self.handle_commands(message)


    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command()
    async def kekw(self, ctx: commands.Context):
        await ctx.send(f'We dont laugh here mr {ctx.author.name}!')


    @commands.command()
    async def test(self, ctx: commands.Context):
        # check if user is 'fiskenhero'
        if ctx.author.name == 'fiskenhero':
            await ctx.send(f'My master {ctx.author.name}!')


bot = Bot()
bot.run()
