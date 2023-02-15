#include <iostream>
#include <cassert>
#include "Matrix.h"

int main() {
    Matrix A(3, 2);
    A(0, 0) = 1; A(0, 1) = 2;
    A(1, 0) = 3; A(1, 1) = 4;
    A(2, 0) = 5; A(2, 1) = 6;

    Matrix B(2, 3);
    B(0, 0) = 7; B(0, 1) = 8; B(0, 2) = 9;
    B(1, 0) = 10; B(1, 1) = 11; B(1, 2) = 12;

    Matrix C = A * B;
    assert(C.rows() == 3);
    assert(C.cols() == 3);
    assert(C(0, 0) == 27);
    assert(C(0, 1) == 30);
    assert(C(0, 2) == 33);
    assert(C(1, 0) == 61);
    assert(C(1, 1) == 68);
    assert(C(1, 2) == 75);
    assert(C(2, 0) == 95);
    assert(C(2, 1) == 106);
    assert(C(2, 2) == 117);

    Matrix D = B.transpose();
    assert(D.rows() == 3);
    assert(D.cols() == 2);
    assert(D(0, 0) == 7);
    assert(D(0, 1) == 10);
    assert(D(1, 0) == 8);
    assert(D(1, 1) == 11);
    assert(D(2, 0) == 9);
    assert(D(2, 1) == 12);

    std::cout << "All tests passed!" << std::endl;

    return 0;
}
