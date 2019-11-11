#appname := hello
appsource := $(appname)*.cpp

CC := g++
CFLAGS := -Wall -g -DDEBUG
TARGET := $(appname)

INC := -I../include

srcfile := $(shell find . -maxdepth 1 -name $(appsource))
includesrcfiles := $(shell find ../include -maxdepth 1 -name "*.cpp")
OBJS  := $(patsubst %.cpp, %.o, $(srcfile) $(includesrcfiles))
$(info $(OBJS))


all: $(appname)

$(appname): $(OBJS)
	$(CC) -o $@ $^

clean:
	rm -f $(objects) $(appname)

run: $(appname)
	./$(appname)

%.o: %.c
	$(CC) $(CFLAGS) $(INC) -o $@ -c $<
