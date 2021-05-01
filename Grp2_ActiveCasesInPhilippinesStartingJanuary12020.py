import pandas as pd
from google.cloud import bigquery  

QUERY = """ 
    WITH
        country_pop AS (
        SELECT
            country_code AS iso_3166_1_alpha_3,
            year_2018 AS population_2018
        FROM
            `bigquery-public-data.world_bank_global_population.population_by_country`)
    SELECT
        date
        country_code,
        country_name,
        cumulative_confirmed,
        cumulative_deceased,
        cumulative_recovered,
        cumulative_confirmed-cumulative_recovered-cumulative_deceased AS active_cases
    FROM
        `bigquery-public-data.covid19_open_data.covid19_open_data`
    JOIN
        country_pop
    USING
        (iso_3166_1_alpha_3)
    WHERE
        country_code = 'PH'
        AND aggregation_level = 0
    ORDER BY
        date
    """

client = bigquery.Client.from_service_account_json( 'Covid-2e75a41f090d.json') 

query_job = client.query(QUERY) 

df = query_job.to_dataframe() 

print ("Records Returned: ", df.shape ) 
print () 
print ("First 100 Records") 
print (df.head(100))

df.to_csv(r'Grp6_ActiveCasesInPhilippinesStartingJanuary12020.csv', index = False, header = True)
