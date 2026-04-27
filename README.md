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

 Exploratory Data Analysis
a) Sales Demand vs Time:Visible Trends

We plotted total quantity ordered every month across 2011–2012
Observation 1 (Trend): Orders in 2012 are clearly higher than 2011. Why? Because the platform was new in 2011 — as more people discovered the app and had good experiences, the user base kept growing naturally


b) Hourly, Daily and Seasonal Patterns

Observation 2 (Monthly): Orders peak around August–September 2012 and dip every December. Why? Summer means holidays, people outdoors, nobody wants to cook — so they order more. December is the opposite — cold weather, families cook at home, festive season reduces delivery demand
Observation 3 (Seasonal): Summer dominates with 2,16,731 total orders — more than DOUBLE Winter's 95,776. This directly tells us season must be a feature in our ML model because it alone can shift demand by over 1 lakh orders


c) Autocorrelation — Does one month affect the next?

Yes — a high sales month is almost always followed by another high month
ACF would show strong correlation at Lag 1 (previous month predicts current month) and Lag 12 (same month last year predicts this year)
This is exactly why we created lag features in the feature engineering step


d) Anomalies and Irregular Spikes

Observation 4 (Anomaly): A big negative spike appears in late 2011 in the residual graph — orders dropped ~4000 below what was expected for several months
Possible reasons: competitor launched, app outage, bad weather, price hike
Key insight: Our ML model MUST include weather and external features — otherwise it will predict normal demand even during crises


e) Decomposition — Trend, Seasonality, Residual

Trend: Smooth upward line from ~20,000 to ~41,000/month — proves the business is genuinely growing regardless of season
Seasonal: Same peaks and dips repeat every year like clockwork — summer always gets +2000 boost, winter always drops -1500 — model can learn this perfectly
Residual: Everything the trend and season can't explain — random shocks, surprise events. Late 2011 cluster of -4000 residuals = something went wrong outside normal patterns
