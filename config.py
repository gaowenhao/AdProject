# encoding=utf-8
import os

PORT = 80

APP_SETTING = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'cookie_secret': 'VincentHeroGao',
}

# url地址推广
url_popularize = ['https://www.2345.com/?k58335833', 'https://www.duba.com/?un_454974_170755',
                  'https://123.sogou.com/?22417-0755']
# 用于存储当日用户的
url_ip_list = {}

# 存储可下载文件目录
down_load_dir = "/home/adserver/file/"

# 2345包文件名
file_2345_movie = "2345_k58335833_movie.exe"