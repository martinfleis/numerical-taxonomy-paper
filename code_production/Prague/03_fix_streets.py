import geopandas as gpd
import momepy as mm
import libpysal

# streets = gpd.read_file("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="streets")
tess = gpd.read_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="tessellation",
)
blg = gpd.read_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="buildings",
)

# streets = mm.network_false_nodes(streets)
# streets.reset_index(inplace=True, drop=True)
#
# streets["nID"] = mm.unique_id(streets)
# blg.drop(columns=["nID"], inplace=True)
# blg["nID"] = mm.get_network_id(blg, streets, "uID", "nID", 300)
# tess = tess.drop(columns=["nID"]).merge(blg[["uID", "nID"]], on="uID", how="left")

# blg["stbSAl"] = mm.street_alignment(blg, streets, "stbOri", "nID", "nID")

# tess["stcSAl"] = mm.street_alignment(tess, streets, "stcOri", "nID", "nID")

# streets["sdsLen"] = mm.perimeter(streets)

# profile = mm.street_profile(streets, blg, heights="sdbHei", distance=3)
# streets["sdsSPW"] = profile["widths"]
# streets["sdsSPH"] = profile["heights"]
# streets["sdsSPR"] = profile["profile"]
# streets["sdsSPO"] = profile["openness"]
# streets["sdsSWD"] = profile["width_deviations"]
# streets["sdsSHD"] = profile["heights_deviations"]
# streets.to_file("files/elements.gpkg", layer="streets", driver="GPKG")

# streets["sssLin"] = mm.linearity(streets)
# streets["sdsAre"] = mm.reached(streets, tess, "nID", "nID", mode="sum", values="sdcAre")
# streets["sisBpM"] = mm.elements_count(streets, blg, "nID", "nID", weighted=True)
#
# # tess.to_file("files/elements.gpkg", layer="tessellation", driver="GPKG")
# # blg.to_file("files/elements.gpkg", layer="buildings", driver="GPKG")
#
#
# str_q1 = libpysal.weights.contiguity.Queen.from_dataframe(streets)
#
# streets["misRea"] = mm.reached(
#     streets, tess, "nID", "nID", spatial_weights=str_q1, mode="count"
# )
# streets["mdsAre"] = mm.reached(
#     streets, tess, "nID", "nID", spatial_weights=str_q1, mode="sum"
# )
#
# streets.to_file("files/elements.gpkg", layer="streets", driver="GPKG")

# graph = mm.gdf_to_nx(streets)
#
# print("node degree")
# graph = mm.node_degree(graph)
#
# print("subgraph")
# graph = mm.subgraph(
#     graph,
#     radius=5,
#     meshedness=True,
#     cds_length=False,
#     mode="sum",
#     degree="degree",
#     length="mm_len",
#     mean_node_degree=False,
#     proportion={0: True, 3: True, 4: True},
#     cyclomatic=False,
#     edge_node_ratio=False,
#     gamma=False,
#     local_closeness=True,
#     closeness_distance="mm_len",
# )
# print("cds length")
# graph = mm.cds_length(graph, radius=3, name="ldsCDL")
#
# print("clustering")
# graph = mm.clustering(graph, name="xcnSCl")
#
# print("mean_node_dist")
# graph = mm.mean_node_dist(graph, name="mtdMDi")
#
# nodes, edges, sw = mm.nx_to_gdf(graph, spatial_weights=True)
#
# fo = libpysal.io.open("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/nodes.gal", "w")
# fo.write(sw)
# fo.close()
#
# nodes.to_file("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="nodes", driver="GPKG")
# edges.to_file("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="edges", driver="GPKG")
nodes = gpd.read_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="nodes"
)
edges = gpd.read_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="edges"
)
edges_w3 = mm.sw_high(k=3, gdf=edges)
edges["ldsMSL"] = mm.segments_length(edges, spatial_weights=edges_w3, mean=True)

edges["ldsRea"] = mm.reached(edges, tess, "nID", "nID", spatial_weights=edges_w3)
edges["ldsRea"] = mm.reached(
    edges, tess, "nID", "nID", spatial_weights=edges_w3, mode="sum", values="sdcAre"
)
# error below
# Traceback (most recent call last):
#   File "03_fix_streets.py", line 99, in <module>
#     nodes_w5 = mm.sw_high(k=5, weights=sw)
#   File "/home/ubuntu/momepy/utils.py", line 94, in sw_high
#     first_order, k=i, silence_warnings=silent
#   File "/home/ubuntu/miniconda3/envs/mmp/lib/python3.7/site-packages/libpysal/weights/util.py", line 427, in higher_order
#     return higher_order_sp(w, k, **kwargs)
#   File "/home/ubuntu/miniconda3/envs/mmp/lib/python3.7/site-packages/libpysal/weights/util.py", line 486, in higher_order_sp
#     if np.unique(np.hstack(list(w.weights.values()))) == np.array([1.0]):
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
sw = libpysal.io.open(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/nodes.gal", "r"
).read()

nodes_w5 = mm.sw_high(k=5, weights=sw)
# fix for string indices (probably due to loading of GAL)
nodes_w5.neighbors = {
    int(k): [int(i) for i in v] for k, v in nodes_w5.neighbors.items()
}
nodes["lddNDe"] = mm.node_density(nodes, edges, nodes_w5)
nodes["linWID"] = mm.node_density(
    nodes, edges, nodes_w5, weighted=True, node_degree="degree"
)
nodes.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="nodes",
    driver="GPKG",
)
edges.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="edges",
    driver="GPKG",
)
# tess.to_file("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="tessellation", driver="GPKG")
# blg.to_file("/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg", layer="buildings", driver="GPKG")

try:
    blg.drop(columns=["nodeID"], inplace=True)
except Exception:
    print("no nodeID")
try:
    tess.drop(columns=["nodeID"], inplace=True)
except Exception:
    print("no nodeID")
blg["nodeID"] = mm.get_node_id(blg, nodes, edges, "nodeID", "nID")
tess = tess.merge(blg[["uID", "nodeID"]], on="uID", how="left")

nodes_w3 = mm.sw_high(k=3, weights=sw)
nodes_w3.neighbors = {
    int(k): [int(i) for i in v] for k, v in nodes_w3.neighbors.items()
}

nodes["lddRea"] = mm.reached(nodes, tess, "nodeID", "nodeID", nodes_w3)
nodes["lddARe"] = mm.reached(
    nodes, tess, "nodeID", "nodeID", nodes_w3, mode="sum", values="sdcAre"
)

nodes["sddAre"] = mm.reached(
    nodes, tess, "nodeID", "nodeID", mode="sum", values="sdcAre"
)
sw.neighbors = {int(k): [int(i) for i in v] for k, v in sw.neighbors.items()}

nodes["midRea"] = mm.reached(nodes, tess, "nodeID", "nodeID", spatial_weights=sw)
nodes["midAre"] = mm.reached(
    nodes, tess, "nodeID", "nodeID", spatial_weights=sw, mode="sum", values="sdcAre"
)

nodes.rename(
    columns={
        "degree": "mtdDeg",
        "meshedness": "lcdMes",
        "local_closeness": "lcnClo",
        "proportion_3": "linP3W",
        "proportion_4": "linP4W",
        "proportion_0": "linPDE",
    },
    inplace=True,
)

print("saving")
nodes.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="nodes",
    driver="GPKG",
)
edges.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="edges",
    driver="GPKG",
)
tess.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="tessellation",
    driver="GPKG",
)
blg.to_file(
    "/Users/martin/Dropbox/Academia/Data/Geo/Prague/Redo/elements.gpkg",
    layer="buildings",
    driver="GPKG",
)
