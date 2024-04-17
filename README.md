# LQR_SBR_Gazebo

Place the project file that has all the launch files and scripts inside src folder   "~/colcon_ws directory/src"

get to "~/colcon_ws directory", then open terminal and run  then "colcon build –symlink-install" (only once)

Now run "source install/setup.bash" in colcon_ws

Now run “ros2 launch teeterbot_gazebo teeterbot_empty_world.launch.py”

Go to src/teeterbot/LQR and run “python3 required_python_file.py” 

