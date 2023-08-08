from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
text=f"""**⎆ مـرحبـًا** {msg.from_user.mention},
**⎆ اضغـط عـلى بـدء استخـراج الجلسـة لبـدء الاستـخراج**
**⎆ أنـا بوت استـخراج كـود تيرمكـس وبايروجـرام لـ تنصيـب @Tepthon**
**⎆ هـذا الكـود خـطير جدًا لا تشاركـه لأحد .**
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="- بـدء استخـراج الجلسـة .", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("- قنـاة السـورس .", url="https://t.me/Tepthon"),
                    InlineKeyboardButton("- المطـور .", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
    