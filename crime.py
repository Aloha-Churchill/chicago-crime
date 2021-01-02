from google.cloud import bigquery
import os
import numpy as np
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Toughbook/Downloads/My First Project-332dd775751a.json"

def graph(crimes_per_year):
    bucket_size = 5000
    buckets = bucket_size*np.arange(2,8)
    crimes_per_year_buckets = {i:[] for i in buckets}
    for num_crimes in crimes_per_year.values():
        key = min(j for j in buckets if j>num_crimes)
        crimes_per_year_buckets[key].append(num_crimes)

    frequencies = []
    for arr in crimes_per_year_buckets.values():
        frequencies.append(len(arr))

    plt.plot([10000,15000,20000,25000,30000,35000], frequencies)
    plt.show()


def main():
    client = bigquery.Client()

    query_job = client.query(
        """SELECT year, COUNT(year)
        FROM `bigquery-public-data.chicago_crime.crime`
        WHERE district = 4 
        GROUP by year
        """)

    results = query_job.result()

    crimes_per_year = {}
    for row in results:
        crimes_per_year[row[0]] = row[1]


    graph(crimes_per_year)


main()

