import datasource

def main():
    cities=datasource.cities_info()
    for city in cities:
        print(city)
    name=datasource.city_names()
    print(name)
    city=datasource.info("新竹市北區")
    print(city)

if __name__ =="__main__":
    main()