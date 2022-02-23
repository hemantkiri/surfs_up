# surfs_up

# Overview of the statistical analysis:
The purpose of the analysis is well defined, W. Avy  wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

# Results:
First Design a query to retrieve the last 12 months of precipitation data starting from the last data point in the database for timeframe 2016-08-23 to 2017-08-23.  We found out number of stations total 9, then we determine the most active station “USC00519281” with counts 2772. Here we complete using jupter notebook.

Now using Visual Studio Code and Terminal to create tables for month of June and December temperature.
In order to connect to the SQLite database, we have use SQLAlchemy Object Relational Mapper (ORM).
ORM allows us to create classes in our code that can be mapped to specific tables in a given database.
This allows us to create a special type of system called a decoupled system.

Here is temperature report for the month of June and December per given database.

# Month     Count   mean      std     min   25%   50%   75%   max
# June      1700    74.944    3.357   64    73    75    77    85
# December  1517    71.041    3.745   56    69    71    74    83

After looking at the tables for the month of June and December reports ‘mean’(average) temperature is around 70 degrees.
The report also notify similar temperatures for both months.(min., max., std,…).

# Summary:
Throughout the year temperature does not change much which gives an opportunity to W.Avy to start the business in Oahu for surf and ice cream shop.
To be sure it is not bad idea to look at the near by location station report.

