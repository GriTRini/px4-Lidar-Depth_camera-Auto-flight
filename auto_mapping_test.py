#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy # ros python
import mavros # mavros
import tf

from geometry_msgs.msg import TwistStamped          # X축,Y축 선형속도 및 각속도 명령폼
from nav_msgs.msg import Odometry                   # 추측항법(IMU, Encoder 기반)
from sensor_msgs.msg import LaserScan               # laser 값
from math import e, pi, degrees, isinf                       # 수학 공식
from sensor_msgs.msg import Range                   # px4flow

class DroneAutoFlight():

    front = 0
    left = 0
    right = 0
    turn_right = 0
    _msg = []
    turn_value = 0.262
    turn_angle = 0.5
    max_left =0
    min_left = 0
    max_right =0
    min_right = 0
    is_takeoff = 0
    pre_right = 0
    yaw = 0
    mapping_front = 0
    
    # 초기 선언
    def __init__(self):
        rospy.init_node('iris_px4_Automapping') # publisher의 노드 이름은 파일과 동일하게 설정함
        self.nav_command = rospy.Publisher("/mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=10)
        self.yaw_command = rospy.Subscriber("/mavros/local_position/odom", Odometry , self.yaw_data)
        self.scan = rospy.Subscriber('/iris_foggy_lidar/scan', LaserScan, self.laser_data)

        self.rate = rospy.Rate(2) #Two messages per second
        self.state_change_time = rospy.Time.now()   
        self.room_turn1= False
        self.room_go1 = False
        self.room_turn2= False
        self.room_go2 = False
        self.room_mapping = False
        self.room_escape_turn1 = False
        self.room_escape_turn2 = False
        self.room_escape_go1 = False
        self.room_escape_go2 = False
        self.corrander = True

    def  autoFlight(self):
        if self.corrander == True:
            self.pre_right = self.right
            print "corrander is True"
            if self.mapping_front > 3.0:
                self.navigation(0.5,0,0,0,0,0)

            else:
                direction = self.pick_free_direction()
                if direction == "left":
                    print("Turning left")
                    self.navigation(0,0,0,0,0,self.turn_value)
                if direction == "right":       
                    print("Turning Right")
                    self.navigation(0,0,0,0,0,-abs(self.turn_value))
                if direction == "right" and direction == "left":
                    self.navigation(0,0,0,0,0,self.turn_value)

            if self.right - self.pre_right >= 3.0:
                print ("right is inf")
                self.navigation(0,0,0,0,0,0)
                current_yaw1 = self.yaw
                if current_yaw1 <= 10.0:
                    current_yaw1 = 359
                self.corrander = False
                self.room_turn1 = True

        if self.room_turn1 == True:
            print"room_turn1 is True"
            while not current_yaw1 - 91 < self.yaw  < current_yaw1 - 89 :
                print( "yaw1 = ",current_yaw1 - 91, self.yaw, current_yaw1 - 89)
                self.navigation(0,0,0,0,0,-abs(self.turn_angle))
            self.navigation(0,0,0,0,0,0)
            self.room_turn1 = False
            self.room_go1 = True

        if self.room_go1 == True:
            print"room_go1 is True"
            while not self.front < 3.5:
                print ("front = ", self.front)
                self.navigation(0.5,0,0,0,0,0)
            self.navigation(0,0,0,0,0,0)
            current_yaw2 = self.yaw
            if current_yaw2 <= 91:
                current_yaw2 = 91
            self.room_go1 = False
            self.room_turn2 = True
            

        if self.room_turn2 == True:
            print("room_turn2 is True")
            while not current_yaw2 - 91 < self.yaw  < current_yaw2 - 89 :
                print( "yaw2 = ",current_yaw2 - 91, self.yaw, current_yaw2 - 89)
                self.navigation(0,0,0,0,0,-abs(self.turn_angle))
            self.navigation(0,0,0,0,0,0)
            self.room_turn2 = False
            self.room_go2 = True

        if self.room_go2 == True:
            print("room_go2 is True")
            while not self.front < 4.5:
                print ("front = ", self.front)
                self.navigation(0.5,0,0,0,0,0)
            self.navigation(0,0,0,0,0,0)
            self.room_go2 = False
            self.room_mapping = True
            
              
        if self.room_mapping == True:
            print("room_mapping is True")
            self.pre_right = self.right
            print ("pre_right = ", self.pre_right)
            if self.mapping_front > 3.0:
                print ("front = ", self.front)
                self.navigation(0.2,0,0,0,0,0)

            else:
                direction = self.pick_free_direction()
                if direction == "left":
                    print("Turning left")
                    self.navigation(0,0,0,0,0,self.turn_value)
                if direction == "right": 
                    print("Turning Right")
                    self.navigation(0,0,0,0,0,-abs(self.turn_value))
                if direction == "right" and direction == "left":
                    self.navigation(0,0,0,0,0,self.turn_value)

            print ('right = ', self.right)
            if self.right - self.pre_right >= 2.0:
                current_yaw3 = self.yaw
                if current_yaw3 <= 91:
                    current_yaw3 = 91
                self.room_mapping = False
                self.room_escape_turn1 = True

        if self.room_escape_turn1 == True:
            print("room_escape_turn1 is True")
            while not current_yaw3 - 91 < self.yaw < current_yaw3 - 89:
                self.navigation(0,0,0,0,0,-abs(self.turn_value))
                print( "yaw3 = ",current_yaw3 - 91, self.yaw, current_yaw3 - 89)
            self.navigation(0,0,0,0,0,0)

            if 80 <= self.yaw <= 100 or 260 <= self.yaw <= 290:
                print("not-escape")
                self.room_escape_turn1 = False
                self.room_escape_go1 = True
                
            else:
                print("escape")
                self.room_escape_turn1 = False
                self.room_escape_go2 = True

        if self.room_escape_go1 == True:
            print("room_escape_go is True")
            while not self.front < 3.0:
                self.navigation(0.5,0,0,0,0,0)
            self.navigation(0,0,0,0,0,0)
            current_yaw4 = self.yaw
            if current_yaw4 <= 91:
                    current_yaw4 = 91
            self.room_escape_go1 = False
            self.room_escape_turn2 = True

        if self.room_escape_turn2 == True:
            print("room_escape_turn2 is True")
            while not current_yaw4 - 91 < self.yaw < current_yaw4 - 89:
                self.navigation(0,0,0,0,0,-abs(self.turn_angle))
                print( "yaw4 = ",current_yaw4 - 91, self.yaw, current_yaw4 - 89)
            self.navigation(0,0,0,0,0,0)
            self.room_escape_turn2 = False
            self.room_escape_go2 = True

        if self.room_escape_go2 == True:
            print("room_escape_go2 is True")
            while isinf(self.right):
                self.navigation(0.5,0,0,0,0,0)
            self.room_escape_go2 = False
            self.corrander = True


    # 원하는 방향으로 이동
    def navigation(self,Lx,Ly,Lz,Ax,Ay,Az):
        self.position = TwistStamped()
        self.position.header.stamp = rospy.Time.now()
        self.position.header.frame_id = ""
        self.position.twist.linear.x = Lx
        self.position.twist.linear.y = Ly
        self.position.twist.linear.z = Lz
        self.position.twist.angular.x = Ax
        self.position.twist.angular.y = Ay
        self.position.twist.angular.z = Az
        self.nav_command.publish(self.position)

    # yaw data 업데이트
    def yaw_data(self, msg):
        quaternion =  (msg.pose.pose.orientation.x,
                                    msg.pose.pose.orientation.y,
                                    msg.pose.pose.orientation.z,
                                    msg.pose.pose.orientation.w)
        theta = tf.transformations.euler_from_quaternion(quaternion)[2]
        
        if theta < 0:
            theta = theta + pi * 2
        if theta > pi * 2:
            theta = theta - pi * 2
        
        self.yaw = degrees(theta) 

#_________________Navigation Algorithm_____________________

    def laser_data(self, msg):
        self._msg = msg.ranges

        #READING AT NEGATIVE ANGLES - To the right of the drone
        self.front = max(msg.ranges[710:730])
        self.mapping_front = min(msg.ranges[660:780])
        self.right = min(msg.ranges[290 : 360])
        self.turn_right = min(msg.ranges[320:360])

    def pick_free_direction(self):
        print("Entered Here")

        if self.Is_rangeFree(self._msg, "left") and self.Is_rangeFree(self._msg,"right"):
            if isinf(self.max_right) and isinf(self.max_left):
                print("both inf")
                return "right"
            if isinf(self.max_left):
                print("max left - inf")
                return "left"
            if isinf(self.max_right):
                print("Max Right -inf")
                return "right"
            if self.max_right > self.max_left:
                print("max right > max left")

                return "right"
            elif self.max_left > self.max_right:
                print("max left > max right")
                return "left"

        if self.Is_rangeFree(self._msg,"left"):
            print("left")
            return "left"
        if self.Is_rangeFree(self._msg,"right"):
            print("right")
            return "right"

    def Is_rangeFree(self,rangeList,direction):
        if len(rangeList) != 0:
            if  direction == "left":
                left_array = rangeList[960:1100]
                self.min_left = min(left_array)
                self.max_left = max(left_array)

                if self.min_left >  1.2:
                    print "left true"
                    return True
                else:
                    print "left false"
                    return False

            elif direction == "right":
                right_array = rangeList[360:480]
                self.min_right = min(right_array)
                self.max_right = max(right_array)

                if self.min_right > 1.2:
                    print "right true"
                    return True
                else:
                    print "right false"
                    return False
        return False

if __name__ == '__main__':
    trip = DroneAutoFlight()
    while not rospy.is_shutdown():
        trip.autoFlight()




