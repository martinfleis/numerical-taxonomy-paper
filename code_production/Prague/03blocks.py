import geopandas as gpd
import momepy as mm

tess = gpd.read_file('files/prg.gpkg', layer='queen')
blg = gpd.read_file('files/prg.gpkg', layer='buildings')

streets = gpd.read_file('files/streets.gpkg', layer='streets')

streets['nID'] = mm.unique_id(streets)

blg['nID'] = mm.get_network_id(blg, streets, 'uID', 'nID', 150)
tess = tess.merge(blg[['uID', 'nID']], on='uID', how='left')

snapped = mm.snap_street_network_edge(streets, blg, 20, tess, 120)

blocks, blg['bID'], tess['bID'] = mm.blocks(tess, snapped, blg, 'bID', 'uID')

tess.to_file('files/elements.gpkg', layer='tessellation', driver='GPKG')
blg.to_file('files/elements.gpkg', layer='buildings', driver='GPKG')
blocks.to_file('files/elements.gpkg', layer='blocks', driver='GPKG')
streets.to_file('files/elements.gpkg', layer='streets', driver='GPKG')
