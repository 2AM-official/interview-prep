CC = g++
CFLAGS = -Wall -Wextra -pedantic -std=c++11

SRC = Matrix.cpp
OBJ = $(SRC:.cpp=.o)
TEST_SRC = MatrixTest.cpp
TEST_OBJ = $(TEST_SRC:.cpp=.o)
EXE = MatrixTest

.PHONY: all clean

all: $(EXE)

$(EXE): $(OBJ) $(TEST_OBJ)
	$(CC) $(CFLAGS) $^ -o $@

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $< -o $@

$(TEST_OBJ): $(TEST_SRC)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TEST_OBJ) $(EXE)
