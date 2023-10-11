import dataSource

def main():
    cities = dataSource.cities_info()
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()