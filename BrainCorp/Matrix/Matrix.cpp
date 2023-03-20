#include "Matrix.h"

// Constructor that initializes a matrix with given number of rows and columns
Matrix::Matrix(int r, int c) {
    rows = r;
    cols = c;
    data.resize(rows, std::vector<double>(cols, 0.0));  // initialize all elements to 0.0
}

// Method to set the value of an element in the matrix
void Matrix::set(int i, int j, double val) {
    data[i][j] = val;
}

// Method to get the value of an element in the matrix
double Matrix::get(int i, int j) const {
    return data[i][j];
}

// Method to get the number of rows in the matrix
int Matrix::getRows() const {
    return rows;
}

// Method to get the number of columns in the matrix
int Matrix::getCols() const {
    return cols;
}

// Method to compute the transpose of the matrix
Matrix Matrix::transpose() const {
    Matrix result(cols, rows);  // create a new matrix with swapped dimensions
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result.set(j, i, data[i][j]);  // set the swapped element
        }
    }
    return result;
}

// Method to compute the product of this matrix with another matrix using cache blocking
Matrix Matrix::multiply(const Matrix& other, int blockSize) const {
    if (cols != other.rows) {
        throw std::invalid_argument("Matrices have incompatible dimensions for multiplication");
    }
    Matrix result(rows, other.cols);  // create a new matrix with appropriate dimensions
    for (int ii = 0; ii < rows; ii += blockSize) {
        for (int jj = 0; jj < other.cols; jj += blockSize) {
            for (int kk = 0; kk < cols; kk += blockSize) {
                // Compute a block of the resulting matrix using blocks of the input matrices
                for (int i = ii; i < std::min(ii + blockSize, rows); i++) {
                    for (int j = jj; j < std::min(jj + blockSize, other.cols); j++) {
                        double sum = 0.0;
                        for (int k = kk; k < std::min(kk + blockSize, cols); k++) {
                            sum += data[i][k] * other.data[k][j];  // compute the dot product of the i-th row of this matrix and the j-th column of the other matrix
                        }
                        result.set(i, j, result.get(i, j) + sum);  // add the resulting element to the corresponding element in the result matrix
                    }
                }
            }
        }
    }
    return result;
}

// Helper function to print a matrix to the console
void printMatrix(const Matrix& mat) {
    for (int i = 0; i < mat.getRows(); i++) {
        for (int j = 0; j < mat.getCols(); j++) {
            std::cout << mat.get(i, j) << " ";
        }
        std::cout << std::endl;
    }
}


