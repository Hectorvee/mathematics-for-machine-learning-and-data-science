import numpy as np
import utils

# Simple linear transformation T((v1, v2)) = (3v1, 0, -2v2)
def T(vector):
    """
    takes a vector v = (v1, v2) and transforms it
    :param vector: vector
    :return: column vector
    """

    result_vector = np.zeros((3, 1))
    result_vector[0,0] = 3*vector[0,0]
    result_vector[2,0] = -2*vector[1,0]

    return result_vector

v = np.array([[3], [5]])
w = T(v)

print(f"Original vector:\n {v}\n Result of the transformation:\n {w}")


# Transformations Defined as a Matrix Multiplication
def L(vector):
    """
        takes a vector v = (v1, v2) and transforms it using the matrix transformation_matrix
        :param vector: vector
        :return: column vector
        """
    transformation_matrix = np.array([[3,0], [0,0], [0,-2]])
    print(f"Transformation matrix:\n{transformation_matrix}\n")
    result_vector = transformation_matrix @ vector

    return result_vector

v = np.array([[3], [5]])
w = L(v)

print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)

#  Horizontal Scaling (Dilation)
def T_hScaling(vector):
    transformation_matrix = np.array([[2,0], [0,1]])  # Scaling horizontally by a factor 2
    result_vector = transformation_matrix @ vector

    return result_vector

def transform_vectors(transformation, vector1, vector2):
    full_vector = np.hstack((vector1, vector2))
    result_vector = transformation(full_vector)

    return result_vector

e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

transformation_result_hScaling = transform_vectors(T_hScaling, e1, e2)

print("Original vectors:\n e1= \n", e1, "\n e2=\n", e2,
      "\n\n Result of the transformation (matrix form):\n", transformation_result_hScaling)

utils.plot_transformation(T_hScaling,e1,e2)





















