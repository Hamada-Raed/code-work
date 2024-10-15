class RecommendationSystem:
    def __init__(self, interaction_matrix, product_ratings):
        """
        Initialize the recommendation system with user-product interaction data and product ratings.
        
        Args:
            interaction_matrix (dict): A dictionary where keys are user IDs and values are lists of product IDs.
            product_ratings (dict): A dictionary where keys are product IDs and values are the average ratings.
        """
        self.interaction_matrix = interaction_matrix
        self.product_ratings = product_ratings

    def recommend_products(self, user_id, top_n=5):
        """
        Recommend top N products to a user based on their interaction history and product ratings.
        
        Args:
            user_id (int): The ID of the user for whom to generate recommendations.
            top_n (int): The number of products to recommend (default is 5).
        
        Returns:
            list: A list of recommended product IDs, sorted by rating.
        """
        if user_id not in self.interaction_matrix:
            raise ValueError(f"User {user_id} does not exist in the interaction matrix.")
        
        user_interacted_products = set(self.interaction_matrix[user_id])
        unviewed_products = {prod_id: rating for prod_id, rating in self.product_ratings.items()
                             if prod_id not in user_interacted_products}

        recommended_products = sorted(unviewed_products, key=unviewed_products.get, reverse=True)[:top_n]
        return recommended_products
