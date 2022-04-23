import pandas as pd
import plotly.figure_factory as ff
import random
import statistics as st

df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 110/medium_data.csv')
value = df['reading_time'].tolist()
# graph = ff.create_distplot([value],['reading time'],show_hist=False)
# graph.show()

finallist = []
def sampling():
    data = []
    for f in range(0,100):
        rp = random.randint(0,len(value)-1)
        data.append(value[rp])
    mean = st.mean(data)
    finallist.append(mean)

for f in range(0,10000):
    sampling()

graph = ff.create_distplot([finallist],['data sample'],show_hist=False)
graph.show()