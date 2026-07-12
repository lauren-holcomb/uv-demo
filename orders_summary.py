import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/orders.csv")

sum_by_category = df.groupby("category", as_index=False).agg({"order_total": "sum"})
sum_by_category = sum_by_category.sort_values(by="order_total", ascending=False)
print(sum_by_category)

sns.barplot(x="category", y="order_total", data=sum_by_category)
plt.show()
