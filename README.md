# px4-project
## 1 .opencv 설치
- ros를 설치하기 전에 먼저 opencv를 설치해야 한다.
- (1) 업데이트
```
sudo apt-get update
sudo apt-get upgrade
```
- (2) 필요한 라이브러리 설치
```
sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy

sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev v4l-utils 
sudo apt-get install libxvidcore-dev libx264-dev libxine2-dev
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev
sudo apt-get install libatlas-base-dev gfortran libeigen3-dev
```
- (3) opencv 설치
```
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip

unzip opencv.zip
unzip opencv_contrib.zip

cd opencv-3.4.0
mkdir build
cd build
```
- (4) opencv 빌드
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=OFF \
-D WITH_IPP=OFF \
-D WITH_1394=OFF \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D WITH_QT=OFF \
-D WITH_GTK=ON \
-D WITH_OPENGL=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.0/modules \
-D WITH_V4L=ON  \
-D WITH_FFMPEG=ON \
-D WITH_XINE=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D PYTHON2_INCLUDE_DIR=/usr/include/python2.7 \
-D PYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/python2.7/dist-packages/numpy/core/include/ \
-D PYTHON2_PACKAGES_PATH=/usr/lib/python2.7/dist-packages \
-D PYTHON2_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
-D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m \
-D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include/  \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D PYTHON3_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
../
```
```
#방열판이 있을경우
make -j4
#방열판이 없을경우
make -j2
```
- (5) opencv 컴파일
```
sudo make install
sudo sh -c 'echo '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```

## 2. px4 파일 설치
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
- 이후에 밑에 내용을 실행한다.
```
 roslaunch f450 display.launch
 ```
 - 
 ![Screenshot from 2021-07-17 18-38-39](https://user-images.githubusercontent.com/43773374/126032892-b5fc2d74-c9f6-4fb7-9874-416852e96e14.png)
 
## 8. 카메라 축 변경
- 먼저 카메라 링크를 수정해야 한다.
```
cd ~/PX4-Autopilot/Tools/sitl_gazebo/models/custom_f450 && gedit custom_f450.sdf
```
![Screenshot from 2021-07-19 17-25-22](https://user-images.githubusercontent.com/43773374/126128406-f653a3b0-af14-442c-88d2-d5b3ec20b9a9.png)

- <frameName>camera_link</frameName>를 다음과 처럼 <frameName>d435_link</frameName> 바꿔준다.

- 카메라 축을 변경하기 위해서는 joint 된 축을 변경해야 한다.
```
cd ~/catkin_ws/src/f450/urdf && gedit f450.urdf
```
![Screenshot from 2021-07-19 17-20-54](https://user-images.githubusercontent.com/43773374/126128383-0bc97acb-3453-432e-96ec-f191b6aadf23.png)

- 실행하면 이러한 창이 뜬다.
- 카메라와 base_link를 서로 joint한 곳을 찾아서 축을 수정한다.
- 처음에는 000 으로 되어있다.

![Screenshot from 2021-07-19 17-22-22](https://user-images.githubusercontent.com/43773374/126128395-00ad19e9-f06e-4cde-a74f-a67c4b276007.png)


- 해당 부분을 위의 사진중에서 rpy="-1.5707 0 -1.5707" 로 수정한다.



## 9. 실행

- 터미널 창에 명령어를 입력한다.
```
roslaunch px4 mavros_posix_sitl.launch
```

```
roslaunch px4 display.launch
```

## 10. orb slam2 설치
- (1) Pangolin
```
# 1. OpenGL
sudo apt install libgl1-mesa-dev

# 2. Glew
sudo apt install libglew-dev

# 3. CMake
sudo apt install cmake

# 4. python
sudo apt install libpython2.7-dev
sudo apt-get install python-pip
sudo python -mpip install numpy pyopengl Pillow pybind11

# 5. wayland
sudo apt install pkg-config
sudo apt install libegl1-mesa-dev libwayland-dev libxkbcommon-dev wayland-protocols

# 6. PCL For ROS
sudo apt-get install libopenni2-dev
sudo apt-get install ros-melodic-pcl-ros
```
- building
```
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake ..
cmake --build .
```

- Eigen3
```
# Eigen 3
sudo apt install libeigen3-dev
```

- (2) Building ORB-SLAM2 Library and Examples
```
# clone the repository
git clone https://github.com/raulmur/ORB_SLAM2.git ORB_SLAM2

# build
cd ORB_SLAM2
chmod +x build.sh
./build.sh
```
![다운로드](https://user-images.githubusercontent.com/43773374/126584130-eff83378-e971-4b04-92aa-64d2deafb93b.png)


- 위와 같은 오류가 뜬다.

- 해결방법 - 1 
- ~/ORB_SLAM2/build.sh
```
echo "Configuring and building Thirdparty/DBoW2 ..."

cd Thirdparty/DBoW2
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j2

cd ../../g2o

echo "Configuring and building Thirdparty/g2o ..."

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j2

cd ../../../

echo "Uncompress vocabulary ..."

cd Vocabulary
tar -xf ORBvoc.txt.tar.gz
cd ..

echo "Configuring and building ORB_SLAM2 ..."

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j2
```
- make -j 를 make -j2로 변경한다.

- 해결방법 - 2
- ~/ORB_SLAM2/include/System.h
```
#include <unistd.h> 
```
- 위의 내용을 추가한다.

- (3) Building ORB-SLAM2 Library and Examples (ROS)

```
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:~/ORB_SLAM2/Examples/ROS

chmod +x build_ros.sh
./build_ros.sh
```
![다운로드 (1)](https://user-images.githubusercontent.com/43773374/126584120-7a2c912f-9923-4b54-b8c1-9105bb87d0b8.png)


- 해결방법 - 1
-  ~/ORB_SLAM2/build_ros.sh
```
echo "Building ROS nodes"

cd Examples/ROS/ORB_SLAM2
mkdir build
cd build
cmake .. -DROS_BUILD_TYPE=Release
make -j2
```
- line 7 에서 make -j를 make -j2로 변경한다.

- 해결방법 - 2
-  ~/ORB_SLAM2/Examples/ROS/ORB_SLAM2/CMakeLists.txt
![다운로드 (2)](https://user-images.githubusercontent.com/43773374/126584111-76ff1759-5bca-4c3b-b20a-97f3d6dedfee.png)


- 위의 초록색 사진의 해당 행을 추가한다.


- (4) ROS Examples (ORB SLAM2 : RGB-D)
- ~/ORB_SLAM2/Examples/ROS/ORB_SLAM2/src/ros_rgbd.cc 수정
```
# ros_rgbd.cc

# line 68
message_filters::Subscriber<sensor_msgs::Image> rgb_sub(nh, "/d435/rgb/image_raw", 1);

# line 69
message_filters::Subscriber<sensor_msgs::Image> depth_sub(nh, "/d435/depth/image_rect_raw", 1);
```
- 수정한 후에 재빌드 한다.
```
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:~/ORB_SLAM2/Examples/ROS

chmod +x build_ros.sh
./build_ros.sh
```

- 실행
```
# 가제보 실행
roslaunch px4 mavros_posix_sitl.launch
```

```
# rviz 실행
roslaunch f450 display.launch
```

```
# orb-slam2 실행
cd ~/ORB_SLAM2

export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:~/ORB_SLAM2/Examples/ROS

rosrun ORB_SLAM2 RGBD ~/ORB_SLAM2/Vocabulary/ORBvoc.txt ~/ORB_SLAM2/Examples/RGB-D/TUM1.yaml
```
