#include <stdio.h>

int main()
{
	int x, y;
	scanf("%d %d", &x, &y);
	int day;
	switch (x)
	{
	case 1:
		day = y % 7;
		break;
	case 2:
		day = (31 * 1 + y) % 7;
		break;

	case 3:
		day = (31 * 1 + 28 * 1 + y) % 7;
		break;

	case 4:
		day = (31 * 2 + 28 * 1 + y) % 7;
		break;

	case 5:
		day = (31 * 2 + 28 * 1 + 30 * 1 + y) % 7;
		break;

	case 6:
		day = (31 * 3 + 28 * 1 + 30 * 1 + y) % 7;
		break;

	case 7:
		day = (31 * 3 + 28 * 1 + 30 * 2 + y) % 7;
		break;

	case 8:
		day = (31 * 4 + 28 * 1 + 30 * 2 + y) % 7;
		break;

	case 9:
		day = (31 * 5 + 28 * 1 + 30 * 2 + y) % 7;
		break;

	case 10:
		day = (31 * 5 + 28 * 1 + 30 * 3 + y) % 7;
		break;

	case 11:
		day = (31 * 6 + 28 * 1 + 30 * 3 + y) % 7;
		break;

	case 12:
		day = (31 * 6 + 28 * 1 + 30 * 4 + y) % 7;
		break;

	}

	switch (day)
	{
	case 0:
		printf("SUN\n");
		break;

	case 1:
		printf("MON\n");
		break;

	case 2:
		printf("TUE\n");
		break;

	case 3:
		printf("WED\n");
		break;

	case 4:
		printf("THU\n");
		break;

	case 5:
		printf("FRI\n");
		break;

	case 6:
		printf("SAT\n");
		break;

	}
	return 0;
}