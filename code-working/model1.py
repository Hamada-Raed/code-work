import numpy as np
import pandas as pd
from scipy.optimize import minimize

def get_user_input():
    num_assets = int(input("Enter the number of assets: "))
    asset_names = []
    expected_returns = []
    historical_data = []
    
    for i in range(num_assets):
        name = input(f"Enter the name of asset {i+1}: ")
        asset_names.append(name)
        
        expected_return = float(input(f"Enter the expected return for {name}: "))
        expected_returns.append(expected_return)
        
        historical = input(f"Enter historical performance data for {name} (comma-separated): ")
        historical_data.append(list(map(float, historical.split(','))))
    
    return asset_names, np.array(expected_returns), np.array(historical_data)

def calculate_covariance_matrix(historical_data):
    return np.cov(historical_data)

def portfolio_optimization(expected_returns, covariance_matrix):
    num_assets = len(expected_returns)
    
    def portfolio_variance(weights):
        return weights.T @ covariance_matrix @ weights
    
    def portfolio_return(weights):
        return np.dot(weights, expected_returns)
    
    def objective_function(weights):
        return portfolio_variance(weights) - portfolio_return(weights)
    
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))
    initial_guess = num_assets * [1. / num_assets]
    
    result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.x

def main():
    asset_names, expected_returns, historical_data = get_user_input()
    covariance_matrix = calculate_covariance_matrix(historical_data)
    
    optimal_weights = portfolio_optimization(expected_returns, covariance_matrix)
    
    print("\nOptimal Portfolio Allocation:")
    for name, weight in zip(asset_names, optimal_weights):
        print(f"{name}: {weight:.2%}")

if __name__ == "__main__":
    main()