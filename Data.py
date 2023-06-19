from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدأ استـخـࢪاج اެݪجـلسة", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ࢪجـوع 🔙", callback_data="home")],
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
        [InlineKeyboardButton("المطـوࢪ", url="https://t.me/e_2_d")],
    ]

    START = """
مـࢪحبـًا عـزيـزي  {}
أنـا مـخـصـص لاسـتخـࢪاج اެݪجـلـسات
بـايـࢪوجࢪام أو تـيـࢪمـكس
للبـدء في الاسـتـخࢪاج اضغط بدأ استـخࢪاج اެݪجـلـسة
المطوࢪ  : @E_2_D
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

مـࢪحبـًا عـزيـزي أنا هـنا لاسـتـخࢪاج الجـلـسات بـࢪمـجـة المطـوࢪ @E_2_D

قناة السوࢪس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Tepthon)
لغة البࢪمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
𝗗𝗘𝗩 : @e_2_d
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
صـل على النبي 🤍  
┏━━━━━━━━━━━━━━━━━┓
┣★ My . [✨](https://t.me/P17_12)
┣★ 𝗗𝗘𝗩 : [اضغط هنا](https://t.me/E_2_D)
┣★ السوࢪس [𝘴ꪮꪊ𝘳ᥴꫀ 𝓽ꫀρ𝓽ꫝꪮꪀ](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فࢪاسل » المطوࢪ » [𝗗𝗘𝗩] @e_2_d
   """
