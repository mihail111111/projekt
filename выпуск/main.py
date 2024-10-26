import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.command('info')
async def info(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о возможностях бота',
        description='В данном боте есть команды, такие как: /start(информация про бота) ; /GW(информация про глобальное потепление) ; /glass /plastic /cardboard(информация о вреде мусора) ; /glass_sorting /plastic_sorting /cardboard_sorting(информация про сортировку мусора)',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)

@bot.command('start')
async def start(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о боте',
        description='Я бот который расскажет тебе про глобальное потепление, вреде мусора со стороны глобального потепления и про его сортировку.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)

@bot.command('GW')
async def GW(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о глобальном потеплении ',
        description='Глобальное потепление — это явление, связанное с постепенным повышением средней температуры на Земле. Оно вызвано увеличением выбросов парниковых газов, таких как углекислый газ, метан и диоксид азота, в атмосферу. Эти газы создают эффект парникового газа, который удерживает тепло и препятствует его уходу в космос.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\global_warning.jpg'))

@bot.command('glass')
async def glass(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о вреде стекла ',
        description='Вред стекла со стороны глобального потепления заключается в том, что для его производства требуется больше ресурсов и энергии, а в процессе изготовления выделяется много углекислого газа',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\glass.png'))

@bot.command('glass_sorting')
async def glass_sorting(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о сортировке стекла',
        description='Сортировка стекла помогает минимизировать ущерб для окружающей среды. При производстве тары из переработанного стекла удаётся сберечь невозобновляемые природные ресурсы и уменьшить потребление энергии на 20% по сравнению с производством новой тары. При этом стекло важно сортировать по цветам, поскольку разные цвета имеют в своей основе различные химические элементы и не могут быть качественно переработаны вместе.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\glass_srt.png'))

@bot.command('plastic')
async def plastic(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о вреде пластика ',
        description='Вред пластика со стороны глобального потепления заключается в том, что при разложении пластик выделяет примеси парниковых газов, в том числе метан, который быстрее и интенсивнее влияет на климат: с ним связывают до 30% повышения температуры на планете. Чем дольше пластик лежит, тем больше образуется вредных испарений.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\plastic.jpg'))

@bot.command('plastic_sorting')
async def plastic_sorting(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о сортировке пластика',
        description='Сортировка пластика может помочь снизить вред для окружающей среды. Например, можно использовать тканевые сумки вместо целлофановых пакетов в магазине, выбирать перерабатываемые варианты упаковки. Механический способ переработки пластика заключается в сортировке и очистке отходов, после чего их измельчают и гранулируют. Готовые гранулы используются как сырьё для производства новых пластиковых изделий.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\scale_1200 (1).png'))

@bot.command('cardboard')
async def cardboard(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о вреде картона',
        description='Картон может оказывать разное влияние на глобальное потепление. Если при производстве картона не используются нефтепродукты, то материал практически не выделяет вредные вещества и не влияет на парниковый эффект. Однако если станки и прессы работают на нефтепродуктах, это может нанести вред окружающей среде.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\cardboard.jpg'))

@bot.command('cardboard_sorting')
async def cardboard_sorting(ctx: commands.Context):
    embed = discord.Embed(
        title='Информация о сортировке картона',
        description='Сортировка картона важна для его переработки. Картонную макулатуру собирают, сортируют, очищают от плёнки, после чего пропускают через специальные установки. Они отделяют примеси и измельчают картон так, что на выходе получается целлюлозное волокно. Его можно использовать для последующего производства бумаги или картона.',
        color=discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    await ctx.send(file=discord.File('images\crdbstr.png'))

bot.run('')