# performance-metrics
A django application to fetch a given performance metrics data from a Relational Database (PostgreSQL) via different use cases.

# REQUIREMENTS
1. Python 3.5
2. PostgreSQL 9.3.10

# API UseCases with Endpoints

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order
# /sales?search=total_clicks,total_impressions&filterBy=date__lte=2017-06-01&groupBy=channel,country&orderBy=clicks,desc

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
# /sales?search=total_installs,date&filterBy=os=ios,date__month=5,date__year=2017&groupBy=date&orderBy=date,asc

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order
# /sales?search=total_revenue,date&filterBy=country=US,date=2017-06-1&groupBy=os&orderBy=total_revenue,desc

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order
# /sales?search=total_spend,cpi&filterBy=country=CA&groupBy=channel&orderBy=cpi,desc
