# Chapter 2 — Implementation

In {ref}`chapter1.md#key-term-widget-architecture`, we defined widget architecture.

## A minimal example

```python
class Widget:
    def __init__(self, name: str):
        self.name = name

    def run(self) -> str:
        return f"Widget {self.name} running"
```
