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


