
import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta
import numpy as np

class FinancialProductRecommender:
    def __init__(self, decay_rate=0.1, top_n=10):
        self.decay_rate = decay_rate
        self.top_n = top_n
        self.product_freq = defaultdict(int)  
        self.customer_transaction_history = defaultdict(list)  

    def update_transactions(self, transactions):
        time_threshold = datetime.now() - timedelta(days=30)  
        
        for transaction in transactions:
            customer_id = transaction['customer_id']
            product_id = transaction['product_id']  
            timestamp = transaction['timestamp']
            
            if timestamp >= time_threshold:
                self.product_freq[product_id] += 1
                self.customer_transaction_history[customer_id].append((product_id, timestamp))

    def apply_decay(self):
        time_threshold = datetime.now() - timedelta(days=30)
        decayed_product_freq = defaultdict(int)

        for customer_id, history in self.customer_transaction_history.items():
            product_count = defaultdict(int)
            
            for product_id, timestamp in history:
                if timestamp >= time_threshold:
                    product_count[product_id] += 1  

            for product_id, count in product_count.items():
                decay_factor = np.exp(-self.decay_rate * count)  
                decayed_product_freq[product_id] += decay_factor * self.product_freq[product_id]

        return decayed_product_freq

    def get_top_recommendations(self):
        decayed_product_freq = self.apply_decay()
        top_recommendations = sorted(decayed_product_freq.items(), key=lambda x: x[1], reverse=True)[:self.top_n]
        return top_recommendations

transactions = [
    {'customer_id': 1, 'product_id': 'CreditCard_A', 'timestamp': datetime.now() - timedelta(days=30)},
    {'customer_id': 1, 'product_id': 'Loan_B', 'timestamp': datetime.now() - timedelta(days=20)},
    {'customer_id': 1, 'product_id': 'CreditCard_A', 'timestamp': datetime.now() - timedelta(days=10)},
    {'customer_id': 2, 'product_id': 'Investment_C', 'timestamp': datetime.now() - timedelta(days=25)},
    {'customer_id': 2, 'product_id': 'Loan_B', 'timestamp': datetime.now() - timedelta(days=15)},
    {'customer_id': 3, 'product_id': 'CreditCard_A', 'timestamp': datetime.now() - timedelta(days=5)},
]

recommender = FinancialProductRecommender(decay_rate=0.1, top_n=10)
recommender.update_transactions(transactions)

top_recommendations = recommender.get_top_recommendations()
print("Top Financial Product Recommendations:", top_recommendations)

