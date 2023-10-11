import dataSource

def main():
    try:
        data_list = dataSource.download()    
    except Exception as e:
        print(f"錯誤:{e}")
    else:
        for row in data_list:
            print(row)

if __name__ == "__main__":
    main()