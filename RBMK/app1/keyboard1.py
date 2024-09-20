from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
button=[
    [KeyboardButton(text="/help"),KeyboardButton(text="Курсы валют"),KeyboardButton(text="калькуляторы валют"),]
]
keyboard=ReplyKeyboardMarkup(keyboard=button,resize_keyboard=True)
inline1 = [
    [InlineKeyboardButton(text="USD", callback_data='1')],
    [InlineKeyboardButton(text="EURO", callback_data='2')],
    [InlineKeyboardButton(text="RUBL", callback_data='3')],
    [InlineKeyboardButton(text="YAN", callback_data='4')]
]
inline2 = InlineKeyboardMarkup(inline_keyboard=inline1)