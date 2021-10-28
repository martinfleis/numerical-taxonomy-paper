import momepy as mm
import geopandas as gpd
import libpysal

tess = gpd.read_file('files/elements.gpkg', layer='tessellation')
blg = gpd.read_file('files/elements.gpkg', layer='buildings')
blocks = gpd.read_file('files/elements.gpkg', layer='blocks')
streets = gpd.read_file('files/elements.gpkg', layer='streets')


queen1 = mm.sw_high(k=1, gdf=tess, ids='uID')
queen3 = mm.sw_high(k=3, weights=queen1)
blg_queen = mm.sw_high(k=1, gdf=blg, ids='uID')


blg['ltbIBD'] = mm.MeanInterbuildingDistance(blg, queen1, 'uID', queen3).series
blg['ltcBuA'] = mm.BuildingAdjacency(blg, queen3, 'uID', blg_queen).series

# blg['temp_fa'] = mm.floor_area(blg, 'sdbHei', 'sdbAre')
# tess = tess.merge(blg[['temp_fa', 'uID']], on='uID', how='left')
# tess['licGDe'] = mm.density(tess, 'temp_fa', queen3, 'uID', 'sdcAre')
tess['ltcWRB'] = mm.BlocksCount(tess, 'bID', queen3, 'uID').series

tess.to_file('files/elements.gpkg', layer='tessellation', driver='GPKG')
blg.to_file('files/elements.gpkg', layer='buildings', driver='GPKG')

fo = libpysal.io.open('files/GRqueen1.gal', 'w')
fo.write(queen1)
fo.close()

fo = libpysal.io.open('files/GRqueen3.gal', 'w')
fo.write(queen3)
fo.close()

fo = libpysal.io.open('files/GRblg_queen.gal', 'w')
fo.write(blg_queen)
fo.close()
