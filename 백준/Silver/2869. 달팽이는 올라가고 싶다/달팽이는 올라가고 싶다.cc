#include <iostream>
using namespace std;

int main()
{
    int A, B, V;
    cin >> A >> B >> V;
    int day = 1;

    day += (V-A)/(A-B);
    if((V-A)%(A-B) != 0)
        day++;
    if(A >= V)
        cout << "1";
    else
        cout << day;
    // int position = 0;
    // int day = 0;
    // while(true)
    // {
    //     day++;
    //     position += A;
    //     if(position >= V)
    //         break;
    //     position -= B;
    // }

}