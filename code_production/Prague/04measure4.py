import momepy as mm
import geopandas as gpd
import libpysal

streets = gpd.read_file("files/elements.gpkg", layer="streets")

graph = mm.gdf_to_nx(streets)

print("node degree")
graph = mm.node_degree(graph)

print("subgraph")
graph = mm.subgraph(
    graph,
    radius=5,
    meshedness=True,
    cds_length=False,
    mode="sum",
    degree="degree",
    length="mm_len",
    mean_node_degree=False,
    proportion={0: True, 3: True, 4: True},
    cyclomatic=False,
    edge_node_ratio=False,
    gamma=False,
    local_closeness=True,
    closeness_distance="mm_len",
)
print("cds length")
graph = mm.cds_length(graph, radius=3, name="ldsCDL")

print("eigenvector")
try:
    graph = mm.eigenvector(graph, name="xcnEiC", max_iter=500)
except Exception:
    graph = mm.eigenvector(graph, name="xcnEiC", max_iter=1000)

print("clustering")
graph = mm.clustering(graph, name="xcnSCl")

print("mean_node_dist")
graph = mm.mean_node_dist(graph, name="mtdMDi")


nodes, edges, sw = mm.nx_to_gdf(graph, spatial_weights=True)

print("saving")
nodes.to_file("files/elements.gpkg", layer="nodes", driver="GPKG")
edges.to_file("files/elements.gpkg", layer="edges", driver="GPKG")

fo = libpysal.io.open("files/GRnodes.gal", "w")
fo.write(sw)
fo.close()

edges_w3 = mm.sw_high(k=3, gdf=edges)
edges["ldsMSL"] = mm.SegmentsLength(edges, spatial_weights=edges_w3, mean=True).series

tess = gpd.read_file("files/elements.gpkg", layer="tessellation")

edges["ldsRea"] = mm.Reached(edges, tess, "nID", "nID", spatial_weights=edges_w3).series
edges["ldsRea"] = mm.Reached(
    edges, tess, "nID", "nID", spatial_weights=edges_w3, mode="sum", values="sdcAre"
).series

nodes_w5 = mm.sw_high(k=5, weights=sw)
nodes["lddNDe"] = mm.NodeDensity(nodes, edges, nodes_w5).series
nodes["linWID"] = mm.NodeDensity(
    nodes, edges, nodes_w5, weighted=True, node_degree="degree"
).series

blg = gpd.read_file("files/elements.gpkg", layer="buildings")

blg["nodeID"] = mm.get_node_id(blg, nodes, edges, "nodeID", "nID")
tess = tess.merge(blg[["uID", "nodeID"]], on="uID", how="left")

nodes_w3 = mm.sw_high(k=3, weights=sw)

nodes["lddRea"] = mm.Reached(nodes, tess, "nodeID", "nodeID", nodes_w3).series
nodes["lddARe"] = mm.Reached(
    nodes, tess, "nodeID", "nodeID", nodes_w3, mode="sum", values="sdcAre"
).series

nodes["sddAre"] = mm.Reached(
    nodes, tess, "nodeID", "nodeID", mode="sum", values="sdcAre"
).series
nodes["midRea"] = mm.Reached(nodes, tess, "nodeID", "nodeID", spatial_weights=sw).series
nodes["midAre"] = mm.Reached(
    nodes, tess, "nodeID", "nodeID", spatial_weights=sw, mode="sum", values="sdcAre"
).series

nodes.rename(
    columns={
        "degree": "mtdDeg",
        "meshedness": "lcdMes",
        "local_closeness": "lcnClo",
        "proportion_3": "linP3W",
        "proportion_4": "linP4W",
        "proportion_0": "linPDE",
    }
)

print("saving")
nodes.to_file("files/elements.gpkg", layer="nodes", driver="GPKG")
edges.to_file("files/elements.gpkg", layer="edges", driver="GPKG")
tess.to_file("files/elements.gpkg", layer="tessellation", driver="GPKG")
blg.to_file("files/elements.gpkg", layer="buildings", driver="GPKG")
# rename meshedness and closeness
