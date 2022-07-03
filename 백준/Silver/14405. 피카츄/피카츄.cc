#include <iostream>
#include <regex>

using namespace std;

int main()
{
    regex r("(pi|ka|chu)+"); 

    string str;

    cin >> str;

   if(regex_match(str,r))
    cout << "YES";
    else
    cout << "NO";
}