# Python Programming Workshop

Welcome to the Library Python Programming Workshop!

We meet once a week to learn how to program in the Python progamming language.  This is a work at your own pace and collaborate with others environment; Just bring any questions and stuff you'd like to look at each week and we all benefit as a group looking at it. 

We have a bunch of coureswork ready to use, including:
* Python Basics 
* Data analysis with "Pandas"

See the Notebooks list below for a more detailed list.

## Current Schedule:
We were meeting on wednesdays during October, but due to a scheduling conflict, we'll bo moving to Thursdays.
* Thursday Dec 12 - 4:30PM to 5:30PM
* Thursday Dec 19 - NO MEETING Library Winter Wonderland Event
* Thursday Dec 26 - 4:30PM to 5:30PM
* Thursday Jan 02 - NO MEETING Vacation
* Thursday Jan 09 - 4:30PM to 5:30PM
* Thursdays ongoing. 

Please check the library calendar here to confirm dates/times: **https://engagedpatrons.org/EventsCalendar.cfm?SiteID=7839**
* Set "limit by location" to "Cameron Park Library".

## Getting Started
You need a place to run python code and open "ipython notebooks".  Let us know if you need a laptop to use during class.

Our recommended mode of work will be in notebooks on google Colab: https://colab.research.google.com/
* Sign up for a google account if you don't have one.
* Log in to https://colab.research.google.com and skim over the readme info
* Open the week one notebook that we'll be working from:
  * Go to File -> Open Notebook -> Github, and paste in "a8ksh4/python_workshop".
  * Open the Library Week 1 notebook file
* There's a nice intro video for colab here: https://www.youtube.com/watch?v=inN8seMm7UI
 
If you're working from your own laptop and want to open notebooks locally rather than in colab, I'd recommend insalling the the Anaconda Python distribution from here: https://www.anaconda.com/products/distribution
  * In windows, I'd recommend NOT running the installer as administrator - Install for only a single user when prompted.  It's easier to install packages if it is installed in your home directory rather than a shared area for all users.
  * Anaconda is available for Windows, Mac, and Linux!
  * You can use any python distribution, but Anaconda is highly recommended becuase its package manager works so well and it has support for so many libraries out-of-the-box.

It's also nice editing notebooks and code in VS Code.  I think that works well with a plain python instal on your computer, so you'd want to use these:
* Python: 
* VS Code: 
  * Install extensions

## Notebooks Summary
We have a series of python notebooks ready to work through to learn from.  They include all of the information you need to learn, links to additional resources, and programming problems to work through for each topic.  

* A-Getting_Started.ipynb - Introduction to Python and Google Colab. Covering variables and data types (numeric, strings, boolean), truthiness, and basic control flow (if-else statements).
* B-Dictionaries_and_Loops.ipynb - Exploring more complex data types (lists, tuples, dictionaries) and advanced control flow (loops: for and while).  Opening files and intro to json.
* C-Functions_and_Module_Imports.ipynb - Introducing functions and modules in Python.
* D0-Pandas_Example.ipynb - An example of importing data and doing some anaylsis and graphing to get a feel for how pandas works. 
* D1-Pandas_Intro_and_Data_selection.ipynb - Some pandas basics including imoprting data, manipulating columns of data, learning ways to select rows and columns of data, and exporting data to file. 
* D3-Pandas_Graphing.ipynb - Goes over a bunch of plot types multi-axis plots, and graphs with multiple plots using pd.plot (wrapper for matplotlib pyplot)
* N-Numpy - Basics using numpy.  Need to add some vectorization problems where we convert python code to numpy code...

**In Development**
* D2-Data_Cleaning.ipynb - Setting column data types, removing missing or invalid data, interpolation, etc tools for preparing data for analysis.

* D4-Advanced_Pandas.ipynb - Pivot, stack, unstack, join, concatenate, etc. 
* D5-Machine_Learning.ipynb - Methods to use machine learning to model data using pandas and common ML libraries. Building on pandas skills with more advanced data manipulation and introduction to data visualization using pandas and matplotlib for generating graphs.
* E-Writing_Scripts.ipynb - Installing python locally, environment, structure of a script, and argparse
* F-Microcontrollers_Intro.ipynb - Circuitpython and Micropython on common microcontroller boards.
* G-Exception_Handling.ipynb - Try/Except blocks and Error Handing.
* H-Unit_Tests.ipynb - Writing test cases to verify your code works as designed.
* S-Subprocess_and_System_Calls.ipynb - Usage of the subprocess module for running commands outside of python
* T-Datetime.ipynb - Python Datetime Objects
* V-Virtual_Environments.ipynb - 

## Resources
**Documentation**
* https://docs.python.org/3/ - Python Documentation
* https://www.w3schools.com/python/default.asp - Great documentation and Examples
* https://peps.python.org/pep-0008/ - "Pep 8" style guide
* https://google.github.io/styleguide/pyguide.html - Google style guide
* https://github.com/jsantarc/cognitiveclass.ai-Python-for-Data-Science - Data science notebooks

**Online Programming Tools**
* https://replit.com/

### Notes on AI like ChatGPT
These tools are **very** helpful for learning.  For this course, use them to explain how things work, but don't ask them to write code for you.  If you don't experiment and learn for yourself, you won't retain as much.  Keep all of your code and use your past code as the start for each more complicated problem.  You'll build a toolkit of libraries and code bits that you understand and make all kinds of things from.

* https://chat.openai.com/chat
* Example questions:
  * How do I use for loops in python?
  * How do I configure VS Code to use my Anaconda python interpreter?
  * etc!  

## Github
This content is hosted here in a Git repository. You can check out a copy to your computer and "pull" updates with a git client:
* Make a github.com account and install git. 
  * Linux:  sudo apt-get install git
  * Windows:  https://git-scm.com/download/win
  * Check out this repository in your project area: git clone https://github.com/a8ksh4/python_workshop.git`

Feel free to open "bug reports" in this repo for content you'd like to see added, changes needed, or corrections.  Or make  an improvement and submit a pull request and I'll merge your changes into the repo.

## Code Editors
Install a text editor with code highlighting or an IDE for writing code in:
* Notepad ++: http://notepad-plus-plus.org/
* VS Code: https://code.visualstudio.com/

If you're programming circuitpython or micropython on a microcontroller, Thonny is the best editor to start with.  It has a built in serial console for seeing output from your code, and helps handle updating the code files on the board for you. An IDE like VS Code or IntelliJ with a Micropython or Circuitpython extension would be more powerful, but more complicated to set up.
* https://thonny.org/

