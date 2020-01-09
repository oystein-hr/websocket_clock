import webbrowser
import websockets
import asyncio
import datetime
import pathlib


async def time(websocket, path):
    while True:
        try:
            now = datetime.datetime.now().time().isoformat()

            await websocket.send(now)
            await asyncio.sleep(1)
        except websockets.ConnectionClosed:
            break

    asyncio.get_event_loop().stop()


def main():
    gui_location = str(pathlib.Path().absolute())
    start_server = websockets.serve(time, "127.0.0.1", 5678)
    webbrowser.open_new_tab("file://" + gui_location + "/gui/index.html")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
