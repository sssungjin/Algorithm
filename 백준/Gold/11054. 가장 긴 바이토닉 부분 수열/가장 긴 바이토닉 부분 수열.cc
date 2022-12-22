#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    int arr[1001];
    int dp_r[1001];
    int dp_l[1001];

    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    for(int i = 1; i <= n; i++) {
        dp_l[i] = 1;
        for(int j = 0; j < i; j++) {
            if(arr[i] > arr[j] && dp_l[i] < dp_l[j] + 1)
                dp_l[i] = dp_l[j] + 1;
        }
    }    
    for(int i = n; i >= 1; i--) {
        dp_r[i] = 1;
        for(int j = n; j > i; j--) {
            if(arr[i] > arr[j] && dp_r[i] < dp_r[j] + 1)
                dp_r[i] = dp_r[j] + 1; 
        }
    }

    int res = 1;
    for(int i = 1; i <= n; i++) {
        res = max(res, dp_l[i] + dp_r[i] - 1);
    }
    cout << res;
}