import geopandas as gpd
import os


def write_geojson(df, path):
    '''Helper function to write a GeoPandas dataframe to GeoJSON. The built-in
    driver for writing GeoJSON doesn't allow for overwriting an existing file.

    '''
    if os.path.exists(path):
        os.remove(path)

    df.to_file(path, driver='GeoJSON')


#
# Simple conversions - strip *all* metadata, keep only location info
#

for feature_type in ['crossings', 'curbramps', 'sidewalks']:
    print('Converting {}...'.format(feature_type))
    df = gpd.read_file('./input/{}.geojson'.format(feature_type))
    df_new = df.loc[:, ['geometry']]
    write_geojson(df_new, './output/{}.geojson'.format(feature_type))

#
# More complex conversions - keep some metadata, format into JSON specification
# in {package} library schema
#

# Sidewalks
print('Converting sidewalks with incline information')
sidewalks_complex = gpd.read_file('./input/sidewalks.geojson')
sidewalks_new_complex = sidewalks_complex[['geometry']]
sidewalks_new_complex['incline'] = sidewalks_complex.loc[:, ['grade']]
write_geojson(sidewalks_new_complex, './output/sidewalks_new_complex.geojson')

# Crossings
print('Converting crossings with incline information')
crossings_complex = gpd.read_file('./input/crossings.geojson')
crossings_new_complex = crossings_complex[['geometry']]
crossings_new_complex['incline'] = crossings_complex.loc[:, ['grade']]
write_geojson(crossings_new_complex, './output/crossings_new_complex.geojson')
