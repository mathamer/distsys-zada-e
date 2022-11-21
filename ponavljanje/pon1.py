import aiohttp
import asyncio
from aiohttp import web

async def get(request):
    duljina = await idi_na_google()
    return web.json_response(data={"status": "OK", "length": duljina})

async def idi_na_google():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as resp:
            return len(await resp.text())

app = web.Application()
app.add_routes([web.get("/service", get)])

web.run_app(app)



