import pandas as pd
import numpy as np
#user_info = [php,java,c#,jp]
user_info = [0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8]

jobs = pd.read_csv('jobs.csv', header=None, skiprows=1)
print(np.array(user_info).dot(np.array(user_info)))
print(np.array(user_info).dot(np.array([0.1,0.5,0.4,0.1,0.9,0.5,0.4,0.8,0.9,0.3,0.4,0.8,0.2,0.5,0.4,0.9,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8,0.9,0.5,0.4,0.8])))
