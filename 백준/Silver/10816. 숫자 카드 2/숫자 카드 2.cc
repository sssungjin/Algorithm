#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    vector<int> my;
    map<int, int> m;

    int N; cin >> N;
    for(int i = 0; i < N; i++)
    {
        int tmp; cin >> tmp;
        m[tmp]++;
    }
    
    int M; cin >> M;

    for(int i = 0; i < M; i++)
    {
        int tmp; cin >> tmp;
        if(m.count(tmp))
            cout << m[tmp] << ' ';
        else
            cout << "0 ";
    }
    

}
