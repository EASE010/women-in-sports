import csv
from pyecharts import options as opts
from pyecharts.charts import WordCloud

word_freq = {}
with open('static/data/分词/女-分词.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        word = row[0]
        freq = int(row[1])
        word_freq[word] = freq

# 创建词云对象
wc = WordCloud()

# 添加词语及其对应的词频
wc.add("", list(word_freq.items()))

# 配置词云样式
wc.set_global_opts(
    title_opts=opts.TitleOpts(title=""),
)

# 保存词云图到本地
wc.render("templates/wordcloud2.html")