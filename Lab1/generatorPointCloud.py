import numpy as np


class GeneratorPointCloud:

    def __init__(self, number_of_points):
        self.number_of_points = number_of_points

    def generate_on_horizontal_surface(self, width, length):
        x = np.random.uniform(-width / 2, width / 2, self.number_of_points)
        y = np.random.uniform(-length / 2, length / 2, self.number_of_points)
        z = np.zeros(self.number_of_points)
        return np.vstack((x, y, z)).T

    def generate_on_vertical_surface(self, width, height):
        x = np.random.uniform(-width / 2, width / 2, self.number_of_points)
        z = np.random.uniform(-height / 2, height / 2, self.number_of_points)
        y = np.zeros(self.number_of_points)
        return np.vstack((x, y, z)).T

    def generate_on_cylindrical_surface(self, radius, height):
        theta = np.random.uniform(0, 2 * np.pi, self.number_of_points)
        z = np.random.uniform(-height / 2, height / 2, self.number_of_points)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        return np.vstack((x, y, z)).T

    def save_to_xyz_file(self, points, filename):
        np.savetxt(filename, points, delimiter=' ', fmt='%1.4f')
