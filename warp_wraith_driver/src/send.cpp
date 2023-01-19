#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/Imu.h>
#include <geometry_msgs/Pose2D.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/JointState.h>
#include <std_msgs/String.h>
#include <std_msgs/Int32MultiArray.h>
#include <std_msgs/UInt64.h>
#include <std_msgs/Bool.h>
#include <math.h>
#include <serial/serial.h>


using namespace std;
using namespace serial;

string message = "";

#define ROS_RECEIVE_BUFFER_SIZE 256
#define ROS_SEND_BUFFER_SIZE 256

//string serialPort;
int baudRate;
int connectTimeout;
uint8_t angles[1024];
bool serialConnected;

serial::Serial WWSerial;
uint8_t *TXBuffer;
uint8_t *RXBuffer;


void JointStateCallback(const sensor_msgs::JointState::ConstPtr & cmd_msg)
{
	ROS_INFO("Callback");
	message = "";
	//message += "H";
	for(int i=0;i<18;i++){
		float value = (float)(cmd_msg->position[i]);

		//message += "S";
		//message += to_string(i);
		//message += "=";

		value = value * 57.2958;
		
		value =value+ 160;
		if(i==2){
			value = 320-value;
		}

		else if(i==5){
			value = 320-value;
		}

		else if(i==8){
			value = 320-value;
		}
		int angle = (int)value;
		angles[i] = (int)value;
		ROS_INFO("Servo%i: %i",i,angle);
		message += to_string(angle);
		if (i != 17)
		{
			message += ",";
		}
	}
	message += "\n";
	//WWSerial.write(angles,sizeof(angles));
	WWSerial.write(message);
	//WWSerial.write(\n);
	ros::Duration(0.1).sleep();

}


int main(int argc, char **argv)
{
	// 初始化ROS节点
	ros::init(argc, argv, "send");
	// 打印调试信息
	ROS_INFO("Node activated");
	// 定义ROS节点处理程序
	ros::NodeHandle nh;
	std::string serial_port_;
	int baudrate_;
	nh.param<std::string>("serial_port", serial_port_, "/dev/ttyACM0");

	ros::Subscriber sub = nh.subscribe("/joint_states", 1, JointStateCallback);
	ROS_INFO("go");

	try
	{
		ROS_INFO("try");
		// 请求打开串口
		WWSerial.setPort(serial_port_);
		ROS_INFO("1");
		WWSerial.setBaudrate(baudrate_);
		ROS_INFO("2");
		serial::Timeout to = serial::Timeout::simpleTimeout(1000);
		ROS_INFO("3");
		WWSerial.setTimeout(to);
		ROS_INFO("4");
		WWSerial.open();
		ROS_INFO("5");
	}
	catch (const std::exception &e)
	{
		ROS_ERROR("%s",e.what());
		return -1;
	}
	
	ros::spin();
	return 0;
}
