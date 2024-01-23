import requests
from plyer import notification
import time

def get_klines():
    url = "https://fapi.binance.com/fapi/v1/klines?symbol=BIGTIMEUSDT&interval=5m"
    response = requests.get(url)
    klines = list(response.json())
    return klines

def sleep_to_5min():
        # 获取当前时间的时间戳（以秒为单位）
    current_timestamp = time.time()

    # 找到当前时间戳所在的5分钟间隔的结束时间
    # 首先，将时间戳转换为以分钟为单位，并对5取整得到最近的5分钟整数倍
    # 然后，将这个整数乘以60（秒）并加上300秒（5分钟）来得到下一个5分钟间隔的结束时间戳
    next_5_minute_end_timestamp = (int(current_timestamp // 300) + 1) * 300

    # 计算当前时间与下一个5分钟收盘时间之间的秒数差
    seconds_to_next_5_minute_end = int(next_5_minute_end_timestamp - current_timestamp)
    for remaining in range(seconds_to_next_5_minute_end, 0, -1):
        print(f"Remaining seconds: {remaining}", end='\r')
        time.sleep(1)

    print("Countdown finished!")
while True:
    sleep_to_5min()
    # 给定的列表
    l = get_klines()

    # l[0]的末尾置为0
    l = l[-5:]
    l[0].append(0.0)
    # 计算l[1]和l[2]的涨跌幅并添加到末尾
    for i in range(1, len(l)):
        previous_close_price = float(l[i-1][4])  # 前一个时间段的收盘价
        current_close_price = float(l[i][4])     # 当前时间段的收盘价
        price_change = ((current_close_price - previous_close_price) / previous_close_price) * 100
        l[i].append(price_change)
    a=1

    for i in l:
        print(i[len(i)-1])
        if(i[len(i)-1]-1>=0):
            a=a&1
        else:
            a=a&0
    while a==1:
        # 发送通知
        notification.notify(
            title='通知标题',
            message='这是通知内容。',
            app_name='应用名称',
            timeout=1  # 通知显示的时间（秒）
        )

        # 每隔一定时间发送一次通知
        time.sleep(1)  # 60秒

exit()