from utils import currency_rates
import sys

if __name__ == '__main__':
    print(currency_rates(sys.argv[1]))
    print(sys.argv)