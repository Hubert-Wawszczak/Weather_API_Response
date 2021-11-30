from modules.demo import *
import config

def main():
    if __name__ == '__main__':
        obj = demo()

        obj.GetResponseWeather(input('Podaj nazwe miasta '),config.x_rapidapi_key)


main()