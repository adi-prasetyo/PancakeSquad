import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_excel('PancakeSquad.xlsx')
df['tokenId'] = df['tokenId'].astype('str')

df_trait = pd.read_excel('PancakeSquadTrait.xlsx')
df_trait = df_trait.drop(['tokenId'], axis=1)
df_trait['Background'] = df_trait['Background'].str.split('\n').str[0]
df_trait['Bunny'] = df_trait['Bunny'].str.split('\n').str[0]
df_trait['Clothes'] = df_trait['Clothes'].str.split('\n').str[0]
df_trait['Eyes'] = df_trait['Eyes'].str.split('\n').str[0]
df_trait['Mouth'] = df_trait['Mouth'].str.split('\n').str[0]
df_trait['Ear'] = df_trait['Ear'].str.split('\n').str[0]
df_trait['Hat'] = df_trait['Hat'].str.split('\n').str[0]

df = pd.concat([df, df_trait], axis=1, join="inner")

bnbPrice = 'currentAskPrice'
df_noz = df[df[bnbPrice] != 0]

df_slice1 = df_noz.copy()
df_slice1 = df_slice1[df_slice1[bnbPrice] <= 103]

#sns.distplot(df_slice['Price (BNB)'], norm_hist=False, kde=False, bins=20, hist_kws={"alpha": 1})
chartSize = (20, 10)

fig, ax = plt.subplots(figsize=chartSize)

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.set_theme()

chartSizeBox = (30, 10)
fig, ax = plt.subplots(figsize=chartSizeBox)
sns_plot = sns.boxplot(x=df_slice1['Background'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxBackground1.png",bbox_inches='tight')

sns_plot = sns.boxplot(x=df_slice1['Bunny'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxBunny1.png",bbox_inches='tight')

sns_plot = sns.boxplot(x=df_slice1['Eyes'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxEyes1.png",bbox_inches='tight')

sns_plot = sns.boxplot(x=df_slice1['Mouth'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxMouth1.png", bbox_inches='tight')

sns_plot = sns.boxplot(x=df_slice1['Ear'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxEar1.png", bbox_inches='tight')


chartSizeBox = (50, 10)
fig, ax = plt.subplots(figsize=chartSizeBox)
sns_plot = sns.boxplot(x=df_slice1['Clothes'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxClothes1.png",bbox_inches='tight')

sns_plot = sns.boxplot(x=df_slice1['Hat'], y=df_slice1[bnbPrice])
sns_plot.figure.savefig(r"C:\Users\adipr\Pictures\boxplot\boxHat1.png", bbox_inches='tight')