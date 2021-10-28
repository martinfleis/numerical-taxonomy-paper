import momepy as mm
import geopandas as gpd
import libpysal

tess = gpd.read_file("files/elements.gpkg", layer="tessellation")
blg = gpd.read_file("files/elements.gpkg", layer="buildings")
blocks = gpd.read_file("files/elements.gpkg", layer="blocks")
streets = gpd.read_file("files/elements.gpkg", layer="streets")

blg["mtbSWR"] = mm.SharedWallsRatio(blg, "uID", "sdbPer").series

queen_1 = libpysal.weights.contiguity.Queen.from_dataframe(tess, ids="uID")

blg["mtbAli"] = mm.Alignment(blg, queen_1, "uID", "stbOri").series
blg["mtbNDi"] = mm.NeighbourDistance(blg, queen_1, "uID").series

tess["mtcWNe"] = mm.Neighbours(tess, queen_1, "uID", weighted=True).series
tess["mdcAre"] = mm.CoveredArea(tess, queen_1, "uID").series

str_q1 = libpysal.weights.contiguity.Queen.from_dataframe(streets)

streets["misRea"] = mm.Reached(
    streets, tess, "nID", "nID", spatial_weights=str_q1, mode="count"
).series
streets["mdsAre"] = mm.Reached(streets, tess, "nID", "nID", spatial_weights=str_q1,
                               mode="sum").series

blg_q1 = libpysal.weights.contiguity.Queen.from_dataframe(blg)

blg["libNCo"] = mm.Courtyards(blg, "bID", blg_q1).series
blg["ldbPWL"] = mm.PerimeterWall(blg, blg_q1).series

blocks["ldkAre"] = mm.Area(blocks).series
blocks["ldkPer"] = mm.Perimeter(blocks).series
blocks["lskCCo"] = mm.CircularCompactness(blocks, "ldkAre").series
blocks["lskERI"] = mm.EquivalentRectangularIndex(blocks, "ldkAre", "ldkPer").series
blocks["lskCWA"] = mm.CompactnessWeightedAxis(blocks, "ldkAre", "ldkPer").series
blocks["ltkOri"] = mm.Orientation(blocks).series

blo_q1 = libpysal.weights.contiguity.Queen.from_dataframe(blocks, ids="bID")

blocks["ltkWNB"] = mm.Neighbors(blocks, blo_q1, "bID", weighted=True).series
blocks["likWBB"] = mm.Count(blocks, blg, "bID", "bID", weighted=True).series

tess.to_file("files/elements.gpkg", layer="tessellation", driver="GPKG")
blg.to_file("files/elements.gpkg", layer="buildings", driver="GPKG")
blocks.to_file("files/elements.gpkg", layer="blocks", driver="GPKG")
streets.to_file("files/elements.gpkg", layer="streets", driver="GPKG")
