# -*- coding: utf-8 -*-


"""
File   : 
Date   :2022/5/22
Author :vingurzhou
Project:pythonProject
Product:PyCharm 
Details:

"""
import json
import time

import requests
import re
import requests
import json

import selenium
from selenium import webdriver

# 生成浏览器对象
driver = webdriver.Chrome(executable_path='/Users/vingurzhou/Downloads/chromedriver')
driver.get("https://login.taobao.com/")

# 等待登录
while True:
    time.sleep(10)
    y = input("登录完成输入1: ")
    if y == "1":
        break

def get_content(url):
    for i in range(10):
        url = f"https://rate.tmall.com/list_detail_rate.htm?itemId=670516432301&spuId=2368903390&sellerId=2208072012317&order=3&currentPage={i + 1}&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvC9vxvX6vUpCkvvvvvjiWRLMhtj1hRFMp0jivPmPhsjnVRLFw0jtEP2F9zj1nPTQCvCUyCnGmDXZv8XwidAyDZT7xzw6gvpvhvvvvvUvCvCB476bM4r147DuFbKNwUHic7uPNZ8QCvCp%2BCWhm%2FM%2BvUpgidAhAZqeBCahTR4QCvvyv2jKCGPvv2oV%2BvpvBUv1h9a2pvveL84%2F9bZbxKaVVvpvhvvpvvvvCvvOvCvvvphvUvpCWm8tzvva4a4mxfXuK4Z7xfaBl533%2BCNLhAnQXHFXXiXVvQE01Ux8x9WLwjLyDZacEKOmAdcHHaNoxfX94jL4UDa7tndw3BOkQD76wdu9Cvv9vvUCvuKMieU9CvvwUvUVCwZjhKvhv8vvvvU1vpvvvvvmCmyCv2mgvvUnvphvpgvvv96Cvpv1dvvm2phCv2V%2BRvpvhMMGvv29Cvvpvvvvvi9hvCvvv9U8%2BvpvoEv9R9OR2vvDD84Ge8ZJrmacDdvhvhkpUgOVPFQvXukeSEkDjdp5xt4QCvvyvmbWm47yvjc4%2BvpvBUvBn9ytRvmhg84%2F9nh2ExLV%2BvpvBUvpGv%2B5EvmjS84GuUZWE3we%2BvpvEvvp%2BvFwzvm7D&needFold=0&_ksTS=1653197882848_461&callback=jsonp462"
        payload = {}
        headers = {
            'authority': 'rate.tmall.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'dnk=tb33757397; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie21=Vq8l%2BKCLivbdjeuVIQ2NTQ%3D%3D&cookie14=UoexMS5sdoAw%2Fg%3D%3D&pas=0&existShop=false; uc3=vt3=F8dCvC%2B6QlWv0eh8jME%3D&id2=UNkwdghTXLozpg%3D%3D&nk2=F5RGNekkd29W1Q%3D%3D&lg2=URm48syIIVrSKA%3D%3D; tracknick=tb33757397; lid=tb33757397; uc4=nk4=0%40FY4NAAqEg9VIadPXqkH76rQ8Zbqm&id4=0%40Ug46uRDniPnGX7bqz44U2LaoeHjb; _l_g_=Ug%3D%3D; unb=3976527866; lgc=tb33757397; cookie1=BxuX4QpLZVp3sXeQC8ho%2FGK%2BoEyqSFDyst2YxzEXuyo%3D; login=true; cookie17=UNkwdghTXLozpg%3D%3D; cookie2=140c5df1d9aefada9cf115ed075b4174; _nk_=tb33757397; sgcookie=E1003u8%2F5aDzofDwfr%2B1Qp4pUfb6fgw%2FkSgrfN02vgOPmjHr8fWOpiLf7HKe%2FLfVxGfz%2BYJBLZDta5HkZhguAi0uomSv%2FRGhFHObdcpzPxU55NlyikJy91U9yTsT%2FNfmQ9GE; cancelledSubSites=empty; t=d337a82bfde72b33898b2de8ac95df9f; sg=762; csg=9a7edfd6; _tb_token_=57e1e35ef69d; cna=+DOWGV4eKQgCAXAVEXtgf2Zo; xlly_s=1; _m_h5_tk=a52cc541c0d33589d12654ac1c9db0c2_1653204841593; _m_h5_tk_enc=6c31c6cc73d48633d77a9c6301c46945; enc=d08TI1Iwj4AijqfAPAErX6tx9yX53lhpAkk3rfvuUW28YGMC43mzi7Z5FPCS3h9gNUf5PW1TxyRBz4hhsOajNQ%3D%3D; isg=BL6-wh3EUOCICYTEXzXaorzhD9IA_4J5i2cIo2jFZoH9C1_l0I-ciOGtg9fHM3qR; l=eBxjEZQuLXsNofMWBO5CFurza77TrQAb8sPzaNbMiInca1PGsFt6ANCh17_k-dtjgtCfXety07yjhRQbW3UN2ZqhuJ1REpZNBxvO.; tfstk=c-qfB2v7b5ErLw_w0-6Pby-lXUmha79ICZG0h_G4ZvdCRTejwsqBYXap6PAtbAH5.',
            'pragma': 'no-cache',
            'referer': 'https://detail.tmall.com/item.htm?id=670516432301&ns=1&abbucket=8',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        content = json.loads((response.text).strip('\r\njsonp462(').strip(')'))['rateDetail']['rateList']
        for i in content:
            for i in i['pics']:
                print(f"https:{i}")
            pass

def itemParse(detail_url):
    get_content(detail_url)


def main():
    goods = "女装"
    for i in range(1):
        # 商品
        # url = f"https://s.taobao.com/search?q={goods}&s={44 * i}"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "cookie": "__wpkreporterwid_=b9e31fb1-5d29-4dcd-34de-b042650bce5a; ctoken=Hu9iKDitNep3_64C8bju9K-H; lego2_cna=XXYRKPWEE4U2UDC4H242P42E; cna=+DOWGV4eKQgCAXAVEXtgf2Zo; _m_h5_tk=785b2304bed6cbd59ca22c50c15f7e82_1653200588312; _m_h5_tk_enc=ccea867884dda142ba435afe0e257ad8; xlly_s=1; _samesite_flag_=true; cookie2=140c5df1d9aefada9cf115ed075b4174; t=d337a82bfde72b33898b2de8ac95df9f; _tb_token_=57e1e35ef69d; sgcookie=E1003u8/5aDzofDwfr+1Qp4pUfb6fgw/kSgrfN02vgOPmjHr8fWOpiLf7HKe/LfVxGfz+YJBLZDta5HkZhguAi0uomSv/RGhFHObdcpzPxU55NlyikJy91U9yTsT/NfmQ9GE; unb=3976527866; uc3=vt3=F8dCvC+6QlWv0eh8jME=&id2=UNkwdghTXLozpg==&nk2=F5RGNekkd29W1Q==&lg2=URm48syIIVrSKA==; csg=9a7edfd6; lgc=tb33757397; cancelledSubSites=empty; cookie17=UNkwdghTXLozpg==; dnk=tb33757397; skt=2097578c8fa629ce; existShop=MTY1MzE5Mjc5NA==; uc4=nk4=0@FY4NAAqEg9VIadPXqkH76rQ8Zbqm&id4=0@Ug46uRDniPnGX7bqz44U2LaoeHjb; tracknick=tb33757397; _cc_=U+GCWk/7og==; _l_g_=Ug==; sg=762; _nk_=tb33757397; cookie1=BxuX4QpLZVp3sXeQC8ho/GK+oEyqSFDyst2YxzEXuyo=; mt=ci=12_1; uc1=cookie14=UoexMS5scJr0NA==&existShop=false&pas=0&cookie21=W5iHLLyFfX5YzvvQHefkmw==&cookie16=VFC/uZ9az08KUQ56dCrZDlbNdA==&cookie15=V32FPkk/w0dUvg==; thw=cn; tfstk=cAjhBjZJECGbemTGlktQVXcxdePAZ5iyigS1bJDr7QYwnESNiOuZuYqQIBVbT41..; l=eBxmsmWcLXRTqbOoBO5CFurza7790IRbzsPzaNbMiInca1-51F_dqNCh1qtvRdtjgtfUaety07yjhdFB-UUa2_f_fOhuBKWOVxJw-; isg=BJycL5y5EibKxOb6kVDdbU7XbbxOFUA_XR1q_XadPAd2wT5LniQizwDzJSk5yXiX"
        }
        html = requests.get(url, headers=headers).text
        content = re.findall('''(?<=auctions":).*?(?=,"recommendAuctions)''', html)
        for i in json.loads(content[0]):
            detail_url = i['detail_url']
            if detail_url.startswith('/'):
                detail_url = f'https:{detail_url}'
            itemParse(detail_url)
            break


        # # 店铺
        # url=f'https://shopsearch.taobao.com/search?q={goods}&s={20 * i}'
        # # 访问页面链接
        # driver.get(url)
        # # 获取页面源代码
        # source_code = driver.page_source
        # print(source_code)
        # # 关闭标签页
        # driver.close()
        # # 退出浏览器
        # driver.quit()



main()
