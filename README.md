# benchmark-deep-learning
I created this repository as an interest to how well apple metal will do in a sample deep learning models opposed to Nvidia Cuda

Here's how to get jupyter notebook to run on macs

System Requirments
Minimum MacOs 13.x Ventura with a GPU
Devices that were dropped are:

iMac17,x and older
Macmini7,1 and older
MacBook9,1 and older
MacBookAir7,x and older
MacBookPro13,x and older
MacPro6,1 and older

Installation Steps for Macs:
command + spacebar and type terminal and enter

install the virtual environment:
python3 -m venv ~/venv-metal (you can change to any name you prefer after ~/)
source ~/venv-metal/bin/activate
python -m pip install -U pip 
pip3 install --upgrade pip

install tensorflow (the libraries)
python -m pip install tensorflow (ver 2.13 or later)
python -m pip install tensorflow-macos (ver 2.12 or earlier)

install tensorflow-metal (the software that instructs the GPU)
python -m pip install tensorflow-metal

install jupyter notebook (at the top level python interface)
pip3 install jupyter

after completing the installation you can install each python libraries in jupyter or in the vitual environment 

while the virtual environment is still on:
type jupyter notebook


