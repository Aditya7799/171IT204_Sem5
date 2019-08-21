#include<stdlib.h>
#include<stdio.h>
#include<omp.h>
#include<math.h>
#define N 1000000
int main()
{   double s;
    long int i =0;
    double A[N];


    s=omp_get_wtime();
    #pragma omp parallel for
    for(i =1 ;i<N;i++)
    {
        A[i]=pow(A[i-1],A[i-1])+A[i-1]*A[i-1];
    }
    #pragma omp parallel for 
    for(i =1 ;i<N;i++)
    {
        A[i]=A[i-1]*A[i-1]+A[i-1]*A[i-1];
    }

    printf("Without Nowait Execution Time: %lf \n",omp_get_wtime()-s);

    s=omp_get_wtime();
    #pragma omp parallel
    {
        #pragma omp for nowait
            for(i =1 ;i<N;i++)
            {
                A[i]=pow(A[i-1],A[i-1])+A[i-1]*A[i-1];
            }
            #pragma omp for 
            for(i =1 ;i<N;i++)
            {
                A[i]=A[i-1]*A[i-1]+A[i-1]*A[i-1];
            }
    
    }
    printf("With Nowait Execution Time: %lf \n",omp_get_wtime()-s);
    return 0;

}