from plyer import notification
import time

while True:
    # 发送通知
    notification.notify(
        title='通知标题',
        message='这是通知内容。',
        app_name='应用名称',
        timeout=1  # 通知显示的时间（秒）
    )

    # 每隔一定时间发送一次通知
    time.sleep(1)  # 60秒
