#include <iostream>
using namespace std;
int n;

void recur(int depth)
{
    for (int i = 0; i < depth; i++) cout << "____";
    cout << "\"����Լ��� ������?\"\n";

    if (depth == n) {
        for (int i = 0; i < depth; i++) cout << "____";
        cout << "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n";
        for (int i = 0; i < depth; i++) cout << "____";
        cout << "��� �亯�Ͽ���.\n";
        return;
    }

    for (int i = 0; i < depth; i++) cout << "____";
    cout << "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n";
    for (int i = 0; i < depth; i++) cout << "____";
    cout << "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n";
    for (int i = 0; i < depth; i++) cout << "____";
    cout << "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n";

    recur(depth + 1);

    for (int i = 0; i < depth; i++) cout << "____";
    cout << "��� �亯�Ͽ���.\n";
}

int main_17478()
{
    cin >> n;
    cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n";
	recur(0);

    return 0;
}