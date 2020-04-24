from AccountAPI import AccountAPI


def main():
    aapi = AccountAPI("token_config.yml")
    stock = aapi.get_entire_stock()['article']
    aapi.update_stock_prices(stock)


if __name__ == "__main__":
    main()
