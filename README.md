# Introduction
This small Python application has been designed to interact with https://www.cardmarket.com/en/Magic API, 
using the mkmsdk library.

I've never found a decent solution to updating my listed cards prices on cardmarket.com automatically, 
and having +500 cards listed manually changing the price was incredibly tedious. 
So, I figured I'd give the MKM API a try to update prices of card in stock 
automatically according to current price trends. 

In all likelihood, there are applications out there doing the exact same thing as this one and probably x100 better. 
But, feel free to use and mess with the code if you wish! 

This application is only meant for dedicated app tokens.

# How to use
First create a token for your magic cardmarket account. 
Go to **Home -> Account -> API Settings** and generate a new Dedicated App token. 

Next, create a new file called "token_config.yml" in the mlm-api-stock-manipulator folder. 
Copy the content in the example_config.yml file and fill in the blanks with your generated token details.

Now you can use main.py to update all your stock prices according to the pricelist. 
Current prices are updated to the average price in last 30 days. If a card is worth more than €5.00, 
the stock price update will be -€0.10.

# To Do
Create parsing for CLI arguments for more specificity regarding certain cards and price differences. 

