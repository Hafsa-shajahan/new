# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:24:18 2024

@author: HAFSA SHAJAHAN
"""

i=0
while i<10:
        print(i)
        i+=2
        
for i in range(5,100,5):  #range(start,stop,step)
  print(i)        
  
  
score=[1,24,32,33,21]
sumscore=0
for scores in score:
    sumscore+=scores
avg_score= sumscore/len(score)
print(f"The average score is:{avg_score}")    

high=score[0]
for scores in score:
    if scores>high:
        high=scores
low=score[0]        
for scores in score:
    if scores<low:
        low=scores
print(f"highest score is{high}") 
print(f"lowest score is {low}")       

#size of multiplication table
table=5
for i in range(1,table+1):
    for j in range(1,table+1):
        priduct=i*j
        print(f"{priduct:7}",end="")
       