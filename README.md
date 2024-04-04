<h1><span style="color:#03234B"> STM32ai-nota </span></h1>

<h2> Neural network pruning by using NetsPresso </h2>

This repository provides a guide on how to compress neural network models to reduce their memory footprints and computational requirements, making deployment on STM32 targets easier. The particular compression method highlighted in this repository is structural pruning, achieved by using NetsPresso. Please browse the [Docs](https://nota-netspresso.github.io/PyNetsPresso/) for details about it  

The tutorials are presented as Jupyter notebooks and config files, which will guide you through the process of training, pruning, fine-tuning, and quantizing a deep learning model using NetsPresso and the STM32AI Model Zoo. You can then benchmark the models by using the STM32Cube.AI Developer Cloud. The notebooks provide a step-by-step guide for users, making it easy for anyone to compress their neural network models efficiently and deploy them on STM32 targets.


<div align="center">
    <p align="center">
        <a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/python-3.9%20%7C%203.10-blue" /></a>
        <a href="https://www.tensorflow.org/install/pip" target="_blank"><img src="https://img.shields.io/badge/TensorFlow-2.8.3-FF6F00?style=flat&logo=tensorflow&logoColor=#FF6F00&link=https://www.tensorflow.org/install/pip"/></a>
        <a href="https://github.com/STMicroelectronics/stm32ai-modelzoo"><img src="https://img.shields.io/badge/stm32ai modelzoo-2.0.0-273B5F?style=flat&logo=github&logoColor=#03234B"/></a>
        <br>
        <a href="https://netspresso.ai?utm_source=git&utm_medium=text_np&utm_campaign=py_launch"><img src="https://img.shields.io/badge/NetsPresso-Open in Website-1BD2EB?style=flat&link=https://netspresso.ai/"/></a>
        <a href="https://stm32ai-cs.st.com/home"><img src="https://img.shields.io/badge/STM32Cube.AI-Developer%20Cloud-FFD700?style=flat&logo=stmicroelectronics&logoColor=white"/></a>  
    </p>
</div>
</br>


## Repository Components

The repository contains the following folders:

- **utils**: Contains utility functions used in the notebooks.
- **image_classification**: 
   - `netspresso_model_pruning.ipynb`: a notebook for image classification model pruning.
   - **config_files** : contains the yaml config files to use with the notebook.
   - **experiments_outputs** : contains the directories and files created during the runs.   
   - **pretrained_models** : contains several baseline models and NetsPresso pruned models with their performances listed in the [README](image_classification/README.md)
- **object_detection**: Coming soon. 

## Before you start

* Create an account on myST and then sign in to [STM32Cube.AI Developer Cloud](https://stm32ai-cs.st.com/home) to be able access the service.
* Alternatively, install [STM32Cube.AI](https://www.st.com/en/embedded-software/x-cube-ai.html) locally by following the instructions provided in the [user manual](https://www.st.com/resource/en/user_manual/um2526-getting-started-with-xcubeai-expansion-package-for-artificial-intelligence-ai-stmicroelectronics.pdf) in **section 2**, and get the path to `stm32ai` executable. 
* Create an account on [NetsPresso](https://netspresso.ai/?utm_source=git&utm_medium=text_signup&utm_campaign=np_renew).
* If you don't have python already installed, you can download and install it from [here](https://www.python.org/downloads/), a **Python Version <= 3.10** is required to be able to use TensorFlow later on, we recommand using **Python v3.9 or v3.10**. (For Windows systems make sure to check the **Add python.exe to PATH** option during the installation process).
* Install Jupyter server and notebook libraries to run the Jupyter notebooks.
* Clone this repository using the following command:
    ```
    git clone https://github.com/STMicroelectronics/stm32ai-nota.git
    ```
* Create a python virtual environment for the project:
    ```
    cd stm32ai-nota
    python -m venv <env-name>
    ```
