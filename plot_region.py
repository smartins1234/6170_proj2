import os

# dataPath = os.path.realpath(os.path.dirname(__file__))
dataPath = os.path.join(os.path.dirname(__file__), "1.5mmRegions")
regionBaseName = "T_E_ROI_42_locations_"
clouds = [
    {"name": "CD8", "color": "orange"},
    {"name": "FoxP3", "color": "skyblue"},
    {"name": "CD68", "color": "purple"},
]

if __name__ == "__main__":
    for cloud in clouds:
        fileName = regionBaseName + cloud["name"] + '.csv'
        filePath = os.path.join(dataPath, cloud["name"], fileName)
        print(filePath)
        print(os.path.isfile(filePath))
        print()