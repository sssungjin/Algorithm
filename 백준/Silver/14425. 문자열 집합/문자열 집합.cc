#include <iostream>
#include <map>
using namespace std;

int N, M, ans = 0;
string s;
map<string, bool> m;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    for(int i = 0; i < N; i++)
    {
        cin >> s;
        m[s] = true;
    }
    for(int i = 0; i < M; i++)
    {
        cin >> s;
        if(m[s]) ans++;
    }
    cout << ans;
}