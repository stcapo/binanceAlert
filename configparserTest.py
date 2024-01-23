import configparser

# 创建一个配置解析器对象
config = configparser.ConfigParser()

# 读取.ini文件
config.read('config.ini')

# 获取特定节中的键值
value1 = config['keys']['api_secret']


# 打印获取的值
print('secret key:', value1)
