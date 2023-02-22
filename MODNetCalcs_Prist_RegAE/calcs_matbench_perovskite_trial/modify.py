import pandas as pd

# Read the data into a pandas dataframe
data = pd.read_csv('data.txt', delimiter='|',skiprows=2, names=['aa','Model', 'Size', 'Score','a'])
data=data.drop(['aa','a'], axis=1)
data=data.drop(0,axis=0)
print(data)
# Select all entries where Size is Full
data['Size']=data['Size'].str.strip()
data['Score']=data['Score'].astype(float)
# where data equals 'Full' calculate the 'Percentage improvement' taking 0.0888 as reference score
data.loc[data['Size'] == 'Full', 'Percentage improvement'] = (data['Score']-0.0888)/0.0888*100
# where data equals '5k' calculate the 'Percentage improvement' taking 0.1667 as reference score
data.loc[data['Size'] == '5k', 'Percentage improvement'] = (data['Score']-0.1667)/0.1667*100
# where data equals '1k' calculate the 'Percentage improvement' taking 0.2802 as reference score
data.loc[data['Size'] == '1k', 'Percentage improvement'] = (data['Score']-0.2802)/0.2802*100
# now sort dataset according to Size and absolute value of the score
data['Percentage improvement abs']=data['Percentage improvement'].abs()
data=data.sort_values(by=['Size','Percentage improvement abs'], ascending=[False,True])
data.drop(['Percentage improvement abs'], axis=1, inplace=True)
# round 'Percentage improvement' to 2 decimals
data['Percentage improvement']=data['Percentage improvement'].round(2)
# rename Percentage improvement to % improvement
data.rename(columns={'Percentage improvement': '% improvement'}, inplace=True)
# print the dataframe to a markdown syntax without index
print(data.to_markdown(index=False))


# Print the selected data
# print(data)