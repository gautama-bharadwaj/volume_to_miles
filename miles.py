from distutils.command.config import config
import json
import math

f = open('config.json')
config_data = json.load(f)

block_distribution = config_data['blocks_walked'];

proj_intersections = 10
proj_volume = 10000

if (len(block_distribution.keys()) > proj_intersections):
    block_distribution[str(proj_intersections)] = sum(
        list(block_distribution.values())[proj_intersections-1:])

for i in range(proj_intersections+1, int(list(block_distribution.keys())[-1])+1):
    del block_distribution[str(i)]

print(block_distribution)
temp = 0
for i in range(1, proj_intersections+1):
    if (int(list(block_distribution.keys())[-1]) < i):
        break
    temp += (block_distribution[str(i)]/100)*(i)

people = math.floor(proj_volume/temp)
print("Unique people: " + str(people))

distance = 0
for i in range(1, proj_intersections+1):
    if (int(list(block_distribution.keys())[-1]) < i):
        break
    distance += people*(block_distribution[str(i)]/100)*(i*(1/9))

print("Total distance travelled: " + str(round(distance)) + " miles")