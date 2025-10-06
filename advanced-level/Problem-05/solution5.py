from scipy.stats import pearsonr

x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]

corr, p_value = pearsonr(x, y)

print(f"Pearson correlation coefficient: {corr:.4f}")
print(f"P-value: {p_value:.4f}")
