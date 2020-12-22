from handlers import MainHandler, AddMessageHandler

handlers = [
    ("/index", MainHandler),  # 界面显示
    ("/form/", AddMessageHandler)  # 提交功能
]