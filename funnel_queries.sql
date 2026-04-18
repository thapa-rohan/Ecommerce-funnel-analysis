USE funnel_db;

-- Query 1: Funnel drop-off by stage
SELECT 
    stage,
    COUNT(DISTINCT user_id) as users,
    ROUND(COUNT(DISTINCT user_id) * 100.0 / 
        (SELECT COUNT(DISTINCT user_id) FROM funnel_events WHERE stage = 'homepage'), 2) as conversion_rate
FROM funnel_events
GROUP BY stage
ORDER BY users DESC;

-- Query 2: Conversion rate by device
SELECT 
    u.device,
    COUNT(DISTINCT u.user_id) as total_users,
    COUNT(DISTINCT CASE WHEN f.stage = 'purchase' THEN f.user_id END) as purchasers,
    ROUND(COUNT(DISTINCT CASE WHEN f.stage = 'purchase' THEN f.user_id END) * 100.0 / 
        COUNT(DISTINCT u.user_id), 2) as conversion_rate
FROM users u
LEFT JOIN funnel_events f ON u.user_id = f.user_id
GROUP BY u.device
ORDER BY conversion_rate DESC;

-- Query 3: Conversion rate by gender
SELECT 
    u.sex,
    COUNT(DISTINCT u.user_id) as total_users,
    COUNT(DISTINCT CASE WHEN f.stage = 'purchase' THEN f.user_id END) as purchasers,
    ROUND(COUNT(DISTINCT CASE WHEN f.stage = 'purchase' THEN f.user_id END) * 100.0 / 
        COUNT(DISTINCT u.user_id), 2) as conversion_rate
FROM users u
LEFT JOIN funnel_events f ON u.user_id = f.user_id
GROUP BY u.sex
ORDER BY conversion_rate DESC;