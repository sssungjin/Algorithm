#include <iostream>
using namespace std;

bool is_prime(int num)
{
    if (num == 1)
    return 0;
   for(int i = 2; i * i <= num; i++)
   {
       if(num % i == 0)
        {
            return 0;
        }
   }
   return 1;
}

int main()
{
    int m, n;

    cin >> m;
    cin >> n;
    while (m <= n){
        if (is_prime(m))
            cout << m << "\n";
        m++;
  }
}