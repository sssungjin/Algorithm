#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{

    while(1) {
        stack<int> st;
        string s;
        bool flag = true;

        getline(cin, s);
        if(s == ".") break;

        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '[') st.push(1);
            if(s[i] == '(') st.push(2);
            if(s[i] == ']' || s[i] == ')') {
                if(st.empty())
                    flag = false; 
                else if(s[i] == ']') {
                    if(st.top() == 1) st.pop();
                    else flag = false;
                }
                else if (s[i] == ')') {
                    if(st.top() == 2) st.pop();
                    else flag = false;
                }
            }
        }
        if(flag && st.empty())
            cout << "yes\n";
        else cout << "no\n";
    }
    
}