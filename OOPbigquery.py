import pandas as pd
from google.cloud import bigquery  

class dataEx:
   def query(self):
       self.QUERY = """ 
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
   def queryId(self,id):
        client = bigquery.Client.from_service_account_json(id)
        self.query_job = client.query(self.QUERY) 
        
   def dataFrame(self):
       self.df = self.query_job.to_dataframe()
       
   def csvSave(self,data):
       self.df.to_csv(data, index = False, header = True)