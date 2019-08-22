%{ #include<stdio.h>	
   #include<string.h>
int com=0;
%}

%%
"//"+.*+"\n" {com++;fprintf(yyout, " ");}
"/*"+.*+"*/" {com++;fprintf(yyout, " ");}


%%


int main(int argc[],char **argv[])
{
 yyin=fopen("open.c","r");
 yyout=fopen("output", "w");
 yylex(); 

 printf("No of Comments %d \n",com);
 return 0;
}