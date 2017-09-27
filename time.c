/*�����2017��9��20�տ�ʼ�ļ�ʱ */

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>


/*- ��ʼ����ʱ����2017-09-20 00:00:00 */


static unsigned int calcSec(struct tm *pTm);

int main(void)
{
	time_t		timeNow = 0;
	struct tm	*pTime = NULL;
	char		timeStr[32] = {'\0'};
	unsigned int timeLog = 0U;

	printf("\n\t************ NOW TIME IS ************\n\n");
	time(&timeNow);
	pTime = localtime(&timeNow);
	sprintf(&timeStr[0],"%04d-%02d-%02d %02d:%02d:%02d",pTime->tm_year + 1900, pTime->tm_mon+1, pTime->tm_mday, pTime->tm_hour, pTime->tm_min, pTime->tm_sec);
	printf("\t %s  ( <-- 2017-09-26 00:00:00 )\n\n",timeStr);
	printf("-----------------------------------------------------\n\n");


	timeLog = calcSec(pTime);
	printf("\tTotal seconds: %d\n\n",timeLog);
	printf("-----------------------------------------------------\n\n\n\n");

	while(1)
	{
		timeLog = timeLog + 1;
		printf("Total seconds:  %d \n",timeLog);
		Sleep(1000);
	}


	return 0;
}

static unsigned int calcSec(struct tm *pTm)
{
	unsigned int ret = 0U;
	unsigned short yearVal = 0U;
	unsigned short dayTemp = 0U;
	unsigned char monVal = 0U;
	unsigned char dayVal = 0U;
	unsigned char hourVal = 0U;
	unsigned char minVal = 0U;
	unsigned char secVal = 0U;
	unsigned char mon_day[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
	/*- �����������ֱ�Ϊ��9�µ�9��ĩ��9�µ�10��ĩ��9�µ�11��ĩ������ */
	unsigned char day_temp[3] = {5,31+11,30+31+11};
	unsigned char index = 0U;

	if(pTm != NULL)
	{
		/*- ��ȡ��ǰ���ڡ�ʱ��ֵ */
		yearVal = pTm->tm_year + 1900;
		monVal = pTm->tm_mon+1;
		dayVal =  pTm->tm_mday;
		hourVal = pTm->tm_hour;
		minVal = pTm->tm_min;
		secVal = pTm->tm_sec;

		if(yearVal == 2017)
		{
			if(monVal == 9)
			{
				/*- ��ǰ��2017-09-26 */
				if(dayVal == 26)
				{
					dayTemp = 0U;
				}
				/*- ��9�£�������26�� */
				else
				{
					dayTemp = dayVal - 26;
				}
			}
			else
			{
				/*- ����9�� */
				dayTemp = day_temp[monVal-9-1] + dayVal;
			}
		}
		else
		{
			/*- ����2017��(��ʱ��2018����) */
			if(monVal == 1)
			{
				/*- ��2018��1�� */
				dayTemp = day_temp[2]+31+dayVal;
			}
			else
			{
				/*- ��ȡ2017��������ͱ��µ�����֮�� */
				dayTemp = day_temp[2]+31+dayVal;
				for(index=0U; index<(monVal-1);index++)
				{
					/*- ��ȡ���걾��֮ǰ���������� */
					dayTemp = mon_day[index];
				}	
			}
		}
		printf("\tTotal days : %d\n",dayTemp);
		ret = hourVal*60*60+minVal*60+secVal+dayTemp*24*60*60;
	}
	else
	{
		printf("Error.\n");
	}

	return ret;
}
