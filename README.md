# ease_ph_pr2_scenes
A Unity project with scenes involving the PR2.

# Running a Unity+ROS scenario

Each scenario contains a ROS world and a Unity scene.

First, initialize the ROS world for the scenario. To do this, go to this package's launch folder and run the appropriate scenario launch file, for example
```
roslaunch scenario_nodding.launch
```

To run the Unity part, start Unity and load this project. Then, select the appropriate scene for the scenario (for the example above, nodding), then run the scene.
