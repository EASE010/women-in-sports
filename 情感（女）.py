import csv
from snownlp import SnowNLP
import numpy as np

# 读取csv文件
filename = "static/data/女性/女（总）.csv"
data = []
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        data.append(row[5])  # 第六列为体育新闻内容

# 对每条新闻进行情感分析
sentiments = []
for content in data:
    s = SnowNLP(content)
    sentiments.append(s.sentiments)

# 统计情感值落在每个区间的个数
bins = np.linspace(0, 1, 21)  # 区间
hist, _ = np.histogram(sentiments, bins=bins)
for i in range(len(hist)):
    print(f"{bins[i]:.2f}-{bins[i+1]:.2f}: {hist[i]}")