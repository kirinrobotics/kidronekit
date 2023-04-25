<img src="./docs/imgs/kidronekit.png" width="100%">

# kidronekit

Premium extended version of dronekit

## Install

```
pip install kidronekit
```

## Getting Started

How to control get drone telemetrys via Mavlink with `kidronekit`:

```python
from kidronekit import connect, VehicleMode

connection_string = "tcp:192.168.0.120:5763"

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)


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
    
```

Output:

```
====================================================
 GPS Status: GPSInfo:fix=6,num_sat=10
 Lat, Lon, Alt: 10.3939486 106.8843985 5.004
 Attitude: Attitude:pitch=-0.00046380647108890116,yaw=-1.9323097467422485,roll=-0.002339589409530163
 Groundspeed: 0.020496351644396782
 Airspeed: 0.0010000000474974513
 Verticalspeed: 17.920000076293945
 Alt (MSL): 0.020496351644396782
 Throttle: -0.005825158208608627
 Heading: 249
 Battery: Battery:voltage=12.587,current=28.16,level=0
 Is Armable?: True
 System status: ACTIVE
 Mode: GUIDED
====================================================
```

## License

Copyright (c) 3D Robotics and Kirinslab. All rights reserved. Licensed under the [Apache 2.0 License](LICENSE) license.