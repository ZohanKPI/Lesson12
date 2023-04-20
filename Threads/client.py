import asyncio

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('localhost', 8888)

    print('Enter two numbers and an operation to perform (e.g. "4 2 add"):')
    data = input().split()
    num1, num2, operation = data

    writer.write(f"{num1} {num2} {operation}".encode())
    await writer.drain()

    result = await reader.read()
    print(f"Result: {result.decode().strip()}")

    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())