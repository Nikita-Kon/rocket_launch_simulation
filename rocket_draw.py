from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
# Ball animation
# Задаем 8 вершин куба в массиве numpy
cube_vertices = np.array([
    [49, 49, 0],  # Нижняя левая задняя
    [51, 49, 0],  # Нижняя правая задняя
    [49, 51, 0],  # Верхняя левая задняя
    [51, 51, 0],  # Верхняя правая задняя
    [49, 49, 8],  # Нижняя левая передняя
    [51, 49, 8],  # Нижняя правая передняя
    [49, 51, 8],  # Верхняя левая передняя
    [51, 51, 8],  # Верхняя правая передняя
])

def create_cube(ax, cube_coords, max_z):
    if cube_coords.shape != (8, 3):
        raise ValueError("Массив должен содержать 8 вершин с 3 координатами (x, y, z) каждая.")

    ax.cla()  # Clear the axis for the next frame
    # Set fixed limits for the axes
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    ax.set_zlim([0, max_z])
    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    faces = [
        [cube_coords[0], cube_coords[1], cube_coords[3], cube_coords[2]],  # Back face
        [cube_coords[4], cube_coords[5], cube_coords[7], cube_coords[6]],  # Front face
        [cube_coords[0], cube_coords[1], cube_coords[5], cube_coords[4]],  # Bottom face
        [cube_coords[2], cube_coords[3], cube_coords[7], cube_coords[6]],  # Top face
        [cube_coords[0], cube_coords[2], cube_coords[6], cube_coords[4]],  # Left face
        [cube_coords[1], cube_coords[3], cube_coords[7], cube_coords[5]],  # Right face
    ]

    # Define colors for each face (you can modify these as needed)
    face_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan']

    # Create 3D polygons for each face and add them to the plot
    poly3d = Poly3DCollection(faces, facecolors=face_colors, linewidths=1, edgecolors='r', alpha=0.5)
    ax.add_collection3d(poly3d)

    # # Plot the cube vertices (optional, if you want to see the vertices)
    # ax.scatter3D(cube_coords[:, 0], cube_coords[:, 1], cube_coords[:, 2], color='b')

def setZCube(cube_vertices, value, objectHigh=8):
    cube_vertices[0][2] = value
    cube_vertices[1][2] = value
    cube_vertices[2][2] = value
    cube_vertices[3][2] = value

    cube_vertices[4][2] = value + objectHigh
    cube_vertices[5][2] = value + objectHigh
    cube_vertices[6][2] = value + objectHigh
    cube_vertices[7][2] = value + objectHigh