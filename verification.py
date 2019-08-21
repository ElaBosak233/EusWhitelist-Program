import asyncio
import requests
from async_mcrcon import MinecraftClient
import time
name = input("Please enter your Minecraft ID:")
print("========================================")
print("  New player "+name+" apply to join the server")
add1 = "https://api.mojang.com/users/profiles/minecraft/"
r = requests.get(add1 + name)
t = r.text
if "name" and "id" and name in t:
    print("========================================")
    print("   Step1.MOJANG Verification passed :)")
    print("========================================")
    time.sleep(1)
    print(" Step2.Upcoming joint server whitelist")
    print("========================================")
    time.sleep(1)
    async def updateWhitelist():
        async with MinecraftClient('address', 'port', 'passwd') as mc:
            output = await mc.send('whitelist add ' + name)
            print(output)
    # asyncio.run(updateWhitelist())

    #Please use the above code as appropriate. 请按照情况使用上面的代码( asyncio.run(updateWhitelist())  )
    # Delete quotation marks around'port' 删除围绕'port'的引号
else:
    print("========================================")
    print("      MOJANG Verification failed :(")
    print("========================================")