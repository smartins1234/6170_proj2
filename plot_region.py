import os
import numpy as np
import matplotlib.pyplot as plt
# from pprint import pprint

dataPath = os.path.join(os.path.dirname(__file__), "1.5mmRegions")

plotPath = os.path.join(os.path.dirname(__file__), "plots")
if not os.path.exists(plotPath):
    os.makedirs(plotPath)

regionBaseName = "T_E_ROI_42_locations_"
clouds = [
    {"name": "CD8", "color": "orange"},
    {"name": "FoxP3", "color": "skyblue"},
    {"name": "CD68", "color": "purple"},
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

        points = read_csv(filePath)
        print(len(points))
        # pprint(points)