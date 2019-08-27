# Minimetro solver

This is a work in progress solver to minimetro. Currently it can detect stations in some input images and plan routes (not based on games rules yet).

# Example

![Input](inputs/1jpg?raw=true "Input")

![Input processed](inputs/proc/1jpg?raw=true "Input processed")

![Output](outputs/1jpg?raw=true "Output")

# Requeriments

- OpenCV
- Numpy
- Tabulate
- Google OR Tools

`pip install opencv-python numpy tabulate ortools`

# Run

To run the script need to receive a image as input, this repo have some images to try on.

`python main.py inputs/1.jpg`
