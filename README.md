Issues in data:
Issue 1 – day_of_week encoding
  Raw : Sunday=6, Monday=0 (off by 1 vs pandas)
  Fix : Recomputed from timestamp → (pandas_dow + 1) % 7
Issue 2 – season encoding
  Raw : Non-standard sliding-window boundaries (~100k mismatches)
  Fix : Standard meteorological seasons (3-month blocks)
Issue 3 – discount not applied to total_price
  Raw : total_price ignores discount_applied rate
  Fix : Added discounted_price column (actual amount paid)
