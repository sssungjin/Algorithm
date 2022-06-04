#include <iostream>
using namespace std;

string BW[8] ={
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
};

string WB[8] = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
};

string board[50];
int BW_cnt(int x, int y)
{
    int ret = 0;
    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            if(board[i + x][j + y] != BW[i][j])
                ret++;
        }
    }
    return ret;
}

int WB_cnt(int x, int y)
{
    int ret = 0;
    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            if(board[i + x][j + y] != WB[i][j])
                ret++;
        }
    }
    return ret;
}


int main()
{
    int N, M;
    int min_val = 1226;
    cin >> N >> M;
    for(int i = 0; i < N; i++)
        cin >> board[i];

    for(int i = 0; i + 7 < N; i++)
    {
        for(int j = 0; j + 7 < M; j++)
        {   
            int tmp;
            tmp = min(BW_cnt(i, j), WB_cnt(i, j));
            if(tmp < min_val)
                min_val = tmp;        
        }
    }
    cout << min_val;
}