# import datetime
# from collections import defaultdict, Counter
# from typing import List, Tuple

# def recommend_products(purchase_history: List[Tuple[int, str]], top_n: int = 10) -> List[int]:
#     """
#     Recommends the top products based on purchase frequency while applying a decay function 
#     to avoid over-recommending.
    
#     :param purchase_history: List of tuples containing product ID and timestamp.
#     :param top_n: Number of top products to recommend.
#     :return: List of recommended product IDs.
#     """
#     # Prepare data
#     purchases_within_month = defaultdict(list)
#     thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)

#     # Convert timestamps and filter purchases made within the last 30 days
#     for product_id, timestamp in purchase_history:
#         time_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
#         if time_obj >= thirty_days_ago:
#             purchases_within_month[product_id].append(time_obj)

#     # Count frequency while applying a decay based on how many times a single product is repeatedly purchased
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
        """Initialize decay rate, top N recommendations, and tracking dictionaries."""
        self.decay_rate = decay_rate
        self.top_n = top_n
        self.product_freq = defaultdict(int)  # Tracks overall product frequency
        self.user_product_history = defaultdict(list)  # Tracks each user's purchase history

    def update_purchases(self, purchases):
        """
        Updates product frequency and user purchase history for recent purchases.
        
        Args:
        - purchases (list): List of purchases with customer ID, product ID, and timestamp.
        """
        time_threshold = datetime.now() - timedelta(days=30)  # Last 30 days only
        for purchase in purchases:
            customer_id = purchase['customer_id']
            product_id = purchase['product_id']
            timestamp = purchase['timestamp']
            
            # Only add purchase if within 30-day window
            if timestamp >= time_threshold:
                self.product_freq[product_id] += 1
                self.user_product_history[customer_id].append((product_id, timestamp))

    def apply_decay(self):
        """
        Applies decay to reduce weight for frequently bought items by a single user.
        
        Returns:
        - Decayed product frequency.
        """
        time_threshold = datetime.now() - timedelta(days=30)  # Last 30 days only
        decayed_product_freq = defaultdict(int)
        
        for customer_id, history in self.user_product_history.items():
            product_count = defaultdict(int)
            
            # Count purchases for each product in the time frame
            for product_id, timestamp in history:
                if timestamp >= time_threshold:
                    product_count[product_id] += 1

            # Apply decay for each product in user's purchase history
            for product_id, count in product_count.items():
                decay_factor = np.exp(-self.decay_rate * count)  # Exponential decay
                decayed_product_freq[product_id] += decay_factor * self.product_freq[product_id]

        return decayed_product_freq

    def get_top_recommendations(self):
        """
        Returns top N products based on decayed product frequency.
        
        Returns:
        - List of top recommended products.
        """
        decayed_product_freq = self.apply_decay()
        # Sort products by frequency and return the top N
        top_recommendations = sorted(decayed_product_freq.items(), key=lambda x: x[1], reverse=True)[:self.top_n]
        return top_recommendations

# Example usage
purchases = [
    {'customer_id': 1, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=30)},
    {'customer_id': 1, 'product_id': 'B', 'timestamp': datetime.now() - timedelta(days=20)},
    {'customer_id': 1, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=10)},
    {'customer_id': 2, 'product_id': 'C', 'timestamp': datetime.now() - timedelta(days=25)},
    {'customer_id': 2, 'product_id': 'B', 'timestamp': datetime.now() - timedelta(days=15)},
    {'customer_id': 3, 'product_id': 'A', 'timestamp': datetime.now() - timedelta(days=5)},
]

# Instantiate and populate recommender with purchase data
recommender = ProductRecommender(decay_rate=0.1, top_n=10)
recommender.update_purchases(purchases)
top_recommendations = recommender.get_top_recommendations()
print("Top Recommendations:", top_recommendations)