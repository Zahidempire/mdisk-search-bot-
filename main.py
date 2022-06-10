# (c) @PredatorHackerzZ
# I just made this for searching a channel message from inline.
# Maybe you can use this for something else.
# I first made this for @TGBotListBot ...
# Edit according to your use.

from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from TeamTeleRoid.forcesub import ForceSub

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):

    await event.reply_text(Config.START_MSG.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="http://t.me/Mdisk_searchrobot?startgroup=true")],
             [InlineKeyboardButton("Support Group", url="https://t.me/TeleRoid14"),
            InlineKeyboardButton("♻ Help", callback_data="Help_msg")],
             [InlineKeyboardButton("👥 About", callback_data="About_msg"), 
            InlineKeyboardButton("Search Inline", switch_inline_query_current_chat=""), InlineKeyboardButton("Go Inline", switch_inline_query="")]
        ])
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(_, event: Message):

    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🚸 Pᴏᴡᴇʀᴇᴅ Bʏ", url="https://t.me/MoviesFlixers_DL"),
             InlineKeyboardButton("🌱 Inspired Channel ", url="https://t.me/TGRobot_List"), 
             InlineKeyboardButton("👥 About", callback_data="About_msg")],
            [InlineKeyboardButton("Search Inline", switch_inline_query_current_chat=""), InlineKeyboardButton("Go Inline", switch_inline_query="")]
        ])
    )

@Bot.on_inline_query()
async def inline_handlers(_, event: InlineQuery):
    answers = list()
    # If Search Query is Empty
    if event.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="This is Inline BotList Search Bot 🔍",
                description="You Can Search All Bots Available On TeleGram.",
                thumb_url="https://telegra.ph/file/cb4099b549491a622c481.jpg", 
                input_message_content=InputTextMessageContent(
                    message_text="A dream does not become reality through magic; it takes sweat, determination, and hard work."

                                  "<a>@TheTeleRoid || @Space_X_Bots</a>"

                                  "<a>🔴 YouTube Channel :</a>"

                                  "<a>https://youtube.com/channel/UCeAteLGyraSil9pErMFTZAg </a>"

                                  "<a>👥 BotChat : @TeleRoid14 </a>"


                                  "<a> Follow Our Bot Updates Channel : @TeleRoidGroup</a>",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Search Here", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("TeleRoid Bots", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                     InlineKeyboardButton("Bots Channel", url="https://t.me/TeleRoidGroup")],
                    [InlineKeyboardButton("TeleGram Bots", url="https://t.me/TGRobot_List")]
                ])
            )
        )
    # Search Channel Message using Search Query Words
    else:
        async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.query):
            if message.text:
                thumb = None
                f_text = message.text
                msg_text = message.text.html
                if "|||" in message.text:
                    thumb = message.text.split("|||",1)[1].strip()
                    f_text = message.text.split("|||",1)[0]
                    msg_text = message.text.html.split("|||",1)[0]
                answers.append(InlineQueryResultArticle(
                    title="{}".format(f_text.split("\n", 1)[0]),
                    description="{}".format(f_text.split("\n", 2)[-1]),
                    thumb_url=thumb,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Search Again", switch_inline_query_current_chat=""), InlineKeyboardButton("Go Inline", switch_inline_query="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=msg_text,
                        parse_mode="html",
                        disable_web_page_preview=True
                    )
                ))
    try:
        await event.answer(
            results=answers,
            cache_time=0
        )
        print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
    except QueryIdInvalid:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("💢 Github", callback_data="https://github.com/PredatorHackerzZ/MessageSearchBot"),
						InlineKeyboardButton("🚸 Powered By", url="https://t.me/MoviesFlixers_DL")
					],
					[
						InlineKeyboardButton("👨‍💻 Developer ", url="https://t.me/TheTeleRoid"),
						InlineKeyboardButton("🏠 Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👥 About", callback_data="About_msg"),
						InlineKeyboardButton("💢 Github Repo", url="https://t.me/Moviesflixers_DL")
					], 
                                        [
						InlineKeyboardButton("Bot List", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
						InlineKeyboardButton("🏠 Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("🛑 Support 🛑", url="https://t.me/TeleRoid14"),
						InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup")
					],
                                        [
						InlineKeyboardButton("👥 Help", callback_data="Help_msg"),
						InlineKeyboardButton("♻ About", callback_data="About_msg")
					],
                                        [
						InlineKeyboardButton("+ Add Your Bots Here + ", callback_data="addbots")
					],
					[
						InlineKeyboardButton("Search Inline ⤵", switch_inline_query_current_chat=""),
						InlineKeyboardButton("Go Inline", switch_inline_query="")
					]
				]
			),
			parse_mode="html"
		)
        elif "addbots" in cb_data:
            await cmd.message.edit(
			text=Config.ADD_BOTS,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👥 TeleRoid Support👥", url="https://t.me/TeleRoid14"),
						InlineKeyboardButton("👥 Space X Bots 👥", url="https://t.me/Sources_Codes")
					],
					[
						InlineKeyboardButton("👥 CodeXBotz 👥", url="https://t.me/CodeXBotZSupport"),
						InlineKeyboardButton("👥 Universal Bots 👥", url="https://t.me/JV_Community")
					], 
                                        [
						InlineKeyboardButton("👥 Heiman Support 👥", url="https://t.me/HeimanSupport"),
						InlineKeyboardButton("👥 TGRobot Support👥", url="https://t.me/joinchat/rqSonBIiCP01NWI1")
					], 
                                        [
						InlineKeyboardButton("🏠 Home ", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
