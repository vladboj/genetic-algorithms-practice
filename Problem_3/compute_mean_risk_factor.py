# Each gene of the chromosome is an amount invested
def compute_mean_risk_factor(chromosome):
    x, y, z = [gene for gene in chromosome]
    return (x + 3 * y + 2 * z) / (x + y + z)
