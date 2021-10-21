import pravega_client

manager = pravega_client.StreamManager("pravega:9090")
reader_group = manager.create_reader_group("rg1", 'stock', 'dbserver1.stock.stock')
reader = reader_group.create_reader("reader_id")

async def read():
    slice = await reader.get_segment_slice_async()
    i = 0
    for event in slice:
        print(event.data())
        i += 1
        if i > 10:
            break

import asyncio

try:
    asyncio.run(read())
finally:
    reader.reader_offline()
