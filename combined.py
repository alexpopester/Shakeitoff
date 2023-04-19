import pyvista as pv
import numpy as np
import matplotlib.pyplot as mt
from matplotlib.colors import ListedColormap
import vtk 
import vtkmodules 

COMBINEDFILES = [
    "CombinedG_0.vtk",
    "CombinedG_1.vtk",
    "CombinedG_2.vtk",
    "CombinedG_3.vtk",
    "CombinedG_4.vtk",
    "CombinedG_5.vtk",
    "CombinedG_6.vtk",
    "CombinedG_7.vtk",
    "CombinedG_8.vtk",
    "CombinedG_9.vtk",
    "CombinedG_10.vtk",
    "CombinedG_11.vtk",
    "CombinedG_12.vtk",
    "CombinedG_13.vtk",
    "CombinedG_14.vtk",
    "CombinedG_15.vtk",
    "CombinedG_16.vtk",
    "CombinedG_17.vtk",
    "CombinedG_18.vtk",
    "CombinedG_19.vtk",
    "CombinedG_20.vtk"
]

def magnitude(arr):
    return np.sqrt(sum(np.square(arr)))

def main():
    print("starting")
    pl = pv.Plotter(off_screen=True) 
    landFeatures = pv.read("./TS21VelocityMesh_VS_R2.vtk")    

    landFeatures = landFeatures.scale((4,4,4))

    landFeatures = landFeatures.threshold(2500, invert=True)
    pl.add_mesh(landFeatures, color="green")

    pl.open_gif("CombinedOverLand.gif")
    for item in COMBINEDFILES[1:]:
        print("Processing:",item)
        waves  = pv.read(item)
        d = np.apply_along_axis(magnitude, 1, waves.point_data["Result"] )
        print(f"Applied magnitude function to: {item}")
        mask =  d > 0.05
        waves1 = waves.points[mask]
        d1 = d[mask]
        print(f"Applied mask function to: {item}")
        pl.add_mesh(waves1, scalars=d1, cmap="inferno", opacity="linear", clim=[0,0.7])
        pl.add_mesh(landFeatures, color="green")
        pl.write_frame()
        pl.write_frame()
        pl.clear_actors()

    pl.close()

main()