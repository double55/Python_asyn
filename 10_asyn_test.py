import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
    print("开始下载：", url)
    loop = asyncio.get_event_loop()

    # requests模块默认不支持异步操作，所以就使用线程池来配合实现
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print("下载完成", url)

    # 图片保存到本地文件
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode="wb") as file_object:
        file_object.write(response.content)


if __name__ == "__main__":
    url_list = ['https://pic3.zhimg.com/v2-58d652598269710fa67ec8d1c88d8f03_r.jpg',
                'https://scpic.chinaz.net/files/pic/pic9/201311/apic2098.jpg']
    tasks = [download_image(url) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
