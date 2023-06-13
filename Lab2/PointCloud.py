import csv
import numpy as np


from Lab2.PlaneRANSAC import PlaneRANSAC

class PointCloud:
    max_iterations = 100
    k = 3
    def kmeans(self):

        centroids = self.points[np.random.choice(self.points.shape[0], size=self.k, replace=False)]
        for _ in range(self.max_iterations):
            distances = np.sqrt(((self.points - centroids[:, np.newaxis]) ** 2).sum(axis=2))
            labels = np.argmin(distances, axis=0)
            new_centroids = np.array([self.points[labels == i].mean(axis=0) for i in range(self.k)])
            if np.all(centroids == new_centroids):
                break

            centroids = new_centroids

        return labels

    def __init__(self, file_name):
        self.points = self._load_points(file_name)

    def _load_points(self, file_name):
        points = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                points.append([float(i) for i in row[0].split()])
        return np.array(points)

    def cluster_points(self, num_clusters):
        self.labels = self.kmeans()
        self.clusters = [self.points[self.labels == i] for i in range(num_clusters)]

    def fit_planes(self, num_iterations, threshold):
        self.planes = []
        for cluster in self.clusters:
            ransac = PlaneRANSAC(num_iterations, threshold)
            ransac.fit(cluster)
            self.planes.append(ransac)

    def analyse_planes(self, distance_threshold):
        for i, (plane, cluster) in enumerate(zip(self.planes, self.clusters)):
            a, b, c, d = plane.coefficients
            distances = plane._distances_from_plane(plane.coefficients, cluster)
            mean_distance = np.mean(distances)
            normal_vector = np.array([a, b, c])

            if mean_distance < distance_threshold:
                print(f"Cloud {i + 1} is a plane with normal vector coordinates: ({a}, {b}, {c})")
                if np.abs(np.dot([0, 0, 1], normal_vector / np.linalg.norm(normal_vector))) < 1 / np.sqrt(2):
                    print("The plane is vertical.")
                else:
                    print("The plane is horizontal.")
            else:
                print(f"Cloud {i + 1} is not a plane.")


