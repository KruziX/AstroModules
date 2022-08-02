from .. import loader, utils
from telethon.tl.types import Message
import asyncio
@loader.tds
class TetrisAnimation(loader.Module):
    strings = {"name": "Tetris Animation"}

    async def itetriscmd(self, message: Message):
        """Tetris Animation | inline"""
        await self.inline.form(
            text="Нажми на кнопку ниже, чтобы увидеть анимацию тетриса:",
            reply_markup=[
                [
                    {
                        "text": "❤️‍🔥",
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
        """Tetris Animation | No inline"""
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