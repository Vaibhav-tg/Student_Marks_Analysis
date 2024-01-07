import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("s_p.csv")
data.rename(columns={'parental level of education':'parental education',
                     'race/ethnicity':'looks',
                     'test preparation course':'prep.course'},inplace=True)
print(data.to_string())
plt.figure(figsize=(4,4))
ax=sns.countplot(data=data, x='gender')
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()
#from the above chart we analysed number of female is more than no of males.
gb=data.groupby('parental education').agg({'math score':'mean',
                                          'reading score':'mean',
                                          'writing score':'mean'})
print(gb)
plt.figure(figsize=(4,4))
plt.title("Relationship Between Parent Education And Student Score")
sns.heatmap(gb,annot=True)
plt.show()
#from the above chart we analysed the parent education impact on their chils marks
gb1=data.groupby('prep.course').agg({'math score':'mean',
                                          'reading score':'mean',
                                          'writing score':'mean'})
print(gb1)
plt.title("Relationship Between Preperation Course And Student Score")
plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=True)
plt.show()
#from above chart we analysed that the preperation course will impact on marks
gb2=data.groupby('lunch').agg({'math score':'mean',
                               'reading score':'mean',
                               'writing score':'mean'})
print(gb2)
plt.title("Relationship Between lunch And Student Score")
plt.figure(figsize=(4,4))
sns.heatmap(gb2,annot=True)
plt.show()
#from above chart we analysed that lunch will impact on marks

#conslusion:
#In This We Can See The Factors That Are Affect Student Marks..






