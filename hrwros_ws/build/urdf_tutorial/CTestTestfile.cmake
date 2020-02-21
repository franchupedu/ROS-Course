# CMake generated Testfile for 
# Source directory: /home/franchupedu/hrwros_ws/src/hrwros/urdf_tutorial
# Build directory: /home/franchupedu/hrwros_ws/build/urdf_tutorial
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_urdf_tutorial_roslaunch-check_launch "/home/franchupedu/hrwros_ws/build/urdf_tutorial/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/franchupedu/hrwros_ws/build/urdf_tutorial/test_results/urdf_tutorial/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/franchupedu/hrwros_ws/build/urdf_tutorial/test_results/urdf_tutorial" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o '/home/franchupedu/hrwros_ws/build/urdf_tutorial/test_results/urdf_tutorial/roslaunch-check_launch.xml' '/home/franchupedu/hrwros_ws/src/hrwros/urdf_tutorial/launch' ")
subdirs("gtest")
