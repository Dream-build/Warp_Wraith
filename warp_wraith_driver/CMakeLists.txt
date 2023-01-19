cmake_minimum_required(VERSION 3.0.2)
project(warp_wraith_driver)

find_package(catkin REQUIRED COMPONENTS
	roslaunch
	geometry_msgs
	nav_msgs
	roscpp
	rospy
	std_msgs
	sensor_msgs
	tf
	serial
)

#add_message_files(FILES
#	
#)

#add_service_files(FILES
#	
#)

generate_messages(
	DEPENDENCIES
	geometry_msgs   
	nav_msgs   
	sensor_msgs
)

catkin_package(
	CATKIN_DEPENDS 
	roscpp 
	std_msgs 
	message_runtime
)

include_directories(
	include
	${catkin_INCLUDE_DIRS}
)

#add_library(warp_wraith_driver 
#	src/send.cpp
#)
add_executable(warp_wraith_driver 	
src/send.cpp
src/stand.py
)


target_link_libraries(warp_wraith_driver ${catkin_LIBRARIES})
#add_executable(warp_wraith_driver_sub 	src/sub.cpp)
#target_link_libraries(warp_wraith_driver_sub ${catkin_LIBRARIES})




#target_link_libraries(warp_wraith_driver)
