#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <vector>

class Matrix {
private:
    std::vector<std::vector<double> > data;  // 2D vector to store matrix elements
    int rows;  // number of rows in the matrix
    int cols;  // number of columns in the matrix

public:
    // Constructor that initializes a matrix with given number of rows and columns
    Matrix(int r, int c);

    // Method to set the value of an element in the matrix
    void set(int i, int j, double val);

    // Method to get the value of an element in the matrix
    double get(int i, int j) const;

    // Method to get the number of rows in the matrix
    int getRows() const;

    // Method to get the number of columns in the matrix
    int getCols() const;

    // Method to compute the transpose of the matrix
    Matrix transpose() const;

    // Method to compute the product of this matrix with another matrix using cache blocking
    Matrix multiply(const Matrix& other, int blockSize) const;
};

// Helper function to print a matrix to the console
void printMatrix(const Matrix& mat);

#endif  // MATRIX_H
