import momepy as mm
import geopandas as gpd

tess = gpd.read_file("files/elements.gpkg", layer="tessellation")
blg = gpd.read_file("files/elements.gpkg", layer="buildings")
# blocks = gpd.read_file('files/elements.gpkg', layer='blocks')
streets = gpd.read_file("files/elements.gpkg", layer="streets")

# blg['sdbAre'] = mm.area(blg)
# blg['sdbVol'] = mm.volume(blg, 'sdbHei', 'sdbAre')
# blg['sdbPer'] = mm.perimeter(blg)
# blg['sdbCoA'] = mm.courtyard_area(blg, 'sdbAre')
#
# blg['ssbFoF'] = mm.form_factor(blg, 'sdbVol', 'sdbAre')
# blg['ssbVFR'] = mm.volume_facade_ratio(blg, 'sdbHei', 'sdbVol', 'sdbPer')
# blg['ssbCCo'] = mm.circular_compactness(blg, 'sdbAre')
# blg['ssbCor'] = mm.corners(blg)
# blg['ssbSqu'] = mm.squareness(blg)
# blg['ssbERI'] = mm.equivalent_rectangular_index(blg, 'sdbAre', 'sdbPer')
# blg['ssbElo'] = mm.elongation(blg)
# blg['ssbCCM'], blg['ssbCCD'] = mm.centroid_corners(blg)
#
# blg['stbOri'] = mm.orientation(blg)
blg["stbSAl"] = mm.street_alignment(blg, streets, "stbOri", "nID", "nID")

# tess['stcOri'] = mm.orientation(tess)
# blg['stbCeA'] = mm.cell_alignment(blg, tess, 'stbOri', 'stcOri', 'uID', 'uID')
#
# tess['sdcLAL'] = mm.longest_axis_length(tess)
# tess['sdcAre'] = mm.area(tess)
# tess['sscCCo'] = mm.circular_compactness(tess, 'sdcAre')
# tess['sscERI'] = mm.equivalent_rectangular_index(tess, 'sdcAre')

tess["stcSAl"] = mm.street_alignment(tess, streets, "stcOri", "nID", "nID")

# tess['sicCAR'] = mm.object_area_ratio(tess, blg, 'sdcAre', 'sdbAre', 'uID')
# fa = mm.floor_area(blg, 'sdbHei', 'sdbAre')
# tess['sicFAR'] = mm.object_area_ratio(tess, blg, 'sdcAre', fa, 'uID')

streets["sdsLen"] = mm.perimeter(streets)

profile = mm.street_profile(streets, blg, heights="sdbHei", distance=3)
streets["sdsSPW"] = profile["widths"]
streets["sdsSPH"] = profile["heights"]
streets["sdsSPR"] = profile["profile"]
streets["sdsSPO"] = profile["openness"]
streets["sdsSWD"] = profile["width_deviations"]
streets["sdsSHD"] = profile["heights_deviations"]

streets["sssLin"] = mm.linearity(streets)
streets["sdsAre"] = mm.reached(streets, tess, "nID", mode="sum", values="sdcAre")
streets["sisBpM"] = mm.elements_count(streets, blg, "nID", "nID", weighted=True)

tess.to_file("files/elements.gpkg", layer="tessellation", driver="GPKG")
blg.to_file("files/elements.gpkg", layer="buildings", driver="GPKG")
streets.to_file("files/elements.gpkg", layer="streets", driver="GPKG")
