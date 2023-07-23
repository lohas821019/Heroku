import pandas as pd
import matplotlib.pyplot as plt

# 假设有一个包含数据的pandas DataFrame
data = {'City': ['New York', 'London', 'Tokyo', 'Paris', 'Beijing'],
        'Population': [8623000, 8908081, 9273000, 2141000, 21540000]}
df = pd.DataFrame(data)

# 绘制柱状图
plt.bar(df['City'], df['Population'])
plt.xlabel('City')
plt.ylabel('Population')
plt.title('Population by City')
plt.xticks(rotation=45)

# 保存图表为图片
plt.savefig('population_chart.png')

# 显示图表（可选）
plt.show()
