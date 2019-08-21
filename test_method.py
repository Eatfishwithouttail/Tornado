from unittest import TestCase
import requests

class TestToenado(TestCase):
    base_url = 'http://10.36.174.26:8000'

    def test_index_post(self):
        url = self.base_url+'/'
        resp = requests.post(url,data={
            'name':'disen',
            'city':'西安'
        })
        print(resp.text)

    def test_index_get(self):
        url = self.base_url + '/'
        resp = requests.get(url, params={
            'wd': 'python',
            "title": ["上海", "北京"]
        })
        print(resp.text)

    def test_search(self):
        resp = requests.get('http://10.36.174.26:8000/search',params={
            "wd":'python'
        })
        print(resp.text)
        print(resp.cookies)
        for key,cookie in resp.cookies.items():
            print(key,resp.cookies.get(key))
    def test_delete(self):
        url = 'http://10.36.174.26:8000/cookie'
        resp = requests.delete(url,parmas={
            'name':'token'
        })

class  TestOrderRequest(TestCase):
    url = 'http://10.36.174.26:8000/order/1/1'
    def test_get(self):
        resq = requests.get(self.url)
        print(resq)

    def test_post(self):
        resq = requests.post(self.url)
        print(resq)



class TestUserRequest(TestCase):
    url = 'http://localhost:8000'
    def test_login(self):
        resp = requests.get(self.url,json={
            'name':'disen',
            'pwd':'123'
        })
        print(resp.text)

    def test_adduser(self):
        resp = requests.post(self.url,json={
            'name':'lm',
            'pwd':'123456',
            'phone':13206897895,
            'city':'西安'
        })
        print(resp.text)

    def test_xiuuser(self):
        resp = requests.put(self.url, json={
            'user_id':2,
            'name': 'mrx',
            'pwd': '521436',
            'phone': 13206897895,
            'city': 'beijing'
        })
        print(resp.text)
