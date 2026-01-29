# Chapter 2 — Implementation

In {ref}`widget-architecture`, we defined widget architecture.

## A minimal example

```python
class Widget:
    def __init__(self, name: str):
        self.name = name

    def run(self) -> str:
        return f"Widget {self.name} running"
```
