#include<omp.h>
#include<stdio.h>
#include<stdlib.h>
//Matrix One Dimentions
#define M 500
#define N 500
//Matrix Two Dimentions
#define P 500
#define Q 500
int main()
{ srand(time(NULL));
  int m, n, p, q, c, d, k, sum = 0;
  double s;
  int first[M][N], second[P][Q], multiply[M][Q];
 
 
  for (c = 0; c < M; c++)
    for (d = 0; d < N; d++)
      first[c][d]=rand();

  for (c = 0; c < P; c++)
    for (d = 0; d < Q; d++)
      second[c][d]=rand();

     //Calculation begins here
    s =omp_get_wtime();
    for (c = 0; c < M; c++) {
      for (d = 0; d < Q; d++) {
        for (k = 0; k < P; k++) {
          sum = sum + first[c][k]*second[k][d];
        }
 
        multiply[c][d] = sum;
        sum = 0;
      }
    }
    
    printf("The Serial Execution took \n%lf",omp_get_wtime()-s);
    // printf("Product of the matrices:\n");
 
    // for (c = 0; c < M; c++) {
    //   for (d = 0; d < Q; d++)
    //     printf("%d\t", multiply[c][d]);
 
    //   printf("\n");
    // }
  

  
 
  return 0;
}