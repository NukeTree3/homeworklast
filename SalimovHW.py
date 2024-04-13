import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
r=[]
h=[]
for i in range(len(data['whoAmI'])):
    if data['whoAmI'][i] == "robot":
        r.append(1)
        h.append(0)
    else:
        r.append(0)
        h.append(1)
one_hot = {"robot":r,"human":h}
df = pd.DataFrame(one_hot)
print(df)