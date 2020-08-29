# screwdriver_ws
Installation
```
cd ~ # Clone workspace to home directory
git clone https://github.com/wafflecat/screwdriver_ws.git
cd screwdriver_ws
catkin_make
```

Add screwdriver_ws workspace to .bashrc
```
echo "source source ~/screwdriver_ws/devel/setup.bash" >> ~/.bashrc
```

Usage
```
roslaunch screwdriver joy_teleop_using_rates.launch
```
