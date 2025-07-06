# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Advanced drawing tools (splines, hatches, dimensions)
- Layer management capabilities
- Block insertion and manipulation
- Drawing modification tools (move, copy, rotate, scale)
- File operations (open, save, import, export)
- Improved error handling and validation
- Cross-platform support exploration

## [0.1.0] - 2025-01-XX

### Added
- Initial release of AutoCAD MCP Server
- Basic drawing tools:
  - `draw_line` - Draw lines between two points
  - `draw_polyline` - Draw polylines through multiple points
  - `draw_rectangle` - Draw rectangles with opposite corners
  - `draw_circle` - Draw circles with center and radius
  - `draw_ellipse` - Draw ellipses with center and axes
  - `draw_arc` - Draw arcs with center, radius, and angles
- FastMCP server framework integration
- AutoCAD COM interface via pyautocad
- Basic project structure and documentation
- MIT License
- Python 3.8+ support
- Windows platform support

### Technical Details
- Model Context Protocol (MCP) server implementation
- Real-time AutoCAD integration
- Type hints and proper error handling
- Comprehensive documentation and examples

### Known Limitations
- Windows only (AutoCAD COM interface requirement)
- Requires AutoCAD to be running
- Basic error handling (improvements planned)
- Limited to 2D drawing operations

---

## Legend

### Types of Changes
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** in case of vulnerabilities

### Release Notes Format
Each release includes:
- Version number and date
- Summary of changes
- Breaking changes (if any)
- Migration guide (if needed)
- Known issues
- Contributors acknowledgment
