from loguru import logger
from imports import *

@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all
    exceptions within task factory tasks.
    """
    logger.add("logs.txt")
    logger.exception(exception)
    logger.debug(update)
    await dp.bot.send_message(chat_id=ADMINS[0], text=f"ERROR!\n{exception}\n\n<code>{update}</code>")
    file = types.InputFile(path_or_bytesio="logs.txt")
    await asyncio.sleep(0.05)
    await dp.bot.send_document(chat_id=ADMINS[0],document=file)
    return True
