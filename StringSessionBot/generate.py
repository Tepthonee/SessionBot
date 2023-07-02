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
        "مـرحبـًا بـك عـزيـزي مـرة أخـرى قـم بـاختـيـار الجـلـسـة المـىاد اسـتـخراجـها",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("بـايـروجـرام", callback_data="pyrogram"),
                    InlineKeyboardButton("تـلـيـثون", callback_data="telethon"),
                ]
            ]
        ),
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply(
        "تـم بدء  {} استـخـراج الجـلسة...".format(
            "Telethon" if telethon else "Pyrogram"
        )
    )
    user_id = msg.chat.id
    api_id_msg = await bot.ask(
        user_id, "أرسـل الآن الخاص بـك `API_ID`", filters=filters.text
    )
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply(
            "غيـر صالـحAPI_ID(أعــد المـحاولـة).  الخاص بـك غيـر صالـح حـاول مـرة أخـرى.",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    api_hash_msg = await bot.ask(
        user_id, "أرسـل الآن الخاص بـك `API_HASH`", filters=filters.text
    )
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(
        user_id,
        "الآن أرسـل رقم الهاتف الخاص بـك`ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ` قم بـكتابة رقم مع رمز بلدك. \nمـثـال : `+96279654210`",
        filters=filters.text,
    )
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("جـاري إرسـال الكـود إلــى حـسابـك انتـظر قـليـلًا......")
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
            "`API_ID` و `API_HASH` الايبيات الخاصة بـك غيـر صـحـيحة يرجـى إعـادة الاستـخـراج مـرة أخـرى.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply(
            "`PHONE_NUMBER` رقم الهاتف الخاص بـك غيـر صـحـيح يرجـى إعـادة الاستـخـراج مـرة أخـرى ",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    try:
        phone_code_msg = await bot.ask(user_id, "[ارسل الكـود مثل اللي في الصورة ](https://telegra.ph/file/da1af082c6b754959ab47.jpg)»  🔍من فضلك افحص حسابـك بالتليجرام وتفقد الكـود من حساب إشعارات التليجرام. إذا كان\n  هـناك تحقق بـخـطوتيـن( المرور ) ، أرسـل كلمة المرور هـنا بعد إرسال كـود الدخول بالتنسيق أدناه.- إذا كانت كلمة المرور أو الكـود  هي\n 12345 يرجـى إرسالها بالشكل التالي 1 2 3 4 5 مع وجود مسـافـات بين الارقام إذا احتجت مساعدة @V_E_1.", filters=filters.text, timeout=600)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply(
            "لقد تـجاوزت الحد الزمني 10 دقائق أعــد استـخـراج الجـلسة مـرة أخـرى.",
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
            " رقم الهاتف الخاص بـك غيـر صـحـيح يرجـى إعـادة الاستـخـراج مـرة أخـرى ",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply(
            "الكـود الـذي أدخلته خاطئ يرجـى إعـادة الإستخراج مـرة أخـرى",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(
                user_id,
                "التـحـقق بـخـطوتيـن مـفـعل بـحـسابـك لـذا قم بإدخـاله هـنا لـطـفًا.",
                filters=filters.text,
                timeout=300,
            )
        except TimeoutError:
            await msg.reply(
                "لقد تـجاوزت المدة الزمنية يـجـب عـليك إعـادة استـخـراج الجـلسة مـرة أخـرى",
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
                "التـحـقق بـخـطوتيـن الـذي أدخـلـته خطــأ يرجـى إعـادة الاستـخـراج مـرة أخـرى 🤍.",
                quote=True,
                reply_markup=InlineKeyboardMarkup(Data.generate_button),
            )
            return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = "**{} كـود الجـلسة** \n\n`{}` \n\مـسـتخرج من @Tepthon".format(
"تليثون" if telethon else "بايروجرام", string_session
    )
    try:
        await client.send_message("me", text)
    except KeyError:
        pass
    await client.disconnect()
    await phone_code_msg.reply(
        "تـم استـخـراج {} الجـلسة. \n\nيرجـى تـفـحص الرسائـل المحفوظـة! \n\nمن @Tepthon".format(
            "telethon" if telethon else "pyrogram"
        )
    )


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply(
            "تـم إلـغاء استـخـراج الجـلسة!",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif "/restart" in msg.text:
        await msg.reply(
            "تـم ترسيت البوت!",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("تـم إلغاؤه!", quote=True)
        return True
    else:
        return False 
