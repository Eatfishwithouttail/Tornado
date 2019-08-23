import asyncio
import requests






@asyncio.coroutine
def downlodad(url):
    resp = requests.get(url)
    return resp.content ,resp.status_code


@asyncio.coroutine
def write_file(filename,content):
    yield from asyncio.sleep(1)
    with open(filename,"wb") as f:
        f.write(content)
    print(filename,"写入完成")



@asyncio.coroutine
def save(url,filename):
    print('%s下载中'%url)
    content ,code = yield  from downlodad(url)
    print(url,code)
    yield from write_file(filename,content)
    print(url,filename,"保存成功")



if __name__ == '__main__':
    #获取事件循环器对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
        save('https://www.baidu.com','baidu.html'),
        save('https://www.jd.com','jd_.html'),
        save('https://mail.qq.com','qq_.html'),
    ]))