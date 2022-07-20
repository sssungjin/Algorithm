#include <iostream>
#include <stack>
using namespace std;

int s = 0;
int a[10000];

void push(int x)
{
    a[s] = x;
    s++;
}

int pop()
{
    if(s == 0) 
        return -1;
    else {
        s--;
        return a[s];
    }
}

int size()
{
    return s;
}

int empty()
{
    if(s <= 0)
        return 1;
    else
        return 0;
}

int top()
{
    if(s== 0)
        return -1;
    else
        return a[s - 1];
}
int main()
{
    int N; cin >> N;

    for(int i = 0; i < N; i++) {
        string str;
        cin >> str;
        if(str == "push") {
            int x; cin >> x;
            push(x);
        }
        else if(str == "pop") {
            cout << pop() << '\n';
        }
        else if(str == "size") {
            cout << size() << '\n';
        }
        else if(str == "empty") {
            cout << empty() << '\n';
        }
        else if(str == "top") {
            cout << top() << '\n';
        }
    }
}