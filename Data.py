from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدأ اسـتـخـراج الـجــلـسـة", callback_data="generate")
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
                "سـورس تـيـبثون الـعـربي", url="https://t.me/Tepthon"
            )
        ],
        [
            InlineKeyboardButton("كيفية استخدام البوت ?", callback_data="help"),
            InlineKeyboardButton("حـول  ❍", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور", url="https://t.me/e_2_d")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
هذا البوت مخصص لاستخراج الجلسات
مثل: - البايروجرام ، التيرمكس
من خلال إرسال الأيبي ايدي والأيبي هاش ورقم هاتفك والكود والتحقق بخطوتين إذا كنت مفعله
𝗗𝗘𝗩 :- @PPF22
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت اليوت
"""

    # About Message
    ABOUT = """
**حول البوت** 

هذا هو بوت استخراج كود تيرمكس وبايروجرام مقدم من @PPF22

قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Tepthon)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
𝗗𝗘𝗩 : @e_2_d
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 أنا مشغل لكي أقوم باستخراج الجلسات 
┏━━━━━━━━━━━━━━━━━┓
┣★ My . [✨](https://t.me/P17_12)
┣★ 𝗗𝗘𝗩 : [اضغط هنا](https://t.me/e_2_d)
┣★ السورس [𝘴ꪮꪊ𝘳ᥴꫀ 𝓽ꫀρ𝓽ꫝꪮꪀ](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فراسل » المطور » [𝗗𝗘𝗩] @e_2_d
   """
