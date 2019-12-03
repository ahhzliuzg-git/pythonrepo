import random
from pyecharts.charts import Bar
bar = Bar("我的第一个图表")
bar.use_theme('vintage')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('vintage.html')
