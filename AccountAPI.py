from pprint import pprint

import mkmsdk
import yaml
import os

from mkmsdk.mkm import Mkm
from mkmsdk.api_map import _API_MAP

class AccountAPI():

    def __init__(self, config_file):
        self.config_file = config_file

        with open(self.config_file) as oauth_details:
            token = yaml.load(oauth_details, Loader=yaml.FullLoader)

        os.environ['MKM_APP_TOKEN'] = token['app_token']
        os.environ['MKM_APP_SECRET'] = token['app_secret']
        os.environ['MKM_ACCESS_TOKEN'] = token['access_token']
        os.environ['MKM_ACCESS_TOKEN_SECRET'] = token['access_token_secret']

        self.mkm = Mkm(_API_MAP["2.0"]["api"], _API_MAP["2.0"]["api_root"])

    def get_entire_stock(self):
        return self.mkm.stock_management.get_stock().json()

    def delete_all_stock(self):
        stock = self.get_entire_stock()

        try:
            for article in stock['article']:
                article_id = article['idArticle']
                count = article['count']
                self.mkm.stock_management.delete_articles(data={"article": [{"idArticle": article_id, "count": count}]})
        except ConnectionError as ce:
            print(ce)

    def delete_article(self, article_id, count):
        try:
            self.mkm.stock_management.delete_articles(data={"article": [{"idArticle": article_id, "count": count}]})
        except mkmsdk.exceptions.ConnectionError as ce:
            print(ce)

    def get_product_avg_price(self, product_id):
        try:
            price_guide = self.mkm.market_place.product(product=product_id)
            return price_guide.json()['product']['priceGuide']['SELL']
        except mkmsdk.exceptions.ConnectionError as ce:
            print(ce)

        except mkmsdk.exceptions.ConnectionError:
            print("Something went wrong.")

    def update_stock_prices(self):
        stock = self.get_entire_stock()

        for article in stock["article"]:
            price = self.get_product_avg_price(article["idProduct"])
            if price > 5:
                new_price = price - .10
            else:
                new_price = price
            data = {'idArticle': article['idArticle'],
                    'idLanguage': article['language']['idLanguage'],
                    'comments': article['comments'],
                    'count': article['count'],
                    'price': new_price,
                    'condition': article['condition'],
                    'isFoil': False,
                    'isSigned': False,
                    'isPlayset': False}

            self.mkm.stock_management.change_articles(data={"article": [data]})

def main():
    aapi= AccountAPI("token_config.yml")
    aapi.update_stock_prices()

if __name__ == "__main__":
    main()
