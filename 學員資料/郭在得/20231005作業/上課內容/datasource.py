import requests
import csv
import io

__cities=[]

def __download()->list[list]:
    # 111年台灣各縣市人口密度
    url="https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108"

    a=requests.request("GET",url)

    try:
        a.raise_for_status()
    except:
        raise Exception("連線發生錯誤，網路中斷")
    else:
        if not a.ok:
            raise Exception("下載失敗，伺服器錯誤訊息")
        else:
            file = io.StringIO(a.text)
            a_reader=csv.reader(file)
            next(a_reader)
            return list(a_reader)

def cities_info()->list[list]:
    if len(__cities)==0: 
        try:
            a_list=__download()
        except Exception as i:
            print(f"錯誤：{i}")
        else:
            for i in a_list:
                if i[0] =='111':
                    __cities.append(i)
        return __cities
    else:
        return __cities
    
def city_names()->list[str]:
    cities=cities_info()
    name=[]
    for i in cities:
        cityname=i[1]
        name.append(cityname)
    return name

def info(name:str)->list[str]:
    cities=cities_info()
    for i in cities:
        if i[1] == name:
            return i
    return []