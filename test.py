import time
from kidronekit import connect, VehicleMode

connection_string = "tcp:192.168.0.120:5763"

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

while True:
    # Get some vehicle attributes (state)
    print("====================================================")
    print(" GPS Status: %s" % vehicle.gps_0)
    print(" Lat, Lon, Alt: %s" % vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, vehicle.location.global_relative_frame.alt)
    print(" Attitude: %s" % vehicle.attitude)
    print(" Groundspeed: %s" % vehicle.groundspeed)    # settable
    print(" Airspeed: %s" % vehicle.airspeed)    # settable
    print(" Verticalspeed: %s" % vehicle.alt)
    print(" Alt (MSL): %s" % vehicle.throttle) 
    print(" Throttle: %s" % vehicle.climb)  
    print(" Heading: %s" % vehicle.heading)
    print(" Battery: %s" % vehicle.battery)
    print(" Is Armable?: %s" % vehicle.is_armable)
    print(" System status: %s" % vehicle.system_status.state)
    print(" Mode: %s" % vehicle.mode.name)    # settable
    print("====================================================")
    time.sleep(0.5)