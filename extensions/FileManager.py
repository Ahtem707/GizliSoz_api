import json
import os
from typing import List

def getJson(filePath: str):
    try:
        f = open(filePath)
        data = json.load(f)
        f.close()
        
        return data
    except:
        return None
    
def findFiles(folderPath: str, filePattern: str) -> List[str]:
    pathFiles: List[str] = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            if file.startswith(filePattern) and file.endswith(".json"):
                pathFiles.append(os.path.join(root, file))
    return pathFiles