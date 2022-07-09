#include <iostream>
#include <regex>
#include <string>
using namespace std;

int main()
{
    int N; cin >> N;
    regex re("(^[A-F]?A+F+C+[A-F]?$)");
    while(N--)
    {
        string str; cin >> str;
        if (regex_match(str, re)) {
            cout << "Infected!" << '\n';
        }
        else
            cout << "Good" << '\n';
    }
}