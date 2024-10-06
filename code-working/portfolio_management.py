from itertools import permutations  
class Portfolio:  
    def __init__(self, assets, investments, total_risk, total_cost):  
        self.assets = assets  
        self.investments = investments  
        self.total_risk = total_risk  
        self.total_cost = total_cost  
        self.expected_return = self.calculate_expected_return()  
        self.risk_balance = self.calculate_risk_balance()  
    def calculate_expected_return(self):  
        # Calculate expected returns based on the selected assets  
        return sum(len(asset) for asset in self.assets)  # Example calculation  
    def calculate_risk_balance(self):  
        # Calculate risk balance based on total risk and investments  
        return self.total_risk - sum(len(inv) for inv in self.investments)  # Example calculation  
    def __repr__(self):  
        return f"Portfolio(assets={self.assets}, investments={self.investments}, " f"total_risk={self.total_risk}, total_cost={self.total_cost}, " f"expected_return={self.expected_return}, risk_balance={self.risk_balance})"


def generate_portfolios(assets, investments, max_risk, max_cost, current_portfolio=None, all_portfolios=None):  
    if current_portfolio is None:  
        current_portfolio = Portfolio([], [], 0, 0)  
    if all_portfolios is None:  
        all_portfolios = []  
    # Check if the current portfolio meets the constraints  
    if current_portfolio.total_risk <= max_risk and current_portfolio.total_cost <= max_cost:  
        all_portfolios.append(current_portfolio)  
    for i in range(len(assets)):  
        new_assets = assets[:i] + assets[i + 1:]  
        for j in range(len(investments)):  
            new_investments = investments[:j] + investments[j + 1:]  
            new_risk = current_portfolio.total_risk + len(assets[i])  # Example risk addition  
            new_cost = current_portfolio.total_cost + len(investments[j])  # Example cost addition  
            # Create a new portfolio with the added asset and investment  
            new_portfolio = Portfolio(current_portfolio.assets + [assets[i]],  
                                      current_portfolio.investments + [investments[j]],  
                                      new_risk,  
                                      new_cost)  
            # Recursive call  
            generate_portfolios(new_assets, new_investments, max_risk, max_cost, new_portfolio, all_portfolios)  
    return all_portfolios  
def rank_portfolios(portfolios):  
    # Rank portfolios based on a custom scoring function  
    def score(portfolio):  
        return portfolio.expected_return * 0.5 + portfolio.risk_balance * 0.5  # Example scoring function  
    return sorted(portfolios, key=score, reverse=True)  
selected_assets = ['Stocks', 'Bonds', 'Real Estate']  
selected_investments = ['Long-term', 'Short-term', 'Balanced']  
max_risk = 10  
max_cost = 15  
all_portfolios = generate_portfolios(selected_assets, selected_investments, max_risk, max_cost)  
ranked_portfolios = rank_portfolios(all_portfolios)  
for portfolio in ranked_portfolios:  
    print(portfolio)