import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Seed for reproducibility ---
rng = np.random.default_rng(42)

# --- Synthetic, realistic customer spend data ---
segments = ["Budget", "Value", "Regular", "Premium", "VIP"]
sizes =     [800,       1000,    1200,      900,       600]

# Log-normal-like spend per segment (heavier tails, higher central tendency for higher tiers)
means =     [3.2, 3.5, 3.9, 4.4, 4.8]   # log-space means
sigmas =    [0.45, 0.5, 0.55, 0.6, 0.65]

records = []
for seg, n, mu, sigma in zip(segments, sizes, means, sigmas):
    # Base spend (lognormal)
    base = rng.lognormal(mean=mu, sigma=sigma, size=n)
    # Add a small fraction of high-ticket outliers per segment
    n_out = max(3, int(0.01 * n))
    outliers = rng.lognormal(mean=mu + 1.4, sigma=sigma + 0.2, size=n_out)
    spend = np.concatenate([base, outliers])
    # Clip extreme values to keep plot readable (simulate reporting caps)
    spend = np.clip(spend, 5, 10000)
    # Convert to dollars (already positive), round to cents
    spend = np.round(spend, 2)
    records.extend([{"segment": seg, "purchase_amount": float(x)} for x in spend])

df = pd.DataFrame.from_records(records)

# --- Seaborn styling for publication ---
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-friendly sizing

# --- Figure and boxplot ---
plt.figure(figsize=(8, 8))  # ensures 512x512 at dpi=64
ax = sns.boxplot(
    data=df,
    x="segment",
    y="purchase_amount",
    palette="Set2",
    width=0.6,
    fliersize=2.5,
    linewidth=1.5
)

# Labels & title
ax.set_title("Purchase Amount Distribution by Customer Segment", pad=14, weight="bold")
ax.set_xlabel("Customer Segment")
ax.set_ylabel("Purchase Amount (USD)")

# Ticks formatting
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y')

# Optional y-axis upper limit for presentation readability
# ax.set_ylim(0, np.percentile(df["purchase_amount"], 99.5) * 1.1)

# Tight layout and save 512x512
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
