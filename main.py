from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

token = '6004836361:AAEqifGg36EChbUgUGKSatjlC1sFNO0E8Z4'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    username = message.from_user.username
    await bot.send_message(chat_id, f'Xush kelibsiz {fullname}, @{username}\n'
                                    f'Masala kiriting probel bilan: misol: 2 + 2 ')

@dp.message_handler(lambda message: 'salom' in message.text)
async def salom(message: Message):
    chat_id = message.chat.id
    # await bot.send_message(chat_id, 'Vaalaykum assalom')
    await message.reply('Vaalaykum assalom')
@dp.message_handler()
async def echo(message: Message):
    text = message.text.split()
    if len(text) == 3:
        son1, amal, son2 = text
        son1 = int(son1)
        son2 = int(son2)
        if amal == '+':
            await message.reply(f'{son1 + son2}')
            print(f'{son1 + son2}')
        elif amal == '-':
            await message.reply(f'{son1 - son2}')
        elif amal == '*':
            await message.reply(f'{son1 * son2}')
        elif amal == '/':
            await message.reply(f'{son1 / son2}')





executor.start_polling(dp, skip_updates=True)
