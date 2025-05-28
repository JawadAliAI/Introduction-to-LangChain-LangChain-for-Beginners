from typing import Dict, Any, List
from langchain.schema.runnable import RunnableConfig, RunnablePassthrough
from langchain.schema.runnable.base import Runnable
from langchain.schema.runnable.parallel import RunnableParallel
from langchain.schema.runnable.conditional import RunnableConditional
from langchain.schema.runnable.map import RunnableMap

class SimpleRunnable(Runnable):
    """Basic runnable that processes input and returns output."""
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        return {"processed": f"Processed {input.get('data', '')}"}

class ChainRunnable(Runnable):
    """Example of chaining multiple runnables."""
    def __init__(self):
        self.step1 = SimpleRunnable()
        self.step2 = SimpleRunnable()
    
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        result1 = self.step1.invoke(input)
        result2 = self.step2.invoke(result1)
        return result2

class ParallelRunnable(Runnable):
    """Example of parallel execution of runnables."""
    def __init__(self):
        self.parallel = RunnableParallel({
            "step1": SimpleRunnable(),
            "step2": SimpleRunnable()
        })
    
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        return self.parallel.invoke(input)

class ConditionalRunnable(Runnable):
    """Example of conditional execution based on input."""
    def __init__(self):
        self.conditional = RunnableConditional(
            condition=lambda x: x.get("type") == "A",
            if_true=SimpleRunnable(),
            if_false=SimpleRunnable()
        )
    
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        return self.conditional.invoke(input)

class MapRunnable(Runnable):
    """Example of mapping a runnable over a list of inputs."""
    def __init__(self):
        self.map_runnable = RunnableMap(SimpleRunnable())
    
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        return self.map_runnable.invoke(input)

def main():
    # Example usage of different runnable types
    print("\n1. Simple Runnable Example:")
    simple = SimpleRunnable()
    print(simple.invoke({"data": "test"}))

    print("\n2. Chain Runnable Example:")
    chain = ChainRunnable()
    print(chain.invoke({"data": "test"}))

    print("\n3. Parallel Runnable Example:")
    parallel = ParallelRunnable()
    print(parallel.invoke({"data": "test"}))

    print("\n4. Conditional Runnable Example:")
    conditional = ConditionalRunnable()
    print("Type A:", conditional.invoke({"type": "A", "data": "test"}))
    print("Type B:", conditional.invoke({"type": "B", "data": "test"}))

    print("\n5. Map Runnable Example:")
    map_runnable = MapRunnable()
    print(map_runnable.invoke({"data": ["test1", "test2", "test3"]}))

if __name__ == "__main__":
    main() 