import dataSource

def main():
    names = dataSource.cityNames()
    city = dataSource.info(name='屏東縣新埤')
    #print(names)
    print(city)
    

if __name__ == "__main__":
    main()