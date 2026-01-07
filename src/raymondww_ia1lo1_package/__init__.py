"""A simple example package."""
__version__ = "0.1.0"

# Import the function from hello_world module
from .hello_world import hello_world

# Make it available when someone imports the package
__all__ = ["hello_world"]