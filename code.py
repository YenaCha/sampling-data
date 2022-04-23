import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random
import statistics as st

df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 110/newdata.csv')
average = df['average'].tolist()
# graph = ff.create_distplot([average],['graph'],show_hist=False)
# graph.show()

finallist = []
def sampling():
    data = []
    for i in range (0,100):
        rp = random.randint(0,len(average)-1)
        data.append(average[rp])
    mean = st.mean(data)
    finallist.append(mean)

for i in range (0,1000):
    sampling()

# graph = ff.create_distplot([finallist],['select'],show_hist=False)
# graph.show()

pmean = st.mean(average)
pstd = st.stdev(average)
print('Population mean : '+str(pmean))
print('Population standard deviation : '+str(pstd))
smean = st.mean(finallist)
sstd = st.stdev(finallist)
print('Sample mean : '+str(smean))
print('Sample standard deviation : '+str(sstd))