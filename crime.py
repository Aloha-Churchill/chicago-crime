from google.cloud import bigquery
import os
import numpy as np
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Toughbook/Downloads/My First Project-332dd775751a.json"

def graph(crimes_per_year):
    bucket_size = 1000
    buckets = bucket_size*np.arange(10,60)

    crimes_per_year_buckets = {i:[] for i in buckets}
    for num_crimes in crimes_per_year.values():
        key = min(j for j in buckets if j>num_crimes)
        crimes_per_year_buckets[key].append(num_crimes)

    frequencies = []
    for arr in crimes_per_year_buckets.values():
        frequencies.append(len(arr))

    plt.bar(np.arange(len(crimes_per_year_buckets.keys())), frequencies)
    plt.show()


def main():
    client = bigquery.Client()

    query_job = client.query(
        """SELECT year, EXTRACT(MONTH from date), count(EXTRACT(MONTH from date))
        FROM `bigquery-public-data.chicago_crime.crime`
        GROUP by year, EXTRACT(MONTH from date)
        """)

    results = query_job.result()

    occurences_per_month = {}
    for row in results:
        occurences_per_month[(row[0],row[1])] = row[2]
        #print(row)

    #WHERE district = 16
    graph(occurences_per_month)


main()

