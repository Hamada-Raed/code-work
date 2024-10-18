import numpy as np
from scipy.optimize import minimize

# Asset class to store asset data
class Asset:
    def __init__(self, name, expected_return, standard_deviation):
        if not name:
            raise ValueError("Asset name cannot be empty.")
        if not (-100 <= expected_return <= 100):
            raise ValueError("Expected return should be between -100% and 100%.")
        if not (0 <= standard_deviation <= 100):
            raise ValueError("Standard deviation should be between 0% and 100%.")
        
        self.name = name
        self.expected_return = expected_return / 100  # Convert to decimal
        self.standard_deviation = standard_deviation / 100  # Convert to decimal

# Portfolio class for holding assets and weights
class Portfolio:
    def __init__(self, assets, weights):
        self.assets = assets
        self.weights = np.array(weights)
    
    # Calculate expected portfolio return
    def expected_return(self):
        return np.sum([a.expected_return * w for a, w in zip(self.assets, self.weights)])

    # Calculate portfolio risk (variance)
    def portfolio_risk(self, cov_matrix):
        return np.sqrt(np.dot(self.weights.T, np.dot(cov_matrix, self.weights)))

# Function to get user input for assets
def get_asset_input():
    while True:
        try:
            asset_count = int(input("Enter the number of assets: "))
            if asset_count <= 0:
                raise ValueError("Number of assets must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    assets = []
    for i in range(asset_count):
        while True:
            try:
                name = input(f"\nAsset {i+1} Name: ").strip()
                expected_return = float(input(f"Expected Return (%) for {name}: "))
                std_deviation = float(input(f"Standard Deviation (%) for {name}: "))
                assets.append(Asset(name, expected_return, std_deviation))
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter valid asset information.")
    
    return assets

# Function to optimize portfolio using mean-variance optimization
def optimize_portfolio(assets, cov_matrix, target_return):
    asset_count = len(assets)
    initial_weights = np.ones(asset_count) / asset_count
    
    # Constraints: sum of weights = 1 and target return
    constraints = (
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},  # weights sum to 1
        {'type': 'eq', 'fun': lambda w: np.sum([w[i] * assets[i].expected_return for i in range(asset_count)]) - target_return}
    )
    
    # Bounds for each weight (0 <= weight <= 1)
    bounds = [(0, 1) for _ in range(asset_count)]
    
    # Objective function: Minimize portfolio variance (risk)
    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    # Optimize
    result = minimize(portfolio_variance, initial_weights, bounds=bounds, constraints=constraints)
    
    if result.success:
        return result.x  # Optimal weights
    else:
        raise Exception("Optimization failed")

# Generate the covariance matrix based on assets' standard deviations and correlations
def generate_cov_matrix(assets):
    asset_count = len(assets)
    cov_matrix = np.zeros((asset_count, asset_count))
    
    for i in range(asset_count):
        for j in range(asset_count):
            if i == j:
                cov_matrix[i, j] = assets[i].standard_deviation ** 2  # Variance on the diagonal
            else:
                # Assuming a fixed correlation of 0.5 for simplicity (in practice, you should calculate or provide it)
                cov_matrix[i, j] = 0.5 * assets[i].standard_deviation * assets[j].standard_deviation
    
    return cov_matrix

# Main program
try:
    assets = get_asset_input()

    while True:
        try:
            target_return = float(input("\nEnter target return (%): ")) / 100
            if not (-1 <= target_return <= 1):
                raise ValueError("Target return should be between -100% and 100%.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid target return.")
    
    # Generate covariance matrix
    cov_matrix = generate_cov_matrix(assets)

    # Optimize portfolio for the target return
    optimal_weights = optimize_portfolio(assets, cov_matrix, target_return)

    # Display results
    print("\nOptimized Portfolio Allocation:")
    for asset, weight in zip(assets, optimal_weights):
        print(f"{asset.name}: {weight * 100:.2f}%")

    # Calculate and display portfolio's expected return and risk
    optimized_portfolio = Portfolio(assets, optimal_weights)
    expected_return = optimized_portfolio.expected_return()
    risk = optimized_portfolio.portfolio_risk(cov_matrix)

    print(f"\nExpected Return: {expected_return * 100:.2f}%")
    print(f"Risk (Standard Deviation): {risk * 100:.2f}%")
    
except Exception as e:
    print(f"Error: {e}")
