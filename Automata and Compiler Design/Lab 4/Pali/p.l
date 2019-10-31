alpha [a-zA-Z]
digit [0-9]

%{ 
    /* Definition section */
    #include <stdio.h> 
    #include <stdlib.h> 
    #include "y.tab.h" 
%} 
  
/* %option noyywrap */
  
/* Rule Section */
%% 
  
({alpha}|{digit})+  {yylval.f = yytext; return STR;} 
[-+()*/]    {return yytext[0];} 
[ \t\n]      {;} 
  
%% 
  
 int yywrap() 
 {  
  return -1;  
 }   
