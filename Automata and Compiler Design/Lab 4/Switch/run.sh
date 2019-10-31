# rm a.out lex.yy.c y.tab.c
flex s.l
yacc s.y
gcc y.tab.c -ll -ly
