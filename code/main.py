import pandas as pd
import numpy as np

# 创建一个DataFrame
df = pd.DataFrame({
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, 22, 35, 32],
    'city': ['New York', 'Paris', 'London', 'Tokyo'],
    'salary': [50000, 45000, 65000, 70000]
})

localhost:8888/notebooks/d2l-zh/pytorth/chapter_preliminaries/pandas.iptnb

# 基本操作
print("基本信息:")
print(df.head())  # 显示前几行
print(df.info())  # 显示DataFrame的信息
print(df.describe())  # 统计摘要

# 过滤
young_people = df[df['age'] < 30]  # 筛选年龄小于30的人
high_salary = df[df['salary'] > 60000]  # 筛选工资大于60000的人

# 排序
sorted_by_age = df.sort_values('age')  # 按年龄排序
sorted_by_salary_desc = df.sort_values('salary', ascending=False)  # 按工资降序排序

# 分组
avg_salary_by_city = df.groupby('city')['salary'].mean()  # 按城市分组并计算平均工资

# 添加新列
df['salary_category'] = df['salary'].apply(lambda x: 'High' if x > 60000 else 'Low')  # 根据工资添加分类列

# 处理缺失值
df_with_nan = df.copy()
df_with_nan.loc[0, 'salary'] = np.nan  # 将第一个人的工资设置为NaN
cleaned_df = df_with_nan.dropna()  # 删除包含NaN的行
filled_df = df_with_nan.fillna(df_with_nan['salary'].mean())  # 用平均值填充NaN

# 导出到CSV
df.to_csv('output.csv', index=False)  # 导出到CSV文件
