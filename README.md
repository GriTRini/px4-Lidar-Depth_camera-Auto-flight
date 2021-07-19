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

##2. ros/gazebo 설치
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


## 5. github에서 해당 프레임 가지고 오기
- home 안에 설치한다.
```
https://github.com/GriTRini/px4-project.git
```
- 안에 있는 px4-quadrotor-HW-parts-main 파일을 home밖으로 꺼낸다.

- 꺼낸후에 밑의 명령어를 실행한다.
```
cd px4-quadrotor-HW-parts-main/
```
```
cp -r custom_f450/ ~/PX4-Autopilot/Tools/sitl_gazebo/models/
```
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



## 6. qgroundcontrol을 설치한다.

- 해당 홈페이지에서 GCS를 설치한다.
![Screenshot from 2021-07-19 09-16-07](https://user-images.githubusercontent.com/43773374/126086709-6e422694-1f0d-4144-8ef1-8e224b7d0773.png)

https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html

- 
![Screenshot from 2021-07-19 09-18-26](https://user-images.githubusercontent.com/43773374/126086777-e09dbb74-f5f2-4b72-a25f-bb4c631d2580.png)

## 7. 다운받은 custom_f450 파일 rviz에서 수정하기

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
roslaunch px4 display.launch
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

- 이후에 밑에 내용을 실행한다.
```
 roslaunch f450 display.launch
 ```
 - 
 ![Screenshot from 2021-07-17 18-38-39](https://user-images.githubusercontent.com/43773374/126032892-b5fc2d74-c9f6-4fb7-9874-416852e96e14.png)
 



