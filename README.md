# px4-project
## 1. px4 파일 설치
- 밑에 홈페이지에서 받으면 된다.  

홈페이지는 https://docs.px4.io/master/en/dev_setup/dev_env_linux_ubuntu.html#gazebo-jmavsim-and-nuttx-pixhawk-targets 이다.

- 파일 다운로드 

![Screenshot from 2021-07-19 09-05-19](https://user-images.githubusercontent.com/43773374/126086513-40fb3178-cbe2-4a4a-9a2b-e832fbe3b679.png)

```
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
```
- 다운로드 받은후 입력
- Run the ubuntu.sh with no arguments (in a bash shell) to install everything:
![Screenshot from 2021-07-19 09-08-51](https://user-images.githubusercontent.com/43773374/126086516-e56d34a5-e21b-4e67-8830-aee0491e5ceb.png)

```
bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
```

## 2. ros/gazebo 설치
- 해당 명령어를 입력해야 나중에 catkin build가 가능
- ros홈페이지에서 설치하는 방식대로 하면 catkin build가 되지 않음 
- ubuntu 18.04이며 melodic 설치이다.
- 밑에 내용은 해당 주소내용을 복사해오는 것이다.
![Screenshot from 2021-07-19 09-10-18](https://user-images.githubusercontent.com/43773374/126086529-9425df94-291f-42c3-991e-fb9eae0cdd78.png)

```
wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
```
- 복사한 내용 실행
```
bash ubuntu_sim_ros_melodic.sh
```

- 만약에 오류가 뜨게 되면 밑의 명령어를 한번 입력한 후에 위의 명령어를 입력하면 된다. (경험상)

```
sudo rosdep init
rosdep update
```

## 3. gazebo 실행 해보기
```
cd PX4-Autopilot
```
- 위의 내용을 입력한 후에 밑의 명령어를 입력한후에 gazebo에서 드론이 나오는지 확인한다.
```
make px4_sitl gazebo
```

## 4. bash에 입력하기
- 명령어를 입력하면 PX4-Autopilot에 있는 내용을 roslaunch가 가능하다.
![Screenshot from 2021-07-19 09-11-17](https://user-images.githubusercontent.com/43773374/126086564-bc4041bd-74f5-49bd-9bb4-7c2ac64e28f8.png)

```
source ~/PX4-Autopilot/Tools/setup_gazebo.bash ~/PX4-Autopilot/ ~/PX4-Autopilot/build/px4_sitl_default

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/PX4-Autopilot

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/PX4-Autopilot/Tools/sitl_gazebo
```

```
source ~/.bashrc
```
- 위의 내용을 하고 나서 밑에 내용이 터미널 창에 뜨면 성공이다.
![Screenshot from 2021-07-19 09-11-59](https://user-images.githubusercontent.com/43773374/126086590-9f3a5a95-b8ea-4139-9b8d-3b6a2517a77d.png)

```
GAZEBO_PLUGIN_PATH :/home/jeong/PX4-Autopilot/build/px4_sitl_default/build_gazebo
GAZEBO_MODEL_PATH :/home/jeong/PX4-Autopilot//Tools/sitl_gazebo/models
LD_LIBRARY_PATH /home/jeong/catkin_ws/devel/lib:/opt/ros/melodic/lib:/home/jeong/PX4-Autopilot/build/px4_sitl_default/build_gazebo
```


## 5. github에서 사용할 custom_f450 프레임
- home 안에 설치한다.
```
git clone https://github.com/GriTRini/px4-project.git
```
- 안에 있는 px4-quadrotor-HW-parts-main 파일로 들어간다.
```
cd ~/px4-project/px4-quadrotor-HW-parts-main/
```
- px4-Autopilot model 안에 custom_f450을 넣는다.
```
cp -r custom_f450/ ~/PX4-Autopilot/Tools/sitl_gazebo/models/
```
- 1026_custom_f450 파일을 해당위치에 넣는다.
```
cp 1026_custom_f450 ~/PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframes/
```
- px4_add_romfs_files 에 1026_custom_f450 을 적어서 추가한다.
![Screenshot from 2021-07-19 09-14-21](https://user-images.githubusercontent.com/43773374/126086667-44e8aae2-ae95-4138-86c2-380507d2f800.png)

```
gedit ~/PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframes/CMakeLists.txt
```
- set(models 안에 custom_f450을 적어서 추가한다.
![Screenshot from 2021-07-19 09-15-12](https://user-images.githubusercontent.com/43773374/126086682-c3685fc7-05c2-4a97-ab46-730273165d0d.png)

```
gedit ~/PX4-Autopilot/platforms/posix/cmake/sitl_target.cmake
```
- 위의 내용을 진행하였으면 roslaunch를 실행한다.
- iris 드론이 켜지는지 확인한다.
```
roslaunch px4 mavros_posix_sitl.launch
```
- 그다음 우리가 넣은 custom_f450드론을 실행시킨다.

- PX4-Autopilot / launch / mavros_posix_sitl.launch를 실행시킨다.
- 14행에 있는 iris를 custom_f450으로 수정한다.
- 만약 오류가 난다면 /home/jeong/.ros/etc/init.d-posix/airframes에서 1026_custom_f450파일을 추가한다.
- 그 다음 밑의 명령어를 실행시킨다.

```
roslaunch px4 mavros_posix_sitl.launch
```

- 만약 오류가 난다면 혹시 .ros 파일에 있는 airframe 안에 처음에 넣었던 1026_custom_f450 파일이 있는지 확인하라는 오류인지 확인해야한다.
- 저는 해당 오류가 떠서 .ros파일안 경로에 들어가서 처음에 복사 붙여넣기한 1026_custom_f450파일을 airframe 파일안에 넣었다.
- 그리고 나서 다시 실행하니 gazebo에서 실행이 되었다.

## 6. orb_slam2 설치
- 파일 설치
```
https://drive.google.com/file/d/1_futH5n7Knyy_PfXcfwZ_K2-hsqBnwtR/view?usp=sharing
```
- 압축파일을 catkin_ws/src 에 풀어야함

- build
```
cd ~/catkin_ws && catkin build
```

- rosdep 설치
```
sudo rosdep init
rosdep update
```
- Eigen3 설치
```
sudo apt install libeigen3-dev
```
- 먼저 위에 git에서 받은 파일중에 orb_slam_2_ros를 catkin_ws/src로 옮긴다.
```
cp -r px4-project/orb_slam_2_ros/ ~/catkin_ws/src
```
- launch 실행 파일 수정
```
cd catkin_ws/src/orb_slam_2_ros/ros/launch/ && gedit orb_slam2_d435_rgbd.launch
```
- line 5, 6 수정
![스크린샷, 2021-07-23 10-32-40](https://user-images.githubusercontent.com/43773374/126727994-3c25a017-12c8-48c2-924f-b8ec5dfe5e4a.png)
- line5 는 to에 /d435/rgb/image_raw
- line6 는 to에 /d435/depth/image_rect_raw

- build
```
cd ~/catkin_ws && catkin build
```
- 실행
```
roslaunch orb_slam2_ros orb_slam2_d435_rgbd.launch
```

## 7. qgroundcontrol을 설치한다.

- 해당 홈페이지에서 GCS를 설치한다.
![Screenshot from 2021-07-19 09-16-07](https://user-images.githubusercontent.com/43773374/126086709-6e422694-1f0d-4144-8ef1-8e224b7d0773.png)

https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html

- 
![Screenshot from 2021-07-19 09-18-26](https://user-images.githubusercontent.com/43773374/126086777-e09dbb74-f5f2-4b72-a25f-bb4c631d2580.png)

## 8. 다운받은 custom_f450 파일 rviz
- px4_config.yaml 에서 line 71 인 #local_position 부분에 send 의 value 값을 false 에서 true 로 바꿔주면 map 에 base_link 가 정상적으로 연결된다.
```
cd ~/catkin_ws/src/mavros/mavros/launch && gedit px4_config.yaml
```

```
cd px4-quadrotor-HW-parts-main/
```
```
cp -r f450 ~/catkin_ws/src
```
```
cd ~/catkin_ws && catkin build f450 && source devel/setup.bash
```
- 그다음 launch파일을 실행 시키면 된다.
```
roslaunch f450 display.launch
```
- 만약 오류가 난다면 오류 내용을 보고 패키지를 설치하면 된다.
- ![Screenshot from 2021-07-17 18-14-45](https://user-images.githubusercontent.com/43773374/126032754-35102308-6a0f-4731-baac-7660eb94e621.png)
- 저는 이러한 오류가 떴는데 해당 joint_state_publisher_gui를 설치한 후에 state_publisher를 설치하였다.
- melodic 버전을 확인하고 설치하면 된다.
- https://github.com/ros/joint_state_publisher 여기 사이트에 들어가서 주소를 복사한다음에 catkin build 실행
```
cd catkin_ws/src
```
```
git clone https://github.com/ros/joint_state_publisher.git
```
```
cd .. && catkin build
```
- 만약 state_publisher 오류가 뜬다면 밑의 내용을 실행한다.
```
cd catkin_ws/src
```
```
git clone https://github.com/ros/robot_state_publisher.git
```
```
cd .. && catkin build
```
![스크린샷, 2021-07-19 20-21-18](https://user-images.githubusercontent.com/43773374/126152811-1d583462-a290-4f5f-ad8c-43d224992538.png)

- 만약 사진과 같은 오류가 뜬다면 밑의 코드를 실행해라
```
sudo apt update
sudo apt install ros-<your_ros_version>-joint-state-publisher-gui
```
- ubuntu 16.04 이면 kinetic, ubuntu 18.04 이면 melodic, ubuntu 20.04 이면 noetic이다.
- map을 fix_frame으로 고정하고 드론을 띄우기 위해서는 send 의 value 값을 false 에서 true 로 바꿔주시면 map 에 base_link 가 정상적으로 연결됩니다.
```
gedit ~/catkin_ws/src/mavros/mavros/launch/px4_config.yaml
```
![스크린샷, 2021-07-23 10-40-53](https://user-images.githubusercontent.com/43773374/126729782-35e69aff-1653-4fa0-946f-4826185130bf.png)

- 이후에 밑에 내용을 실행한다.
```
 roslaunch f450 display.launch
 ```
 - 
 ![Screenshot from 2021-07-17 18-38-39](https://user-images.githubusercontent.com/43773374/126032892-b5fc2d74-c9f6-4fb7-9874-416852e96e14.png)
 

## 9. 실행

- 터미널 창에 명령어를 입력한다.
- gazebo 실행
```
roslaunch px4 mavros_posix_sitl.launch
```
- rviz 실행
```
roslaunch px4 display.launch
```
```
- slam2 실행
roslaunch orb_slam2_ros orb_slam2_d435_rgbd.launch
```


## 11. px4-avoidance 설치
- Install avoidance module dependencies (pointcloud library and octomap).
```
sudo apt install libpcl1 ros-melodic-octomap-*
```
- catkin/src 안에 avoidance 파일 다운로드
```
cd ~/catkin_ws/src
git clone https://github.com/PX4/avoidance.git
```
- catkin build
```
cd ~/catkin_ws && catkin build
```
- Qt-related errors 예방하기 위해서 .bashrc 에 넣기
```
export QT_X11_NO_MITSHM=1
```
- local_planner_stereo: simulates a vehicle with a stereo camera that uses OpenCV's block matching algorithm (SGBM by default) to generate depth information
```
roslaunch local_planner local_planner_stereo.launch
```
![스크린샷, 2021-07-26 16-41-42](https://user-images.githubusercontent.com/43773374/126951496-ee0ee9bd-b874-4190-8c4c-c807cf02c431.png)

- local_planner_depth_camera: simulates vehicle with one forward-facing kinect sensor
```
roslaunch local_planner local_planner_depth-camera.launch
```
![스크린샷, 2021-07-26 16-42-42](https://user-images.githubusercontent.com/43773374/126951634-954926f2-fdac-4118-98e6-8c10b4626664.png)

- local_planner_sitl_3cam: simulates vehicle with 3 kinect sensors (left, right, front)
```
roslaunch local_planner local_planner_sitl_3cam.launch
```
![스크린샷, 2021-07-26 16-43-33](https://user-images.githubusercontent.com/43773374/126951792-e2aa4f49-c6fb-4e78-84f0-7be1f9aac8dc.png)

- Global Planner (advanced, not flight tested) This section shows how to start the global_planner and use it for avoidance in offboard mode.
```
roslaunch global_planner global_planner_stereo.launch
```
![스크린샷, 2021-07-26 16-44-22](https://user-images.githubusercontent.com/43773374/126951881-585879f5-6ec2-4861-a83e-4b7a101d312d.png)

- 해당 코드를 실행하게 되면 왼쪽 오른쪽 카메라가 보여지고 전면 카메라가 보이게 된다.
```
rosrun image_view stereo_view stereo:=/stereo image:=image_rect_color
```
![스크린샷, 2021-07-26 16-45-13](https://user-images.githubusercontent.com/43773374/126952151-1336b3bc-328e-40a3-bb67-43cb96f5f4b4.png)

- 수정없이 그냥 하게 된다면 gazebo가 실행되지 않고 rviz만 실행이 된다. gazebo도 실행을 시키려면 밑의 사진대로 하면 된다.
```
cd ~/catkin_ws/src/avoidance/avoidance/launch && gedit avoidance_sitl_mavros.launch
```
![스크린샷, 2021-07-26 16-40-05](https://user-images.githubusercontent.com/43773374/126951252-5a3446d5-c36e-4203-85d9-086fc38e92d4.png)
- line 3에 있는 false를 true로 바꾸게 되면 gazebo가 화면에 출력된다.

## 12. 2d laser slam
- 먼저 lidar가 달린 드론을 제작해야 한다.
- 본인은 px4내에 있는 iris_foggy_lidar를 가지고 만들었다.
- 먼저 xtdrone에 있는 hokuyo lidar를 px4 models 안으로 옮긴다.
- xtdrone 설치
```
git clone https://gitee.com/robin_shaun/XTDrone.git
```
- xt drone 안에 있는 hokuyo_lidar 파일을 px4_Autofpilot 안으로 옮긴다.

- /XTDrone/sitl_config/models에 있는 hokuyo_lidar 파일을 복사한 후에 PX4-Autopilot/Tools/sitl_gazebo/models 안에 넣는다.
- /XTDrone/sitl_config/worlds에 있는 indoor3.world를 가지고 와서 PX4-Autopilot/Tools/sitl_gazebo/worlds에 넣는다.
- 
- 그리고 나서 models 안에 있는 iris_foggy_lidar.sdf 파일을 수정한다.
```
cd ~/PX4-Autopilot/Tools/sitl_gazebo/models/iris_foggy_lidar && gedit iris.foggy_lidar.sdf
```
- 밑에 있는 코드를 복사후 붙여 넣는다.
```html
<?xml version="1.0" ?>
<sdf version='1.5'>
  <model name='iris_foggy_lidar'>

    <include>
      <uri>model://iris</uri>
    </include> 
<!--
    <include>
      <uri>model://foggy_lidar</uri>
      <pose>0 0 0.1 0 1.571 0</pose>
    </include>
    <joint name="foggy_lidar_joint" type="revolute">
      <parent>iris::base_link</parent>
      <child>foggy_lidar::link</child>
      <pose>0 0 0.1 0 1.571 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>
-->
<!-- For Hokuyo Lidar Payload -->
    <include>
        <uri>model://hokuyo_lidar</uri>
        <pose>0 0 0.1 0 0 0</pose>
      </include>
    <joint name="lidar_joint" type="fixed">
      <parent>iris::base_link</parent>
      <child>hokuyo_lidar::link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>
  </model>
</sdf>
<!-- vim: set noet fenc=utf-8 ff=unix sts=0 sw=4 ts=4 : -->
```
- 그다음에 실행할 mavros_posix_sitl.launch 파일을 수정해야 한다.
```
cd ~/PX4-Autopilot/launch && gedit mavros_posix_sitl.launch
```
- line 14에서 default를 iris_foggy_lidar로 수정한다.
- line 15에서 default를 indoor3.world로 수정한다.

![123](https://user-images.githubusercontent.com/43773374/127287599-f5decda6-da03-49d7-a493-af1c354306f7.png)




- 먼저 pkg를 다운로드 한다.
```
sudo apt install ros-<your_ros_version>-laser-scan-matcher
```

- 해당 패키지를 받으면 opt파일 안에 존재한다.
```
cd /opt/ros/melodic/share/laser_scan_matcher/demo
```
- 폴더 안에 있는 파일은 읽기 전용으로 밖에 열리지 않아서 명령어를 입력하여 파일을 열어야 한다.
```
sudo gedit demo.launch
```
- demo.launch 파일을 연다.
- 해당 파일은 laser slam을 작동 시키기 위한 launch 파일이다.
- 밑에 있는 내용을 복사해서 붙여넣기 하면 된다.
```html
<!--
Example launch file: launches the scan matcher with pre-recorded data
-->

<launch>
  <arg name="IS_TWISTSTAMPED" default="true" />
  <arg name="use_rviz" default="true" />
  <arg name="publish_covariance" default="false"/>

  #### publish an example base_link -> laser transform ###########
  <node pkg="tf" type="static_transform_publisher" name="iris_base_link_to_laser" args="0.0 0.0 0.1 0.0 0.0 0.0 /iris/base_link /iris_foggy_lidar/laser_2d 40" />
  #### set up data playback from bag #############################
  
  <param name="/use_sim_time" value="true"/>
  <param name="/stamped_vel" value="$(arg IS_TWISTSTAMPED)"/>

  <group if="$(arg use_rviz)">
    <node pkg="rviz" type="rviz" name="rviz"
          args="-d $(find laser_scan_matcher)/demo/demo.rviz"/>
  </group>
  #### start the laser scan_matcher ##############################

  <group if="$(arg publish_covariance)">
    <param name="laser_scan_matcher_node/do_compute_covariance" value="1"/>
    <param name="laser_scan_matcher_node/publish_pose_with_covariance" value="true"/>
    <param name="laser_scan_matcher_node/publish_pose_with_covariance_stamped" value="true"/>
  </group>
  <node pkg="laser_scan_matcher" type="laser_scan_matcher_node" name="laser_scan_matcher_node" output="screen">
    <param name="fixed_frame" value = "odom"/>
    <param name="base_frame" value = "iris/base_link"/>
    <param name="max_iterations" value="10"/>
    <param name="use_imu" value="false"/>
    <param name="use_odom" value="false"/>
    <remap from="scan" to="/iris_foggy_lidar/scan"/>
    <remap from="pose2D" to="iris/pose2D"/>
  </node>

</launch>
```
- demo.rviz에는 밑에 내용을 붙여넣으면 된다.
```
sudo gedit demo.rviz
```
```yaml
Panels:
  - Class: rviz/Displays
    Help Height: 78
    Name: Displays
    Property Tree Widget:
      Expanded:
        - /Global Options1
        - /Status1
        - /Grid1
        - /LaserScan1
        - /TF1
        - /TF1/Frames1
      Splitter Ratio: 0.5
    Tree Height: 434
  - Class: rviz/Selection
    Name: Selection
  - Class: rviz/Tool Properties
    Expanded:
      - /2D Pose Estimate1
      - /2D Nav Goal1
      - /Publish Point1
    Name: Tool Properties
    Splitter Ratio: 0.588679
  - Class: rviz/Views
    Expanded:
      - /Current View1
    Name: Views
    Splitter Ratio: 0.5
  - Class: rviz/Time
    Experimental: false
    Name: Time
    SyncMode: 0
    SyncSource: LaserScan
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Size: 1
      Class: rviz/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.03
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 10
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 0.2
      Autocompute Intensity Bounds: true
      Autocompute Value Bounds:
        Max Value: 10
        Min Value: -10
        Value: true
      Axis: Z
      Channel Name: intensity
      Class: rviz/LaserScan
      Color: 255; 0; 0
      Color Transformer: FlatColor
      Decay Time: 0
      Enabled: true
      Invert Rainbow: false
      Max Color: 255; 0; 0
      Max Intensity: 4096
      Min Color: 0; 0; 0
      Min Intensity: 0
      Name: LaserScan
      Position Transformer: XYZ
      Queue Size: 10
      Selectable: true
      Size (Pixels): 3
      Size (m): 0.1
      Style: Flat Squares
      Topic: /iris_0/scan
      Use Fixed Frame: true
      Use rainbow: true
      Value: true
    - Class: rviz/TF
      Enabled: true
      Frame Timeout: 15
      Frames:
        All Enabled: true
        base_link:
          Value: true
        laser:
          Value: true
        odom:
          Value: true
      Marker Scale: 3
      Name: TF
      Show Arrows: true
      Show Axes: true
      Show Names: true
      Tree:
        odom:
          base_link:
            laser:
              {}
      Update Interval: 0
      Value: true
  Enabled: true
  Global Options:
    Background Color: 0; 0; 0
    Fixed Frame: odom
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz/Interact
      Hide Inactive Objects: true
    - Class: rviz/MoveCamera
    - Class: rviz/Select
    - Class: rviz/FocusCamera
    - Class: rviz/Measure
    - Class: rviz/SetInitialPose
      Topic: /initialpose
    - Class: rviz/SetGoal
      Topic: /move_base_simple/goal
    - Class: rviz/PublishPoint
      Single click: true
      Topic: /clicked_point
  Value: true
  Views:
    Current:
      Angle: 0
      Class: rviz/TopDownOrtho
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.06
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Name: Current View
      Near Clip Distance: 0.01
      Scale: 150
      Target Frame: <Fixed Frame>
      Value: TopDownOrtho (rviz)
      X: 0
      Y: 0
    Saved: ~
Window Geometry:
  Displays:
    collapsed: false
  Height: 721
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd00000004000000000000013c0000023dfc0200000008fb0000001200530065006c0065006300740069006f006e00000001e10000009b0000005300fffffffb0000001e0054006f006f006c002000500072006f007000650072007400690065007302000001ed000001df00000185000000a3fb000000120056006900650077007300200054006f006f02000001df000002110000018500000122fb000000200054006f006f006c002000500072006f0070006500720074006900650073003203000002880000011d000002210000017afb000000100044006900730070006c00610079007301000000360000023d000000b700fffffffb0000002000730065006c0065006300740069006f006e00200062007500660066006500720200000138000000aa0000023a00000294fb00000014005700690064006500530074006500720065006f02000000e6000000d2000003ee0000030bfb0000000c004b0069006e0065006300740200000186000001060000030c00000261000000010000010f0000023dfc0200000003fb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000041000000780000000000000000fb0000000a0056006900650077007301000000360000023d0000009b00fffffffb0000001200530065006c0065006300740069006f006e010000025a000000b200000000000000000000000200000490000000a9fc0100000001fb0000000a00560069006500770073030000004e00000080000002e10000019700000003000004000000003efc0100000002fb0000000800540069006d00650100000000000004000000024500fffffffb0000000800540069006d00650100000000000004500000000000000000000001a90000023d00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Selection:
    collapsed: false
  Time:
    collapsed: false
  Tool Properties:
    collapsed: false
  Views:
    collapsed: false
  Width: 1024
  X: -2
  Y: -2
  ```
- mapping을 하기 위해서는 demo_gmapping.launch파일을 수정해야 합니다.
```
sudo gedit demo_gmapping.launch
```
```html
<!-- 
Example launch file: uses laser_scan_matcher together with
slam_gmapping 
-->

<launch>

  <param name="/use_sim_time" value="true"/>

#### publish an example base_link -> laser transform ###########
  <node pkg="tf" type="static_transform_publisher" name="iris_base_link_to_laser" args="0.0 0.0 0.1 0.0 0.0 0.0 /iris/base_link /iris_foggy_lidar/laser_2d 40" />

  #### start rviz ################################################

  <node pkg="rviz" type="rviz" name="rviz" 
    args="-d $(find laser_scan_matcher)/demo/demo_gmapping.rviz"/>

  #### start the laser scan_matcher ##############################

  <node pkg="laser_scan_matcher" type="laser_scan_matcher_node"
    name="laser_scan_matcher_node" output="screen">
    <param name="fixed_frame" value = "odom"/>
    <param name="base_frame" value = "iris/base_link"/>
    <param name="max_iterations" value="10"/>
    <param name="use_imu" value="false"/>
    <param name="use_odom" value="false"/>
    <remap from="scan" to="/iris_foggy_lidar/scan"/>
    <remap from="pose2D" to="iris/pose2D"/>
  </node>

  #### start gmapping ############################################

  <node pkg="gmapping" type="slam_gmapping" name="slam_gmapping" output="screen">
    <param name="base_frame" value='iris/base_link'/>
    <param name="map_udpate_interval" value="1.0"/>
    <param name="maxUrange" value="5.0"/>
    <param name="sigma" value="0.1"/>
    <param name="kernelSize" value="1"/>
    <param name="lstep" value="0.15"/>
    <param name="astep" value="0.15"/>
    <param name="iterations" value="1"/>
    <param name="lsigma" value="0.1"/>
    <param name="ogain" value="3.0"/>
    <param name="lskip" value="1"/>
    <param name="srr" value="0.1"/>
    <param name="srt" value="0.2"/>
    <param name="str" value="0.1"/>
    <param name="stt" value="0.2"/>
    <param name="linearUpdate" value="1.0"/>
    <param name="angularUpdate" value="0.5"/>
    <param name="temporalUpdate" value="0.4"/>
    <param name="resampleThreshold" value="0.5"/>
    <param name="particles" value="10"/>
    <param name="xmin" value="-5.0"/>
    <param name="ymin" value="-5.0"/>
    <param name="xmax" value="5.0"/>
    <param name="ymax" value="5.0"/>
    <param name="delta" value="0.02"/>
    <param name="llsamplerange" value="0.01"/>
    <param name="llsamplestep" value="0.05"/>
    <param name="lasamplerange" value="0.05"/>
    <param name="lasamplestep" value="0.05"/>
    <remap from="scan" to="/iris_foggy_lidar/scan"/>
    <remap from="pose2D" to="iris/pose2D"/>
  </node>

</launch>
```
- demo_gmapping.rviz 파일을 수정한다.
```
sudo gedit demo_gmapping.rviz
```
```yaml
Panels:
  - Class: rviz/Displays
    Help Height: 78
    Name: Displays
    Property Tree Widget:
      Expanded:
        - /Global Options1
        - /Status1
        - /Grid1
        - /LaserScan1
        - /TF1
        - /TF1/Frames1
        - /TF1/Frames1/odom1
        - /Map1
      Splitter Ratio: 0.5
    Tree Height: 434
  - Class: rviz/Selection
    Name: Selection
  - Class: rviz/Tool Properties
    Expanded:
      - /2D Pose Estimate1
      - /2D Nav Goal1
      - /Publish Point1
    Name: Tool Properties
    Splitter Ratio: 0.588679
  - Class: rviz/Views
    Expanded:
      - /Current View1
    Name: Views
    Splitter Ratio: 0.5
  - Class: rviz/Time
    Experimental: false
    Name: Time
    SyncMode: 0
    SyncSource: LaserScan
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Size: 1
      Class: rviz/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.03
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 10
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 1
      Autocompute Intensity Bounds: true
      Autocompute Value Bounds:
        Max Value: 10
        Min Value: -10
        Value: true
      Axis: Z
      Channel Name: intensity
      Class: rviz/LaserScan
      Color: 255; 0; 0
      Color Transformer: FlatColor
      Decay Time: 0
      Enabled: true
      Invert Rainbow: false
      Max Color: 255; 0; 0
      Max Intensity: 4096
      Min Color: 0; 0; 0
      Min Intensity: 0
      Name: LaserScan
      Position Transformer: XYZ
      Queue Size: 10
      Selectable: true
      Size (Pixels): 3
      Size (m): 0.1
      Style: Flat Squares
      Topic: /iris_0/scan
      Use Fixed Frame: true
      Use rainbow: true
      Value: true
    - Class: rviz/TF
      Enabled: true
      Frame Timeout: 15
      Frames:
        All Enabled: true
        base_link:
          Value: true
        laser:
          Value: true
        map:
          Value: true
        odom:
          Value: true
      Marker Scale: 3
      Name: TF
      Show Arrows: true
      Show Axes: true
      Show Names: true
      Tree:
        map:
          odom:
            base_link:
              laser:
                {}
      Update Interval: 0
      Value: true
    - Alpha: 0.7
      Class: rviz/Map
      Color Scheme: map
      Draw Behind: false
      Enabled: true
      Name: Map
      Topic: /map
      Value: true
  Enabled: true
  Global Options:
    Background Color: 0; 0; 0
    Fixed Frame: odom
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz/Interact
      Hide Inactive Objects: true
    - Class: rviz/MoveCamera
    - Class: rviz/Select
    - Class: rviz/FocusCamera
    - Class: rviz/Measure
    - Class: rviz/SetInitialPose
      Topic: /initialpose
    - Class: rviz/SetGoal
      Topic: /move_base_simple/goal
    - Class: rviz/PublishPoint
      Single click: true
      Topic: /clicked_point
  Value: true
  Views:
    Current:
      Angle: 0
      Class: rviz/TopDownOrtho
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.06
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Name: Current View
      Near Clip Distance: 0.01
      Scale: 150
      Target Frame: <Fixed Frame>
      Value: TopDownOrtho (rviz)
      X: 0
      Y: 0
    Saved: ~
Window Geometry:
  Displays:
    collapsed: false
  Height: 721
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd00000004000000000000013c0000023dfc0200000008fb0000001200530065006c0065006300740069006f006e00000001e10000009b0000005300fffffffb0000001e0054006f006f006c002000500072006f007000650072007400690065007302000001ed000001df00000185000000a3fb000000120056006900650077007300200054006f006f02000001df000002110000018500000122fb000000200054006f006f006c002000500072006f0070006500720074006900650073003203000002880000011d000002210000017afb000000100044006900730070006c00610079007301000000360000023d000000b700fffffffb0000002000730065006c0065006300740069006f006e00200062007500660066006500720200000138000000aa0000023a00000294fb00000014005700690064006500530074006500720065006f02000000e6000000d2000003ee0000030bfb0000000c004b0069006e0065006300740200000186000001060000030c00000261000000010000010f0000023dfc0200000003fb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000041000000780000000000000000fb0000000a0056006900650077007301000000360000023d0000009b00fffffffb0000001200530065006c0065006300740069006f006e010000025a000000b200000000000000000000000200000490000000a9fc0100000001fb0000000a00560069006500770073030000004e00000080000002e10000019700000003000004000000003efc0100000002fb0000000800540069006d00650100000000000004000000024500fffffffb0000000800540069006d00650100000000000004500000000000000000000001a90000023d00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Selection:
    collapsed: false
  Time:
    collapsed: false
  Tool Properties:
    collapsed: false
  Views:
    collapsed: false
  Width: 1024
  X: -2
  Y: -2
  ```
  - 그리고 나서 roslaunch px4 mavros_posix_sitl.launch를 실행하면 gazebo가 열린다.
  ```
  roslaunch px4 mavros_posix_sitl.launch
  ```

  ![12](https://user-images.githubusercontent.com/43773374/127287522-fdaf4f2a-ed12-482a-a795-46aeae6bacdf.png)


  - 그리고나서 demo.launch를 실행시킨다.
  ```
  roslaunch laser_scan_matcher demo.launch
  ```

  ![1](https://user-images.githubusercontent.com/43773374/127287482-cbef3c0a-fe3e-4d15-9a8a-9c5b9d76bc1e.png)


  - demo.launch를 종료하고 나서 demo_gmapping.launch를 실행한다.
  ```
  roslaunch laser_scan_matcher demo_gmapping.launch
  ```

  ![12345](https://user-images.githubusercontent.com/43773374/127287500-2c5f8149-d783-465d-a921-bd6b4f9d55e2.png)
  
  - 만약 실행시켰을 때 오류가 난다면 밑의 코드를 실행시켜서 패키지를 다운받는다.
  ```
  sudo apt-get install ros-melodic-slam-gmapping
  ```
  

## 11. optical flow senser와 stereo camera 추가하기
  - iris_foggy_lidar에 opt_flow와 stereo camera를 추가한다.
  ```
  cd ~/PX4-Autopilot/Tools/sitl_gazebo/models/iris_foggy_lidar && gedit iris_foggy_lidar.sdf
  ```
  - 해당 파일을 열고 밑에 있는 코드를 추가한다.
  ```html
 <!--px4flow camera-->
    <include>
      <uri>model://px4flow</uri>
      <pose>0.05 0 -0.05 0 0 0</pose>
    </include>

    <joint name="px4flow_joint" type="revolute">
      <parent>iris::base_link</parent>
      <child>px4flow::link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

 <!--lidar-->
    <include>
      <uri>model://lidar</uri>
      <pose>0 0 -0.05 0 0 0</pose>
    </include>

    <joint name="lidar_joint1" type="fixed">
      <parent>iris::base_link</parent>
      <child>lidar::link</child>
    </joint>
 <!-- For Stereo camera -->
    <include>
          <uri>model://stereo_camera</uri>
          <pose>0.1 0 0 0 0 0</pose>
        </include>

        <joint name="stereo_camera_joint" type="revolute">
          <parent>iris::base_link</parent>
          <child>stereo_camera::link</child>
          <axis>
            <xyz>0 0 1</xyz>
            <limit>
              <upper>0</upper>
              <lower>0</lower>
            </limit>
          </axis>
        </joint>
 ```
  ![00](https://user-images.githubusercontent.com/43773374/127591716-1ed012cb-c5d9-430a-86c3-a1d11c0528d2.png)
  - demo.launch와 demo_gmapping.launch 파일을 수정한다.
  ```
  cd /opt/ros/melodic/share/laser_scan_matcher/demo && sudo gedit demo.launch
  ```
  ```
  cd /opt/ros/melodic/share/laser_scan_matcher/demo && sudo gedit demo_gmapping.launch
  ```
  
  - line 12와 line 13처럼 해당 코드를 입력한다.
  ![0000](https://user-images.githubusercontent.com/43773374/127592796-f69d3201-fd26-4c5e-8107-00a7350398eb.png)
![00000](https://user-images.githubusercontent.com/43773374/127592801-b5810ff2-c739-46f9-bf60-c0056bdec4d6.png)
  ```
  <node pkg="tf" type="static_transform_publisher" name="iris_base_link_to_flow" args="0.0 0.0 -0.05 0.0 0.0 0.0  base_link /px4flow 40" />
  ```
  ```
  <node pkg="tf" type="static_transform_publisher" name="iris_base_link_to_camera" args="0.1 0.0 0.0 0.0 0.0 0.0 base_link /camera_link 40" />
  ```
  - 그리고 나서 다시 실행시킨후에 rostopic을 이용하여 opticalflow의 topic값이 출력되는지 확인한다.
  ```
  roslaunch px4 mavros_posix_sitl.launch
  ```
  ```
  rostopic echo /mavros/px4flow/ground_distance
  ```
  ![000](https://user-images.githubusercontent.com/43773374/127592049-441f0aab-ea27-4a5c-b2e5-9b08a26c09ce.png)
  - 그리고 나서 demo.launch 또는 demo_gmapping.launch를 실행시켜서 camera 가 잘 나오는지 확인한다.
  ```
  roslaunch laser_scan_matcher demo.launch
  ```
  ![Screenshot from 2021-07-30 11-58-00](https://user-images.githubusercontent.com/43773374/127593149-17f525e8-084e-42a0-afbc-ab965a4008d6.png)

    
## 12. 새로운 f450 만들어서 lidar와 opt_flow 그리고 d435 추가하기
- 일단 먼저 px4-autopilot/model에 들어가서 기존에 있던 custom_f450을 복사한다.
- 그리고 나서 mission_f450으로 폴더명을 수정했다.
- 안에 있는 sdf파일도 mission_f450으로 변경한다.
```html
<sdf version='1.6'>
  <model name='mission_f450'>
    <include>
      <uri>model://custom_f450</uri>
    </include>
   <!-- hokuyo_lidar -->
    <include>
      <uri>model://hokuyo_lidar</uri>
      <pose>0 0 0.25 0 0 0</pose>
    </include>
    <joint name="hokuyo_lidar_joint" type="revolute">
      <parent>custom_f450::base_link</parent>
      <child>hokuyo_lidar::link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

  <!--px4flow camera-->
  <include>
    <uri>model://px4flow</uri>
    <pose>0 0 0.1 0 0 0</pose>
  </include>

  <joint name="px4flow_joint" type="revolute">
    <parent>custom_f450::base_link</parent>
    <child>px4flow::link</child>
    <axis>
      <xyz>0 0 1</xyz>
      <limit>
        <upper>0</upper>
        <lower>0</lower>
      </limit>
    </axis>
  </joint>

<!--lidar-->
  <include>
    <uri>model://lidar</uri>
    <pose>0 0 0.1 0 0 0</pose>
  </include>

  <joint name="lidar_joint" type="fixed">
    <parent>custom_f450::base_link</parent>
    <child>lidar::link</child>
  </joint>
  </model>
</sdf>
```
- display.launch 수정하기
```
cd ~/catkin_ws/src/f450/launch && gedit display.launch
```
```html
<launch>
  <arg name="model" />
  <param name="robot_description" textfile="$(find f450)/urdf/f450.urdf" />
  <param name="/use_sim_time" value="true"/>
  <node name="joint_state_publisher_gui" pkg="joint_state_publisher_gui" type="joint_state_publisher_gui" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
 ### tf ##################################

 <node pkg="tf" type="static_transform_publisher" name="mission_f450_to_lidar" args="0.0 0.0 0.25 0.0 0.0 0.0 /custom_f450/base_link /mission_f450/laser_2d 40" />
 <node pkg="tf" type="static_transform_publisher" name="mission_f450_to_flow" args="0.0 0.0 0.1 0.0 0.0 0.0 /base_link /px4flow 40" />
 <node pkg="tf" type="static_transform_publisher" name="mission_f450_to_laser" args="0.0 0.0 0.1 0.0 0.0 0.0 /base_link /lidar 40" />

  #### start the laser scan_matcher ##############################

  <node pkg="laser_scan_matcher" type="laser_scan_matcher_node"
    name="laser_scan_matcher_node" output="screen">
    <param name="fixed_frame" value = "odom"/>
    <param name="base_frame" value = "/custom_f450/base_link"/>
    <param name="max_iterations" value="10"/>
    <param name="use_imu" value="false"/>
    <param name="use_odom" value="false"/>
    <remap from="scan" to="/mission_f450/scan"/>
    <remap from="pose2D" to="mission_f450/pose2D"/>
  </node>

  #### start gmapping ############################################

  <node pkg="gmapping" type="slam_gmapping" name="slam_gmapping" output="screen">
    <param name="base_frame" value='/base_link'/>
    <param name="map_udpate_interval" value="1.0"/>
    <param name="maxUrange" value="5.0"/>
    <param name="sigma" value="0.1"/>
    <param name="kernelSize" value="1"/>
    <param name="lstep" value="0.15"/>
    <param name="astep" value="0.15"/>
    <param name="iterations" value="1"/>
    <param name="lsigma" value="0.1"/>
    <param name="ogain" value="3.0"/>
    <param name="lskip" value="1"/>
    <param name="srr" value="0.1"/>
    <param name="srt" value="0.2"/>
    <param name="str" value="0.1"/>
    <param name="stt" value="0.2"/>
    <param name="linearUpdate" value="1.0"/>
    <param name="angularUpdate" value="0.5"/>
    <param name="temporalUpdate" value="0.4"/>
    <param name="resampleThreshold" value="0.5"/>
    <param name="particles" value="10"/>
    <param name="xmin" value="-5.0"/>
    <param name="ymin" value="-5.0"/>
    <param name="xmax" value="5.0"/>
    <param name="ymax" value="5.0"/>
    <param name="delta" value="0.02"/>
    <param name="llsamplerange" value="0.01"/>
    <param name="llsamplestep" value="0.05"/>
    <param name="lasamplerange" value="0.05"/>
    <param name="lasamplestep" value="0.05"/>
    <remap from="scan" to="/mission_f450/scan"/>
    <remap from="pose2D" to="mission_f450/pose2D"/>
  </node>

  #### start rviz ################################################
  <node name="rviz" pkg="rviz" type="rviz" args="-d $(find f450)/f450_urdf.rviz" />
</launch>
```
- mavros_posix_sitl.launch 수정
```
cd ~/PX4-Autopilot/launch && gedit mavros_posix_sitl.launch
```
```html
<?xml version="1.0"?>
<launch>
    <!-- MAVROS posix SITL environment launch script -->
    <!-- launches MAVROS, PX4 SITL, Gazebo environment, and spawns vehicle -->
    <!-- vehicle pose -->
    <arg name="x" default="0"/>
    <arg name="y" default="0"/>
    <arg name="z" default="0"/>
    <arg name="R" default="0"/>
    <arg name="P" default="0"/>
    <arg name="Y" default="0"/>
    <!-- vehicle model and world -->
    <arg name="est" default="ekf2"/>
    <arg name="vehicle" default="mission_f450"/>
    <arg name="world" default="$(find mavlink_sitl_gazebo)/worlds/indoor3.world"/>
    <arg name="sdf" default="$(find mavlink_sitl_gazebo)/models/$(arg vehicle)/$(arg vehicle).sdf"/>

    <!-- gazebo configs -->
    <arg name="gui" default="true"/>
    <arg name="debug" default="false"/>
    <arg name="verbose" default="false"/>
    <arg name="paused" default="false"/>
    <arg name="respawn_gazebo" default="false"/>
    <!-- MAVROS configs -->
    <arg name="fcu_url" default="udp://:14540@localhost:14557"/>
    <arg name="respawn_mavros" default="false"/>
    <!-- PX4 configs -->
    <arg name="interactive" default="true"/>
    <!-- PX4 SITL and Gazebo -->
    <include file="$(find px4)/launch/posix_sitl.launch">
        <arg name="x" value="$(arg x)"/>
        <arg name="y" value="$(arg y)"/>
        <arg name="z" value="$(arg z)"/>
        <arg name="R" value="$(arg R)"/>
        <arg name="P" value="$(arg P)"/>
        <arg name="Y" value="$(arg Y)"/>
        <arg name="world" value="$(arg world)"/>
        <arg name="vehicle" value="$(arg vehicle)"/>
        <arg name="sdf" value="$(arg sdf)"/>
        <arg name="gui" value="$(arg gui)"/>
        <arg name="interactive" value="$(arg interactive)"/>
        <arg name="debug" value="$(arg debug)"/>
        <arg name="verbose" value="$(arg verbose)"/>
        <arg name="paused" value="$(arg paused)"/>
        <arg name="respawn_gazebo" value="$(arg respawn_gazebo)"/>
    </include>
    <!-- MAVROS -->
    <include file="$(find mavros)/launch/px4.launch">
        <!-- GCS link is provided by SITL -->
        <arg name="gcs_url" value=""/>
        <arg name="fcu_url" value="$(arg fcu_url)"/>
        <arg name="respawn_mavros" value="$(arg respawn_mavros)"/>
    </include>
</launch>
```

- 실행하기
- qground control 실행
- gazebo 실행
```
roslaunch px4 mavros_posix_sitl.launch
```
- rviz 와 gmapping 실행
```
roslaunch f450 display.launch
```
- orb_slam 실행
```
roslaunch orb_slam2_ros orb_slam2_d435_rgbd.launch
```
![0](https://user-images.githubusercontent.com/43773374/128119879-f7764788-975b-42a5-841c-2d569a26e70a.png)
![00](https://user-images.githubusercontent.com/43773374/128119883-c96c33de-4193-4bc6-8585-14a3b6c06b16.png)
![000](https://user-images.githubusercontent.com/43773374/128119886-5a47bdf0-78ea-4428-bacd-5e67ecfd60ab.png)

13. 최종 프로젝트
- iris 드론에 전, 후, 좌, 우에 depth camera를 장착한 후에 Lidar를 이용하여 자율주행을 실시하고 depth camera를 이용하여 mapping을 실시한다.

- 맵은 보통 건물의 한 층에 해당하는 형식으로 진행할 것이며 가운데에 복도가 있고 양옆에는 방 또는 다른 공간이 존재한다.

- iris_foggy_lidar 드론 수정
- 카메라를 전, 후, 좌, 우에 설치한다.
```html
<?xml version="1.0" ?>
<sdf version='1.5'>
  <model name='iris_foggy_lidar'>

    <include>
      <uri>model://iris</uri>
    </include> 
<!--
    <include>
      <uri>model://foggy_lidar</uri>
      <pose>0 0 0.1 0 1.571 0</pose>
    </include>
    <joint name="foggy_lidar_joint" type="revolute">
      <parent>iris::base_link</parent>
      <child>foggy_lidar::link</child>
      <pose>0 0 0.1 0 1.571 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>
-->
<!-- hokuyo_lidar -->
      <include>
      <uri>model://hokuyo_lidar</uri>
      <pose>0 0 0.1 0 0 0</pose>
    </include>
    <joint name="hokuyo_lidar_joint" type="revolute">
      <parent>iris::base_link</parent>
      <child>hokuyo_lidar::link</child>
      <pose>0 0 0.1 0 0 0</pose>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>


<!-- front depth camera -->
    <include>
      <uri>model://front_depth_camera</uri>
      <pose>0.1 0 0 0 0 0</pose>
    </include>
    <joint name="front_depth_camera_joint" type="revolute">
      <child>front_depth_camera::link</child>
      <parent>iris::base_link</parent>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

<!-- back depth camera -->
    <include>
      <uri>model://back_depth_camera</uri>
      <pose>-0.15 0 0 0 0 3.14</pose>
    </include>
    <joint name="back_depth_camera_joint" type="revolute">
      <child>back_depth_camera::link</child>
      <parent>iris::base_link</parent>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

<!-- left depth camera -->
    <include>
      <uri>model://left_depth_camera</uri>
      <pose>0 0.1 0 0 0 1.5707</pose>
    </include>
    <joint name="left_depth_camera_joint" type="revolute">
      <child>left_depth_camera::link</child>
      <parent>iris::base_link</parent>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

<!-- right depth camera -->
    <include>
      <uri>model://right_depth_camera</uri>
      <pose>0 -0.1 0 0 0 -1.5707</pose>
    </include>
    <joint name="right_depth_camera_joint" type="revolute">
      <child>right_depth_camera::link</child>
      <parent>iris::base_link</parent>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <upper>0</upper>
          <lower>0</lower>
        </limit>
      </axis>
    </joint>

  </model>
</sdf>


<!-- vim: set noet fenc=utf-8 ff=unix sts=0 sw=4 ts=4 : -->
```

- 전, 후, 좌, 우 카메라를 각각 model안에 새로 만든다.
- 전방 카메라
```html
<!-- DO NOT EDIT: Generated from depth_camera.sdf.jinja -->
<?xml version="1.0" ?>
<sdf version="1.5">
  <model name="front_depth_camera">
    <pose>0 0 0.035 0 0 0</pose>
    <link name="link">
      <inertial>
        <pose>0.01 0.025 0.025 0 0 0</pose>
        <mass>0.01</mass>
        <inertia>
          <ixx>4.15e-6</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>2.407e-6</iyy>
          <iyz>0</iyz>
          <izz>2.407e-6</izz>
        </inertia>
      </inertial>
      <visual name="visual">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://realsense_camera/meshes/realsense.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <sensor name="depth_camera" type="depth"><update_rate>30</update_rate>
        <camera>
          <horizontal_fov>1.02974</horizontal_fov>
          <image>
            <format>R8G8B8</format>
            <width>640</width>
            <height>480</height>
          </image>
          <clip>
            <near>0.5</near>
            <far>5</far>
          </clip>
        </camera>
        <plugin filename="libgazebo_ros_openni_kinect.so" name="camera_controller">
          <cameraName>camera</cameraName>
          <alwaysOn>true</alwaysOn>
          <updateRate>20</updateRate>
          <pointCloudCutoff>0.2</pointCloudCutoff>
          <pointCloudCutoffMax>20</pointCloudCutoffMax>
          <imageTopicName>rgb/image_raw</imageTopicName>
          <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
          <depthImageTopicName>depth/image_raw</depthImageTopicName>
          <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
          <pointCloudTopicName>depth/points</pointCloudTopicName>
          <frameName>front_camera_link</frameName>
          <distortion_k1>0.0</distortion_k1>
          <distortion_k2>0.0</distortion_k2>
          <distortion_k3>0.0</distortion_k3>
          <distortion_t1>0.0</distortion_t1>
          <distortion_t2>0.0</distortion_t2>
        </plugin></sensor>
    </link>
  </model>
</sdf>
```

- 후방 카메라
```html
<!-- DO NOT EDIT: Generated from depth_camera.sdf.jinja -->
<?xml version="1.0" ?>
<sdf version="1.5">
  <model name="back_depth_camera">
    <pose>0 0 0.035 0 0 0</pose>
    <link name="link">
      <inertial>
        <pose>0.01 0.025 0.025 0 0 0</pose>
        <mass>0.01</mass>
        <inertia>
          <ixx>4.15e-6</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>2.407e-6</iyy>
          <iyz>0</iyz>
          <izz>2.407e-6</izz>
        </inertia>
      </inertial>
      <visual name="visual">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://realsense_camera/meshes/realsense.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <sensor name="depth_camera" type="depth"><update_rate>30</update_rate>
        <camera>
          <horizontal_fov>1.02974</horizontal_fov>
          <image>
            <format>R8G8B8</format>
            <width>640</width>
            <height>480</height>
          </image>
          <clip>
            <near>0.5</near>
            <far>5</far>
          </clip>
        </camera>
        <plugin filename="libgazebo_ros_openni_kinect.so" name="camera_controller">
          <cameraName>camera</cameraName>
          <alwaysOn>true</alwaysOn>
          <updateRate>20</updateRate>
          <pointCloudCutoff>0.2</pointCloudCutoff>
          <pointCloudCutoffMax>20</pointCloudCutoffMax>
          <imageTopicName>rgb/image_raw</imageTopicName>
          <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
          <depthImageTopicName>depth/image_raw</depthImageTopicName>
          <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
          <pointCloudTopicName>depth/points</pointCloudTopicName>
          <frameName>back_camera_link</frameName>
          <distortion_k1>0.0</distortion_k1>
          <distortion_k2>0.0</distortion_k2>
          <distortion_k3>0.0</distortion_k3>
          <distortion_t1>0.0</distortion_t1>
          <distortion_t2>0.0</distortion_t2>
        </plugin></sensor>
    </link>
  </model>
</sdf>
```
- 좌측 카메라
```html
<!-- DO NOT EDIT: Generated from depth_camera.sdf.jinja -->
<?xml version="1.0" ?>
<sdf version="1.5">
  <model name="left_depth_camera">
    <pose>0 0 0.035 0 0 0</pose>
    <link name="link">
      <inertial>
        <pose>0.01 0.025 0.025 0 0 0</pose>
        <mass>0.01</mass>
        <inertia>
          <ixx>4.15e-6</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>2.407e-6</iyy>
          <iyz>0</iyz>
          <izz>2.407e-6</izz>
        </inertia>
      </inertial>
      <visual name="visual">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://realsense_camera/meshes/realsense.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <sensor name="depth_camera" type="depth"><update_rate>30</update_rate>
        <camera>
          <horizontal_fov>1.02974</horizontal_fov>
          <image>
            <format>R8G8B8</format>
            <width>640</width>
            <height>480</height>
          </image>
          <clip>
            <near>0.5</near>
            <far>5</far>
          </clip>
        </camera>
        <plugin filename="libgazebo_ros_openni_kinect.so" name="camera_controller">
          <cameraName>camera</cameraName>
          <alwaysOn>true</alwaysOn>
          <updateRate>20</updateRate>
          <pointCloudCutoff>0.2</pointCloudCutoff>
          <pointCloudCutoffMax>20</pointCloudCutoffMax>
          <imageTopicName>rgb/image_raw</imageTopicName>
          <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
          <depthImageTopicName>depth/image_raw</depthImageTopicName>
          <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
          <pointCloudTopicName>depth/points</pointCloudTopicName>
          <frameName>left_camera_link</frameName>
          <distortion_k1>0.0</distortion_k1>
          <distortion_k2>0.0</distortion_k2>
          <distortion_k3>0.0</distortion_k3>
          <distortion_t1>0.0</distortion_t1>
          <distortion_t2>0.0</distortion_t2>
        </plugin></sensor>
    </link>
  </model>
</sdf>
```

- 우측 카메라
```html
<!-- DO NOT EDIT: Generated from depth_camera.sdf.jinja -->
<?xml version="1.0" ?>
<sdf version="1.5">
  <model name="right_depth_camera">
    <pose>0 0 0.035 0 0 0</pose>
    <link name="link">
      <inertial>
        <pose>0.01 0.025 0.025 0 0 0</pose>
        <mass>0.01</mass>
        <inertia>
          <ixx>4.15e-6</ixx>
          <ixy>0</ixy>
          <ixz>0</ixz>
          <iyy>2.407e-6</iyy>
          <iyz>0</iyz>
          <izz>2.407e-6</izz>
        </inertia>
      </inertial>
      <visual name="visual">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://realsense_camera/meshes/realsense.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <sensor name="depth_camera" type="depth"><update_rate>30</update_rate>
        <camera>
          <horizontal_fov>1.02974</horizontal_fov>
          <image>
            <format>R8G8B8</format>
            <width>640</width>
            <height>480</height>
          </image>
          <clip>
            <near>0.5</near>
            <far>5</far>
          </clip>
        </camera>
        <plugin filename="libgazebo_ros_openni_kinect.so" name="camera_controller">
          <cameraName>camera</cameraName>
          <alwaysOn>true</alwaysOn>
          <updateRate>20</updateRate>
          <pointCloudCutoff>0.2</pointCloudCutoff>
          <pointCloudCutoffMax>20</pointCloudCutoffMax>
          <imageTopicName>rgb/image_raw</imageTopicName>
          <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
          <depthImageTopicName>depth/image_raw</depthImageTopicName>
          <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
          <pointCloudTopicName>depth/points</pointCloudTopicName>
          <frameName>right_camera_link</frameName>
          <distortion_k1>0.0</distortion_k1>
          <distortion_k2>0.0</distortion_k2>
          <distortion_k3>0.0</distortion_k3>
          <distortion_t1>0.0</distortion_t1>
          <distortion_t2>0.0</distortion_t2>
        </plugin></sensor>
    </link>
  </model>
</sdf>
```
- 그리고 나서 전에 pkg로 설치한 octomap_server에 들어가서 octomap_mapping.launch를 수정한다.
```html
<!-- 
  Example launch file for octomap_server mapping: 
  Listens to incoming PointCloud2 data and incrementally builds an octomap. 
  The data is sent out in different representations. 

  Copy this file into your workspace and adjust as needed, see
  www.ros.org/wiki/octomap_server for details  
-->
<launch>
	<node pkg="octomap_server" type="octomap_server_node" name="octomap_server">
		<param name="resolution" value="0.05" />
		
		<!-- fixed map frame (set to 'map' if SLAM or localization running!) -->
		<param name="frame_id" type="string" value="map" />
		
		<!-- maximum range to integrate (speedup!) -->
		<param name="sensor_model/max_range" value="5.0" />
		
		<!-- data source to integrate (PointCloud2) -->
		<remap from="cloud_in" to="/camera_kinect/depth/points" />
	
	</node>
</launch>
```
- 이렇게 하고 명령어를 입력해서 실행해본다.
```
roslaunch px4 mavros_posix_sitl.launch
```
```
roslaunch octomap_server octomap_mapping.launch
```
```
rosrun mavros_simple_control py.py
```
- 먼저 teleopy로 이륙을 시킨다음에 자율주행하는 알고리즘을 실행시키면 된다.