#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int tmp = n;
    int num = 0, num2 = 0;
    while(tmp > 0) {
        if(tmp % 2 == 1) {
            num++;
        }
        tmp /= 2;
    }
    while(1) {
        n++;
        tmp = n;
        while(tmp > 0) {
            if(tmp % 2 == 1) {
                num2++;
            }
            tmp /= 2;
        }
        if(num == num2) {
            answer = n;
            break;
        }
        else num2 = 0;
    }
    return answer;
}