#include<omp.h>
#include<stdio.h>
#include<stdlib.h>


void main()
{	int x=100;
	int threads=0;
	scanf("%d",&threads);
	omp_set_num_threads(threads);
	#pragma omp parallel shared(x)
	{
		// for(int i=0;i<2;i++)
			printf("%s\n","adsadasd");
		
		x+=1;

	}

	printf("%d",x);
}