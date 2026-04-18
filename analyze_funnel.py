import pandas as pd

# Load all tables
home = pd.read_csv('data/home_page_table.csv')
search = pd.read_csv('data/search_page_table.csv')
payment = pd.read_csv('data/payment_page_table.csv')
confirmation = pd.read_csv('data/payment_confirmation_table.csv')
users = pd.read_csv('data/user_table.csv')

# Count users at each stage
home_count = home['user_id'].nunique()
search_count = search['user_id'].nunique()
payment_count = payment['user_id'].nunique()
confirmation_count = confirmation['user_id'].nunique()

# Average order value assumption
AOV = 50  # $50 per order

# Build funnel
funnel = {
    'Stage': ['Homepage', 'Search Page', 'Payment Page', 'Purchase'],
    'Users': [home_count, search_count, payment_count, confirmation_count]
}

df_funnel = pd.DataFrame(funnel)
df_funnel['Conversion_Rate'] = (df_funnel['Users'] / home_count * 100).round(2)
df_funnel['Drop_Off'] = df_funnel['Users'].diff(-1).fillna(0).astype(int)
df_funnel['Revenue_Lost'] = (df_funnel['Drop_Off'] * AOV).astype(int)
df_funnel['Potential_Revenue'] = (df_funnel['Users'] * AOV).astype(int)

print(df_funnel)
print(f"\nOverall conversion rate: {round(confirmation_count/home_count*100, 2)}%")
print(f"Total revenue lost to drop-offs: ${df_funnel['Revenue_Lost'].sum():,}")
print(f"Actual revenue generated: ${confirmation_count * AOV:,}")

# Save
df_funnel.to_csv('data/funnel_results.csv', index=False)
print("\nSaved funnel_results.csv!")