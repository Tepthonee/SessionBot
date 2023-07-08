from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدء استـخراج الجلسـة 🖥️", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝗧𝗲𝗽𝘁𝗵𝗼𝗻 - سـورس تيبـثون 🌐", url="https://t.me/Tepthon"
            )
        ],
        [
            InlineKeyboardButton("كيفيـة الاستـخدام   ⍰ ", callback_data="help"),
            InlineKeyboardButton("حـول البـوت ℹ️", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/PPF22")],
    ]

    START = """
**مـرحبـًا عـزيزي 🔦** {}
━━━━━━━━━━━━━━━━━━
** في بـوت استـخراج كود تيـرمكس وبايـروجـرام التابـع لـ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 🚮**
━━━━━━━━━━━━━━━━━━
**قـم بالضغـط علـى بـدء استخـراج الجـلسـة ℹ️**
━━━━━━━━━━━━━━━━━━
**- مـلاحـظات هامـة 🚨 : -**
**لا تقـم بطـرد الجلسـة التي اسمهـا Bit 64 لأنـك إذا طردتـها سيتوقـغ تنصيبـك**
**احـذر مشاركـة الكود لأي شخـص لأنه يستطـيع اخـتراق حسابـك**
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

هـذا البوت تـم تشـغيله بواسطـة 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 و المـطور @PPF22

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻](https://t.me/Tepthon)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @PPF22
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 
لا تنسـى الصـلاة على النبي 🤍 .
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 . [اضـغط هـنا ❗](https://t.me/Tepthon)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/PPF22)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛ 
تابـع لـ - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 🌐
   """
