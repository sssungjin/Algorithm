#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() 
{
    int N; cin >> N;
    int arr[100000];
    int cnt = 0;
    stack<int> st;
    vector<char> ans;

    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    for(int i = 1; i <= N; i++)
    {
       st.push(i);
       ans.push_back('+');

       while(!st.empty() && st.top() == arr[cnt]) {
        st.pop();
        ans.push_back('-');
        cnt++;
       }
    }
    if(!st.empty())
        cout << "NO\n";
    else {
        for(char ch : ans) 
            cout << ch << '\n';
    }
}