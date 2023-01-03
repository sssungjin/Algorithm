#include <iostream>
using namespace std;

int main()
{
    int A[9][9];
    int max = -1;
    int x, y;
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            cin >> A[i][j];
            if(max < A[i][j]) {
            max = A[i][j];
            x = i;
            y = j;
            }
        }
    }
    cout << max << endl << x+1 << " " << y+1;
}