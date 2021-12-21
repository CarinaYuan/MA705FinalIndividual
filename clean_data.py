import pandas as pd
import datetime
import geopandas


# import dataset
df=pd.read_csv('listings.csv')
print(df.shape)
# remove rows that contains missing/wrong values in Borough or Latitude/Longitude
df=df.dropna(subset=['neighbourhood_group_cleansed','latitude','longitude'])
df = df[(df.latitude != 0) | (df.longitude != 0)]
df=df.reset_index(drop=True)

borough = geopandas.read_file('/Users/yuanzehui/PycharmProjects/MA705/individual project2/nybb/geo_export_6aa743eb-5393-4742-b69c-807986e5fc8c.shp')

df_geo = geopandas.GeoDataFrame(df, crs="EPSG:4326",
                                geometry=geopandas.points_from_xy(df.longitude, df.latitude))
d_f = pd.DataFrame()
for boro in ['Manhattan','Brooklyn','Bronx','Queens','Staten Island']:
    df_sub=df_geo[df_geo['neighbourhood_group_cleansed']==boro]
    df_sub=df_sub.reset_index(drop=True)
    #print(df_sub.shape)
    poly=borough[borough['boro_name']==boro.title()]['geometry']
    #print(poly)
    is_in=[]
    for i in df_sub.index:
        is_in_boro = poly.contains(df_sub.geometry[i])
        is_in.append(is_in_boro.iloc[0])
    df_sub['is_in']=is_in
    print(df_sub.shape)
    df_sub=df_sub[df_sub['is_in']]
    print(df_sub.shape)

    d_f=d_f.append(df_sub)





print(d_f.shape)

# reformat variables
print(d_f.loc[3,'price'])
d_f['price']=d_f['price'].apply(lambda x: (x.replace('$', '')))
d_f['price']=d_f['price'].apply(lambda x: (x.replace(',', '')))
d_f['price']=d_f['price'].apply(lambda x: float(x))
print(type(d_f.loc[3,'price']))
print(d_f.loc[3,'price'])
d_f=d_f[['id','name','description','neighbourhood_group_cleansed','room_type','price',
         'review_scores_rating','host_response_rate','host_acceptance_rate','listing_url','latitude','longitude']]

d_f = d_f.rename({'listing_url': 'URL', 'neighbourhood_group_cleansed': 'Borough', 'review_scores_rating': 'Review Score', 'price':'Price',
                  'room_type': 'Room Type', 'host_response_rate': 'Host Response Rate', 'host_acceptance_rate': 'Host Acceptance Race'}, axis=1)
d_f = d_f.reset_index(drop=True)
d_f.to_csv('airbnb_ny_listing.csv')
