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
    data = r.text
    print(r.status_code)
    print(data)

    for i in range(10):
        print(i, '---------')
        time.sleep(5)
    
    print('Done.')
