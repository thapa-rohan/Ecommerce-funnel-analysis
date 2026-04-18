# E-Commerce Customer Funnel Analysis

## Business Problem
An e-commerce company is losing significant revenue due to low conversion rates. 
Out of 90,400 website visitors, only 452 complete a purchase — a 0.5% conversion rate. 
This analysis identifies exactly where customers drop off and quantifies the revenue impact.

## Tools Used
- **Python & Pandas** — data cleaning and funnel analysis
- **MySQL** — data storage and SQL querying
- **Tableau** — interactive dashboard visualization

## Key Findings
- Overall conversion rate: **0.5%**
- Total revenue lost to drop-offs: **$4,497,400**
- Actual revenue generated: **$22,600**
- Biggest drop-off: Search Page → Payment Page (**87% drop**)
- Mobile converts **4x better** than Desktop (1.00% vs 0.25%)
- Female users convert slightly higher than Male (0.53% vs 0.47%)

## Recommendations
1. Simplify the payment page to reduce the 87% drop-off
2. Optimize the desktop experience — mobile converts 4x better
3. Send reminder emails to users who reach search but don't proceed to payment
4. Add trust signals (security badges, reviews) on the payment page

## Business Impact
Improving the Search → Payment conversion by just 10% would recover approximately **$195,850 in lost revenue**

## Dashboard
[View Live Dashboard on Tableau Public]((https://public.tableau.com/app/profile/rohan.thapa/viz/E-CommerceCustomerFunnelAnalysis/Dashboard1))

## Files
- `python/analyze_funnel.py` — funnel analysis and revenue calculation
- `sql/funnel_queries.sql` — SQL queries for funnel, device, and gender analysis
- `data/funnel_results.csv` — cleaned funnel output
