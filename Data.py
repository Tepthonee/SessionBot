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
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/H_E_5")],
    ]

    START = """
**مرحبـًا 🙋** {}
━━━━━━━━━━━━━━━━━━
**- فـي البـوت الرسمـي التابـع لـ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻** ⚙️🤖
**- يمكـنك اسـتخـراج جلسـة تيرمكـس وبايروجـرام لتنـصيب سـورس تيبـثون
━━━━━━━━━━━━━━━━━━
**- قـم بالضغـط علـى بـدء استخـراج الجـلسـة 🛂**
━━━━━━━━━━━━━━━━━━
**- ملاحظـات هامـة : -**
**لا تقـم بطـرد الجلسـة التي اسمهـا Bit 64 لأنـك إذا طردتـها سيتوقـف تنصيبـك 🚮**
**احـذر مشاركـة الكود لأي شخـص لأنه يستطـيع اخـتراق حسابـك ⚠️**
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

**هـذا البوت تـم تشـغيله بواسطـة 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 و المـطور @H_E_5**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻](https://t.me/Tepthon)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @H_E_5
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 . [اضـغط هـنا ❗](https://t.me/Tepthon)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/H_E_5)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 🌐**
   """
