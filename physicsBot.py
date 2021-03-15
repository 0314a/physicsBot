import discord, asyncio, datetime, pytz
from discord.ext.commands import bot
from discord.ext import commands
import random
import math

from discord.utils import get

# client = discord.Client()
client = commands.Bot(command_prefix='&')

@client.remove_command('help')

@client.event
async def on_ready():
    print("bot successfully started")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='&help'))

@client.command(pass_context = True)
async def version(ctx):
    embed=discord.Embed(title="Version Information", description="```CURRENT VERSION : BETA v1.1```", color=(0xc80000))
    embed.add_field(name='**Last Update**', value='`BETA v1.1 - 20210312`', inline=False) # latest update
    embed.add_field(name='**Next Update**', value='`BETA v1.2 - 20210315`', inline=False) # expected date
    embed.add_field(name='**Update Log**', value="type **`&updates`**", inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def updates(ctx):
    embed=discord.Embed(title="PhysicsBot Update Log", description="```CURRENT VERSION : BETA v1.1```", color=0xc80000)
    embed.add_field(name='ALPHA v1.0', value='`&ping` command added\n`&pong` command added', inline=False)
    embed.add_field(name='ALPHA v1.1', value='`&formula` command added\n`&const` command added', inline=False)
    embed.add_field(name='ALPHA v1.2', value='`&formula` image embed updated\n--thumbnail format → image format\n--Wikipedia link added\n`&prime` reprogrammed\n\
         `&dice` command updated\n--number text embed → dice image embed', inline=False)
    embed.add_field(name='BETA v1.0 - 20210311', value='**PhysicsBot first added to server**\n`&formula` command completed\n`&const` command completed\n`&version` command completed\n\
          `&help` command updated\n--`&help`(powered by <@!801172696448499723>)\n--`&help all/formula/const`', inline=False)
    embed.add_field(name='BETA v1.1 - 20210313', value='`&color` command added\n--`&color rgb` added\n`&version` command updated\n--`&updates` command added\n`str.lower(arg)` added\n\
        `&const` command updated\n--Wikipedia link added', inline=False)

    DMmsg=discord.Embed(title="Update Log", description="{}, DM을 확인해주세요".format(ctx.author.mention), color=0xc80000)
    await ctx.author.send(embed=embed)
    await ctx.send(embed=DMmsg)

@client.command(pass_context = True) 
async def help(ctx, arg):
    arg = str.lower(arg)
    if arg == 'all':
        helpList='\
        **`&version`** : 봇의 버전을 제공합니다.\n\
        **`&ping`** : 핑\n\
        **`&dice`** : 주사위를 굴립니다.\n\
        **`&formula`** : 수학/물리 공식을 제공합니다. 더 알아보려면 **`&help formula`**를 해보세요.\n\
        **`&const`** : 여러 물리 상수의 값을 제공합니다. 더 알아보려면 **`&help const`**를 해보세요.\n\
        **`&prime`** : 입력한 수의 소수 여부를 판단합니다.\n\
        **`&ang rad/degrees`** : 입력한 각도를 라디안/육십분법으로 변환합니다.\n\
        **`&color`** : 색상과 관련된 여러 작업을 수행합니다. 더 알아보려면 **&help color**를 해보세요.\n'

        embed=discord.Embed(color=0xc80000)
        embed.add_field(name = "PhysicsBot 도움말", value=helpList, inline = False)
        await ctx.send(embed=embed)

    if arg == 'formula':
        formulaList='\
        **`relativity`** : 질량-가속도 등가법칙\n\
        **`newton`** : 뉴턴의 운동 법칙\n\
        **`pyth`** : 피타고라스의 정리\n\
        **`ohm`** : 옴의 법칙\n\
        **`gravity`** : 만유인력의 법칙\n\
        **`snell`** : 스넬의 법칙\n\
        **`motion`** : 등가속도 직선운동 방정식\n\
        **`coulomb`** : 쿨롱의 법칙\n'

        embed=discord.Embed(title='**도움말:&formula**', color=0xc80000)
        embed.add_field(name="**`&formula <arg>`**", value = formulaList, inline = False)
        await ctx.send(embed=embed)

    if arg == 'const':
        constList= '\
        **`pi`** : 원주율\n\
        **`gravity`** : 중력 상수\n\
        **`planck`** : 플랑크 상수\n\
        **`avogadro`** : 아보가드로 상수\n\
        **`sol`** : 빛의 속도\n\
        **`ga`** : 중력가속도\n\
        **`expo`** : 지수\n\
        **`e`** : 기본 전하량\n\
        **`gas`** : 기체 상수\n\
        **`coulomb`** : 쿨롱 상수\n'

        embed=discord.Embed(title="**도움말:&const**", color=0xc80000)
        embed.add_field(name='**`&const <arg>`**',  value = constList, inline = False)
        await ctx.send(embed=embed)

    if arg == 'color':
        colorhelp='\
        **`rgb`** : 입력한 색의 RGB값을 알려줍니다.\n\
        **`cmyk`** : 입력한 색의 CMYK값을 알려줍니다.(완성 안됨)\n\
        **`color`** : 입력한 RGB값의 색을 알려줍니다.(완성 안됨)\n'
        embed=discord.Embed(title="**도움말:&color**", color=0xc80000)
        embed.add_field(name='**`&color <arg>`**', value=colorhelp, inline=False)
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def formula(ctx, arg):
    arg = str.lower(arg)
    if arg == 'relativity':
        embed=discord.Embed(title="질량-에너지 등가원리", color=(0xc80000))
        embed.set_image(url="https://cdn.discordapp.com/attachments/818298657124122704/818298710442246154/unknown.png")
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EC%A7%88%EB%9F%89-%EC%97%90%EB%84%88%EC%A7%80_%EB%93%B1%EA%B0%80", inline=False)
        await ctx.send(embed=embed)

    if arg == 'newton':
        embed=discord.Embed(title="뉴턴의 운동법칙", color=(0xc80000))
        embed.set_image(url='https://media.discordapp.net/attachments/818298657124122704/819202221974749194/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EB%89%B4%ED%84%B4_%EC%9A%B4%EB%8F%99_%EB%B2%95%EC%B9%99")
        await ctx.send(embed=embed)

    if arg == 'pyth':
        embed=discord.Embed(title="피타고라스의 정리", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/818299136003801128/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%ED%94%BC%ED%83%80%EA%B3%A0%EB%9D%BC%EC%8A%A4_%EC%A0%95%EB%A6%AC")
        await ctx.send(embed=embed)

    if arg == 'ohm':
        embed=discord.Embed(title="옴의 법칙", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819205996823183400/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EC%98%B4%EC%9D%98_%EB%B2%95%EC%B9%99")
        await ctx.send(embed=embed)

    if arg == 'gravity':
        embed=discord.Embed(title="만유인력의 법칙", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819224131689644072/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EB%A7%8C%EC%9C%A0%EC%9D%B8%EB%A0%A5%EC%9D%98_%EB%B2%95%EC%B9%99")
        await ctx.send(embed=embed)

    if arg == 'snell':
        embed=discord.Embed(title="스넬의 법칙", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/818302306910339083/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%84%AC%EC%9D%98_%EB%B2%95%EC%B9%99")
        await ctx.send(embed=embed)

    if arg == 'motion':
        embed=discord.Embed(title="등가속도 직선운동 공식", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/818303839651364874/unknown.png')
        embed.add_field(name="Wikipedia", value="no wikipedia link")
        await ctx.send(embed=embed)

    if arg == 'coulomb':
        embed=discord.Embed(title="쿨롱의 법칙", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819387681784070204/unknown.png')
        embed.add_field(name="Wikipedia", value="https://ko.wikipedia.org/wiki/%EC%BF%A8%EB%A1%B1_%EB%B2%95%EC%B9%99")
        await ctx.send(embed=embed)
    
    if arg == 'euler':
        embed=discord.Embed(title="오일러 공식", color=0xc80000)
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/820170994445582426/unknown.png') 
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%EA%B3%B5%EC%8B%9D')
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def const(ctx, arg):
    arg = str.lower(arg)
    if arg == 'pi':
        embed=discord.Embed(title="Digits of π", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819448687872442378/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%9B%90%EC%A3%BC%EC%9C%A8', inline=False)
        embed.add_field(name="All Digits of Pi(website by Peter Trüb)", value="https://pi2e.ch/blog/2017/03/10/pi-digits-download/", inline=False)
        await ctx.send(embed=embed)

    if arg == 'gravity':
        embed=discord.Embed(title="중력 상수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819263411636273182/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%A4%91%EB%A0%A5_%EC%83%81%EC%88%98')
        await ctx.send(embed=embed)

    if arg == 'planck':
        embed=discord.Embed(title="플랑크 상수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819378563718447104/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9E%91%ED%81%AC_%EC%83%81%EC%88%98')
        await ctx.send(embed=embed)

    if arg == 'avogadro':
        embed=discord.Embed(title="아보가드로 수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819379755664932894/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%95%84%EB%B3%B4%EA%B0%80%EB%93%9C%EB%A1%9C_%EC%88%98')
        await ctx.send(embed=embed)

    if arg == 'sol':
        embed=discord.Embed(title="진공에서의 빛의 속력", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819381568240877588/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EB%B9%9B%EC%9D%98_%EC%86%8D%EB%A0%A5')
        await ctx.send(embed=embed)

    if arg == 'ga':
        embed=discord.Embed(title="중력가속도", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819381338586349588/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%A4%91%EB%A0%A5_%EA%B0%80%EC%86%8D%EB%8F%84')
        await ctx.send(embed=embed)

    if arg == 'expo':
        embed=discord.Embed(title="자연 상수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819383229978509312/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98_%EB%B0%91')
        await ctx.send(embed=embed)

    if arg == 'e':
        embed=discord.Embed(title="기본 전하량", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819384465338925056/unknown.png')
        embed.add_field(name='Wikipedia', value='https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%B3%B8_%EC%A0%84%ED%95%98')
        await ctx.send(embed=embed)

    if arg == 'gas':
        embed=discord.Embed(title="기체 상수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819385224290893864/unknown.png')
        embed.add_field(name='https://ko.wikipedia.org/wiki/%EA%B8%B0%EC%B2%B4_%EC%83%81%EC%88%98')
        await ctx.send(embed=embed)

    if arg == 'coulomb':
        embed=discord.Embed(title="쿨롱 상수", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819386216146403388/unknown.png')
        embed.add_field(name='Wikipedia-en', value='https://en.wikipedia.org/wiki/Coulomb_constant')
        await ctx.send(embed=embed)

    if arg == 'tau':
        embed=discord.Embed(title="타우", description="**τ = 2π**", color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/818298657124122704/819434862183579658/unknown.png')
        embed.add_field(name='Wikipedia', value='https://en.wikipedia.org/wiki/Turn_(angle)#Tau_proposals')
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def dice(ctx):
    rnum = random.randint(1, 7)
    if rnum == 1:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265421852147812/inverted-dice-1.png')
        await ctx.send(embed=embed)
    if rnum == 2:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265464265867264/inverted-dice-2.png')
        await ctx.send(embed=embed)
    if rnum == 3:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265482879795220/inverted-dice-3.png')
        await ctx.send(embed=embed)
    if rnum == 4:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265496473796648/inverted-dice-4.png')
        await ctx.send(embed=embed)
    if rnum == 5:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265508611850270/inverted-dice-5.png')
        await ctx.send(embed=embed)
    if rnum == 6:
        embed=discord.Embed(color=(0xc80000))
        embed.set_image(url='https://cdn.discordapp.com/attachments/819260355829432382/819265522683215902/inverted-dice-6.png')
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def pong(ctx):
    embed=discord.Embed(title="Ping", description=('**{}** _ms_'.format(round(client.latency*1000, 1))), color=(0xc80000))
    await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def ping(ctx):
    embed=discord.Embed(title="Pong", color=(0xc80000))
    await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def prime(ctx, arg):
    arg=int(arg)
    if arg > 1:
        for i in range(2, arg):
            if (arg % i) == 0:
                embed=discord.Embed(title="소수 판정기", description="**False**", color=(0xc80000))
                await ctx.send(embed=embed)
                break
        else:
            embed=discord.Embed(title="소수 판정기", description="**True**", color=(0xc80000))
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="소수 판정기", description="**False**", color=(0xc80000))
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def ang(ctx, arg1, arg2):
    arg1 = str.lower(arg1)
    if arg1 == 'rad': #degrees to rad
        arg2=float(arg2)
        rad=math.radians(arg2)
        embed=discord.Embed(title="육십분법 → 라디안", description='**' + str(arg2) + '**' + ' degrees = ' + '**' + str(round(rad, 5)) + '**'+ ' rad', color=0xc80000)
        await ctx.send(embed=embed)
    
    if arg1 == 'degrees': #rad to degrees
        arg2=float(arg2)
        degrees=math.degrees(arg2)
        embed=discord.Embed(title="라디안 → 육십분법", description='**' + str(arg2) + '**' + ' rad = ' + '**' + str(round(degrees, 5)) + '**'+ ' degrees', color=0xc80000)
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def abs(ctx, arg):
    arg=int(arg)
    if arg == 0:
        embed=discord.Embed(title="절댓값", description="**0**", color=0xc80000)
        await ctx.send(embed=embed)
    if arg > 0:
        embed=discord.Embed(title="절댓값", description="| {} | = **{}**".format(arg, arg), color=0xc80000)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="절댓값", description="| {} | = **{}**".format(arg, -arg), color=0xc80000)
        await ctx.send(embed=embed)

@client.command(pass_context = True) 
async def color(ctx, arg1, arg2):
    arg1 = str.lower(arg1)
    if arg1 == 'rgb':
        arg2 = str.lower(arg2)
        #RGB
        if arg2 == 'red':
            embed=discord.Embed(title="Red", description="#FF0000", color=0xFF0000)
            await ctx.send(embed=embed)
        if arg2 == 'green':
            embed=discord.Embed(title="Green", description="#008000", color=0x008000)
            await ctx.send(embed=embed)
        if arg2 == 'blue':
            embed=discord.Embed(title="Blue", description="#0000FF", color=0x0000FF)
            await ctx.send(embed=embed)
        #lightRGB
        if arg2 == 'pink':
            embed=discord.Embed(title="Pink", description="#FF00FF", color=0xff00ff)
            await ctx.send(embed=embed)
        if arg2 == 'lime':
            embed=discord.Embed(title="Lime", description="#00FF00", color=0x00FF00)
            await ctx.send(embed=embed)
        if arg2 == 'lgreen':
            embed=discord.Embed(title="Lime", description="#00FF00", color=0x00ff00)
            await ctx.send(embed=embed)
        if arg2 == 'cyan':
            embed=discord.Embed(title="Cyan", description="#00FFFF", color=0x00FFFF)
            await ctx.send(embed=embed)
        if arg2 == 'skyblue':
            embed=discord.Embed(title="Sky Blue", description="#87CEEB", color=0x87CEEB)
            await ctx.send(embed=embed)
        #darkRGB
        if arg2 == 'dred':
            embed=discord.Embed(title="Dark Red", description="#8B0000", color=0x8b0000)
            await ctx.send(embed=embed)
        if arg2 == 'dgreen':
            embed=discord.Embed(title="Dark Green", descirption="#006400", color=0x006400)
            await ctx.send(embed=embed)
        if arg2 == 'navy':
            embed=discord.Embed(title="Navy", description="#000080", color=0x000080)
            await ctx.send(embed=embed)
        if arg2 == 'dblue':
            embed=discord.Embed(title="Navy", description="#000080", color=0x000080)
            await ctx.send(embed=embed)
        #key
        if arg2 == 'white':
            embed=discord.Embed(title="White", description="#FFFFFF", color=0xFFFFFF)
            await ctx.send(embed=embed)
        if arg2 == 'black':
            embed=discord.Embed(title="Black", description="#000000", color=0x000000)
            await ctx.send(embed=embed)
        if arg2 == 'gray':
            embed=discord.Embed(title="Gray", description="#808080", color=0x808080)
            await ctx.send(embed=embed)
        
        if arg2 == 'magenta':
            embed=discord.Embed(title="Magenta", description="#FF00FF", color=0xFF00FF)
            await ctx.send(embed=embed)
        if arg2 == 'yellow':
            embed=discord.Embed(title="Yellow", description="#FFFF00", color=0xFFFF00)
            await ctx.send(embed=embed)
        
        if arg2 == 'silver':
            embed=discord.Embed(title="Silver", description="#C0C0C0", color=0xc0c0c0)
            await ctx.send(embed=embed)
        if arg2 == 'gold':
            embed=discord.Embed(title="Gold", description="#FFD700", color=0xffd700)
            await ctx.send(embed=embed)
        if arg2 == 'purple':
            embed=discord.Embed(title="Purple", description="#800080", color=0x800080)
            await ctx.send(embed=embed)
        if arg2 == 'brown':
            embed=discord.Embed(title="Brown", description="#654321", color=0x654321)
            await ctx.send(embed=embed)
        if arg2 == 'violet':
            embed=discord.Embed(title="Violet", description="#EE82EE", color=0xee82ee)
            await ctx.send(embed=embed)
        
@client.command(pass_context = True) # 디스코드 채팅 단축키/메시지 변형 도움말
async def discordchat(ctx):
    embed=discord.Embed(title='디스코드 채팅 도움말', description='**단축키 보기 : Ctrl + /**', color=0xc80000)
    embed.add_field(name='\`message\`', value='`message`', inline=False)
    embed.add_field(name='\`\`message\`\`', value='``message``', inline=False)
    embed.add_field(name='\`\`\`message\`\`\`', value='```message```', inline=False)
    
    embed.add_field(name='\*message\*', value='*message*', inline=False)
    embed.add_field(name='\*\*message\*\*', value='**message**', inline=False)
    embed.add_field(name='\*\*\*message\*\*\*', value='***message***', inline=False)
    
    embed.add_field(name='\_message\_', value='_message_', inline=False)
    embed.add_field(name='\_\_message\_\_', value='__message__', inline=False)
    embed.add_field(name='\_\_\_message\_\_\_', value='___message___', inline=False)
    embed.add_field(name='\~\~message\~\~', value='~~message~~', inline=False) 
    
    embed.add_field(name='\> message', value='> message', inline=False)
    
    DM=discord.Embed(title='디스코드 채팅 도움말', description='{}, DM을 확인해주세요'.format(ctx.author.mention), color=0xc80000)
    await ctx.send(embed=DM)
    await ctx.author.send(embed=embed)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == '멍청이':
        await message.channel.send('너 멍청이')
    if message.content == '닥쳐':
        await message.channel.send('ㅠ')
    if message.content == '아인슈타인':
        await message.channel.send('<:einstein:818411995748368444>')
    if message.content == 'illuminati':
        await message.channel.send('https://cdn.discordapp.com/attachments/818298657124122704/819454078006067210/illuminati_small.png')
    if message.content == '와 샌즈!':
        await message.channel.send('https://cdn.discordapp.com/attachments/819260355829432382/819469134713978890/awT2wY_xEXyyFQut_v_iVQ_uBxYvXVZT5krt4CJIBOzg1hAX1127jfIocto9GtQTaZ_xi7WbAQG6i9sHkoK7-K-f9DejoljgIuJi.png')
    if message.content == '참깨빵위에 순쇠고기 패티두장 특별한소스 양상추 치즈피클 양파까아지':
        await message.channel.send('https://www.youtube.com/watch?v=1MEDVbDgVh0')
    if message.content == '헤이 디벨로퍼':
        await message.channel.send('<@&817171068836904991>')
    if message.content == '<@!818069103532572672>':
        await message.channel.send('뭐') 
    if message.content == '<@818069103532572672>':
        await message.channel.send('뭐')
    if message.content == '폭8':
        await message.channel.send('https://cdn.discordapp.com/attachments/783906926601306195/819914744088887356/Explosion.jpg')

@client.command(pass_context = True)
async def ggeretsae(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.author.send('yad ecin a evah .easteregg a dnuof uoy .olleh')

client.run('ODE4MDY5MTAzNTMyNTcyNjcy.YESsOQ.nA2gH3em5Dd2CwfLeKEgJke3RYs')