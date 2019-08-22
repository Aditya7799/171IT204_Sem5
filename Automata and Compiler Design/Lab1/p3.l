%{ #include<stdio.h>	
   #include<string.h>
char c;
%}

%%
[a-zA-Z] {
c=yytext[0];
if(c>=97)
{
    c=c-97;
    c=(c+5)%26;
    c+=97;
}
else
{
    c-=65;
    c=(c+5)%26;
    c+=65;
}

printf("%c",c);
}
%%


int main(int argc[],char **argv[])
{
 yyin=fopen("abc.txt","r");
 yylex(); 

 printf("\n");
 return 0;
}