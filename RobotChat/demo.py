import json
from urllib.request import urlopen, Request
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


class ChatRobot(object):
    def __init__(self):
        # API接口地址
        self.url = 'http://api.tianapi.com/txapi/robot/index'
        self.app_key = '?key=3a698998a268519ba10159b432016308&question='

    def getChatText(self, text):
        """获取聊天返回内容"""
        # 发送聊天请求
        request = Request(self.url + self.app_key + text)
        try:
            w_data = urlopen(request)
        except Exception as error_info:
            return error_info
        response_text = w_data.read().decode('utf-8')
        json_result = json.loads(response_text)
        return json_result['newslist'][0]["reply"]


# 聊天程序主入口
if __name__ == '__main__':
    print("--------------------退出请输入q")
    robot = ChatRobot()
    while True:
        msg = input("\n本人:")
        if msg == 'q':
            exit("聊天结束!")
        else:
            robot_data = robot.getChatText(msg)
            print("机器人:", robot_data)
