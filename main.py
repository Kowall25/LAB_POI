# This is a sample Python script.
from Lab1.generatorPointCloud import GeneratorPointCloud
from Lab2.PlaneDBSCAN import PlaneDBSCAN
from Lab2.PointCloud import PointCloud

def start_screen():
    while True:
        print("Choose LAB:")
        print("1. LAB 1")
        print("2. LAB 2")
        print("4. Exit")

        lab = input("Enter the number of the LAB: ")

        if lab == '1':
            while True:
                print("1. Generate points on a horizontal surface")
                print("2. Generate points on a vertical surface")
                print("3. Generate points on a cylindrical surface")
                print("4. Return to exercise selection")

                choice = input("Enter the number of the operation you want to perform: ")

                if choice == '1':
                    width = float(input("Enter the width of the surface: "))
                    length = float(input("Enter the length of the surface: "))
                    number_of_points = int(input("Enter the number of points to generate: "))
                    gen = GeneratorPointCloud(number_of_points)
                    points = gen.generate_on_horizontal_surface(width, length)
                    filename = input("Enter the name of the file you want to save points to: ")
                    gen.save_to_xyz_file(points, filename + '.xyz')
                elif choice == '2':
                    width = float(input("Enter the width of the surface: "))
                    height = float(input("Enter the height of the surface: "))
                    number_of_points = int(input("Enter the number of points to generate: "))
                    gen = GeneratorPointCloud(number_of_points)
                    points = gen.generate_on_vertical_surface(width, height)
                    filename = input("Enter the name of the file you want to save points to: ")
                    gen.save_to_xyz_file(points, filename + '.xyz')
                elif choice == '3':
                    radius = float(input("Enter the radius of the cylindrical surface: "))
                    height = float(input("Enter the height of the surface: "))
                    number_of_points = int(input("Enter the number of points to generate: "))
                    gen = GeneratorPointCloud(number_of_points)
                    points = gen.generate_on_cylindrical_surface(radius, height)
                    filename = input("Enter the name of the file you want to save points to: ")
                    gen.save_to_xyz_file(points, filename + '.xyz')
                elif choice == '4':
                    print("Returning to exercise selection.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif lab == '2':
            while True:
                print("1. Load point cloud from file and analyse RANSAC.")
                print("2. Load point cloud from file and analyse DBSCAN.")
                print("3. Return to exercise selection")

                choice = input("Enter the number of the operation you want to perform: ")
                if choice == '1':
                    file_name = input("Enter file name: ")
                    pc = PointCloud(file_name)
                    pc.cluster_points(3)
                    pc.fit_planes(1000, 0.1)
                    pc.analyse_planes(0.1)
                elif choice == '2':
                    file_name = input("Enter file name: ")
                    analyzer = PlaneDBSCAN(file_name)
                    analyzer.analyze_cloud()
                elif choice == '3':
                    print("Returning to exercise selection.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            break
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    start_screen()


