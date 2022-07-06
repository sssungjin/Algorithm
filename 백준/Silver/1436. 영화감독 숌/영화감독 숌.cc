#include <iostream>
using namespace std;

int end_num(int N)
{
    int ans = 666;
    int cnt = 0;
    int temp;

    while(cnt != N)
    {
        temp = ans;
        
        while(temp != 0) {
            if(temp % 1000 == 666) {
                cnt++;
                break;
            }
            else temp /= 10;
        }
        ans++;
    }
    return ans-1;
}

int main()
{
    int N; cin >> N;

    cout << end_num(N);
}