from mcp.server.fastmcp import FastMCP
import httpx

# 1. สร้างตัว MCP Server
mcp = FastMCP("Sales API Server")

# 2. ประกาศฟังก์ชันนี้เป็น Tool เพื่อให้ AI รู้จักและเรียกใช้ได้
@mcp.tool()
def get_sales_data() -> str:
    """ดึงข้อมูลยอดขายจาก REST API (http://localhost:8000/api/sales) เพื่อนำมาวิเคราะห์"""
    try:
        # ให้ MCP Server วิ่งไปดึงข้อมูลจาก API ที่เรารันไว้
        response = httpx.get("http://localhost:8000/api/sales")
        if response.status_code == 200:
            return str(response.json())
        return "Failed to fetch data from API"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # รัน Server ผ่านช่องทาง stdio (ให้ AI Client เป็นคนปลุกมันขึ้นมาเอง)
    mcp.run_stdio()