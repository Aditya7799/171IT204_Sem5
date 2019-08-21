#include<stdlib.h>
#include<stdio.h>
#include<omp.h>

#define N 90000

int findprimeS()
{   double s =omp_get_wtime();
    int count=0;
    for(int i =0;i<N;i++)
    {   int flag =1;
        for(int j =2;j<N/2;j++)
        {
            if(i%j==0)
                {flag=0;break;}
        }
        if(flag==1)
        count++;

    }
    printf("Time Serial %lf \n",s-omp_get_wtime());
    return count;
}

int findprimeP()
{   double s =omp_get_wtime();
    int count=0;
    #pragma omp parallel
    {
        #pragma omp for reduction(+:count)
        for(int i =0;i<N;i++)
        {   int flag =1;
            for(int j =2;j<N/2;j++)
            {
                if(i%j==0)
                    {flag=0;break;}
            }
            if(flag==1)
            count++;

        }
    }
    printf("Time Parallel %lf \n",s-omp_get_wtime());
    return count;
}

int findprimePS()
{   double s =omp_get_wtime();
    int count=0;
    #pragma omp parallel
    {
        #pragma omp for reduction(+:count) schedule(static,100)
        for(int i =0;i<N;i++)
        {   int flag =1;
            for(int j =2;j<N/2;j++)
            {
                if(i%j==0)
                    {flag=0;break;}
            }
            if(flag==1)
            count++;

        }
    }
    printf("Time Parallel Static Schedule %lf \n",s-omp_get_wtime());
    return count;
}

int findprimePD()
{   double s =omp_get_wtime();
    int count=0;
    #pragma omp parallel
    {
        #pragma omp for reduction(+:count) schedule(dynamic,100)
        for(int i =0;i<N;i++)
        {   int flag =1;
            for(int j =2;j<N/2;j++)
            {
                if(i%j==0)
                    {flag=0;break;}
            }
            if(flag==1)
            count++;

        }
    }
    printf("Time Parallel Dynamic Schedule %lf \n",s-omp_get_wtime());
    return count;
}

int main()
{
    findprimeS();
    findprimeP();
    findprimePS();
    findprimePD();


}

