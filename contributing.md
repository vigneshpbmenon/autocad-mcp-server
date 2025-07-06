# Contributing to AutoCAD MCP Server

Thank you for your interest in contributing to the AutoCAD MCP Server! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue templates** when available
3. **Provide detailed information**:
   - AutoCAD version
   - Python version
   - Operating system
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages or logs

### Suggesting Features

1. **Check the roadmap** in README.md to see if it's already planned
2. **Open a feature request** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach
   - Any relevant examples or references

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch** from `main`
3. **Make your changes** following the coding standards
4. **Test your changes** thoroughly
5. **Submit a pull request**

## 🔧 Development Setup

### Prerequisites

- Windows (required for AutoCAD COM interface)
- Python 3.8+
- AutoCAD (for testing)
- uv (recommended) or pip

### Environment Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/autocad-mcp-server.git
cd autocad-mcp-server

# Install dependencies
uv sync

# Install development dependencies
uv add --dev pytest black flake8 mypy
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=server

# Run specific test file
uv run pytest tests/test_drawing.py
```

### Code Quality

```bash
# Format code
uv run black .

# Lint code
uv run flake8 .

# Type checking
uv run mypy .
```

## 📝 Coding Standards

### Python Style

- Follow **PEP 8** guidelines
- Use **Black** for code formatting
- Line length: 88 characters
- Use type hints for all functions
- Write docstrings for all public functions

### Code Structure

```python
@mcp.tool(
    name="tool_name",
    description="Clear description of what the tool does and its parameters."
)
def tool_function(param1: type, param2: type) -> str:
    """
    Brief description of the function.
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
        
    Returns:
        Description of what the function returns
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    try:
        # Implementation
        acad = Autocad(create_if_not_exists=True)
        # ... AutoCAD operations
        return "Success message describing what was done"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Error Handling

- Always handle potential AutoCAD connection errors
- Provide meaningful error messages
- Return descriptive strings for both success and failure cases
- Use try-except blocks for external library calls

### Documentation

- Update README.md for new tools
- Add docstrings to all functions
- Include parameter descriptions and types
- Provide usage examples

## 🧪 Testing Guidelines

### Test Structure

```python
import pytest
from unittest.mock import Mock, patch
from server import draw_line, draw_circle

class TestDrawingTools:
    @patch('server.Autocad')
    def test_draw_line_success(self, mock_autocad):
        # Setup
        mock_acad_instance = Mock()
        mock_autocad.return_value = mock_acad_instance
        
        # Execute
        result = draw_line(0, 0, 10, 10)
        
        # Assert
        assert "Drew line from (0, 0) to (10, 10)" in result
        mock_acad_instance.model.AddLine.assert_called_once()
```

### Test Coverage

- Test successful operations
- Test error conditions
- Test edge cases (negative coordinates, zero radius, etc.)
- Mock AutoCAD interactions
- Test parameter validation

## 📚 Adding New Tools

### Step-by-Step Guide

1. **Plan the tool**:
   - Define the tool's purpose
   - Identify required parameters
   - Consider edge cases

2. **Implement the function**:
   - Follow the coding standards
   - Handle errors appropriately
   - Return descriptive messages

3. **Add documentation**:
   - Update README.md tool table
   - Add usage examples
   - Include parameter descriptions

4. **Write tests**:
   - Test normal operation
   - Test error conditions
   - Mock AutoCAD interactions

5. **Update version**:
   - Consider if this is a patch, minor, or major change
   - Update version in pyproject.toml

### Example Tool Implementation

```python
@mcp.tool(
    name="draw_polygon",
    description="Draw a regular polygon with specified center, radius, and number of sides."
)
def draw_polygon(x: float, y: float, radius: float, sides: int) -> str:
    """
    Draw a regular polygon in AutoCAD.
    
    Args:
        x: X coordinate of center
        y: Y coordinate of center
        radius: Radius of circumscribed circle
        sides: Number of sides (minimum 3)
        
    Returns:
        Success or error message
    """
    if sides < 3:
        return "Error: Polygon must have at least 3 sides"
    
    try:
        acad = Autocad(create_if_not_exists=True)
        
        # Calculate polygon points
        points = []
        angle_step = 2 * math.pi / sides
        
        for i in range(sides):
            angle = i * angle_step
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append([px, py])
        
        # Close the polygon
        points.append(points[0])
        
        # Draw polyline
        pts = [APoint(px, py) for px, py in points]
        acad.model.AddPolyline(pts)
        
        return f"Drew {sides}-sided polygon at ({x}, {y}) with radius {radius}"
        
    except Exception as e:
        return f"Error drawing polygon: {str(e)}"
```

## 🏷️ Version Management

### Semantic Versioning

- **Major** (1.0.0): Breaking changes
- **Minor** (0.1.0): New features, backwards compatible
- **Patch** (0.0.1): Bug fixes, backwards compatible

### Release Process

1. Update version in `pyproject.toml`
2. Update `README.md` version history
3. Create a pull request
4. After merge, create a git tag
5. Create a GitHub release

## 🔄 Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] Changes are tested with AutoCAD
- [ ] Commit messages are clear

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested locally with AutoCAD
- [ ] Unit tests pass
- [ ] Integration tests pass

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 📞 Getting Help

- **GitHub Discussions**: For questions and general discussion
- **Issues**: For bug reports and feature requests
- **Discord/Slack**: [Community links if available]

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing to AutoCAD MCP Server!
