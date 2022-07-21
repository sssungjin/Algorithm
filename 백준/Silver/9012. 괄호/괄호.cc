#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool check_stack(string str)
{
    int len = (int)str.length();
    stack<char> stk;
    for(int i = 0; i < len; i++)
    {
        char c = str[i];
        if(c == '(') {
            stk.push(c);
        }
        else {
            if(!stk.empty())
                stk.pop();
            else
                return false;
        }
    }
    return stk.empty(); //비어있으면 true 있으면 false
}

int main() 
{
    int T; cin >> T;
    while(T--) {
        string str; cin >> str;
        if(check_stack(str) == true)
            cout << "YES\n";
        else
            cout << "NO\n";
        } 
}
