from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدأ استـخـراج الجـلسة", callback_data="generate")
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
                "سـوࢪس تـيـبثون الـعـࢪبي", url="https://t.me/Tepthon"
            )
        ],
        [
            InlineKeyboardButton("- كيـفـية اެݪاستـخـدام", callback_data="help"),
            InlineKeyboardButton("- حـول", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور", url="https://t.me/V_E_1")],
    ]

    START = """
مـࢪحبـًا عـزيـزي  {}
أنـا مـخـصـص لاسـتخـࢪاج اެݪجـلـسات
بـايـࢪوجࢪام أو تـيـࢪمـكس
للبـدء في الاسـتـخࢪاج اضغط بدأ استـخࢪاج اެݪجـلـسة
المطوࢪ  : @V_E_1
    """

    HELP = """
 **الأوامࢪ المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ࢪيبو البوت
/generate - لاستخࢪاج الجلسات 
/cancel - لإلغاء الاستخࢪاج 
/restart - لتࢪسيت اليوت
"""

    # About Message
    ABOUT = """
**حول البوت** 

مـࢪحبـًا عـزيـزي أنا هـنا لاسـتـخࢪاج الجـلـسات بـࢪمـجـة المطـوࢪ @V_E_1

قناة السوࢪس : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻](https://t.me/Tepthon)
لغة البـرمـجـة : [بـايروجرام](docs.pyrogram.org)
اللغة : [بايثون](www.python.org)
المـطـور : @V_E_1
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
صـل على النبي 🤍  
┏━━━━━━━━━━━━━━━━━┓
┣★ معلومات عن مطـوري . [✨](https://t.me/P17_12)
┣★ الـمطور : [اضغط هنا](https://t.me/V_E_1)
┣★ السـورس [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فࢪاسل » المطوࢪ » [المـطور] @V_E_1
   """
