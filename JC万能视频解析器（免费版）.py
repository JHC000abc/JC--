#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('--------------------------------------------------------------------')
print('-                                                                  -')
print('-                    欢迎使用JC万能视频解析器                      -')
print('-     解析通道不定期更新，如1分钟以上无法解析，请自行尝试其他接口  -')
print('-                                                                  -')
print('--------------------------------------------------------------------')
print('-            优酷视频请选择10号以后接口进行解析                    -')
print('--------------------------------------------------------------------')
print('-                                                                  -')
print('-  本软件完全免费，仅供学习交流，严禁用于商用,一切法律后果自负     -')
print('-  本软件支持全网所有视频解析，如超过1分钟未成功解析请切换接口尝试 -')
print('-  因服务器速度有限，如告诉接口请联系作者进行捐助                  -')
print('-使用过程中如遇问题或对本软件有好的建议 请联系软件作者VX:HS5788044 -')
print('-  您的建议是我们前进的动力，愿我们一同携手，共建美好网络环境      -')
print('-                                                                  -')
print('--------------------------------------------------------------------')


import webbrowser
import time


num = input('请输入要选择的解析通道号（1-13）：')
print('接口连接中，请稍后……')

time.sleep(15)

if num == '1':
    h1 = 'https://jx.quanmingjiexi.com/?url='
elif num == '2':
    h1 = 'https://jsap.attakids.com/?url='
elif num == '3':
    h1 = 'https://tool.bitefu.net/video/?url='
elif num == '4':
    h1 = 'https://www.nxflv.com/?url='
elif num == '5':
    h1 = 'http://17kyun.com/api.php?url='
elif num == '6':
    h1 = 'https://www.qianyicp.com/jiexi/index.php?url='
elif num == '7':
    h1 = 'https://jx.kingtail.xyz/?url='
elif num == '8':
    h1 = 'https://api.yueliangjx.com/?url='
elif num == '9':
    h1 = 'https://www.2ajx.com/vip.php?url='
elif num == '10':
    h1 = 'https://www.kpezp.cn/jlexi.php?url='
elif num == '11':
    h1 = 'https://jx.618g.com/?url='
elif num == '12':
    h1 = 'https://jx.km58.top/jx/?url='
elif num == '13':
    h1 = 'https://vip.52jiexi.top/?url='
    
   
h2= input('请输入要解析的视频网址：')
h3 = h1 + h2
print('服务器正在全力解析中，请稍后……')

time.sleep(15)

webbrowser.open(h3)


