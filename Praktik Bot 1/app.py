import asyncio
from aiogram import Bot, Dispatcher
import os
from handlers.user_private import user_private_router
from common.bot_cmd_list import listOfCommands
from aiogram.types import BotCommandScopeAllPrivateChats
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_routers(user_private_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=listOfCommands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)
    
try: 
    asyncio.run(main())
except KeyboardInterrupt:
    print('End of work')