import requests
import csv
import io

def download() -> list[list]:
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
    response = requests.request('GET',url)
    try:
        response.raise_for_status()
    except:
        raise Exception("連線發生錯誤","網路中斷")    
    else:
        if not response.ok:
            raise Exception("下載錯誤","伺服器錯誤訊息!")    
        else:
            file = io.StringIO(response.text)
            csv_reader = csv.reader(file)
            next(csv_reader)
            return list(csv_reader)