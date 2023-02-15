#include "Matrix.h"

Matrix::Matrix(int rows, int cols) : m_rows(rows), m_cols(cols), m_data(rows * cols) {}

int Matrix::rows() const {
    return m_rows;
}

int Matrix::cols() const {
    return m_cols;
}

double& Matrix::operator()(int row, int col) {
    return m_data[row * m_cols + col];
}

double Matrix::operator()(int row, int col) const {
    return m_data[row * m_cols + col];
}

Matrix Matrix::transpose() const {
    Matrix result(m_cols, m_rows);
    for (int i = 0; i < m_rows; ++i) {
        for (int j = 0; j < m_cols; ++j) {
            result(j, i) = (*this)(i, j);
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix& other) const {
    if (m_cols != other.m_rows) {
        throw std::invalid_argument("Matrix dimensions are incompatible for multiplication.");
    }

    Matrix result(m_rows, other.m_cols);
    for (int i = 0; i < m_rows; ++i) {
        for (int j = 0; j < other.m_cols; ++j) {
            double dot_product = 0.0;
            for (int k = 0; k < m_cols; ++k) {
                dot_product += (*this)(i, k) * other(k, j);
            }
            result(i, j) = dot_product;
        }
    }
    return result;
}
