import pandas as pd
#convert csv's to line protocol

#convert sample data to line protocol (with nanosecond precision)
# df = pd.read_csv("data/BTC_sm_ns.csv")
# df["measurement"] = ['price' for t in range(len(df))]
# lines = [str(df["measurement"][d])
#          + ",type=BTC"
#          + " "
#          + "close=" + str(df["close"][d]) + ","
#          + "high=" + str(df["high"][d]) + ","
#          + "low=" + str(df["low"][d]) + ","
#          + "open=" + str(df["open"][d]) + ","
#          + "volume=" + str(df["volume"][d])
#          + " " + str(df["time"][d]) for d in range(len(df))]
# thefile = open('data/chronograf.txt', 'w')
# for item in lines:
#     thefile.write("%s\n" % item)

#covert full data to line protocol (with nanosecond precision)
df_full = pd.read_csv("data/BTC_ns.csv")
df_full["measurement"] = ['price' for t in range(len(df_full))]
lines = [str(df_full["measurement"][d])
         + ",type=BTC"
         + " "
         + "close=" + str(df_full["close"][d]) + ","
         + "high=" + str(df_full["high"][d]) + ","
         + "low=" + str(df_full["low"][d]) + ","
         + "open=" + str(df_full["open"][d]) + ","
         + "volume=" + str(df_full["volume"][d])
         + " " + str(df_full["time"][d]) for d in range(len(df_full))]
#append lines to a text file with DDL & DML:
thefile = open('data/import.txt', 'a+')
for item in lines:
    thefile.write("%s\n" % item)
