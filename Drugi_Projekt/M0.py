import asyncio
import aiohttp
import pandas as pd

client_ids = list(range(1, 10001))

df = pd.read_json("this-file.json", lines=True)

rows_per_client = len(df) // len(client_ids)

df_chunks = [
    df.iloc[i : i + rows_per_client] for i in range(0, len(df), rows_per_client)
]

clients = {idx: chunk["content"].tolist() for idx, chunk in zip(client_ids, df_chunks)}


async def process_codes(client_id, codes):
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            "http://localhost:31310/", json={"client": client_id, "codes": codes}
        )
        result = await response.json()
        return result


async def main():
    tasks = [process_codes(client_id, codes) for client_id, codes in clients.items()]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(
            f"Prosjecna velicina koda za klijents sa ID {result['client']} is {result['averageWordcount']}"
        )


asyncio.run(main())
