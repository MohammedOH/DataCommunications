# DataCommunications

#### Info
```
This repository is for learning about Data Communication in a university course. 
This project will generate a PDF file that shows the topology that connects you to the internet.
```
### Prerequisites
Make sure you have installed all of the following prerequisites on your pc:
* You should have [Python 3.x](https://www.python.org/downloads/) on your system.
* Graphviz - [Download & Install Graphviz](https://graphviz.org/download/). Note that for Linux you just execute the command. However, for windows you should download the [Setup file](https://www2.graphviz.org/Packages/development/windows/10/cmake/Release/), and install it. Then you should add the path of Graphviz (e.g. "C:\Program Files\Graphviz 2.44.1\bin\dot.exe") to your system enviroment variables as GRAPHVIZ_DOT, see this [link](https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them) if you need help on doing this.

#### Usage

Edit `config.py`, add or remove any website you want.
Run `main.py`, and wait for the result.

#### Note that
* It's going to take some time to finsish executing.
* For each websites there is two files will be generated. First one is `website`.txt & `website`-graph.txt, if you wish to delete these files after the program ends edit `config.py`.
* Result is generated as a pdf file, change `result_file_name` from `config.py` if you wish.
