import random
import discord
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from discord.ext import commands

TOKEN = 'OTM1NjE0NjE0OTY2Nzc1OTM5.YfBNAw.zPAnsUL6Xs4HwF2BoVIc6hxYl1I'

bot = commands.Bot(command_prefix='-')

@bot.command(pass_context=True)
async def info(ctx):
    information = f'Список команд:1) -info - выводит список команд. 2) -answer - отвечу на вопрос "Справедливо" или "Несправедливо". 3) -weather - покажу погоду "Обязательно укажите свой город через пробел! '
    await ctx.send(information)

@bot.command(pass_context=True)
async def answer(ctx):
    if random.randint(1,2) == 1:
        answer = 'Справедливо'
    else:
        answer = 'Несправедливо'

    await ctx.send(answer)

@bot.command(pass_context=True)
async def weather(ctx, arg):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('ea1a216efdfbdceae7e9aba20b117bd1', config_dict)

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(arg)
    weather = observation.weather

    a = arg
    b = weather.temperature('celsius')['temp']
    c = weather.detailed_status

    result = f'Короче говоря, в городе {a} {c}, темперетура {b}'

    await ctx.send(result)


bot.run('OTM1NjE0NjE0OTY2Nzc1OTM5.YfBNAw.zPAnsUL6Xs4HwF2BoVIc6hxYl1I') 