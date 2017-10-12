========================
Avida-ED Testing Project
========================

Introduction
------------
This project contains a test suite for the web-based version of Avida-ED_, an award-winning educational application developed at `Michigan State University`_ for undergraduate biology courses to help students learn about evolution and scientific method by allowing them to design and perform experiments to test hypotheses about evolutionary mechanisms using evolving digital organisms.

.. _Avida-ED: https://avida-ed.msu.edu/
.. _`Michigan State University`: https://msu.edu/

This project uses Selenium to run automated tests in a web browser against the Avida-ED application (running either locally or on the Internet). The test suite is being developed mainly with Chrome in mind, but tests should be runnable in Firefox at some future point.

Installation
------------

**IMPORTANT**:

One of the most important things to be conscious of during the installation process is that you are always using the correct Python interpreter. Almost all Mac users and many Windows users will already have a Python 2.7 installation on their computer, which will NOT be able to run this testing project.

You can determine which Python interpreter your computer runs by default by running the command ``which python`` (for Mac) or ``where python`` (for Windows) from a command prompt window. If the path that these commands output contains ``python36``, you should be fine -- if it contains ``python27`` instead, you will need to be careful.

If you run into this problem, see the section labelled *Dealing With Multiple Python Versions* below.

**Windows:**

1. Install `Python 3.6`_. During the installation process, make sure that the option to also install pip_ is checked. Alternatively, you can install pip_ separately.
2. (Optional) Install PyCharm_ or another Python IDE of your choice.
3. If you have not already done so, download/clone this repository to your computer. If you plan on running the test suite locally (which is the default setting), you should also acquire a local version of the main `Avida-ED UI repository`_. You do not have to put these in any specific place, but keep track of their locations -- you will need them later.
4. Install any browsers that you plan to run the test suite with. This test suite currently supports Chrome_ and may support Firefox_ in the future.
5. If you are using Chrome, you will need to download Chromedriver_, the tool that allows Selenium to interact with Chrome. The directory where chromedriver.exe is located must also be added to your system path. See `this tutorial`_ on how to do this in Windows. If you are using Firefox, you will need to download Geckodriver_ and add its location to the system path -- however, you should be aware that not all tests run properly in Firefox at this time.
6. (Recommended) This project requires several specific Python packages to run properly. If you use or plan to use the Python 3 installation on your computer to do anything outside the scope of this project, it is helpful to isolate the package requirements for this project to prevent clashing of dependencies with other Python projects. This can be done with a virtual environment. It is possible to set up a project-specific virtual environment `through PyCharm`_, or you can create one manually (the virtualenv_ Python package would be useful for this -- install it via the command ``pip install virtualenv``).
7. Use pip to install the required packages listed in requirements.txt. This can be done easily by running the command ``pip install -r requirements.txt`` from the ``avida_ed_testing`` folder.
8. If you want to run the tests locally (which is the default setting), you will need to provide the location of the Avida-ED UI repository using the --setuipath option. More information about this option is given below. NOTE: You only need to use --setuipath the first time you run the experiment -- the location you give will be saved by the test suite.

**Mac:**

The installation process is essentially the same as for Windows. However, the process of adding something to the system path will be different -- this guide_ explains how you can do this. Also, it is important to make sure you are using the correct Python interpreter to run the test suite, since Macs tend to come with Python 2.7 preinstalled. Please see the section marked IMPORTANT above for more information.

**Dealing With Multiple Python Versions:**

Windows:

It will be quite difficult to manage two separate Python installations that are both  easy to use on Windows. However, if you find yourself in a situation where this is necessary, there are a few steps that you can take. Launching Python should be fairly easy using the Python Launcher for Windows -- simply type ``py -3`` for Python 3.6 and ``py -2`` for Python 2.7. To run both versions of pip at the same time, there are specifically named versions of pip called ``pip2`` and ``pip3``. To use them, you will need to add the folders they are stored in to your system path (see `this tutorial`_. The folders should be something like this: ``C:\\Path\to\Python36\Scripts`` and ``C:\\Path\to\Python27\Scripts``. Once these folders are added to your system path, you should be able to use both versions of pip without trouble. You will then need to replace any use of ``python`` in the installation/use instructions with ``py -3`` and ``pip`` with ``pip3``. However, as this setup can be confusing, I would highly recommend creating a virtual environment to isolate your dependencies and interpreter using either of the methods described in the installation instructions.

Mac:

Affix a '3' to Python-related command on the command line; for example, ``python3`` instead of ``python`` or ``pip3`` instead of ``pip``. This should work in most instances -- if it does not, you may need to add the some of the Python folders to your system path (see this guide_).


Use
----

**Note: If you plan to run the tests locally, you will need to use the --setuipath [PATH] option during your first test run to specify the location of your local copy of the Avida-ED UI. In subsequent runs you won't need to do this unless you change the location of av_ui. Likewise, if you are running the tests on the online version of Avida-ED, you will need to use --seturl [URL] to specify the URL to the online version. See below for more information.**

First, if you are using a virtual environment, make sure that it is activated. You should see the name of the virtual environment in parentheses before each line you type in your command-line interface if the virtual environment is activated.

The easiest way to run the tests is through the test suite files, located in the tests folder. The following command (simply typed into a command-line interface from the root folder of the project) will run all tests classified as 'basic':

``python tests/test_suite_basic.py``

There is also a test suite for tests that are considered 'advanced' -- however, this suite does not run any tests, because there are none marked as advanced. If you would like to inspect this file, it is located at ``tests\test_suite_advanced.py``.

It is possible to run a single test file (containing one or more test cases with a common purpose) using the following command:

``pytest path\to\test\testfile.py``

All of the tests are located within subdirectories of the ``tests`` folder within the ``avida_ed_testing`` folder. For example, there is a simple navigation test at ``tests\common\common_basic\navigaton\basic_nav_test.py``.

Alternatively, one can simply run ``pytest`` from the ``avida_ed_testing`` folder to run all of the tests from all of the test files.

There are also several command-line options that can be provided:

- --browser [BROWSER]\: Changes the browser used to run the tests. Current options are chrome (default) and firefox (not fully supported yet).

- --local [true/false]\: Sets whether the tests should be run on a local copy of Avida-ED (using a simple Python web server) or the copy hosted online by MSU. Providing "false" as the argument will run the tests on the MSU version, while any other input (or not specifying) will make the tests run locally.

- --setuipath [PATH]: Used to set the path to the Avida-ED UI repository, which is used to run the tests locally. You should provide the path to the ``av_ui`` folder (assuming you didn't change the name of the folder that contains the Git repository).

- --setffpath [PATH]: Used to set the path to the Firefox binary, which at this time is needed to run the tests via Firefox. However, this has not been thoroughly tested and Chrome is recommended to run tests at this time.

- --seturl [URL]: Used to set the URL for the online version on Avida-ED.

These options can be used when running individual tests or the test suite.

.. _`Python 3.6`: https://www.python.org/downloads/
.. _pip: https://pypi.python.org/pypi/pip/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _`Avida-ED UI repository`: https://github.com/DBlackwood/av_ui
.. _Chrome: https://www.google.com/intl/en/chrome/browser/desktop/index.html
.. _Firefox: https://www.mozilla.org/en-US/firefox/new/
.. _Geckodriver: https://github.com/mozilla/geckodriver/releases
.. _Chromedriver: https://sites.google.com/a/chromium.org/chromedriver/
.. _`this tutorial`: https://www.java.com/en/download/help/path.xml
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
.. _`through PyCharm`: https://www.jetbrains.com/help/pycharm/2017.1/creating-virtual-environment.html
.. _guide: https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/#.Waog9umQxPY
