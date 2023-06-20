from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError,
)


@Client.on_message(filters.private & ~filters.forwarded & filters.command("generate"))
async def main(_, msg):
    await msg.reply(
        "مـࢪحبـًا بـك عـزيـزي مـࢪة أخـࢪى قـم بـاختـيـاࢪ اެݪجـلـسـة اެݪمـىاد اسـتـخࢪاجـها",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("بـايـࢪوجـࢪام", callback_data="pyrogram"),
                    InlineKeyboardButton("تـلـيـثون", callback_data="telethon"),
                ]
            ]
        ),
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply(
        "تـم بدء  {} استـخـࢪاج اެݪجـلسة...".format(
            "Telethon" if telethon else "Pyrogram"
        )
    )
    user_id = msg.chat.id
    api_id_msg = await bot.ask(
        user_id, "أࢪسـل اެݪآن اެݪخاص بـك `API_ID`", filters=filters.text
    )
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply(
            "غيـࢪ صالـحAPI_ID(أعــد اެݪمـحاولـة).  اެݪخاص بـك غيـࢪ صالـح حـاول مـࢪة أخـࢪى.",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    api_hash_msg = await bot.ask(
        user_id, "أࢪسـل اެݪآن اެݪخاص بـك `API_HASH`", filters=filters.text
    )
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(
        user_id,
        "اެݪآن أࢪسـل ࢪقم اެݪهاتف اެݪخاص بـك`ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ` قم بـكتابة ࢪقم مع ࢪمز بلدك. \nمـثـال : `+96279654210`",
        filters=filters.text,
    )
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("جـاࢪي إࢪسـال الكـود إلــى حـسابـك انتـظࢪ قـليـلًا......")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply(
            "`API_ID` و `API_HASH` اެݪايبيات اެݪخاصة بـك غيـࢪ صـحـيحة يـࢪجـى إعـادة اެݪاستـخـࢪاج مـࢪة أخـࢪى.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply(
            "`PHONE_NUMBER` ࢪقم اެݪهاتف اެݪخاص بـك غيـࢪ صـحـيح يـࢪجـى إعـادة اެݪاستـخـࢪاج مـࢪة أخـࢪى ",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    try:
        phone_code_msg = await bot.ask(user_id, "[اࢪسل اެݪكـود مثل اެݪلي في اެݪصوࢪة ](https://telegra.ph/file/da1af082c6b754959ab47.jpg)»  🔍من فضلك افحص حسابـك باެݪتليجࢪام وتفقد اެݪكـود من حساب إشعاࢪات اެݪتليجࢪام. إذا كان\n  هـناك تحقق بـخـطوتيـن( اެݪمࢪوࢪ ) ، أࢪسـل كلمة اެݪمࢪوࢪ هـنا بعد إࢪساެݪ كـود اެݪدخول باެݪتنسيق أدناه.- إذا كانت كلمة اެݪمࢪوࢪ أو اެݪكـود  هي\n 12345 يـࢪجـى إࢪساެݪها باެݪشكل اެݪتاެݪي 1 2 3 4 5 مع وجود مسـافـات بين اެݪاࢪقام إذا احتجت مساعدة @S_4_N.", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply(
            "لقد تـجاوزت اެݪحد اެݪزمني 10 دقائق أعــد استـخـࢪاج اެݪجـلسة مـࢪة أخـࢪى.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply(
            " ࢪقم اެݪهاتف اެݪخاص بـك غيـࢪ صـحـيح يـࢪجـى إعـادة اެݪاستـخـࢪاج مـࢪة أخـࢪى ",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply(
            "اެݪكـود اެݪـذي أدخلته خاطئ يـࢪجـى إعـادة اެݪإستخࢪاج مـࢪة أخـࢪى",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(
                user_id,
                "اެݪتـحـقق بـخـطوتيـن مـفـعل بـحـسابـك لـذا قم بإدخـاله هـنا لـطـفًا.",
                filters=filters.text,
                timeout=300,
            )
        except TimeoutError:
            await msg.reply(
                "لقد تـجاوزت اެݪمدة اެݪزمنية يـجـب عـليك إعـادة استـخـࢪاج اެݪجـلسة مـࢪة أخـࢪى",
                reply_markup=InlineKeyboardMarkup(Data.generate_button),
            )
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply(
                "اެݪتـحـقق بـخـطوتيـن اެݪـذي أدخـلـته خطــأ يـࢪجـى إعـادة اެݪاستـخـࢪاج مـࢪة أخـࢪى 🤍.",
                quote=True,
                reply_markup=InlineKeyboardMarkup(Data.generate_button),
            )
            return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = "**{} كـود اެݪجـلسة** \n\n`{}` \n\مـسـتخࢪج من @Tepthon".format(
"تليثون" if telethon else "بايࢪوجࢪام", string_session
    )
    try:
        await client.send_message("me", text)
    except KeyError:
        pass
    await client.disconnect()
    await phone_code_msg.reply(
        "تـم استـخـࢪاج {} اެݪجـلسة. \n\nيـࢪجـى تـفـحص اެݪࢪسائـل اެݪمحفوظـة! \n\nمن @Tepthon".format(
            "telethon" if telethon else "pyrogram"
        )
    )


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply(
            "تـم إلـغاء استـخـࢪاج اެݪجـلسة!",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif "/restart" in msg.text:
        await msg.reply(
            "تـم تࢪسيت اެݪبوت!",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("تـم إلغاؤه!", quote=True)
        return True
    else:
        return False 
