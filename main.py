from twitchio.ext import commands
from datetime import datetime, timezone
import is_up
import uptime
import sys
import secrets
import time
import asyncio

streamer = secrets.streamer
super_secret_password = secrets.super_secret_password
hue = secrets.creator


class Bot(commands.Bot):

    counter = 0
    onOff = False

    def __init__(self):
        super().__init__(
            token=super_secret_password, prefix="?", initial_channels=[streamer]
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

        if is_up.get_stream():
            print("Stream is live")
            stream_started = is_up.get_stream_start_time()
            print("Stream has been up for" + uptime.calculate_time(stream_started))
        else:
            print("Offline")

    async def event_message(self, message):
        if message.echo:
            return

        print(
            message.author.name, "(", time.strftime("%H:%M"), ")", ": ", message.content
        )
        await self.handle_commands(message)

    @commands.command()
    async def pity(self, ctx: commands.Context):
        await ctx.send(f"Pity counter is at: {self.counter}")

    @commands.command()
    async def pitySet(self, ctx: commands.Context, value: int):
        if ctx.author.name == streamer or ctx.author.name == hue:
            self.counter = value
            await ctx.send(f"Counter is now: {self.counter}")

    @commands.command()
    async def pityAdd(self, ctx: commands.Context):
        self.counter += 1
        await ctx.send(f"Counter is now: {self.counter}")

    @commands.command()
    async def pityClear(self, ctx: commands.Context):
        if ctx.author.name == streamer or ctx.author.name == hue:
            self.counter = 0
            await ctx.send("Counter has been cleared.")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def kekw(self, ctx: commands.Context):
        await ctx.send(f"We dont laugh here mr {ctx.author.name}!")

    @commands.command()
    async def whoisyourdaddy(self, ctx: commands.Context):
        if ctx.author.name == hue:
            await ctx.send(f"My master {ctx.author.name}!")

    @commands.command()
    async def shutdown(self, ctx: commands.Context):
        if ctx.author.name == streamer or ctx.author.name == hue:
            await ctx.send(f"Shutting down..., goodbye {ctx.author.name}!")
            sys.exit()

    @commands.command()
    async def twentyfour(self, ctx: commands.Context):
        if ctx.author.name == streamer or ctx.author.name == hue:
            await ctx.send("Starting 24h countdown...")
            StreamerHasUptime = 20
            for i in range(24, 0, -1):
                await asyncio.sleep(3600)
                if StreamerHasUptime > 0:
                    i = i - StreamerHasUptime
                if i > 0:
                    await ctx.send(f"{i} hours left...")
                if i < 1:
                    await ctx.send(
                        "You managed to complete a full 24h stream! Congratz :D"
                    )
                    break

    @commands.command()
    async def kommand(self, ctx: commands.Context):
        await ctx.send(
            "Commands: ?hello, ?kekw, ?whoisyourdaddy, ?shutdown, ?twentyfour"
        )


bot = Bot()
bot.run()
