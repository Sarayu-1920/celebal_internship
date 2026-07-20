-- Basic queries

-- 1. Total Revenue Per Category

SELECT
    p.category,
    ROUND(SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ),2) AS total_revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 2. Top 10 Customers

SELECT
    c.customer_id,
    c.customer_name,
    ROUND(SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent/100.0)
    ),2) AS total_order_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_id,c.customer_name
ORDER BY total_order_value DESC
LIMIT 10;

-- 3. Month-wise Order Count

SELECT
    strftime('%Y-%m',order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY month
ORDER BY month DESC
LIMIT 12;

--Intermediate queries


-- 4. Customers Who Never Had Delivered Orders

SELECT DISTINCT
    c.customer_id,
    c.customer_name
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_id,c.customer_name
HAVING SUM(
CASE
WHEN o.status='DELIVERED'
THEN 1
ELSE 0
END
)=0;

-- 5. Products With More Returns Than Purchases

SELECT
    p.product_id,
    p.product_name,
    SUM(CASE WHEN o.status='RETURNED' THEN oi.quantity ELSE 0 END) AS returned_items,
    SUM(CASE WHEN o.status='DELIVERED' THEN oi.quantity ELSE 0 END) AS purchased_items
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
JOIN orders o
ON oi.order_id=o.order_id
GROUP BY p.product_id,p.product_name
HAVING
    SUM(CASE WHEN o.status='RETURNED' THEN oi.quantity ELSE 0 END)
    >
    SUM(CASE WHEN o.status='DELIVERED' THEN oi.quantity ELSE 0 END);

-- 6. Return Rate Per Category

SELECT
    p.category,

    SUM(
        CASE
            WHEN o.status = 'RETURNED'
            THEN oi.quantity
            ELSE 0
        END
    ) AS returned_quantity,

    SUM(oi.quantity) AS total_quantity,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN o.status = 'RETURNED'
                THEN oi.quantity
                ELSE 0
            END
        ) /
        SUM(oi.quantity),
        2
    ) AS return_rate

FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN orders o
ON oi.order_id = o.order_id

GROUP BY p.category;



-- Advanced Queries (Window Functions, CTEs, Subqueries)

-- 7. Running Revenue

WITH daily_revenue AS (

SELECT
    o.region_code,
    DATE(o.order_date) AS order_date,

    SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_percent / 100.0)
    ) AS daily_revenue

FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id

GROUP BY
    o.region_code,
    DATE(o.order_date)

)

SELECT
    region_code,
    order_date,
    daily_revenue,

    SUM(daily_revenue) OVER (
        PARTITION BY region_code
        ORDER BY order_date
    ) AS running_total

FROM daily_revenue
ORDER BY region_code, order_date;


-- 8. Ranking with DENSE_RANK

SELECT
    category,
    product_name,
    total_revenue,
    DENSE_RANK() OVER (
        PARTITION BY category
        ORDER BY total_revenue DESC
    ) AS rank_in_category
FROM (
    SELECT
        p.category,
        p.product_name,
        ROUND(SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_percent / 100.0)
        ), 2) AS total_revenue
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    GROUP BY p.category, p.product_name
)
ORDER BY category, rank_in_category;

-- 9. LAG/LEAD Analysis

WITH order_history AS (

SELECT
    customer_id,
    order_date,

    LAG(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_date

FROM orders

),

order_gap AS (

SELECT
    customer_id,
    order_date,
    previous_order_date,

    julianday(order_date) -
    julianday(previous_order_date) AS days_gap

FROM order_history

)

SELECT
    customer_id,
    order_date,
    previous_order_date,
    ROUND(days_gap,0) AS days_gap,

    CASE
        WHEN AVG(days_gap)
             OVER(PARTITION BY customer_id) > 30
        THEN 'At Risk'
        ELSE 'Active'
    END AS customer_status

FROM order_gap;

-- 10. Monthly Customer Category

WITH monthly_revenue AS (

SELECT
customer_id,
strftime('%Y-%m',order_date) AS month,

SUM(
quantity*unit_price*(1-discount_percent/100.0)
) AS revenue

FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id

GROUP BY customer_id,month

),

customer_category AS (

SELECT *,

CASE

WHEN revenue>10000 THEN 'High'
WHEN revenue>=5000 THEN 'Medium'
ELSE 'Low'

END AS customer_type

FROM monthly_revenue

)

SELECT

month,
customer_type,
COUNT(*) customers

FROM customer_category

GROUP BY month,customer_type;

-- 11. Customer Quartiles

WITH customer_revenue AS (
    SELECT
        c.customer_id,
        c.customer_name,
        ROUND(
            SUM(
                oi.quantity * oi.unit_price *
                (1 - oi.discount_percent / 100.0)
            ),
            2
        ) AS total_revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.customer_name
),
ranked AS (
    SELECT
        customer_id,
        customer_name,
        total_revenue,
        NTILE(4) OVER (ORDER BY total_revenue DESC) AS quartile
    FROM customer_revenue
)

SELECT
    customer_id,
    customer_name,
    total_revenue,
    quartile,
    CASE quartile
        WHEN 1 THEN 'Platinum'
        WHEN 2 THEN 'Gold'
        WHEN 3 THEN 'Silver'
        ELSE 'Bronze'
    END AS quartile_label
FROM ranked
ORDER BY total_revenue DESC;



-- 12. Year-over-Year  Revenue Comparision

WITH monthly_revenue AS
(
SELECT strftime('%Y',o.order_date) AS year,
strftime('%m',o.order_date) AS month,
ROUND(SUM(
oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)
),2) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY year, month
)

SELECT year,
month,
total_revenue,
LAG(total_revenue,12) OVER(ORDER BY year,month) AS prev_year_revenue,
ROUND(
100.0*(total_revenue - LAG(total_revenue,12) OVER(ORDER BY year,month))
/ LAG(total_revenue,12) OVER(ORDER BY year,month)
,2) AS yoy_growth_percent
FROM monthly_revenue
ORDER BY year, month;


-- 13. First & Last Purchased Category

WITH purchases AS (

SELECT

o.customer_id,

p.category,

o.order_date,

ROW_NUMBER() OVER(
PARTITION BY customer_id
ORDER BY order_date
) first_order,

ROW_NUMBER() OVER(
PARTITION BY customer_id
ORDER BY order_date DESC
) last_order

FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
JOIN products p
ON oi.product_id=p.product_id

)

SELECT

customer_id,

MAX(CASE WHEN first_order=1 THEN category END) first_category,

MAX(CASE WHEN last_order=1 THEN category END) last_category,

CASE

WHEN
MAX(CASE WHEN first_order=1 THEN category END)=
MAX(CASE WHEN last_order=1 THEN category END)

THEN 'No'

ELSE 'Yes'

END category_shift

FROM purchases

GROUP BY customer_id;

-- 14. Revenue Distribution

WITH customer_revenue AS
(
SELECT c.customer_id,
ROUND(SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)),2) AS revenue
FROM customers c
JOIN orders o ON c.customer_id=o.customer_id
JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY c.customer_id
)

SELECT customer_id,
revenue,
SUM(revenue) OVER(ORDER BY revenue DESC) AS cumulative_revenue,
ROUND(
100.0*SUM(revenue) OVER(ORDER BY revenue DESC)
/ SUM(revenue) OVER()
,2) AS cumulative_percent
FROM customer_revenue
ORDER BY revenue DESC;

-- 15. Complex CTE: Cohort Analysis

WITH cohort AS (

    SELECT
        customer_id,
        strftime('%Y-%m', registration_date) AS cohort_month
    FROM customers

),

customer_orders AS (

    SELECT
        c.customer_id,
        c.cohort_month,
        strftime('%Y-%m', o.order_date) AS order_month,

        (
            (CAST(strftime('%Y', o.order_date) AS INTEGER) -
             CAST(strftime('%Y', c.cohort_month || '-01') AS INTEGER)) * 12
            +
            (CAST(strftime('%m', o.order_date) AS INTEGER) -
             CAST(strftime('%m', c.cohort_month || '-01') AS INTEGER))
        ) AS month_number

    FROM cohort c
    JOIN orders o
    ON c.customer_id = o.customer_id

),

cohort_size AS (

    SELECT
        cohort_month,
        COUNT(DISTINCT customer_id) AS total_customers
    FROM cohort
    GROUP BY cohort_month

),

cohort_activity AS (

    SELECT
        cohort_month,
        month_number,
        COUNT(DISTINCT customer_id) AS active_customers
    FROM customer_orders
    WHERE month_number BETWEEN 0 AND 3
    GROUP BY cohort_month, month_number

)

SELECT
    ca.cohort_month,
    ca.month_number,
    ca.active_customers,
    cs.total_customers,
    ROUND(100.0 * ca.active_customers / cs.total_customers, 2) AS retention_rate

FROM cohort_activity ca
JOIN cohort_size cs
ON ca.cohort_month = cs.cohort_month

ORDER BY ca.cohort_month, ca.month_number;

-- 16. Self-Join with Window Function

SELECT
    a.product_id AS product_a,
    b.product_id AS product_b,
    COUNT(*) AS times_bought_together

FROM order_items a
JOIN order_items b
ON a.order_id = b.order_id
AND a.product_id < b.product_id

GROUP BY a.product_id, b.product_id
ORDER BY times_bought_together DESC;