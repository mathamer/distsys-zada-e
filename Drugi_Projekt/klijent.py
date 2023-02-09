import asyncio
import aiofiles
import json
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


async def process_data(client, code):
    avg = sum(len(word) for word in code.split()) / len(code.split())
    print(f"Za {client}, prosjecan broj slova koji sadrzi sav kod: {avg}")


@routes.get("/JsonData")
async def json_data(request):
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("this-file.json", mode="r") as file_data:
            read_data = [await file_data.readline() for _ in range(10)]
            whole_data = [json.loads(line) for line in read_data]
            client_ids = [f"client{i}" for i in range(10)]
            tasks = []
            database = []
            for i, item in enumerate(whole_data):
                db_item = {"client_id": client_ids[i], "python_code": item["content"]}
                database.append(db_item)
                wait = database
                tasks.append(
                    asyncio.create_task(
                        session.post("http://localhost:8082/JsonData", json=database)
                    )
                )
                final = await asyncio.gather(*wait)
                final = [await x.json() for x in final]

            return web.json_response(final, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=31310)
