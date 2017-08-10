# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.4-slim


CMD /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# RUN brew update


RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \ 
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN apt-get install python3-dev

# The rest of this file just runs an example script.


 In order to get this program to run as a live feed

# Vaidehi adds
RUN git clone https://github.com/davisking/dlib.git && \
    cd dlib && \
    mkdir build && \
    cd build && \
    cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1 && \
    cmake --build . && \
    cd .. && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA && \
    cd && \
    pip install face_recognition && \
    pip install pyglet 
RUN cd && \
    git clone https://github.com/opencv/opencv.git && \
    cd opencv && \
    git checkout 3.1.0 && \
    cd ~ && \
    git clone https://github.com/opencv/opencv_contrib.git && \
    cd opencv_contrib && \
    git checkout 3.1.0 && \
    cd ~/opencv && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON .. && \
    make -j4 && \
    make install && \
    ldconfig && \
    cd ~ && \
    ln -s /usr/local/lib/python3.4/site-packages/cv2.so cv2.so
RUN cd ~ && \
    git clone https://github.com/vduraphe/face_recognition.git && \
    cd face_recognition/examples/

When I first started my internship, I was immersed into all of these topics I had never worked with before, Machine Learning and Edge computing being two of many. In terms of machine learning, I learned about the three different categories of machine learning (Supervised, Unsupervised, and Reinforcement Learning). This was useful when working with Austin and Xiang on our design project, as when designing the projector they talked about earlier, we focused in on image classification and regression within supervised learning. Classification was a main category of machine learning we explored when creating use cases such as a machine learning security camera, and regression fell more into the category of mapping.

Surface level research of edge computing was necessary for our design project to understand the connections between the local device and cloud.

From the demo I showed you guys, you were able to see the various user stories of the snack security facial recognition system. While I would like to say that I designed the whole thing starting from the parsing of the webcam captured frame, I was actually lucky to have found a open source project that used the facial_recognition python in combination with the cross-platform library Dlib library to build a program that can recognize any face that you feed it. For example, if I supplied the program with a jpg file of Barack Obama, it would be able to recognize him in any other image that had his face.

The open source I used supplied some stepping stones to get live image recognition going, but the real pain of the process was getting opencv, a python computer vision library, installed on my machine. After many failed attempts, I used a partially preconfigured VM to work around the installations and spend time on the actual program. Before starting this project, I was pretty naive about software installations in general, and I had gotten into a pretty big mess with many different versions of python and other libraries because of repeated attempts at getting this software going. 

Eventually, I cleaned up my machine and used python's virtual environment tool to create an isolated python environment for all my installations. These are the different libraries and APIs I used to create my program. Pyglet is a package good for developing games, which I used to play an alarm sound in my program when the camera spots an unknown face. Subprocess is used to start another program on your machine from the python script, so I used this to start powerpoint upon face detection. When the software recognizes a face, if it finds a corresponding presentation of the same name in the file system, it starts it in presentation mode. OpenCV of course is used for computer vision, and face_recognition is an API that can parse image data to have the ability to recognize. It is used with Dlib, as mentioned earlier, that has software components for image processing and machine learning. To help others interested in the process of getting started with these softwares, I also created a docker file which is able to successfully install all of these. The problem with the file that I'm still working with, however, is that it is unable to automatically grab a reference to the default webcam to be able to capture an image.


When developing the snack security web interface, I started with the basic layout of what I wanted to showcase: Unknown faces, known faces, a basic about tab, and a function that allowed a user to submit their own face to the program. Dyami guided me in setting up a node.js server using the express web app framework. One of the challenges faced during this was parsing the image data received when a user submits their picture, and Dyami and Fabian directed me through converting the data from a json string to a javascript object and then using the final base 64 data extracted into the file system with the name sent with it.

Cycling through the whole process of configuring the Web UI, Client-Side JS, Node JS, File system, and Display really improved my understanding of the model view controller architecture.

Another part of my internship was conducting QA testing for Bandwidth. I covered basic black box testing for the application by going through end to end user stories and logging bugs on Trello. Doing QA testing helped my internship come a bit of full circle since I was able to communicate with the India team and see that final editing phase of the application take place for version 0.1.0.


https://n31.ultipro.com/Login.aspx?ReturnUrl=%2f






 