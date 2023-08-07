from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("- بـدء استـخراج الجلسـة .", callback_data="generate")
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "قنـاة السـورس", url="https://t.me/Tepthon"
    ]

    START = """
**⎆ مـرحبـًا** {}
**⎆ اضغـط عـلى بـدء استخـراج الجلسـة لبـدء الاستـخراج**
**⎆ أنـا بوت استـخراج كـود تيرمكـس وبايروجـرام لـ تنصيـب @Tepthon**
**⎆ هـذا الكـود خـطير جدًا لا تشاركـه لأحد .**
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
