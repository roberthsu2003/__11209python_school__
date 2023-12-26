try:
    f = open('data.txt', 'r', encoding="utf8") 
    print(f.read( ))  
except FileNotFoundError: 
    print("找不到檔案")
except PermissionError: 
    print("你沒有權限存取")
except IOError: 
    print("其他檔案IO問題")
except: 
    print("其他例外")
    
f.close( )