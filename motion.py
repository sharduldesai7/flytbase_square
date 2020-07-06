#!/usr/bin/env python

import time
import argparse
from flyt_python import api
from math import pi

#parser = argparse.ArgumentParser()
#parser.add_argument("--side_length", nargs='?', const=6.5, type=float, help="--side_length 'your side length'")
#args = parser.parse_args()

traj_len = 6.5
height = 5.0

def main():
	print("Creating UAV")
	vehicle = api.navigation(timeout = 120000)
	time.sleep(3)
	print("Taking off")
	vehicle.take_off(height)
	time.sleep(1)
	vehicle.position_set(0, 0, 0, relative=True, tolerance=0.1, yaw_valid=True, yaw=-vehicle.get_vfr_hud().heading*pi/180)
	print("Took off to height %2.2f metre" % -vehicle.get_local_position().z)

	init_x = float(vehicle.get_local_position().x)
	init_y = float(vehicle.get_local_position().y)
	vehicle.position_set(traj_len, 0, 0, relative=True, tolerance=0.1, async=False, yaw_valid=False)
	#while(float(vehicle.get_local_position().x)-init_x < traj_len):
	#	pass
	move = float(vehicle.get_local_position().x)-init_x
	print("Moved %2.2f metre" % abs(move))
	
	init_x = float(vehicle.get_local_position().x)
	init_y = float(vehicle.get_local_position().y)
	vehicle.position_set(0, traj_len, 0, relative=True, tolerance=0.1, async=False, yaw_valid=True, yaw=90*pi/180)
	#while(float(vehicle.get_local_position().y)-init_y < traj_len):
	#	pass
	move = float(vehicle.get_local_position().y)-init_y
	print("moved %2.2f metre" % abs(move))

	init_x = float(vehicle.get_local_position().x)
	init_y = float(vehicle.get_local_position().y)
	vehicle.position_set(-traj_len, 0, 0, relative=True, tolerance=0.1, async=False, yaw_valid=True, yaw=90*pi/180)
	#while(float(vehicle.get_local_position().x)-init_x < traj_len):
	#	pass
	move = float(vehicle.get_local_position().x)-init_x
	print("moved %2.2f metre" % abs(move))

	init_x = float(vehicle.get_local_position().x)
	init_y = float(vehicle.get_local_position().y)
	vehicle.position_set(0, -traj_len, 0, relative=True, tolerance=0.1, async=False, yaw_valid=True, yaw=90*pi/180)
	#while(float(vehicle.get_local_position().y)-init_y < traj_len):
	#	pass
	move = float(vehicle.get_local_position().y)-init_y
	print("moved %2.2f metre" % abs(move))

	vehicle.position_set(0, 0, 0, relative=True, tolerance=0.1, yaw_valid=True, yaw=90*pi/180)

	print("Initiating landing")
	vehicle.land(async=False)
	print("Landed")

	vehicle.disconnect()

if __name__=="__main__":
	main()
