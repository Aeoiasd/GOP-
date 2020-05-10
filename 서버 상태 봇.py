import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("Mady By 이쁘고 잘생기고 귀엽고 능력자 Xenix#6607") # 이거 지우면 너는 음... 진짜 양식 없는 XX (이쁘고 잘생기고 귀엽고 능력자는 지워도 됨)
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):

    if message.author.guild_permissions.administrator and message.content.startswith("/서버 시작"):
        embed = discord.Embed(title="```🔔아폴론 서버 상태🔔```", description="```아폴론 서버 상태 : SERVER ON 🟢```", color=0x62c1cc)
        embed.set_footer(text="Mady By 이쁘고 잘생기고 귀엽고 능력자 Xenix#6607") # 이거 지우면 너는 음... 진짜 양식 없는 XX (이쁘고 잘생기고 귀엽고 능력자는 지워도 됨)
        embed.set_image(url="당신의 사진 링크를 넣으시오!")
        await message.channel.send(embed=embed)

    if message.author.guild_permissions.administrator and message.content.startswith("/서버 종료"):
        embed = discord.Embed(title="```🔔아폴론 서버 상태🔔```", description="```아폴론 서버 상태 : SERVER OFF 🔴```", color=0x62c1cc)
        embed.set_footer(text="Mady By 이쁘고 잘생기고 귀엽고 능력자 Xenix#6607") # 이거 지우면 너는 음... 진짜 양식 없는 XX (이쁘고 잘생기고 귀엽고 능력자는 지워도 됨)
        embed.set_image(url="당신의 사진 링크를 넣으시오!")
        await message.channel.send(embed=embed)

    if message.author.guild_permissions.administrator and message.content.startswith("/서버 리붓"):
        embed = discord.Embed(title="```🔔아폴론 서버 상태🔔```", description="```아폴론 서버 상태 : SERVER REBOOT ✔️```", color=0x62c1cc)
        embed.set_footer(text="Mady By 이쁘고 잘생기고 귀엽고 능력자 Xenix#6607") # 이거 지우면 너는 음... 진짜 양식 없는 XX (이쁘고 잘생기고 귀엽고 능력자는 지워도 됨)
        embed.set_image(url="당신의 사진 링크를 넣으시오!")
        await message.channel.send(embed=embed)

    if message.author.guild_permissions.administrator and message.content.startswith("/서버 정검"):
        embed = discord.Embed(title="```🔔아폴론 서버 상태🔔```", description="```잠시 서버 정검 있겠습니다. 잠시만 기달려주세요!```", color=0x62c1cc)
        embed.set_footer(text="Mady By 이쁘고 잘생기고 귀엽고 능력자 Xenix#6607") # 이거 지우면 너는 음... 진짜 양식 없는 XX (이쁘고 잘생기고 귀엽고 능력자는 지워도 됨)
        embed.set_image(url="당신의 사진 링크를 넣으시오!")
        await message.channel.send(embed=embed)


client.run("YOUR DISCORD BOT TOKEN")
