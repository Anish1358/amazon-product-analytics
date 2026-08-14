"""
Step 2: SQL Analysis (MySQL version)
"""

import pandas as pd
from sqlalchemy import create_engine, text

DB_USER = "student"
DB_PASSWORD = "student123"
DB_HOST = "localhost"
DB_NAME = "amazon_project"

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
df = pd.read_csv("amazon_cleaned.csv")

df.to_sql("products", engine, if_exists="replace", index=False, chunksize=500)
print(f"Loaded {len(df)} rows into MySQL table 'products'")

def run(title, query):
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    result = pd.read_sql_query(text(query), engine)
    print(result.to_string(index=False))
    return result

# 1. Top categories by estimated demand (price x review volume)
run("Top categories by estimated demand (price x review volume)", """
    SELECT main_category,
           ROUND(SUM(discounted_price * rating_count), 0) AS estimated_revenue,
           COUNT(*) AS num_products
    FROM products
    GROUP BY main_category
    ORDER BY estimated_revenue DESC
    LIMIT 10;
""")

# 2. Average discount by category
run("Average discount % by category", """
    SELECT main_category,
           ROUND(AVG(discount_percentage), 1) AS avg_discount_pct,
           COUNT(*) AS num_products
    FROM products
    GROUP BY main_category
    ORDER BY avg_discount_pct DESC
    LIMIT 10;
""")

# 3. Best-rated categories (minimum review volume so results aren't noisy)
run("Best-rated categories (min 1000 total reviews)", """
    SELECT main_category,
           ROUND(AVG(rating), 2) AS avg_rating,
           SUM(rating_count) AS total_reviews
    FROM products
    GROUP BY main_category
    HAVING SUM(rating_count) > 1000
    ORDER BY avg_rating DESC
    LIMIT 10;
""")

# 4. Red flag products: heavy discount but weak rating
run("Heavily discounted but poorly rated (possible quality issues)", """
    SELECT product_name, main_category, discount_percentage, rating, rating_count
    FROM products
    WHERE discount_percentage > 50 AND rating < 3.5
    ORDER BY discount_percentage DESC
    LIMIT 10;
""")

# 5. Price bucket distribution
run("Product count and average rating by price bucket", """
    SELECT price_bucket,
           COUNT(*) AS num_products,
           ROUND(AVG(rating), 2) AS avg_rating
    FROM products
    GROUP BY price_bucket
    ORDER BY num_products DESC;
""")

# 6. Top 10 highest-rated products with strong review volume
run("Top 10 highest-rated products (min 5000 reviews)", """
    SELECT product_name, main_category, rating, rating_count, discounted_price
    FROM products
    WHERE rating_count > 5000
    ORDER BY rating DESC, rating_count DESC
    LIMIT 10;
""")

print("\nDone. Data now lives in MySQL database 'amazon_project', table 'products'.")
print("You can also inspect it with MySQL Workbench or the mysql CLI.")