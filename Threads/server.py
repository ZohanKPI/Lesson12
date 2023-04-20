import asyncio


async def send_request(reader, writer, message):
    writer.write(message.encode())
    await writer.drain()

    response = await reader.read(1024)
    result = response.decode()
    print(f"Result: {result}")


async def main():
    reader, writer = await asyncio.open_connection('localhost', 8888)

    while True:
        op = input("Enter operation (add/subtract): ")
        if op not in ["add", "subtract"]:
            print("Invalid operation")
            continue

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        message = f"{op} {a} {b}"
        await send_request(reader, writer, message)


if __name__ == '__main__':
    asyncio.run(main())