title: Introduction to PyOpenCL
authors: Alex Fforde, Roshan Pasupathy
date: 2017-03-20
tags: NGCM, OpenCL, Python, C, PyOpenCL
slug: OpenCL2017

![OpenCL Logo]({filename}/PyOpenCL/opencl_logo.jpg)

# OpenCL #

Open Computing Language is a framework for writing programs that execute across heterogeneous platforms consisting of several elements, of which we're going to working with central processing units (CPUs) and graphics processing units (GPUs). OpenCL offers highly decreased computation times for complex programs by taking advantage of the CPU/GPUs ability to run programs in parallel.

# Workshop #

While OpenCL offers much higher performance, it also has a difficult entry barrier that requires a good understanding of the concepts behind OpenCL's operation. The aim of this workshop is to introduce those concepts and lower the barrier by showing users how to interface with it using Python and an extension called PyOpenCL. 

# Prerequisites #

Use of PyOpenCL requires users to have knowledge of programming in both the Python and C languages. A Virtual Machine is available with all the software pre-installed [here](www.southampton.ac.uk/~ngcmbits/virtualmachines/Ubuntu14_PyOpenCL.ova) (WARNING: 4 GB Download). For those not using the VM, they will need to install Python and PyOpenCL on their machine and OpenCL as well if it isn't already included. Note that not using the Virtual Machine does allow PyOpenCL to access devices besides the  CPU (if your machine has them).

The password for the VM is **feeg6003**. In Terminal, users should navigate to **feeg6003/Documents/opencl_workshop/** and run the command **git pull origin**.

This will download the exercises for the workshop. To access all the exercise materials (including correct exercise answers), they can be downloaded from [here]({filename}/PyOpenCL/Exercises.zip).

# Presentation Slides #

For just the slideshow used during the workshop, it can be retrieved from [here]({filename}/PyOpenCL/Presentation.pptx) and provides an introduction to the concepts of OpenCL's operation as well as a rough guide to the individual Python commands to use PyOpenCL. The presentation provides clues to completing the exercises and should be seen as a guide of sorts.

# Exercise 1 #

Exercise 1 is designed to get users familiar with writing code for the kernel that PyOpenCL feeds to the CPU or GPU. A template called **vector_add.cl** is provided and should be edited using a text editor of your choice. The skeleton of the function is provided and all that is required is to write the function body.

Save the completed .cl file and in the same folder it is located, run **python vector_add.py**. This will run the kernel through a python script and determine whether it was successful.

# Exercise 2 #

This exercise requires the user to edit the kernel **matrix_mult.cl** and complete the function body. The aim of this is to get users familiar with using more than just one global id.

When completed, save the file and run **python matrix_mult.py**, if the file is correct no error will be printed, just the time taken to complete the operation.

# Exercise 3 #

This exercise introduces the concept of fitting multiple work-items into a single work-group and requires the user to edit **vector_iteradd.cl** and complete the function body.

When completed, save the file and run **python vector_iteradd.py**, the python script will determine if the kernel was correct.

# Exercise 4 #

Finally, this exercise aims to show users how to write Python commands to use OpenCL. A incomplete file, **exercise4.py** has been provided with several arguments missing that need to be inserted;

* d_b
* d_c
* globalrange
* localrange
* arg_type_list

When complete, save the file and run **python exercise4.py**, a correctly filled in file will produce no errors and just a run time associated with running the kernel.



Hopefully users should now feel more comfortable creating their own programs to run through PyOpenCL. 
