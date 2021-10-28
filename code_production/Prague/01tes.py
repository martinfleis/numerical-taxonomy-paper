#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import geopandas as gpd
import momepy as mm
import libpysal


# In[ ]:


buildings = gpd.read_file('files/prg.gpkg', layer='buildings')


# In[ ]:


# buildings = mm.preprocess(buildings)
# buildings['uID'] = mm.unique_id(buildings)


# In[ ]:


buildings.to_file('files/prg.gpkg', layer='buildings', driver='GPKG')


# In[ ]:


limit = mm.buffered_limit(buildings, 100)


# In[ ]:


tessellation = mm.tessellation(buildings, 'uID', limit, queen_corners=False)
tessellation.to_file('files/prg.gpkg', layer='tessallation', driver='GPKG')


# In[ ]:


queen = libpysal.weights.Queen.from_dataframe(tessellation)


# In[ ]:


islands = queen.islands
tessellation.drop(islands, inplace=True)
buildings.drop(islands, inplace=True)


# In[ ]:


tessellation.to_file('files/prg.gpkg', layer='tessallation', driver='GPKG')
buildings.to_file('files/prg.gpkg', layer='buildings', driver='GPKG')


# In[ ]:
