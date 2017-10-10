/*计算从2017年9月20日开始的计时 */

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>


/*- 起始计算时间是2017-10-10 00:00:00 */


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
	printf("\t %s  ( <-- 2017-10-10 00:00:00 )\n\n",timeStr);
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
	/*- 下面这个数组分别为：10月到10月末、10月到11月末的天数、10月到12月末的天数 */
	unsigned char day_temp[3] = {22,30+22,30+31+22};
	unsigned char index = 0U;

	if(pTm != NULL)
	{
		/*- 获取当前日期、时间值 */
		yearVal = pTm->tm_year + 1900;
		monVal = pTm->tm_mon+1;
		dayVal =  pTm->tm_mday;
		hourVal = pTm->tm_hour;
		minVal = pTm->tm_min;
		secVal = pTm->tm_sec;

		if(yearVal == 2017)
		{
			if(monVal == 10)
			{
				/*- 当前是2017-10-10 */
				if(dayVal == 10)
				{
					dayTemp = 1U;
				}
				/*- 是10月，但不是10号 */
				else
				{
					dayTemp = dayVal - 10+1;
				}
			}
			else
			{
				/*- 不是10月 */
				dayTemp = day_temp[monVal-10-1] + dayVal;
			}
		}
		else
		{
			/*- 不是2017年(暂时按2018年算) */
			if(monVal == 1)
			{
				/*- 是2018年1月 */
				dayTemp = day_temp[2]+dayVal;
			}
			else
			{
				/*- 获取2017年的天数和本月的天数之和 */
				dayTemp = day_temp[2]+dayVal;
				for(index=0U; index<(monVal-1);index++)
				{
					/*- 获取本年本月之前的整月天数 */
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
