# E-commerce marketplace data analysis

![](/olist_frontend.png)

## About Olist:
[Olist](https://olist.com/) is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services. Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

## Objective
To analyse Olist's dataset and answer the following question:
"How to increase customer satisfaction (so as to increase profit margin) while maintaining a healthy order volume?"



------------------------------------

Here are the seller and customer workflows:

## Seller:
- Seller joins Olist.
- Seller uploads products catalogue.
- Seller gets notified when a product is sold.
- Seller hands over an item to the logistic carrier.

👉 Note that multiple sellers can be involved in one customer order.


## Customer:
- Browses products on the marketplace.
- Purchases products from Olist.store.
- Gets an expected date for delivery.
- Receives the order.
- Leaves a review about the order.

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet.


## Dataset
The dataset consists of 100k orders from 2016 and 2018 that were made on the Olist store, available as a csv on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).


## Engineering
This scheme shows how the dataset was organised and linked so as to improve feature engineering and analysis. Therefore, multiple classes have been created to allow to import models from one file to another.

![](/data_model_olist.png)

NB: work in progress
