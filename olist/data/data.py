import os
import pandas as pd


class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Keys = 'sellers', 'orders', 'order_items' etc...
        Values = pandas.DataFrame loaded from csv files
        """
        path = os.path.dirname(os.getcwd())
        path_2 = os.path.dirname(path)
        path_3 = os.path.join(path_2, 'data', 'csv')
        
        file_names = [file_name for file_name in os.listdir(path_3) if file_name.endswith('.csv')]

        key_names = [i.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '') for i in file_names if i.endswith('.csv')]
        data = {}
        for key, values in zip(key_names, file_names):
            df = pd.read_csv(os.path.join(path_3, values))
            data[key] = df
        
        return data
        

    def get_matching_table(self):
        """
        This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        data = Olist().get_data()
        orders = data['orders'][['order_id', 'customer_id']]
        items = data['order_items'][['order_id', 'product_id', 'seller_id']]
        reviews = data['order_reviews'][['order_id', 'review_id']]
        matching_table = orders.merge(items, how='outer', on='order_id').merge(reviews, how='outer', on='order_id')
        
        return matching_table


    def ping(self):
        """
        Test: you call ping I print pong.
        """
        print('pong')
