#include <iostream>
using namespace std;

int arr[8];

int num_len(int num)
{
    int len = 0;

    while(num > 0)
    {
        num /= 10;
        len++;
    }
    return len;
}

int res(int N)
{
    int ret = 0;
    int min = 999999;

   for(int i = 1; i < N; i++)
   {
       int temp = N - i;
       int sum = temp;
       ret = temp;
       int len = num_len(temp);
       for(int j = 0; j < len; j++)
       {
           arr[j] = temp % 10;
           temp /= 10;
           sum += arr[j];
       }

       if(sum == N)
       {
           if(ret < min)
                min = ret;
       }
   }
   if(min != 999999)
    return min;
    else
    return 0;
}

int main()
{
    int N;

    cin >> N;
    cout << res(N);

    return 0;
}