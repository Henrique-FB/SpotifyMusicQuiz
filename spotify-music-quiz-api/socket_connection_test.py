import socketio
import asyncio

async def socket_test(playlist, name, user_type="player"):
    sio = socketio.AsyncClient()

    @sio.on('message')
    def on_message(data):
        print(f"{name} receives -->> {data}")

    @sio.on('auth_url')
    def on_auth_url(data):
        print(f"{name} receives -->> {data}")
        
    await sio.connect('http://localhost:3000')
    await sio.emit("join", {"username": name})
    await sio.sleep(2)

    redirect_response = input("Paste the full redirect URL here: ")
    await sio.emit("auth_code", {"redirect_response": redirect_response})
    await sio.sleep(2)
    
    await sio.emit("add_playlist", {"playlist": playlist})
    await sio.sleep(3)
    if (user_type == "owner"):
        await sio.emit("start_game")
    await sio.sleep(5)
    await sio.disconnect()

async def main():
    a = asyncio.create_task(socket_test("5JRTdzA7qakwsZwNmBwEgk", "Henrique", "owner"))
    #b = asyncio.create_task(socket_test("0sauyWfVZVsuQ5GanN5ted", "Gabi"))
    await a
    #await b

asyncio.run(main())