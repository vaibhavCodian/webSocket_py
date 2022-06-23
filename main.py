import asyncio
import os

import websockets

connected = set()


async def server(websocket, path):
    # Register
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f'Got a new Masssage: {message}')
    finally:
        connected.remove(websocket)

port = int(os.environ.get("PORT", 5000))
start_server = websockets.serve(server, '0.0.0.0', 80)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()