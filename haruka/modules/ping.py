# Copyright (C) 2020 by dark12knight@Github, < https://github.com/dark12knight >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime
from knight2.0 import knight2.0, Message


@knight2.0.on_cmd(
    "ping", about={'header': "check how long it takes to ping your bot"})
async def pingme(message: Message):
    start = datetime.now()
    await message.edit('`Pong!`')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
