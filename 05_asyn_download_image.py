import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        with open(file_name, mode="wb") as file_object:
            file_object.write(content)
        print("下载完成：", url)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = ['https://pic3.zhimg.com/v2-58d652598269710fa67ec8d1c88d8f03_r.jpg',
                    'https://scpic.chinaz.net/files/pic/pic9/201311/apic2098.jpg']
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())
