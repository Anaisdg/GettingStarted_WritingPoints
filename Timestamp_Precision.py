
import pandas as pd
# import csv
df = pd.read_csv('data/BTC.csv')
df.head()
# convert minute precision to nanosecond precision
df["time"] = [str(df["time"][t]) + "000000000" for t in range(len(df))]
df.head()
# export as csv
ns_precision = df
ns_precision.to_csv('data/BTC_ns.csv', index=False)
