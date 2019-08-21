#include<stdio.h>
#include<omp.h>
#define m 500
#define n 500
int mat1[m][n], mat2[n][m], outs[m][m], outp[m][m];
int i,j,k;

int main()
{
	double st,pt; 
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			mat1[i][j] = rand();
			mat2[i][j] = rand();
			outs[i][j] = 0;
			outp[i][j] = 0;
		}
	}

	st = omp_get_wtime();
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				outs[i][j] += mat1[i][k]*mat2[k][j];
			}
		}
	}
	st = omp_get_wtime() - st;

	pt = omp_get_wtime();
	#pragma omp parallel for
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				outp[i][j] += mat1[i][k]*mat2[k][j];
			}
		}
	}
	pt = omp_get_wtime() - pt;

	printf("time taken for serial compute: %lf \n", st);
	printf("time taken for parallel compute: %lf \n", pt);

	return 0;

}