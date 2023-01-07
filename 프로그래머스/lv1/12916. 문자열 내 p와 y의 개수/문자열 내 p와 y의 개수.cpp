#include <string>
#include <iostream>
#include <string>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int y_count = 0, p_count = 0;
    
    for(int i = 0; i < s.length(); i++) {
    if(s[i] == 'y' || s[i] == 'Y')
        y_count++;
    if(s[i] == 'p' || s[i] == 'P')
        p_count++;
    }
    
    if(y_count == p_count)
        answer = true;
    else answer = false;

    return answer;
}