from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram import Router
from aiogram.types import Message
from app1.keyboard1 import *
from aiogram.fsm import FSMContext, State, StatesGroup
from bs4 import BeautifulSoup
import aiohttp

router = Router()


class FSM(StatesGroup):
    OZIDANIE = State()
    TUDASUDA = State()
    OTVET = State()
@router.message(Command('help'))
async def start_bot(message: Message):
    await message.reply("Привет нужные тебе команды   /news , /convert", reply_markup=keyboard)
@router.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("Привет", reply_markup=keyboard)

@router.message(Command('news'))
async def start_parsing_news(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://24.kg/') as response:
                soup = BeautifulSoup(await response.text(), 'lxml')
                news_items = soup.find_all('div', class_="col-xs-12")
                if news_items:
                    for item in news_items:
                        text = item.text.strip()
                        if text:  
                            await message.reply(text)

@router.message(F.text == 'Курсы валют')
async def start_parsing(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.nbkr.kg/index.jsp?lang=RUS') as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            courses = soup.find_all('div', class_='exchange-rates-body')
            for course in courses:
                await message.reply(f'{course.text}')

@router.message(Command('convert'))
async def start_conversion(message: Message, state: FSMContext):
    await message.reply("Введите валюту, которую хотите конвертировать в сомы (например, USD,EURO,RUBL):")
    await state.set_state(FSM.OZIDANIE)
    if message.text=="USD":
        await message.reply('введите количество')
        nerd=message.text*84,3622
        await message.reply(f" ваша сумма{nerd}")
    if message.text=="EURO":
        await message.reply('введите количество')
        nerd1=message.text*93,8909
        await message.reply(f" ваша сумма{nerd1}")
    if message.text=="RUBL":
        await message.reply('введите количество')
        nerd3=message.text*0,9223
        await message.reply(f" ваша сумма{nerd3}")
    if message.text=="YAN":
        await message.reply('введите количество')
        nerd4=message.text*11,9019
        await message.reply(f" ваша сумма{nerd4}")
    else :
        await message.reply("такого выбора нет ")


