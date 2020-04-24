# Introduction
This small Python application has been designed to interact with https://www.cardmarket.com/en/Magic API, using the mkmsdk library.

I've always had the problem of never finding an easy way to update my listed cards prices on cardmarket.com automatically. And having +500 cards listed, manually changing the price was incredibly tedious. So, I figured I'd give the API a try to update the prices automatically. 

This application is only meant for dedicated app tokens.

# How to use
First create a token for your magic cardmarket account. 
Go to Home -> Account -> API Settings and generate a new Dedicated App token. 

Next, create a new file called "token_config.yml" in the mlm-api-stock-manipulator folder. 
Copy the contect in the example_config.yml file and fill in the info with your generated token details.

Now you can use main.py to update all your stock prices according to the pricelist (-€0.10 if a card is more than €5.00).

# To Do
Create parsing for CLI arguments for more specificity regarding certain cards and price differences. 

