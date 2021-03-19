<h1 align="center">Innopolis Simulator</h1>

<div align="center">
<a href="https://github.com/inno-robolab/InnoSimulator/releases/latest">
<img src="https://img.shields.io/github/v/release/inno-robolab/InnoSimulator.svg" alt="Github release" /></a>
<a href="">
<img src="https://img.shields.io/github/downloads/inno-robolab/InnoSimulator/total.svg" alt="Release downloads" /></a>
</div>


<a href="Docs/Media/SimHeaderHD.png"><img src="Docs/Media/SimHeaderHD.png" style="width: 500px; max-width: 100%; height: auto" title="SimHeaderHD" /></a>
<div align="center">
  <h4>
    <a href="https://github.com/inno-robolab/InnoSimulator/releases/latest" style="text-decoration: none">
    Download</a>
    <span> | </span>
   <a href="Docs/HowToUse.md" style="text-decoration: 
   none">How To Use</a> 
    <span> | </span>
    <a href="https://robotics.innopolis.university/en/labs/laboratoriya-avtonomnyh-transportnyh-sistem/" style="text-decoration: 
   none">Autonomous Transportation Systems Lab</a> 
  </h4>
</div>

## Introduction
This simulator was designed especially for autonomous driving systems developers. InnoSim has been developed from the scratch by [Autonomous Transportation Systems Lab](https://robotics.innopolis.university/en/labs/laboratoriya-avtonomnyh-transportnyh-sistem/) of Innopolis University. Simulator could be used in development, testing, training and validation processes of autonomous systems in a close to real operational conditions. 
InnoSim allows to significantly decrease the cost of autonomous systems development process, especially in part of sensor equipment tuning and testing, control and interaction with another static and dynamic objects.

![Inno_Car_Model](Docs/Media/SimPriusNight.PNG)


## Functionalities

InnoSim provides the environment for debugging and modeling the behavior of users autonomous systems in real-time and in real 3D environment, which will avoid critical design errors, quickly clarify low-level requirements for individual nodes, shift the verification process to earlier stages, carry out more iterations of the prototype research in a short period of time and save on field tests.

## Video


[![Video](https://img.youtube.com/vi/AlKk73xMKE8/0.jpg)](https://www.youtube.com/watch?v=AlKk73xMKE8)



### Run tests with simulator
For carrying out of full-scale tests and testing of the entire functionality of the simulator, [Apollo](https://github.com/lgsvl/apollo-5.0) needs to be installed (preferably on another computer to achieve high-level performance). It is required to run the bridge to connect the Innopolis Simulator with Apollo. Since Apollo 5 does not use ROS, need to install the cyber bridge.


1. Create bridge.sh with following code then put it into apollo/scripts folder. Download
[bridge.tar.gz ](https://github.com/inno-robolab/InnoSimulator/blob/master/bridge.tar.gz) and extract into apollo/cyber folder.
```
    #!/usr/bin/env bash
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

    cd "${DIR}/.."

    bazel-bin/cyber/bridge/cyber_bridge
```

2. Run the command `bazel build //cyber/bridge:cyber_bridge`. If command bazel is not found, then make sure that you are inside the docker container.
3. Execute `/apollo/scripts/bridge.sh`. If you receive the error "permission denied" then write `chmod +x /apollo/scripts/bridge.sh` and repeat. It is also better to enter source scripts/apollo_base.sh before to avoid any problems. If the server started successfully then you will see the output:
_[cyber_bridge] host ip: **you ip address**_
4. Success! Connect your Innopolis Simulator to the bridge.
5. To check whether messages are received in apollo
```
    apollo.sh build_cyber
    source /apollo/cyber/setup.bash
    cyber_monitor
```

6. Don't forget to download our latest [HD map](hdmap/) before starting the simulation and extract it into _/apollo/modules/map/data folder_. Execute `cd /apollo/modules/common/data` then open global_flagfile.txt and change the line: `--map_dir=/apollo/modules/map/data/innopolis_mppi`. Restart DreamView `/apollo/scripts/bootstrap.sh stop` and `/apollo/scripts/bootstrap.sh start`


**Full description how to use simulator you can find [here](Docs/HowToUse.md).**

### Premade scenes
There're some example ready-to-use scenes. Every scene is dedicated to our team's internal requests for testing purposes. 

## Python API
Innopolis Simulator supports Python API functionality. Full description can be found [here](Docs/PythonApi.md). 

## License
This project is licensed under the [MIT License](LICENSE)
