1. Before ingesting data into a pre-existing reporting structure, I would have a number of logistical and conceptual questions I would want to ask and discuss with my team.

   1. First, before doing any technical work, I would want to ensure that we have permission to use the new data. I would ask if the owner of the new data is aware that we are using it. Is this data open source? Are we being given this data by an outside stakeholder? Should we be taking extra security precautions when handling this data?
   2. Relatedly, I would be concerned with whether or not the new data is reliable and accurate. I would ask, how was this data collected in the first place? What was it's original use? Do we trust where this data is coming from?
   3. Next, it's important to check that the new data actually represents what we think it represents. For example, let's say the new data source contains data pertaining to voter turnout for a given election. If the data has a column named 'percent_turnout', we need to clarify what this actually means. Is this the percent of eligible voters who voted? Is this the percent of registered voters who voted? Is this percent in terms of fips, zip code, county, state, etc?
   4. As a data engineer, one major concern would be if the new data matches the pre-existing report structure. For example, does the new data have all of the pre-existing columns, or are certain columns missing? What transformations are needed to perform so that the data types and formats of the new and pre-existing data align?
   5. In order to make our jobs easier moving forward, I would want to know if we are able to injest this new data in an automated fashion. Can we access it via API? Do we need to download the new data manually? Will the data be available in 1 week, month, or year+?
   6. Finally, I would want to know if there is a way we can check ourselves before injesting new data into our database (for example, in a staging database). That way, we can write automated tests to ensure that our production database is always in good shape.

2.

3.
