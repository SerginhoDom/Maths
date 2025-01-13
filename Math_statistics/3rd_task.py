import numpy as np
import matplotlib.pyplot as plt

lambda_values = [10.0]

lambda_estimates = []

fig, axs = plt.subplots(3, 2, figsize=(12, 15))

colors = ['red', 'blue', 'green', 'purple']

for i, lambda_param in enumerate(lambda_values):
    lambda_estimates = []

    for n in range(1, 1001):
        sample = np.random.exponential(scale=1/lambda_param, size=n)
        mean_x = np.mean(sample)
        median_x = np.median(sample)
        log_2_median_x = np.log(2) / median_x
        inverse_mean_x = 1 / mean_x
        log_n_over_n_plus_mean_x = 1 / ((np.log(n) / n) + mean_x)
        lambda_estimates.append([mean_x, log_2_median_x, inverse_mean_x, log_n_over_n_plus_mean_x])
    for j in range(4):
        axs[j // 2, j % 2].plot(range(1, 1001), [est[j] for est in lambda_estimates], label=f'λ = {lambda_param}', color=colors[j])
        axs[j // 2, j % 2].set_xlabel('Sample Size')
        axs[j // 2, j % 2].set_ylabel('Lambda Estimate')
        axs[j // 2, j % 2].set_title(f'Estimation Method {j+1}')
        axs[j // 2, j % 2].legend()

for j in range(4):
    axs[2, 1].plot(range(1, 1001), [est[j] for est in lambda_estimates], label=f'Estimation Method {j+1}', color=colors[j])
    axs[2, 1].set_xlabel('Sample Size')
    axs[2, 1].set_ylabel('Lambda Estimate')
    axs[2, 1].set_title('All Estimation Methods')
    axs[2, 1].legend()

plt.tight_layout()
plt.show()