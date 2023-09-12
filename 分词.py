import csv
import jieba
from collections import Counter

# 读取原始数据
with open('static/data/女性/女（总）.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
texts = [row[5] for row in data[1:]]  # 提取第6列中除首行之外的所有文字

# 分词并统计词频
words = []
for text in texts:
    seg_list = jieba.cut(text)
    words.extend(seg_list)
word_counts = Counter(words)

# 按照词频降序排序
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# 将结果保存到新的CSV文件中
with open('static/data/分词/女-分词.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'count'])
    for word, count in sorted_word_counts:
        writer.writerow([word, count])
