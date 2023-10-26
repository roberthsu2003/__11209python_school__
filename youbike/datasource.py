import requests

def download_youbike_data():
    '''
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    if requests.status_codes == 200:
        #print("下載成功")
        raise Exception("下載失敗")
    else:
        raise Exception("下載失敗")