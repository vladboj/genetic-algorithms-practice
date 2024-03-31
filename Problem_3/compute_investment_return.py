def compute_investment_return(chromosome):
    investment_return = 0
    return_rates = [0.03, 0.04, 0.035]
    for i in range(3):
        investment_return += chromosome[i] * return_rates[i]
    return investment_return
