import webbrowser
import websockets
import asyncio
import datetime
import pathlib


# Websocket server loop
async def time(websocket, path):    # ws_handler requires 2 arguments, path not used in this code
    while True:
        try:
            # Get current time, isoformat() makes it a string in ISO 8601 format
            now = datetime.datetime.now().time().isoformat(timespec='seconds')

            await websocket.send(now)       # Send current time to GUI
            await asyncio.sleep(1)          # Wait one second before running loop again

        # If GUI is closed, exit the while loop
        except websockets.ConnectionClosed:
            break

    # Stop the asyncio event loop - closing the program
    asyncio.get_event_loop().stop()


def main():
    # Assign the websocket server
    start_server = websockets.serve(time, "127.0.0.1", 5678)

    # (mac os) Get current path and open the gui in default web browser
    gui_location = str(pathlib.Path().absolute())
    webbrowser.open_new_tab("file://" + gui_location + "/gui/index.html")

    # Start the websocket server
    asyncio.get_event_loop().run_until_complete(start_server)

    # Keep the program running
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
