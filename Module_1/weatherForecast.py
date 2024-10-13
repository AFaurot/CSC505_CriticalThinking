import requests


def main():

    # Variable to store zipcode or city name
    city = input("Enter a zipcode or city name: ")
    print("Getting the weather for {} area".format(city))

    # Requests module to pull weather data from wttr api.
    url = 'http://wttr.in/{}'.format(city)
    res = requests.get(url)

    # Print weather data
    print(res.text)


if __name__ == '__main__': main()


