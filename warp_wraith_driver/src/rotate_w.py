#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
 
class rotate_w:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node('rotate_w', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        #warp_wraith = moveit_commander.MoveGroupCommander('warp_wraith')
        abde = moveit_commander.MoveGroupCommander('abde')
	bcef = moveit_commander.MoveGroupCommander('bcef')
	acdf = moveit_commander.MoveGroupCommander('acdf')

        #ad = moveit_commander.MoveGroupCommander('ad')
	#be = moveit_commander.MoveGroupCommander('be')
	#cf = moveit_commander.MoveGroupCommander('cf')
        # 设置机械臂和夹爪的允许误差值
        #warp_wraith.set_goal_joint_tolerance(0.001)
        abde.set_goal_joint_tolerance(0.001)
	bcef.set_goal_joint_tolerance(0.001)
	acdf.set_goal_joint_tolerance(0.001)
	#ad.set_goal_joint_tolerance(0.001)
	#be.set_goal_joint_tolerance(0.001)
	#cf.set_goal_joint_tolerance(0.001)
        
        # 控制机械臂先回到初始化位置

         
        acdf.set_named_target('rotate_w_a0')
        acdf.go()
	acdf.set_named_target('rotate_default_acdf')
	acdf.go()
	abde.set_named_target('rotate_w_b0')
	abde.go()
	abde.set_named_target('rotate_default_abde')
	abde.go()
	bcef.set_named_target('rotate_w_c0')
	bcef.go()
	bcef.set_named_target('rotate_default_bcef')
	bcef.go()

	acdf.set_named_target('rotate_w_a0')
        acdf.go()
	acdf.set_named_target('rotate_default_acdf')
	acdf.go()
	abde.set_named_target('rotate_w_b0')
	abde.go()
	abde.set_named_target('rotate_default_abde')
	abde.go()
	bcef.set_named_target('rotate_w_c0')
	bcef.go()
	bcef.set_named_target('rotate_default_bcef')
	bcef.go()

	acdf.set_named_target('rotate_w_a0')
        acdf.go()
	acdf.set_named_target('rotate_default_acdf')
	acdf.go()
	abde.set_named_target('rotate_w_b0')
	abde.go()
	abde.set_named_target('rotate_default_abde')
	abde.go()
	bcef.set_named_target('rotate_w_c0')
	bcef.go()
	bcef.set_named_target('rotate_default_bcef')
	bcef.go()

        rospy.sleep(1)

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)
 
if __name__ == "__main__":
    try:
        rotate_w()
    except rospy.ROSInterruptException:
        pass
