# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020, Yazılımcıların Mola Yeri (ymydepo)
#

from cogs.utils import checks

from discord.ext import commands
import discord


class Mod(commands.Cog):
    """The description for Mod goes here."""

    def __init__(self, bot):
        self.bot = bot

    @checks.is_mod()
    @commands.command(aliases=["süpür"])
    async def clean(self, ctx, amount=1):
        channel = ctx.message.channel

        messages = list()
        # Verdiğimiz komutda bir mesaj olduğu için fazladan 1 tane daha siliyoruz.
        async for message in channel.history(limit=int(amount) + 1):
            messages.append(message)

        await channel.delete_messages(messages)
        await channel.send(
            f"`{len(messages)}` mesaj başarıyla süpürüldü!", delete_after=3,
        )

    @checks.is_mod()
    @commands.command(aliases=["yazdır"])
    async def print(self, ctx, channel: discord.TextChannel, *, content):
        await channel.send(content)


def setup(bot):
    bot.add_cog(Mod(bot))
