from twitchio.ext import commands
import sys
import secrets
import time
import asyncio

streamer=secrets.streamer
super_secret_password=secrets.super_secret_password
hue=secrets.creator


class Bot(commands.Bot):

    counter = 0
    onOff = False
    def __init__(self):
        super().__init__(token=super_secret_password , prefix='?', initial_channels=[streamer])


    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

#        channel = streamer
#        if channel:
#            await channel.send("Greetings, The fishy bot is now online!, type ?kommand for a list of commands")


    async def event_message(self, message):
        if message.echo:
            return

        print(message.author.name, time.strftime('%H:%M') ,': ' , message.content)
        await self.handle_commands(message)

#    async def send_message_to_stream(self, message):
#        channel = self.get_channel("streamer")
#        if channel:
#            await channel.send(message)


    # see the amount of pity counter
    @commands.command()
    async def pity(self, ctx: commands.Context):
        await ctx.send(f'Pity counter is at: {self.counter}')


    @commands.command()
    async def pitySet(self, ctx: commands.Context, value: int):
       if ctx.author.name == streamer or ctx.author.name == hue:
            self.counter = value
            await ctx.send(f'Counter is now: {self.counter}')


    @commands.command()
    async def pityAdd(self, ctx: commands.Context):
        self.counter += 1
        await ctx.send(f'Counter is now: {self.counter}')


    @commands.command()
    async def pityClear(self, ctx: commands.Context):
       if ctx.author.name == streamer or ctx.author.name == hue:
            self.counter = 0
            await ctx.send('Counter has been cleared.')


    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command()
    async def kekw(self, ctx: commands.Context):
        await ctx.send(f'We dont laugh here mr {ctx.author.name}!')


    @commands.command()
    async def whoisyourdaddy(self, ctx: commands.Context):
        # check if user is streamer or hue
        if ctx.author.name == hue:
            await ctx.send(f'My master {ctx.author.name}!')


    @commands.command()
    async def shutdown(self, ctx: commands.Context):
        # check if user is 'fiskenhero'
        if ctx.author.name == streamer or ctx.author.name == hue:
            await ctx.send(f'Shutting down..., goodbye {ctx.author.name}!')
            sys.exit()



    @commands.command()
    async def twentyfour(self, ctx: commands.Context):
        if ctx.author.name == streamer or ctx.author.name == hue:
            await ctx.send('Starting 24h countdown...')
            for i in range(24):
                await asyncio.sleep(3600)
                i = i - 1
                await ctx.send(f'{i} hours left...')
            await ctx.send('Countdown finished!')


    @commands.command()
    async def kommand(self, ctx: commands.Context):
        await ctx.send('Commands: ?hello, ?kekw, ?whoisyourdaddy, ?shutdown, ?twentyfour')


bot = Bot()
bot.run()
