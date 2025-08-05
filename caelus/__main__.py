"""
📡 Caelus CLI Entry Point

Allows running caelus as a module: python -m caelus
"""

from .cli import caelus

if __name__ == "__main__":
    caelus()