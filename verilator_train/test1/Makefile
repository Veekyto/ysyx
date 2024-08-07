# npc/Makefile

# Variables
VERILATOR = verilator
CXX = g++
CXXFLAGS = -Wall -Wextra -g
OBJ_DIR = obj_dir
EXE = $(OBJ_DIR)/Vtop

# Source files
VERILOG_SRC = top.v
SYSTEMC_SRC = main.cpp

# Default target
all: sim

# Simulation target
sim: $(EXE)
	@echo "Running Verilog with SystemC simulation..."
	./$(EXE)
	@echo "Simulation completed."

$(EXE): $(OBJ_DIR)/Vtop.mk
	$(MAKE) -j -C $(OBJ_DIR) -f Vtop.mk Vtop

$(OBJ_DIR)/Vtop.mk: $(VERILOG_SRC) $(SYSTEMC_SRC)
	$(VERILATOR) --sc --exe $(VERILOG_SRC) $(SYSTEMC_SRC) --trace-fst
	cd $(OBJ_DIR) && make -f Vtop.mk Vtop

clean:
	rm -rf $(OBJ_DIR)

.PHONY: all sim clean

