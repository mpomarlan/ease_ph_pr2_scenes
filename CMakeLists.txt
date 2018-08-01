cmake_minimum_required(VERSION 2.8.3)
project(ease_ph_pr2_scenes)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES 
  CATKIN_DEPENDS 
  DEPENDS 
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

