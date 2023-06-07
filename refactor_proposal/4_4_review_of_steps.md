### Review of Build Steps

The biggest issues with following these steps are mostly due to the challenge of tracing down what each task does, what it needs to be successful, and how to test if it is successful.

#### Data Directory

The writing of the data to files to store the results between each task while it works well is not docuemented. So from an outside context it is hard to determine what file/directory is created from which function. This can be solved by any of these methods: 
- using documentation in each function listing where the data will be written
- separating the steps with their data into specific directories
- renaming the data directories to match the function's they are created by

#### Failure Handling and Checking

In the annotation phase, external APIs are used to harmonize the parsed variables. In this process if the API fails then the entire process will crash. This is just one example of the lack of failure handling in this process. Allowing for graceful failure of a step will greatly reduce the dealy time of running these processes.
In other portions of the code it is very challenging to know if the results are correct or if there is a failure. This can be solved by each step utilizing tests that tell the user whether the results are correct or not.

#### Code Placement

It is very challenging to read/follow this codebase for several reasons:

- The amount of components that are needed to run the process are massive. Also the components themselves are complex and opaque. This makes making even small changes to the code or data very hard. i.e. Tranql and Plater and their interaction with knowledge graph.
- The code is configured into montolithic files. i.e. All of the steps mentioned in phases 1-3 use core.py. This makes the code hard to read.
- The code incorporates Dug repository. If an error is encountered in Dug then a new release of Dug must be created to fix the issue in Roger.

#### Documentation

I have already stated this earlier but if the code can be split out then creating documentation for each component will help users understand what each step is doing and how to measure its success or failure.

In my mind there should be user documentation for each type of build (i.e. commandline/makefile, Argo, Airflow), each step in the process with it's outcomes and where the results are written, and each function with all of it's dependencies written as well.