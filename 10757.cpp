#include <iostream>
#include <string.h>
using namespace std;

char res[10001];
char a[10001];
char b[10001];

void initChar(char *str)
{
    char temp[10001];
    for(int i = 0; i < strlen(str) / 2; i++)
    {
        char temp = str[i];
        str[i] = str[strlen(str) - i - 1];
        str[strlen(str) - i - 1] = temp;
    }
}

void add(char *a, char *b)
{
    initChar(a);
    initChar(b);

    for(int i = 0; (i < strlen(a))|(i<strlen(b)); i++)
    {
        int temp_a = a[i] - '0';
        int temp_b = b[i] - '0';
        int sum = temp_a + temp_b;

        if (sum > 9)
        {
            if(strlen(b) > strlen(a)){
                if(i == strlen(b) - 1){
                    res[i + 1] = '1';
            }
            else{
                b[i + 1]++;
            }
            }
            else
            {
                if (i == strlen(a) - 1){
                    res[i + 1] = '1';
                }
                else{
                    a[i + 1]++;
                }
            }
        }
        sum %= 10;
        res[i] = sum + '0';
    }
    initChar(res);
}

int main()
{
    cin >> a >> b;
   
   add(a, b);
   cout << res << endl;
    
    return 0;
}