# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package


### Using pip3 to install from PyPI

```bash
pip3 install chenla_diffusion2D
```

### Required dependencies

* Check if your system has Python version >= 3.6 and update it if it is older than 3.6.
* Install pip, build, and Twine.
* Install NumPy and Matplotlib with pip.

## Running this package

You could run the package via `diffusion2d.solve()` after import. This will generate 4 plots with the default parameters `dx=0.1, dy=0.1, D=4.`, where `dx` and `dy` are intervals in x-, y- directions (mm), and `D` is the thermal diffusivity of steel (mm^2/s).

```python
from chenla_diffusion2D import diffusion2d

diffusion2d.solve()
```

You could also assign the values of `dx`, `dy` and `D` by yourself.

```python
from chenla_diffusion2D import diffusion2d

diffusion2d.solve(dx=0.5, dy=0.5, D=16)
```

## Citing
