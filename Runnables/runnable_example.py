from typing import Dict, Any
from langchain.schema.runnable import RunnableConfig
from langchain.schema.runnable.base import Runnable

class SimpleRunnable(Runnable):
    """A simple example of a runnable component."""
    
    def __init__(self, name: str):
        """Initialize the runnable with a name."""
        self.name = name
    
    def invoke(self, input: Dict[str, Any], config: RunnableConfig = None) -> Dict[str, Any]:
        """Process the input and return a result."""
        return {
            "message": f"Hello from {self.name}!",
            "input_received": input
        }

def main():
    # Create an instance of the runnable
    runnable = SimpleRunnable("ExampleRunnable")
    
    # Example usage
    result = runnable.invoke({"test": "data"})
    print(result)

if __name__ == "__main__":
    main() 