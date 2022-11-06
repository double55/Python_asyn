import requests


def download_image(url):
    print("开始下载：", url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    print("下载完成。")
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode="wb") as file_object:
        file_object.write(response.content)


if __name__ == "__main__":
    url_list = ['https://pic3.zhimg.com/v2-58d652598269710fa67ec8d1c88d8f03_r.jpg',
                'https://scpic.chinaz.net/files/pic/pic9/201311/apic2098.jpg']
    for item in url_list:
        download_image(item)
