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
InnoSim allows significantly decrease the cost of autonomous systems development process, especially in part of sensor equipment tuning and testing, control and interaction with another static and dynamic objects.

![Inno_Car_Model](Docs/Media/SimView01.png)


## Functionalities

InnoSim provide the environment for debugging and modeling the behavior of users autonomous systems in real-time and in real 3D environment, which will avoid critical design errors, quickly clarify low-level requirements for individual nodes, shift the verification process to earlier stages, carry out more iterations of the prototype research in a short period of time and save on field tests.

## Video


[![Watch the video](Docs/Media/VidPreview.png)](Docs/Media/SimVid.mp4)


### Run tests with simulator
For carrying out full-scale tests and testing of the entire functionality of the simulator, [Apollo](https://github.com/lgsvl/apollo-5.0) need to be installed (preferably on another computer to achieve high-level performance). To allow the simulator communicate with Apollo you need to install Rosbridge and read installation instructions from [here](https://github.com/lgsvl/rosbridge_suite). 


1.  Run rosbridge:
```
   roslaunch rosbridge_server rosbridge_websocket.launch
```

2.  Run Apollo:To launch apollo, first launch and enter a container as described in the same [link](https://github.com/lgsvl/apollo) as in description of this chapter.
```
   ./scripts/bootstrap.sh
```
Don't forget to download our latest [HD map](hdmap/) before starting the simulation

**Full description how to use simulator you can find [here](Docs/HowToUse.md).**

### Premade scenes
There're some example ready-to-use scenes. Every scene is dedicated to our team's internal requests for testing purposes. 

## Pyhton API
Innopolis Simulator supports Python API functionality. Full description can be found [here](Docs/PythonApi.md). 

## Licence
This project is licensed under the [MIT License](LICENSE)
