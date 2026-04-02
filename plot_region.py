import os
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

dataPath = os.path.join(os.path.dirname(__file__), "1.5mmRegions")

plotPath = os.path.join(os.path.dirname(__file__), "plots")
if not os.path.exists(plotPath):
    os.makedirs(plotPath)

regionBaseName = "T_E_ROI_42_locations_"
clouds = [
    {"name": "CD8", "color": "orange", "points": []},
    {"name": "FoxP3", "color": "skyblue", "points": []},
    {"name": "CD68", "color": "purple", "points": []},
]

def read_csv(csvPath):
    # print(f"read_csv called on file {csvPath}")

    # read in the csv file as a list of point coordinates and return the list
    fileText = ''
    with open(csvPath, "r") as file:
        fileText = file.read()

    lines = fileText.split('\n')
    points = []
    for line in lines:
        try:
            coord = [float(e) for e in line.split(',')]
            points.append(coord)
        except:
            # print(f'{line} is not a valid coordinate')
            continue

    return points


if __name__ == "__main__":


    for cloud in clouds:
        fileName = regionBaseName + cloud["name"] + '.csv'
        filePath = os.path.join(dataPath, cloud["name"], fileName)
        # print(filePath)
        # print(os.path.isfile(filePath))
        if not os.path.isfile(filePath):
            print(f"Could not find point cloud {filePath}")
            continue

        points = np.array(read_csv(filePath))
        print(points.shape)
        # pprint(points)

        fig = plt.figure(1)
        plt.title(f'Region T E ROI 42: {cloud["name"]}')
        plt.scatter(points[:, 0], points[:, 1], color=cloud["color"], s=4)
        plt.show()

        cloud["points"] = points

    fig = plt.figure(1)
    plt.title(f'Region T E ROI 42')
    for cloud in clouds:
        plt.scatter(cloud["points"][:, 0], cloud["points"][:, 1], color=cloud["color"], s=4, label=cloud["name"])
    plt.legend(loc="best", shadow=False, ncols=1, fontsize='small')
    plt.show()