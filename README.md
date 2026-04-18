# E-Commerce Customer Funnel Analysis

## Executive Summary
An e-commerce company is losing significant revenue due to low conversion rates. Using Python, MySQL, and Tableau, I analyzed 90,400 user sessions to track customers through the purchase funnel. After identifying that the largest revenue opportunity is to reduce drop-off between the Search and Payment pages, I recommend the following adjustments:

1. Simplify the payment page checkout process
2. Send reminder emails to users who abandon the search
3. Optimize the desktop experience
4. Add trust signals on the payment page

## Business Problem
Completed purchases are essential for e-commerce revenue. Stakeholders have noticed the conversion rate is much lower than expected. Out of 90,400 visitors,
only 452 complete a purchase — a 0.5% conversion rate. How can we determine where customers are dropping off and what product adjustments will increase conversion?

<img width="1350" height="813" alt="funnel_flowchart png " src="https://github.com/user-attachments/assets/dad7f7ec-57c1-4deb-80e9-187d8c48df17" />




## Methodology
1. Python script that loads, cleans, and transforms data from 5 raw CSV files
2. MySQL database to store funnel events and user data for SQL analysis
3. SQL queries to analyze conversion by stage, device, and gender
4. Tableau dashboard to visualize the funnel and revenue impact

## Skills
**Python:** Pandas, data cleaning, funnel calculation, revenue modeling

**MySQL:** Table creation, data loading, JOIN queries, CASE statements, aggregate functions

**Tableau:** Bar charts, color encoding, dashboard design, Tableau Public publishing

## Key Findings
- Overall conversion rate: **0.5%**
- Total revenue lost to drop-offs: **$4,497,400**
- Actual revenue generated: **$22,600**
- Biggest drop-off: Search Page → Payment Page (**87% loss**)
- Mobile converts **4x better** than Desktop (1.00% vs 0.25%)
- Female users convert slightly higher than Male (0.53% vs 0.47%)

## Results & Business Recommendation
This analysis identified that the e-commerce funnel loses $4.4M in potential revenue — primarily at the Search to Payment stage where 87% of users drop off.
SQL analysis revealed that mobile users convert at 4x the rate of desktop users, indicating a significant desktop experience problem. Improving the Search → Payment conversion
by just 10% would recover approximately **$195,850 in lost revenue.**

I recommend the following product adjustments:
1. Simplify the payment page — reduce form fields and unexpected costs
2. Add trust signals such as security badges and customer reviews on the payment page
3. Send automated reminder emails to users who reach search but don't proceed
4. Prioritize mobile optimization — desktop conversion is critically low at 0.25%

## Next Steps
1. A/B test a simplified one-page checkout
2. Implement email reminders for abandoned sessions
3. Measure impact of trust signals on payment page conversion

## Dashboard
[View Live Dashboard on Tableau Public](https://public.tableau.com/app/profile/rohan.thapa/viz/E-CommerceCustomerFunnelAnalysis/Dashboard1)

OR


<img width="2111" height="1207" alt="dashboard" src="https://github.com/user-attachments/assets/03f7e546-f93a-422e-b620-8612846a25d4" />


## Files
- `python/analyze_funnel.py` — funnel analysis and revenue calculation
- `python/load_mysql.py` — loads data into MySQL database
- `sql/funnel_queries.sql` — SQL queries for funnel, device, and gender analysis
- `data/funnel_results.csv` — cleaned funnel output
