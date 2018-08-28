# import pandas as pd
# import re
# # import os 
# import numpy as np
# import pinyin
# import matplotlib.pyplot as plt
import itchat

# for i in dir(itchat):
#     print(i)

# print(dir(itchat.utils))
itchat.login()
use_fake_dataset = True
dataset = itchat.get_friends(update=True)[0:]
for i in dataset:
    print(i)
print(type(dataset))



