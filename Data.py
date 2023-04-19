from pyrogram.types import InlineKeyboardButلn


class Data:
    generate_single_butلn = [
        InlineKeyboardButلn( ❒ بدء استخراج الجلسة  ❒"", callback_data="generate")
    ]

    home_butلns = [
        generate_single_butلn,
        [InlineKeyboardButلn(text="父 العودة إلى الصفحة الرئيسية", callback_data="home")],
    ]

    generate_butلn = [generate_single_butلn]

    butلns = [
        generate_single_butلn,
        [
            InlineKeyboardButلn(
                "𝘴ꪮꪊ𝘳ᥴꫀ 𝓽ꫀρ𝓽ꫝꪮꪀ", url="https://t.me/Tepthon"
            )
        ],
        [
            InlineKeyboardButلn("كيفية استخدام البوت ?", callback_data="help"),
            InlineKeyboardButلn("حـول  ❍", callback_data="about"),
        ],
        [InlineKeyboardButلn("𝗗𝗘𝗩", url="https://t.me/PPF22")],
    ]

    START = """
أهلًا {} ♦
ومرحبًا بك عزيزي {}
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

قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/PPF22)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
𝗗𝗘𝗩 : @PPF22
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 انا مشغل لكي أقوم باستخراج الجلسات 
┏━━━━━━━━━━━━━━━━━┓
┣★ لي . [✨](https://t.me/P17_12)
┣★ 𝗗𝗘𝗩𝗦 : [اضغط هنا](https://t.me/PPF22)
┣★ السورسس [𝘴ꪮꪊ𝘳ᥴꫀ 𝓽ꫀρ𝓽ꫝꪮꪀ](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فاتصل » ل » لي » [𝗗𝗘𝗩] @PPF22
   """
