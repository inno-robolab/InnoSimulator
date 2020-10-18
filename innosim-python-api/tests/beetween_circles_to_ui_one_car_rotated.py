#!/usr/bin/env python3
#

import os
import innosim
import math

def separation(V1, V2):
    xdiff = V1.x - V2.x
    ydiff = V1.y - V2.y
    zdiff = V1.z - V2.z
    return math.sqrt(xdiff * xdiff + ydiff * ydiff + zdiff * zdiff)

sim = innosim.Simulator(address = "127.0.0.1", port = 8181)
if sim.current_scene == "Innopolis":
  sim.reset()
else:
  sim.load("Innopolis")

spawns = sim.get_spawn()

spawns[0].position.y+=1
spawns[0].position.z+=16
print(spawns[0].position)
forward = innosim.utils.transform_to_forward(spawns[0])
right = innosim.utils.transform_to_right(spawns[0])

state = innosim.AgentState()
state.transform = spawns[0] 
state.transform.position = state.transform.position 

ego = sim.add_agent("Prius-Robo-ap5", innosim.AgentType.EGO, state)
ego.connect_bridge(os.environ.get("BRIDGE_HOST", "127.0.0.1"), 9090)

state = innosim.AgentState()



# 10 meters ahead, on left lane
state.transform.position = spawns[0].position+ 20.0 * forward  -2.6*right
#state.transform.position.x+=5
#state.transform.position.z+=5
state.transform.rotation = spawns[0].rotation*1.8

POV = sim.add_agent("BMWX3", innosim.AgentType.NPC, state)


# If the passed bool is False, then the NPC will not moved
# The float passed is the maximum speed the NPC will drive
# 11.1 m/s is ~40 km/h
print(POV.follow_closest_lane(True, 7.0, True))

input("Press Enter to run")

left_line = False

while True:
  sim.run(0.5)
  egoCurrentState = ego.state
  POVCurrentState = POV.state

  if separation(egoCurrentState.position, POVCurrentState.position)< 20.0 and not left_line:
   POV.change_lane(True)
   left_line = True

  if separation(egoCurrentState.position, POVCurrentState.position)> 20.0 and left_line:
    POV.change_lane(False)
    left_line = False  
      


