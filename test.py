import requests
import pickle
import json

class Hospital:
    def __init__(self):
        self.query_hospital_url = "https://www.114yygh.com/hospital"
        self.config = Config()

    def gen_department_url(self):
        return self.query_hospital_url + "/" + str(self.config.hospital_id) + "/home"

    def get_duty_time(self):
        """获取放号时间"""
        addr = self.gen_department_url()
        print(f"addr:{addr}")
        response = requests.get(addr)
        ret = response.text
        print(f"ret:{ret}")
        data = json.loads(ret)
        print(f"data:{data}")
        return data["data"]["dutyTime"]

class Config:
    def __init__(self):
        self.hospital_id = "H02110003"

if __name__ == "__main__":
    hospital = Hospital()
    duty_time = hospital.get_duty_time()
    print(f"放号时间：{duty_time}")

    # 将放号时间保存到文件中
    with open("放号时间.pickle", "wb") as f:
        pickle.dump(duty_time, f)

    # 从文件中读取放号时间
    with open("放号时间.pickle", "rb") as f:
        duty_time = pickle.load(f)

    print(f"从文件中读取的放号时间：{duty_time}")