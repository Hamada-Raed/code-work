# import datetime
# from collections import defaultdict, Counter
# from typing import List, Tuple

# def recommend_products(purchase_history: List[Tuple[int, str]], top_n: int = 10) -> List[int]:
#     purchases_within_month = defaultdict(list)
#     thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)

#     for product_id, timestamp in purchase_history:
#         time_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
#         if time_obj >= thirty_days_ago:
#             purchases_within_month[product_id].append(time_obj)

#     product_weights = {}
#     decay_factor = 0.9

#     for product_id, times in purchases_within_month.items():
#         frequency = len(times)
#         # Apply decay function: Reduce weight based on frequency (e.g., frequency ** decay_factor)
#         # This reduces the weight as frequency becomes higher
#         product_weights[product_id] = frequency ** decay_factor

#     # Sort products by their weights
#     sorted_products = sorted(product_weights.items(), key=lambda x: x[1], reverse=True)

#     # Return the top_n product IDs
#     top_recommended_products = [product_id for product_id, _ in sorted_products[:top_n]]

#     return top_recommended_products


# # Example usage
# purchase_history_example = [
#     (1, "2023-09-25 08:45:00"),
#     (2, "2023-09-26 09:15:00"),
#     (1, "2023-09-27 10:20:00"),
#     (3, "2023-09-28 11:45:00"),
#     (2, "2023-09-28 12:00:00"),
#     (4, "2023-09-29 13:30:00"),
#     (1, "2023-09-30 14:00:00"),
#     (4, "2023-09-29 13:30:00"),
#     (1, "2023-09-30 14:00:00"),
#     (4, "2023-09-29 13:30:00"),
#     (1, "2023-09-30 14:00:00"),
#     (4, "2023-09-29 13:30:00"),
#     (1, "2023-09-30 14:00:00"),
# ]

# # Get the top product recommendations
# top_recommendations = recommend_products(purchase_history_example, top_n=3)
# print(top_recommendations) 


import pandas as pd
from collections import defaultdict
from datetime import datetime, timedelta
import numpy as np


class ProductRecommender:
    def __init__(self, decay_rate=0.1, top_n=10):
        self.decay_rate = decay_rate
        self.top_n = top_n
        self.product_freq = defaultdict(int)  
        self.user_product_history = defaultdict(list)  

    def update_purchases(self, purchases):
        
        time_threshold = datetime.now() - timedelta(days=30) 
        for purchase in purchases:
            customer_id = purchase['customer_id']
            product_id = purchase['product_id']
            timestamp = purchase['timestamp']
            
            if timestamp >= time_threshold:
                self.product_freq[product_id] += 1
                self.user_product_history[customer_id].append((product_id, timestamp))

    def apply_decay(self):
        time_threshold = datetime.now() - timedelta(days=30)  
        decayed_product_freq = defaultdict(int)
        
        for customer_id, history in self.user_product_history.items():
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

purchases = [
    {'customer_id': 1, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=30)},
    {'customer_id': 1, 'product_id': 'B', 'timestamp': datetime.now() - timedelta(days=20)},
    {'customer_id': 1, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=10)},
    {'customer_id': 2, 'product_id': 'C', 'timestamp': datetime.now() - timedelta(days=25)},
    {'customer_id': 2, 'product_id': 'B', 'timestamp': datetime.now() - timedelta(days=15)},
    {'customer_id': 3, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=5)},
]

recommender = ProductRecommender(decay_rate=0.1, top_n=10)
recommender.update_purchases(purchases)
top_recommendations = recommender.get_top_recommendations()
print("Top Recommendations:", top_recommendations)