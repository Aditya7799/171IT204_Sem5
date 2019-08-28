#include <stdio.h> 
#include <omp.h>
  
long int serial_fib(long int n) 
{ 

    if(n==0 || n==1)
        return 1;
    return serial_fib(n-1)+serial_fib(n-2);
}

long int optimized_fib(long int n)
{
  long int i, j;
  if (n<2)
    return 1;
  if(n <= 30)
    return serial_fib(n);
  else
    {
       #pragma omp task shared(i) 
       i=optimized_fib(n-1);

       #pragma omp task shared(j)
       j=optimized_fib(n-2);

       #pragma omp taskwait
       return i+j;
    }
}

long int parallel_fib(long int n)
{
  long int i, j;
  if (n<2)
    return 1;
  if(n <= 30)
    return serial_fib(n);
  else
    {
       #pragma omp task shared(i) 
       i=parallel_fib(n-1);

       #pragma omp task shared(j)
       j=parallel_fib(n-2);

       #pragma omp taskwait
       return i+j;
    }
} 

  
int main() 
{   FILE *fp;
    fp=fopen("output.txt","w+");
    double t,st,pt;
    int i =0;
    long int n = 45;
    for(i=1;i<=n;i++)
    {    omp_set_dynamic(0);
        omp_set_num_threads(8); 
        t = omp_get_wtime();
        printf("%ld\n", serial_fib(i));
        st=omp_get_wtime()-t;
        printf("Serial Execution  took time:%lf \n",st);

        t = omp_get_wtime();
        #pragma omp parallel shared(n)
        {   
            #pragma omp single
            {printf("%ld\n", optimized_fib(i));}
        }
        pt=omp_get_wtime()-t;
        printf("Optimized Execution took time:%lf \n",pt);
        fprintf(fp,"%lf %lf %lf\n",st,pt,st/pt);
    }
	printf("For n=45 the spped up is %lf\n",st/pt);
    fclose(fp); 
    return 0; 
} 
