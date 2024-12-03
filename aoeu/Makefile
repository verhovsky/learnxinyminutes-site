UNAME_S := $(shell uname -s)
CFLAGS=$(shell python3-config --includes) -Wall -g
LDFLAGS=$(shell python3-config --ldflags)
LIBS = -lcmark -lyaml -lpython3.13

ifeq ($(UNAME_S),Darwin)
    # macOS
    CFLAGS += -I/opt/homebrew/include
    LDFLAGS += -L/opt/homebrew/lib
else
    # Linux
    CFLAGS +=
    LDFLAGS +=
endif

CC = cc
TARGET = build
SRCS = build.c
OBJS = $(SRCS:.c=.o)
ASM_FILES = $(SRCS:.c=.s)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET) $(LDFLAGS) $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.s: %.c
	$(CC) $(CFLAGS) -S -fno-verbose-asm $< -o $@

debug: $(ASM_FILES)
	cat $(ASM_FILES)

clean:
	rm -f $(OBJS) $(TARGET) $(ASM_FILES)

.PHONY: all debug clean
