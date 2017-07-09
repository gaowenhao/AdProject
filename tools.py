# encoding=utf-8
import config
import datetime
import threading
import time


# 每日删除config中网址宣传的Ip列表
def clear_config_ip_days(interval):
    config.url_ip_list.clear()
    threading.Timer(interval, clear_config_ip_days).start()


# 开启某个任务，固定每日每时执行
def task_start_day_hour(task, which_hour=0, max_error=10, interval=86400):
    """
        task : 开启的任务
        which_hour : 每天开启的时间（小时）
        max_error : 最大误差（秒）
        interval : 每隔多久执行一次（秒）
    """
    while True:
        now = datetime.datetime.now()
        if now.hour == which_hour:
            task(interval)
            return
        else:
            time.sleep(max_error)
