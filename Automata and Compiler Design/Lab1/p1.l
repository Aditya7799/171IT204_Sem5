%{ #include<stdio.h>	
   #include<string.h>
int k=0;
char *c;
%}

%%
[a-zA-Z]+ {
if(yyleng>k)
{  k= yyleng;
	free(c);
	c=(char*)malloc(sizeof(char)*(k+1));
	strcpy(c,yytext);
}

}
%%
char *strrev(char *str)
{
    if (!str || ! *str)
        return str;

    int i = strlen(str) - 1, j = 0;

    char ch;
    while (i > j)
    {
        ch = str[i];
        str[i] = str[j];
        str[j] = ch;
        i--;
        j++;
    }
    return str;
}

int main(int argc[],char **argv[])
{
 yyin=fopen("abc.txt","r");
 yylex(); 
 printf("largest: %d\n",k);
 strrev(c);
 printf("Reversed:%s",c);
 printf("\n");
 return 0;
}
