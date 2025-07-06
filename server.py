from mcp.server.fastmcp import FastMCP
from pyautocad import Autocad, APoint
import math

# Create the FastMCP app
mcp = FastMCP(title="AutoCAD MCP Server")

# Define a tool that draws a line
@mcp.tool(
    name="draw_line",
    description="Draw a line in AutoCAD from (x1,y1) to (x2,y2)."
)
def draw_line(x1: float, y1: float, x2: float, y2: float) -> str:
    acad = Autocad(create_if_not_exists=True)
    p1 = APoint(x1, y1)
    p2 = APoint(x2, y2)
    acad.model.AddLine(p1, p2)
    return f"Drew line from ({x1}, {y1}) to ({x2}, {y2})"

# Draw a polyline through a sequence of points
@mcp.tool(
    name="draw_polyline",
    description="Draw a polyline through given points: a list of [x, y] pairs."
)
def draw_polyline(points: list[list[float]]) -> str:
    acad = Autocad(create_if_not_exists=True)
    pts = [APoint(x, y) for x, y in points]
    # Use AddPolyline (expects a sequence of points)
    acad.model.AddPolyline(pts)
    return f"Drew polyline through {len(points)} points."

# Draw a rectangle given two opposite corners
@mcp.tool(
    name="draw_rectangle",
    description="Draw a rectangle given two opposite corners (x1,y1) and (x2,y2)."
)
def draw_rectangle(x1: float, y1: float, x2: float, y2: float) -> str:
    acad = Autocad(create_if_not_exists=True)
    # Define corners
    p1 = APoint(x1, y1)
    p2 = APoint(x2, y1)
    p3 = APoint(x2, y2)
    p4 = APoint(x1, y2)
    # Draw four sides
    acad.model.AddLine(p1, p2)
    acad.model.AddLine(p2, p3)
    acad.model.AddLine(p3, p4)
    acad.model.AddLine(p4, p1)
    return f"Drew rectangle with corners ({x1},{y1}) and ({x2},{y2})."

# Draw a circle given center and radius
@mcp.tool(
    name="draw_circle",
    description="Draw a circle in AutoCAD with center (x, y) and radius r."
)
def draw_circle(x: float, y: float, radius: float) -> str:
    acad = Autocad(create_if_not_exists=True)
    center = APoint(x, y)
    acad.model.AddCircle(center, radius)
    return f"Drew circle at ({x}, {y}) with radius {radius}."

# Draw an ellipse given center, major axis length, and minor axis length
@mcp.tool(
    name="draw_ellipse",
    description="Draw an ellipse with center (x, y), major axis length, and minor axis length."
)
def draw_ellipse(x: float, y: float, major: float, minor: float) -> str:
    acad = Autocad(create_if_not_exists=True)
    center = APoint(x, y)
    # Major axis endpoint along the x-axis
    end_point = APoint(x + major, y)
    ratio = minor / major if major != 0 else 0
    acad.model.AddEllipse(center, end_point, ratio)
    return f"Drew ellipse at ({x}, {y}) with major {major} and minor {minor}."

# Draw an arc given center, radius, start angle, and end angle (degrees)
@mcp.tool(
    name="draw_arc",
    description="Draw an arc with center (x, y), radius r, from start_angle to end_angle (in degrees)."
)
def draw_arc(x: float, y: float, radius: float, start_angle: float, end_angle: float) -> str:
    acad = Autocad(create_if_not_exists=True)
    center = APoint(x, y)
    # Convert degrees to radians for AutoCAD
    start_rad = math.radians(start_angle)
    end_rad = math.radians(end_angle)
    acad.model.AddArc(center, radius, start_rad, end_rad)
    return f"Drew arc at ({x}, {y}) with radius {radius} from {start_angle}° to {end_angle}°." 

# 3. Run the server on STDIO
if __name__ == "__main__":
    mcp.run()