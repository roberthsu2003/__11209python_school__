import datasource

def main():
    jsonData = datasource.download_youbike_data()
    print(jsonData)

if __name__ == "__main__":
    main()