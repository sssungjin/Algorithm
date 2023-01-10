#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int i = 0, back;
    
    while(people.size() > i) {
        int back = people.back();
        people.pop_back();
        if(people[i] + back <= limit) {
            answer++; i++;
        }
        else answer++;
    }
    return answer;
}