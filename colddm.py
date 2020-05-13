import discord
import asyncio
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('1개의 서버에서 사용중입니다!')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('!dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 540511614844010497:                       
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="콜드샵에서 알려드립니다!")
                        embed.add_field(name="오늘도 콜드샵을 이용해주셔서 감사합니다!", value=msg, inline=True)
                        embed.set_footer(text=f"콜드샵은 항상 여러분들을 기다립니다! 초대링크: discord.gg/c6SxN8e")
                        await i.send(embed=embed)
                except:
                    pass

access_token = os.environ["BOT_TOKEN"]
client.run()
