import numpy as np
from scipy.spatial import distance

def nearestDistances(c1, c2):
    c_1 = np.array(c1)
    c_2 = np.array(c2)    
    return distance.cdist(c_1, c_2).min(axis=1)

def calculate_acd(contour_xy_1, contour_xy_2):
    d1 = nearestDistances(contour_xy_1, contour_xy_2)
    d2 = nearestDistances(contour_xy_2, contour_xy_1)

    return round(0.5 * (d1.sum() / len(contour_xy_1) + d2.sum() / len(contour_xy_2)), 5)