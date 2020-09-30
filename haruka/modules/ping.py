

@knight2.0.on_cmd(
    "!ping", about={'header': " def pingme(message: Message):
    start = datetime.now()
    await message.edit('Pong!')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit💎(f"**Pong!**\n{m_s} ms ✅")
