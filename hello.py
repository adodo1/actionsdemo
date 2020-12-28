# -*- coding: utf-8 -*-
import io, sys, os, time, requests


if __name__ == '__main__':
    #
    print('Hello DoDo!')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 
    url = 'http://dzdy.itzjj.cn/static/skin/summer/images/top1.jpg'
    url = 'https://avgle.com/videos'
    r = requests.get(url)
    data = r.content
    print(r.status_code)
    print(data)
