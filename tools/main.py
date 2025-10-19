# 大麦网的登录URL和抢票URL
# another demo , singel script
import requests
from bs4 import BeautifulSoup

login_url = 'https://www.damai.cn/login.aspx'
ticket_url = 'https://m.damai.cn/shows/item.html?from=def&itemId=960773583291&sqm=dianying.h5.unknown.value&spm=a2o71.category_musicfestival.floor1.item_0'  # 替换为实际的抢票URL

# 登录信息
login_data = {
    'username': '1355417237',
    'password': 'Play19940520ab'
}

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 创建一个会话
session = requests.Session()

# 登录
def login():
    response = session.post(login_url, data=login_data, headers=headers)
    if response.status_code == 200:
        print("登录成功")
    else:
        print("登录失败")

# 获取票务信息
def get_ticket_info():
    response = session.get(ticket_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 解析票务信息，这里需要根据实际页面结构来编写
        ticket_info = soup.find('div', class_='ticket-info')
        if ticket_info:
            print("获取票务信息成功")
            return ticket_info
        else:
            print("获取票务信息失败")
    else:
        print("请求票务信息失败")

# 提交订单
def submit_order():
    # 这里需要根据实际页面结构来编写提交订单的逻辑
    order_data = {
        'ticket_id': '123456',  # 替换为实际的票ID
        'quantity': '1'  # 替换为实际的购买数量
    }
    response = session.post(ticket_url, data=order_data, headers=headers)
    if response.status_code == 200:
        print("提交订单成功")
    else:
        print("提交订单失败")

# 主函数
def main():
    login()
    ticket_info = get_ticket_info()
    if ticket_info:
        print("login success")
        # submit_order()

if __name__ == '__main__':
    main()
