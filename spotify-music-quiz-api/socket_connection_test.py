import socketio
import asyncio


async def socket_test():
    sio = socketio.AsyncClient()
    #connect to server

    @sio.on('message')
    def on_message(data):
        print(data)

    await sio.connect('http://localhost:3000')
    await sio.emit("join", {"username": "test_user"})
    await sio.emit("add_playlist", {"playlist": "5JRTdzA7qakwsZwNmBwEgk"})
    await sio.sleep(2)
    await sio.emit("get_info",{})
    await sio.sleep(10)
    await sio.disconnect()

asyncio.run(socket_test())