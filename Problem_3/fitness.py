from compute_mean_risk_factor import compute_mean_risk_factor
from compute_investment_return import compute_investment_return


def fitness(chromosome):
    mean_risk_factor = compute_mean_risk_factor(chromosome)
    if mean_risk_factor >= 1.5:
        return 0
    amount_invested = sum(chromosome)
    if not (50000 <= amount_invested <= 80000):
        return 0
    investment_return = compute_investment_return(chromosome)
    return investment_return
