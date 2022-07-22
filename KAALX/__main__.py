import glob
import os
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from KAALX import bot, kaalver
from KAALX.Config import Var
from KAALX.utils import load_module,start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from KAALX import CMD_HNDLR

MANJEET = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT

# let's get the bot ready
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startup_log_all_done():
    try:
        await bot.send_message(MANJEET, f"**Check your bot**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

#
if len(argv) not in (1, 3, 4):

    bot.disconnect()

else:

    bot.tgbot = None

    if Var.TG_BOT_USER_NAME_BF_HER is not None:

        print("Initiating Inline Bot")

        # ForTheGreatrerGood of beautification

        bot.tgbot = TelegramClient(

            "TG_BOT_TOKEN_BF_HER", api_id=Var.APP_ID, api_hash=Var.API_HASH

        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)

        print("Initialised Sucessfully")

        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))

        print("Startup Completed")

    else:

        bot.start()

path = 'KAALX/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "KAALX/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")

# that's life...
async def kaal_is_on():
    try:
        if Config.PRIVATE_GROUP_ID != 0:
            await bot.send_file(
                Config.PRIVATE_GROUP_ID,
                caption=f"deploy done",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join kaal Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Murat_30_God"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@kaalxsupport"))
#    except BaseException:
#        pass


bot.loop.create_task(kaal_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()


