import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/getActivity")
async def get_activity(req):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(8):
            tasks.append(
                asyncio.create_task(
                    session.get("https://www.boredapi.com/api/activity")
                )
            )
        res = await asyncio.gather(*tasks)
        res = [await x.json() for x in res]
        print(tasks)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(len(res)):
            tasks.append(
                asyncio.create_task(
                    session.post("http://127.0.0.1:8081/parseActivities", json=res[i])
                )
            )
        res = await asyncio.gather(*tasks)
        res = [await x.json() for x in res]
    print(res)
    return web.json_response({"status": "ok", "messages": res}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
