# Runnables

This directory contains runnable components and examples for the LangChain project.

## Overview

Runnables are executable components that can be used to build and run LangChain applications. This directory contains various examples and implementations of runnable components.

## Types of Runnables

1. **Simple Runnables**
   - Basic runnable components that process input and return output
   - Example: `SimpleRunnable` in runnable_example.py

2. **Chain Runnables**
   - Combine multiple runnables in sequence
   - Process data through a series of steps
   - Example: `ChainRunnable` in chain_runnable.py

3. **Parallel Runnables**
   - Execute multiple runnables in parallel
   - Combine results from multiple operations
   - Example: `ParallelRunnable` in parallel_runnable.py

4. **Conditional Runnables**
   - Execute different runnables based on conditions
   - Implement branching logic in your chains
   - Example: `ConditionalRunnable` in conditional_runnable.py

5. **Map Runnables**
   - Apply the same runnable to multiple inputs
   - Process lists or batches of data
   - Example: `MapRunnable` in map_runnable.py

## Structure

- `runnable_example.py`: Basic runnable implementation
- `chain_runnable.py`: Example of chaining multiple runnables
- `parallel_runnable.py`: Example of parallel execution
- `conditional_runnable.py`: Example of conditional execution
- `map_runnable.py`: Example of mapping over inputs
- Additional files will be added as needed

## Usage

To use the runnable components:

1. Import the required components from this directory
2. Follow the examples in the Python files
3. Customize the components according to your needs

## Requirements

- Python 3.8+
- LangChain
- Other dependencies as specified in the project's requirements 