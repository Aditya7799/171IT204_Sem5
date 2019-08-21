#include<omp.h>
#include<stdio.h>
#include<stdlib.h>





void parallel_pi(long steps,int threads)
{   
    double step=1.0/(double)steps;
    long double pi=0.0,sum=0.0;
    omp_set_num_threads(threads);
    double x;
    long double aux=0.0;
    long i=0;
    long double s= omp_get_wtime();
    
    #pragma omp parallel  private(i,x,aux) shared(sum)
    {   
        int thread_no=omp_get_thread_num();
        long int start=steps*(thread_no/(1.0*threads));
        long int end=steps*((thread_no+1)/(1.0*threads));
        
        
        printf("%s%ld%s%ld\n","Thread is running from step",start,"to step",end);
        // #pragma omp parallel for
        for(i=start;i<end;i++)
        {
            x=(0.5+i)*step;
            // #pragma omp critical
            aux+=+4.0/(1.0+x*x);
        }
        // printf("%Lf\n",sum);
        #pragma omp critical
        {   sum=sum+aux;
            }
        
    }
    pi+=step*sum;
    s= omp_get_wtime()-s;
    printf("%Lf   %LF\n",pi,s);

}

    




void main()
{
    printf("Parallel PI calculation\n");
    parallel_pi(100000,8);


}
