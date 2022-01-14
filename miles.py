from distutils.command.config import config
import json
import math

f = open('config.json')
config_data = json.load(f)

block_distribution = config_data['blocks_walked'];

proj_intersections = 10
proj_volume = 423

if (len(block_distribution.keys()) > proj_intersections):
    block_distribution[str(proj_intersections)] = sum(
        list(block_distribution.values())[proj_intersections-1:])
    print(block_distribution)

temp = 0
for i in range(1, proj_intersections+1):
    temp += (block_distribution[str(i)]/100)*(i)

people = math.floor(proj_volume/temp)
print("Unique people: " + str(people))

distance = 0
for i in range(1, proj_intersections+1):
    distance += people*(block_distribution[str(i)]/100)*(i*(1/9))

print("Total distance travelled: " + str(distance) + " miles")