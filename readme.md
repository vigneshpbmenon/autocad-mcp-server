# AutoCAD MCP Server v0.1

A Model Context Protocol (MCP) server that enables AI agents to interact with AutoCAD through Python automation. This server provides basic drawing tools for creating geometric shapes and elements in AutoCAD.

## 🚀 Features

- **Basic Drawing Tools**: Lines, polylines, rectangles, circles, ellipses, and arcs
- **AI Agent Integration**: Compatible with MCP-enabled AI assistants
- **Real-time AutoCAD Control**: Direct integration with running AutoCAD instances
- **Simple Setup**: Easy configuration and deployment

## 📋 Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `draw_line` | Draw a line between two points | `x1, y1, x2, y2` |
| `draw_polyline` | Draw a polyline through multiple points | `points` (list of [x, y] pairs) |
| `draw_rectangle` | Draw a rectangle with opposite corners | `x1, y1, x2, y2` |
| `draw_circle` | Draw a circle with center and radius | `x, y, radius` |
| `draw_ellipse` | Draw an ellipse with center and axes | `x, y, major, minor` |
| `draw_arc` | Draw an arc with center, radius, and angles | `x, y, radius, start_angle, end_angle` |

## 🛠️ Prerequisites

- **AutoCAD**: Must be installed and running on Windows
- **Python**: 3.8 or higher
- **uv**: Python package manager (recommended)

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/vigneshpbmenon/autocad-mcp-server.git
cd autocad-mcp-server
```

2. Install dependencies:
```bash
uv sync
```

Or with pip:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Ensure AutoCAD is running on your system
2. Add the server configuration to your MCP client:

```json
{
  "mcpServers": {
    "autocad": {
      "command": "uv",
      "args": ["run", "python", "server.py"]
    }
  }
}
```

## 🚀 Usage

### Starting the Server

```bash
uv run python server.py
```

### Example AI Agent Commands

Once connected to an MCP-enabled AI assistant, you can use natural language commands:

- "Draw a line from (0,0) to (10,10)"
- "Create a rectangle with corners at (5,5) and (15,15)"
- "Draw a circle at the origin with radius 5"
- "Make an arc centered at (10,10) with radius 8 from 0° to 90°"

### Direct API Usage

```python
from mcp.client import Client

# Connect to the server
client = Client()

# Draw a line
result = client.call_tool("draw_line", {
    "x1": 0, "y1": 0, 
    "x2": 10, "y2": 10
})

# Draw a circle
result = client.call_tool("draw_circle", {
    "x": 5, "y": 5, 
    "radius": 3
})
```

## 🔧 Development

### Project Structure

```
autocad-mcp-server/
├── server.py              # Main MCP server implementation
├── server_config.json     # Server configuration
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License
```

### Adding New Tools

To add a new drawing tool:

1. Define the tool function with the `@mcp.tool` decorator
2. Use the `pyautocad` library to interact with AutoCAD
3. Return a descriptive string about the action performed

Example:
```python
@mcp.tool(
    name="draw_polygon",
    description="Draw a regular polygon with n sides."
)
def draw_polygon(x: float, y: float, radius: float, sides: int) -> str:
    # Implementation here
    return f"Drew {sides}-sided polygon at ({x}, {y})"
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Version History

- **v0.1** - Initial release with basic drawing tools
  - Lines, polylines, rectangles, circles, ellipses, and arcs
  - Basic MCP server implementation
  - AutoCAD integration via pyautocad

## 🔮 Roadmap

- Advanced drawing tools (splines, hatches, dimensions)
- Layer management
- Block insertion and manipulation
- 3D drawing capabilities
- Drawing modification tools (move, copy, rotate, scale)
- File operations (open, save, import, export)

## ⚠️ Known Limitations

- Windows only (due to AutoCAD COM interface requirements)
- Requires AutoCAD to be running
- Basic error handling (improvements planned for v0.2)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastMCP](https://github.com/jlowin/fastmcp) for the MCP server framework
- [pyautocad](https://github.com/reclosedev/pyautocad) for AutoCAD automation
- The Model Context Protocol community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/autocad-mcp-server/issues) page
2. Create a new issue with detailed information
3. Join the discussion in the MCP community

---

**Note**: This is version 0.1 - a foundational release. More advanced features and tools are in development and will be released in future versions.