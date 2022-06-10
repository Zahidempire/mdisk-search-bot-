# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is a TeleGram BotList Search Bot of @CyniteBots And Some Other Bots Available On TeleGram.

🤖 My Name: <a href='https://t.me/mdisk1_search_bot'> Mᴅɪsᴋ Sᴇᴀʀᴄʜ Rᴏʙᴏᴛ </a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

📡 Server: <a href='https://heroku.com'> Heroku </a>

👨‍💻 Modified By: <a href='https://t.me/Imdb_updates'>Imdb-updates</a>

🌀 Youtube: <a href='https://youtube.com/c/TechnicalAks01'>Technical Aks</a>

👥 Bots Support: <a href='https://t.me/Imdb_updates'>IMDBBOTS</a>

📢 Bots Updates: <a href='https://t.me/Imdb_updates'>IMDB-BOTS</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>👨‍💻 Developers : <a href='https://t.me/Aks_support01_bot'>Aks</a>

Bots are simply Telegram accounts operated by software – not people – and they'll often have AI features. They can do anything – teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

🌀 I will help you to find Best Telegram Bots.

🌀 If you Get Any Error In Searching Please Report at **@Aks_support01_bot**.

🌀 Our Project Channel: <a href='https://t.me/Imdb_updates'>Imdb-updates</a>.

🌀 All Bots Based On Users and Developer Demands. 

🤖 Join For All Available Bots On Telegram: @Imdb_updates.
"""
    
    HOME_TEXT = """
<b>👋 Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/mdisk1_search_bot'>mdisk</a>.

<a> Modified By : @Imdb_updates</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With ❤ By @Aks_support01_bot </a>
"""


    START_MSG = """
<b>👋 Hey {}, 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂  <a href='https://t.me/mdisk1_search_bot'>mdisksearchbot</a>.
<a> 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.. 𝚃𝙷𝙴𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂 ♥️♥️🔥 </a>
"""
    ADD_BOTS = """<b>Heya! {} Want Same Like This Then Contact The Support.</b>"""
