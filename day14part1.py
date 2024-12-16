from math import floor

with open("./inputs/14input.txt", "r") as f:
    data = f.read()

roboDict = {}
for idx, robo in enumerate(data.splitlines()):
    roboDict[idx] = {
        "position": [int(num) for num in robo.split(" ")[0].replace("p=", "").split(",")],
        "velocity": [int(num) for num in robo.split(" ")[1].replace("v=", "").split(",")],
    }

def simNSecond(position, velocity, n, gridX, gridY):
    
    x, y = position[0] + (n * velocity[0]), position[1] + (n * velocity[1])
    xN, yN = x % gridX, y % gridY
    return xN, yN

nSim = [
    simNSecond(d["position"], d["velocity"], 100, 101, 103)
     for d in roboDict.values()
]

gridX, gridY = 101, 103
xmid, ymid = floor(gridX / 2), floor(gridY / 2)
impPos = [
    val
     for val in nSim
     if val[0] != floor(gridX / 2)
     if val[1] != floor(gridY / 2)
]

quad1 = len([
    pos
     for pos in impPos
     if 0 <= pos[0] < xmid
     if 0 <= pos[1] < ymid
])

quad2 = len([
    pos
     for pos in impPos
     if xmid < pos[0]
     if 0 <= pos[1] < ymid
])

quad3 = len([
    pos
     for pos in impPos
     if 0 <= pos[0] < xmid
     if ymid < pos[1]
])

quad4 = len([
    pos
     for pos in impPos
     if xmid < pos[0]
     if ymid < pos[1]
])

print(quad1 * quad2 * quad3 * quad4)
