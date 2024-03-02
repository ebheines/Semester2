## Author:: Øyvind Nohr <oyvind.a.nohr@uit.no>
EXEC=parser
CC= gcc

SRC= parser.c plot.c
HEADER= plot.h
CFLAGS= -Wall -Wextra -g
COPTS= -lm -DDEBUG


parser: parser.c
	$(CC) $(CFLAGS) $(COPTS) $(HEADERS) -o $(EXEC) $(SRC)

clean:
	rm -f *.o *.pdf *.dot
	rm -f *~
	rm -f *.exe $(EXEC)
	rm -rf *.dSYM	
