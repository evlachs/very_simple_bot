from aiogram import types

from loader import dp
from conf import GROUP_ID, CHANNEL_ID
from messages import MESSAGES


@dp.message_handler(content_types=['new_chat_members'])
async def new_member_notify(message: types.Message):
    if message.chat.id == GROUP_ID:
        await dp.bot.send_message(CHANNEL_ID, MESSAGES['new_member'].format(message.from_user.username, message.from_user.full_name))
