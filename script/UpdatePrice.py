import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime

def load_df(r, drill1, drill2):
    json_data = json.loads(r.text)
    df_data = json_data[drill1][drill2]
    df = pd.DataFrame(df_data)
    return df

df_init_col = ['tokenId','currentAskPrice', 'latestTradedPriceInBNB', 'totalTrades', 'tradeVolumeBNB', 'transactionHistory']
df_init = pd.DataFrame(columns=df_init_col)
df_init['tokenId'] = np.arange(10000)
df_init['tokenId'] = df_init['tokenId'].astype(str)

url = 'https://api.thegraph.com/subgraphs/name/pancakeswap/nft-market'

df_init_col = ['tokenId','currentAskPrice', 'latestTradedPriceInBNB', 'totalTrades', 'tradeVolumeBNB', 'transactionHistory']
df_init = pd.DataFrame(columns=df_init_col)
df_init['tokenId'] = np.arange(10000)
df_init['tokenId'] = df_init['tokenId'].astype(str)
df_init = df_init.set_index('tokenId')

count = 1000 #max can only get 1000
start = 0
end = 10000

for x in range(start, end, count):
    
    gt = x - 1    
    lt = x + count

    query = """query NFT {{
      nfts(first: {0}, where:{{
        tokenId_gt:{1}, 
        tokenId_lt:{2},
        collection:"0x0a8901b0e25deb55a87524f0cc164e9644020eba"}}) 
      {{
        tokenId
        currentAskPrice
        totalTrades
        latestTradedPriceInBNB
        tradeVolumeBNB
        transactionHistory {{
          id
        }}
      }}
    }}"""
    
    query = query.format(count, gt, lt)
    r = requests.post(url, json={'query': query})
    
    df_query = load_df(r, 'data', 'nfts')
    df_query = df_query.set_index('tokenId')
    
    #df = pd.concat([df_init.set_index('tokenId'), df_test.set_index('tokenId')], axis=1)
    #df = pd.concat([df, df_query.set_index('tokenId')], axis=1)
    
    df_init.update(df_query)
    
#df.rename(columns={'currentAskPrice': 'price_bnb'}, inplace=True)

#df['price_bnb'] = df['price_bnb'].astype(float)
    
#df['id'] = df['id'].astype('str')
#df['id'] = df['id'].str.zfill(4)
#df = df.set_index('id').sort_index()
df_price = df_init.copy()
df_price = df_price.reset_index()

writer = pd.ExcelWriter('PancakeSquad.xlsx', engine='xlsxwriter')
df_price.to_excel(writer,  sheet_name='Sheet1', index = False)  

worksheet = writer.sheets['Sheet1']

# Set the column width and format.
worksheet.set_column('A:A', 8)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 100)

writer.save()