#include<omp.h>
#include<stdio.h>
#include<stdlib.h>

void serial_pi(long steps)
{
	long i=0;
	double step=1.0/(double)steps;
	double x;
	long double pi,sum=0.0;
	long double start = omp_get_wtime();
	for(i=0;i<steps;i++)
	{
		x=(0.5+i)*step;
		sum=sum+4.0/(1.0+x*x);
	}
	pi=step*sum;
	start= omp_get_wtime()-start;
	printf("%Lf   %LF\n",pi,start);
}

//parallel calculation using reduction clause in OMP
void parallel_pi(long steps,int threads)
{	
	int i,j;
    double x;
    double pi, sum = 0.0;
    double  delta;
    double s = omp_get_wtime();
    double step = 1.0/(double) steps;
       omp_set_num_threads(threads);
       sum = 0.0;

        #pragma omp parallel for reduction(+:sum) private(x)
        for (i=0; i < steps; i++) {
            x = (i+0.5)*step;
            sum += 4.0 / (1.0+x*x); 
        }


        pi = step * sum;

        s= omp_get_wtime()-s;
	printf("%Lf   %LF\n",pi,s);


}



	




void main()
{	printf("Serial PI calculation\n");
	serial_pi(100000);
	


}