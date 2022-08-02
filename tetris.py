__version__ = (1, 0, 2)
from .. import loader, utils
from telethon.tl.types import Message
import asyncio
@loader.tds
class TetrisAnimation(loader.Module):
    strings = {"name": "Tetris Animation"}

    async def itetriscmd(self, message: Message):
        """Tetris Animation | Inline"""
        await self.inline.form(
            text="💥 Нажмите на кнопку ниже, чтобы увидеть анимацию игры Tetris:",
            reply_markup=[
                [
                    {
                        "text": "👀 Увидеть",
                        "callback": self.inline_animation
                    }
                ]
            ],
            message=message
        )
    
    async def inline_animation(self, message: Message):
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)

    async def tetriscmd(self, message: Message):
        """Tetris Animation | No Inline"""
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟧⬛️⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n🟨🟨⬛⬛️⬛️⬛️⬛️ \n⬛⬛🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n⬜⬜⬜⬜⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n🟨🟨🟧🟥⬛️⬛️⬛️ \n🟧🟧🟧🟥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n💥💥💥💥⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await message.edit("⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)

    async def ihtetriscmd(self, message: Message):
        """Tetris Heart Animation | Inline"""
        await self.inline.form(
            text="💥 Нажмите на кнопку ниже, чтобы увидеть анимацию сердца Tetris:",
            reply_markup=[
                [
                    {
                        "text": "👀 Увидеть",
                        "callback": self.inline_animation
                    }
                ]
            ],
            message=message
        )
    
    async def inline_animation(self, message: Message):
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️🟥⬛️🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟥⬛️🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛⬛️⬛️ \n⬛️⬛️🟥⬛🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛⬛️⬛️ \n⬛️⬛️⬛⬛⬛⬛️⬛️ \n⬛️⬛️🟥⬛🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)

    async def htetriscmd(self, message: Message):
        """Tetris Heart Animation | No Inline"""
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️🟥⬛️🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️🟥⬛️🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛⬛️⬛️ \n⬛️⬛️🟥⬛🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
        await utils.answer(message, "⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛⬛️⬛⬛️⬛️ \n⬛️⬛️⬛⬛⬛⬛️⬛️ \n⬛️⬛️🟥⬛🟥⬛️⬛️ \n⬛️⬛️⬛️🟥⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n")
        await asyncio.sleep(0.7)
