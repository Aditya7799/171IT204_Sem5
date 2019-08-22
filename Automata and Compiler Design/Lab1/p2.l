%{ #include<stdio.h>
int sf=0,pf=0;
%}

/* defined section */

%%
"scanf"	{ sf++; fprintf(yyout,"readf");}           // replace scanf  with readf
"printf" { pf++; fprintf(yyout,"writef");}            // replace printf  with writef
. {fprintf(yyout,"%s",yytext); printf("%s",yytext);}
'\n' {fprintf(yyout,"\n");printf("\n");}


%%

int main()
{
	yyin=fopen("open.c","r");                            // input file open.c
	yyout=fopen("new.c","w");                           // output file new.c with replace 
	yylex();

     //no of printf and scanf in the file
	printf("Number of scanf=%d\nNumber of printf=%d\n",sf,pf);

return 0;

}