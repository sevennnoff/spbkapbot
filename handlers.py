from aiogram import Dispatcher, Bot, F, Router
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery
from aiogram.filters import Command
import requests
import inline
import parser
router =  Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловат а учебного бота, созданного для <i>Ещё не придумали для чего</i>", reply_markup=inline.menu())

@router.message()
async def text(message: Message, bot: Bot):
    if message.text=="/9kl":
        await message.answer(str(parser.nkl))
    elif message.text=="/11kl":
        await message.answer(str(parser.ekl))

@router.callback_query(F.data)
async def keyboard_handler(call: CallbackQuery):
    if call.data == "info":
        await call.message.edit_text("Сколько классов вы окончили?", reply_markup=inline.klass())
    elif call.data == "9kl":
        await call.message.answer(str(parser.nkl))
    elif call.data == "11kl":
        await call.message.answer(str(parser.ekl))
    await call.answer()

