#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wc++11-extensions"
#include <iostream>
#include <vector>


using namespace std;

// transpose a MxN matrix
vector<vector<int> > transpose(vector<vector<int> >& matrix) {
    int M = matrix.size();
    int N = matrix[0].size();
    vector<vector<int> > transposed(N, vector<int>(M));

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            transposed[j][i] = matrix[i][j];
        }
    }

    return transposed;
}

// multiply two matrices A and B, where A is MxN and B is NxP
vector<vector<int> > multiply(vector<vector<int> >& A, vector<vector<int> >& B) {
    int M = A.size();
    int N = A[0].size();
    int P = B[0].size();

    vector<vector<int> > result(M, vector<int>(P, 0));

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < P; j++) {
            for (int k = 0; k < N; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

int main() {
    vector<vector<int> > A;
    vector<int> a1;
    a1.push_back(1);
    a1.push_back(2);
    a1.push_back(3);
    vector<int> a2;
    a2.push_back(4);
    a2.push_back(5);
    a2.push_back(6);
    A.push_back(a1);
    A.push_back(a2);

    vector<vector<int> > B;
    vector<int> b1;
    b1.push_back(7);
    b1.push_back(8);
    vector<int> b2;
    b2.push_back(9);
    b2.push_back(10);
    vector<int> b3;
    b3.push_back(11);
    b3.push_back(12);
    B.push_back(b1);
    B.push_back(b2);
    B.push_back(b3);

    cout << "A =" << endl;
    for (auto row : A) {
        for (auto element : row) { 
            cout << element << " ";
        }
        cout << endl;
    }

    cout << "B =" << endl;
    for (auto row : B) {
        for (auto element : row) {
            cout << element << " ";
        }
        cout << endl;
    }

    auto C = multiply(A, B);

    cout << "C = A * B =" << endl;
    for (auto row : C) {
        for (auto element : row) {
            cout << element << " ";
        }
        cout << endl;
    }

    auto D = transpose(C);

    cout << "D = transpose(C) =" << endl;
    for (auto row : D) {
        for (auto element : row) {
            cout << element << " ";
        }
        cout << endl;
    }

    return 0;
}
