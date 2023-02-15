#ifndef MATRIX_H
#define MATRIX_H

#include <vector>

class Matrix {
public:
    Matrix(int rows, int cols);
    int rows() const;
    int cols() const;
    double& operator()(int row, int col);
    double operator()(int row, int col) const;
    Matrix transpose() const;
    Matrix operator*(const Matrix& other) const;

private:
    int m_rows;
    int m_cols;
    std::vector<double> m_data;
};

#endif // MATRIX_H
