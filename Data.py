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
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/A_D_P")],
    ]

    START = """
*مرحـبًا 🙋* {}
━━━━━━━━━━━━━━━━━
*أنا بوت استخراج الجلسـات التابـع لـ 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 ⎙*
━━━━━━━━━━━━━━━━━
*اضغط على بـدء استخـراج الجلسـة لبدء الاستخراج*
━━━━━━━━━━━━━━━━━
*كلمة تيرمـكس إذا كنت تريد استخـراج كود تيرمـكس أما إذا كنت تريـد كود بايروجـرام فاختر بايروجـرام*
*لا تشـارك كود تيرمـكس لأحـد ⚠️*
*المطـور مـحمد : @A_D_P*
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/repo - لعرض معلومـات عـن السـورس 💡
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

**هـذا البوت تـم تشـغيله بواسطـة 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 و المـطور @A_D_P**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻](https://t.me/Tepthon)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @A_D_P
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس تيبـثون - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 . [اضـغط هـنا ❗](https://t.me/Tepthon)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/A_D_P)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 🌐**
   """
