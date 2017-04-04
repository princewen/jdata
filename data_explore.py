# coding:utf-8
import os
import pandas as pd
user = pd.read_csv("data/user.csv", encoding="utf-8", sep='\t')
# user.to_csv("data/user.csv", encoding='utf-8')
# user = pd.read_csv("data/user.csv", encoding="utf-8")
# print(user.head(10))
# action = pd.read_csv('data/JData_Action_201602.csv')
# print(action.head(10))
# comment = pd.read_csv('data/JData_Comment.csv')
print(user.head(10))
