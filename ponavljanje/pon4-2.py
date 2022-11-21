import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

temp = []

@routes.post("/parseActivities")
async def parse_act(request):
    try:
        json_data = await request.json()
        if json_data.get("type") == "relaxation":
            temp.append(json_data)
            return web.json_response({"Message":json_data.get("activity")}, status=200)
        else:
            return web.json_response({"Failed":"Krivi tip"}, status=400)
    except Exception as e:
        return web.json_response({"Failed":str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)