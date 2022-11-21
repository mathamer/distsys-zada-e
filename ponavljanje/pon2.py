import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

temp = [{"ime":"Stol"},{"ime":"Laptop"}]

@routes.get("/")
async def get_hendler(request):
    return web.json_response({"status":"ok"}, status=200)

@routes.get("/artikl")
async def get_artikl(request):
    """
    data = request.query
    print(type(data))
    print(data)
    data = data.get("ime")
    print(data)
    """
    data = request.query.get("ime")
    res = [d for d in temp if d.get("ime") == data]

    return web.json_response({"status":"ok", "data":res}, status=200)

@routes.post("/artikl")
async def post_artikl(request):
    json_data = await request.json()
    print(json_data)
    return web.json_response({"status":"ok"}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
