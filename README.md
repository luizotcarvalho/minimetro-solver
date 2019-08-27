# Minimetro solver

This is a work in progress solver to minimetro. Currently it can detect stations in some input images and plan routes (not based on games rules yet).

# Example

![Input](inputs/1jpg?raw=true "Input")

![Input processed](inputs/proc/1jpg?raw=true "Input processed")

![Output](outputs/1jpg?raw=true "Output")

# Requirements

- OpenCV
- Numpy
- Tabulate
- Google OR Tools

`pip install opencv-python numpy tabulate ortools`

# Run

To run the script need to receive a image as input, this repo have some images to try on.

`python main.py inputs/1.jpg`

and will output something like this:

```
Stations

|   index | type     | pos          | centroid     | size     |
|---------|----------|--------------|--------------|----------|
|       0 | circle   | (1235, 1105) | (1253, 1122) | (37, 36) |
|       1 | circle   | (1741, 1066) | (1758, 1083) | (37, 36) |
|       2 | rhombus  | (1040, 1065) | (1058, 1083) | (38, 38) |
|       3 | circle   | (1858, 988)  | (1875, 1005) | (36, 36) |
|       4 | droplet  | (1158, 987)  | (1175, 1006) | (36, 34) |
|       5 | circle   | (1430, 949)  | (1447, 966)  | (36, 36) |
|       6 | cross    | (1662, 947)  | (1680, 966)  | (39, 40) |
|       7 | pentagon | (1275, 909)  | (1291, 927)  | (35, 35) |
|       8 | star     | (1544, 868)  | (1564, 888)  | (42, 39) |
|       9 | circle   | (1002, 793)  | (1019, 810)  | (36, 36) |
|      10 | triangle | (1778, 755)  | (1797, 776)  | (40, 34) |
|      11 | circle   | (1158, 715)  | (1175, 732)  | (36, 37) |
|      12 | square   | (887, 639)   | (902, 655)   | (32, 33) |
|      13 | circle   | (1547, 637)  | (1564, 655)  | (36, 37) |
|      14 | circle   | (1274, 637)  | (1291, 655)  | (37, 37) |
|      15 | circle   | (1702, 599)  | (1720, 616)  | (37, 36) |
|      16 | circle   | (1041, 599)  | (1058, 616)  | (36, 36) |
|      17 | triangle | (728, 599)   | (747, 620)   | (39, 34) |
|      18 | circle   | (1430, 560)  | (1447, 577)  | (36, 36) |
|      19 | triangle | (572, 521)   | (591, 542)   | (40, 34) |
|      20 | triangle | (1224, 473)  | (1253, 506)  | (60, 52) |
|      21 | triangle | (1039, 443)  | (1058, 464)  | (40, 34) |
|      22 | triangle | (1467, 405)  | (1486, 425)  | (40, 33) |
|      23 | circle   | (885, 404)   | (902, 421)   | (36, 37) |
|      24 | triangle | (689, 327)   | (708, 348)   | (39, 33) |
|      25 | circle   | (1274, 326)  | (1291, 343)  | (37, 37) |
|      26 | triangle | (1156, 249)  | (1175, 270)  | (40, 34) |
|      27 | triangle | (844, 249)   | (863, 270)   | (40, 34) |
|      28 | circle   | (1547, 248)  | (1564, 265)  | (36, 37) |
|      29 | circle   | (1002, 209)  | (1019, 227)  | (36, 37) |
|      30 | circle   | (1313, 170)  | (1330, 188)  | (37, 37) |
|      31 | circle   | (1469, 132)  | (1486, 149)  | (37, 36) |
|      32 | circle   | (691, 132)   | (708, 149)   | (36, 36) |

Routes

|   index |   vehicle_index | route                                    |
|---------|-----------------|------------------------------------------|
|       0 |               0 | [0, 5, 8, 13, 15, 10, 3, 1, 6]           |
|       1 |               1 | [0, 17, 19, 24, 32, 27, 23]              |
|       2 |               2 | [0, 2, 9, 12, 16, 21, 29, 26, 20, 14, 7] |
|       3 |               3 | [0, 4, 11, 25, 30, 31, 28, 22, 18]       |

Results saved in output/1.jpg
```
