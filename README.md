# Homework 3: From Notebooks to Research Packages, Part II

_This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Fall 2025 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science](https://ucb-stat-159-f25.github.io/site/). Authorship of the original analysis code rests with the LIGO collaboration._

## Description:
This repository creates the LIGO project as a reproducible research package, specifically focusing on the GW150914 event. There exists 3 folders to store data, audio, and figures for the LOSC_Event_tutorial.ipynb and an installable ligotools package. There also exists a utils module to transform, save, and plot specific data. There are tests for ligotools and utils to make sure the functions work as intended which can be checked with the `pytest ligotools` command. A Makefile exists to create an environment, build the html, and clean the audio, figures, and _build folders. There is a binder link below to open this repository in a separate Jupyter environment and run the notebook.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-sofialen0408.git/HEAD?urlpath=%2Fdoc%2Ftree%2FLOSC_Event_tutorial.ipynb)

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)