#建立行李的建構子
class 行李:
    def __init__(self, 行李ID, 行李重量, 行李出發機場, 行李目的地機場, 行李所屬旅客姓名):
        self.行李ID = 行李ID
        self.行李重量 = 行李重量
        self.行李出發機場 = 行李出發機場
        self.行李目的地機場 = 行李目的地機場
        self.行李所屬旅客姓名 = 行李所屬旅客姓名

    def display_info(self):
        print(f"行李ID: {self.行李ID}")
        print(f"行李重量: {self.行李重量} 公斤")
        print(f"行李出發機場: {self.行李出發機場}")
        print(f"行李目的地機場: {self.行李目的地機場}")
        print(f"行李所屬旅客姓名: {self.行李所屬旅客姓名}")
    #使屬性能做更動
    def update_info(self, attribute, value):
        setattr(self, attribute, value)

#建立登機證的建構子
class 登機證:
    def __init__(self, 旅客姓名, 登機證編號, 登機時間, 登機門編號, 座位位置, 行李件數, 行李ID):
        self.旅客姓名 = 旅客姓名
        self.登機證編號 = 登機證編號
        self.登機時間 = 登機時間
        self.登機門編號 = 登機門編號
        self.座位位置 = 座位位置
        self.行李件數 = 行李件數
        self.行李ID = 行李ID

    def display_info(self):
        print(f"旅客姓名: {self.旅客姓名}")
        print(f"登機證編號: {self.登機證編號}")
        print(f"登機時間: {self.登機時間}")
        print(f"登機門編號: {self.登機門編號}")
        print(f"座位位置: {self.座位位置}")
        print(f"行李件數: {self.行李件數}")
        print(f"行李ID: {self.行李ID}")
    #使屬性能做更動
    def update_info(self, attribute, value):
        setattr(self, attribute, value)
        
    

# 建立三個行李
行李1 = 行李("L001", 20, "機場A", "機場B", "陳")
行李2 = 行李("L002", 15, "機場C", "機場D", "建")
行李3 = 行李("L003", 30, "機場E", "機場F", "霖")

# 建立三個登機證
登機證1 = 登機證("陳", "BP001", "12:00 下午", "門 1", "A12", 1, "L001")
登機證2 = 登機證("建", "BP002", "1:30 下午", "門 2", "B14", 1, "L002")
登機證3 = 登機證("霖", "BP003", "3:00 下午", "門 3", "C16", 1, "L003")

# 顯示行李資訊
print("\n行李資訊:")
行李1.display_info()
print("\n")
行李2.display_info()
print("\n")
行李3.display_info()
print("\n")
# 顯示登機證資訊
print("\n登機證資訊:")
登機證1.display_info()
print("\n")
登機證2.display_info()
print("\n")
登機證3.display_info()

# 更新行李資訊
行李1.update_info("行李重量", 25)
行李1.update_info("行李目的地機場", "機場A")
行李1.update_info("行李出發機場", "機場B")
行李1.update_info("行李ID", "L004")
# 更新登機證資訊
登機證1.update_info("行李ID", "L004")


# 顯示更新後的行李資訊
print("\n更新後的行李資訊:")
行李1.display_info()
# 顯示更新後的登機證資訊
print("\n更新後的登機證資訊:")
登機證1.display_info()
