#include<stdio.h>
#include<stdlib.h>
#include<omp.h>
void serial_quicksort(int *number,int first,int last){
   int i, j, pivot, temp;

   if(first<last){
      pivot=first;
      i=first;
      j=last;

      while(i<j){
         while(number[i]<=number[pivot]&&i<last)
            i++;
         while(number[j]>number[pivot])
            j--;
         if(i<j){
            temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
      }

      temp=number[pivot];
      number[pivot]=number[j];
      number[j]=temp;
      serial_quicksort(number,first,j-1);
      serial_quicksort(number,j+1,last);

   }
}





int parallel_partition(int * a, int p, int r)
{
    int lt[r-p];
    int gt[r-p];
    int i;
    int j;
    int key = a[r];
    int lt_n = 0;
    int gt_n = 0;

#pragma omp parallel for
    for(i = p; i < r; i++){
        if(a[i] < a[r]){
            lt[lt_n++] = a[i];
        }else{
            gt[gt_n++] = a[i];
        }   
    }   

    for(i = 0; i < lt_n; i++){
        a[p + i] = lt[i];
    }   

    a[p + lt_n] = key;

    for(j = 0; j < gt_n; j++){
        a[p + lt_n + j + 1] = gt[j];
    }   

    return p + lt_n;
}

void parallel_quicksort(int * a, int p, int r)
{
    int div;

    if(p < r){ 
        div = parallel_partition(a, p, r); 

           
#pragma omp task
            parallel_quicksort(a, p, div - 1); 
#pragma omp task
            parallel_quicksort(a, div + 1, r); 

        
    }
}

int main(){
   int i,n,c;
   FILE *fp=fopen("output.txt","w+");

   n=500000;
   double t ,st,pt;
   int number1[n];
   int number2[n];

   for(n=0;n<300000;n=n+5000)
   {
      for (c = 1; c <=n; c++) {
       number1[c]= rand() % 100 + 1;
      }
      for (c = 1; c <= n; c++) {
       number2[c]= number1[c];
      }

      


      t=omp_get_wtime();
      serial_quicksort(number1,0,n-1);
      st=omp_get_wtime()-t;

      t=omp_get_wtime();
      #pragma omp parallel 
      {  
      #pragma omp single
         parallel_quicksort(number2,0,n-1);
      }
      pt=omp_get_wtime()-t;

      printf("Serial Time: %lf \n ",st);
      printf("Parallel Time: %lf \n ",pt);
      fprintf(fp,"%lf %lf %lf\n",st,pt,st/pt);

   }
   fclose(fp);

   return 0;
}
