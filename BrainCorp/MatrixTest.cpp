#include "Matrix.h"
#include <cassert>
#include <iostream>
using namespace std;

// Test the Matrix constructor and get/set methods
void testMatrixConstructionAndAccess() {
    // Create a 3x2 matrix
    Matrix mat(3, 2);

    // Set the values of the matrix elements
    mat.set(0, 0, 1.0);
    mat.set(0, 1, 2.0);
    mat.set(1, 0, 3.0);
    mat.set(1, 1, 4.0);
    mat.set(2, 0, 5.0);
    mat.set(2, 1, 6.0);

    // Test the get method
    assert(mat.get(0, 0) == 1.0);
    assert(mat.get(0, 1) == 2.0);
    assert(mat.get(1, 0) == 3.0);
    assert(mat.get(1, 1) == 4.0);
    assert(mat.get(2, 0) == 5.0);
    assert(mat.get(2, 1) == 6.0);

    // Test the dimensions of the matrix
    assert(mat.getRows() == 3);
    assert(mat.getCols() == 2);
}

// Test the Matrix transpose method
void testMatrixTranspose() {
    // Create a 3x2 matrix
    Matrix mat1(3, 2);

    // Set the values of the matrix elements
    mat1.set(0, 0, 1.0);
    mat1.set(0, 1, 2.0);
    mat1.set(1, 0, 3.0);
    mat1.set(1, 1, 4.0);
    mat1.set(2, 0, 5.0);
    mat1.set(2, 1, 6.0);

    // Compute the transpose of the matrix
    Matrix mat2 = mat1.transpose();

    // Test the dimensions of the transpose matrix
    assert(mat2.getRows() == 2);
    assert(mat2.getCols() == 3);

    // Test the values of the transpose matrix
    assert(mat2.get(0, 0) == 1.0);
    assert(mat2.get(0, 1) == 3.0);
    assert(mat2.get(0, 2) == 5.0);
    assert(mat2.get(1, 0) == 2.0);
    assert(mat2.get(1, 1) == 4.0);
    assert(mat2.get(1, 2) == 6.0);
}

void testMatrixMultiplication() {
    // Create a 3x2 matrix
    Matrix mat1(3, 2);
    mat1.set(0, 0, 1.0);
    mat1.set(0, 1, 2.0);
    mat1.set(1, 0, 3.0);
    mat1.set(1, 1, 4.0);
    mat1.set(2, 0, 5.0);
    mat1.set(2, 1, 6.0);

    // Create a 2x4 matrix
    Matrix mat2(2, 4);
    mat2.set(0, 0, 1.0);
    mat2.set(0, 1, 2.0);
    mat2.set(0, 2, 3.0);
    mat2.set(0, 3, 4.0);
    mat2.set(1, 0, 5.0);
    mat2.set(1, 1, 6.0);
    mat2.set(1, 2, 7.0);
    mat2.set(1, 3, 8.0);

    // Compute the product of the two matrices
    Matrix mat3 = mat1.multiply(mat2, 1);

    // Test the dimensions of the product matrix
    assert(mat3.getRows() == 3);
    assert(mat3.getCols() == 4);

    // Test the values of the product matrix
    assert(mat3.get(0, 0) == 11.0);
    assert(mat3.get(0, 1) == 14.0);
    assert(mat3.get(0, 2) == 17.0);
    assert(mat3.get(0, 3) == 20.0);
    assert(mat3.get(1, 0) == 23.0);
    assert(mat3.get(1, 1) == 30.0);
    assert(mat3.get(1, 2) == 37.0);
    assert(mat3.get(1, 3) == 44.0);
    assert(mat3.get(2, 0) == 35.0);
    assert(mat3.get(2, 1) == 46.0);
    assert(mat3.get(2, 2) == 57.0);
    assert(mat3.get(2, 3) == 68.0);
}

void testMatrixMultiplicationPerformance() {
    const int N = 1500;
    const int block_size = 64;

    // Create two random matrices of size N x N
    Matrix mat1(N, N);
    Matrix mat2(N, N);

    // Initialize the matrices with random values
    srand(time(nullptr));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            double val = static_cast<double>(rand()) / RAND_MAX;
            mat1.set(i, j, val);
            val = static_cast<double>(rand()) / RAND_MAX;
            mat2.set(i, j, val);
        }
    }

    // Multiply the matrices with cache blocking
    auto start_time = chrono::high_resolution_clock::now();
    Matrix result = mat1.multiply(mat2, block_size);
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end_time - start_time;
    cout << "Time with cache blocking: " << duration.count() << " seconds" << endl;

    // Multiply the matrices without cache blocking
    start_time = chrono::high_resolution_clock::now();
    result = mat1.multiply(mat2, N);
    end_time = chrono::high_resolution_clock::now();
    duration = end_time - start_time;
    cout << "Time without cache blocking: " << duration.count() << " seconds" << endl;
}

int main() {
    testMatrixConstructionAndAccess();
    cout << "Test Matrix Construction andn Access Success!" << endl;
    testMatrixTranspose();
    cout << "Test Matrix Transpose Success!" << endl;
    testMatrixMultiplication();
    cout << "Test Matrix Multiply Success!" << endl;
    testMatrixMultiplicationPerformance();
    return 0;
}