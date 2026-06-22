from mcp.server.fastmcp import FastMCP
import httpx

# สร้างตัว MCP Server
mcp = FastMCP("Sales API Server")

# ประกาศฟังก์ชันเป็น Tool เพื่อให้ AI รู้จัก
@mcp.tool()
def get_sales_data() -> str:
    """ดึงข้อมูลยอดขายจาก REST API (http://localhost:8000/api/sales) เพื่อนำมาวิเคราะห์"""
    try:
        response = httpx.get("http://localhost:8000/api/sales")
        if response.status_code == 200:
            return str(response.json())
        return "Failed to fetch data from API"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # 💡 แก้ไขบรรทัดนี้: เปลี่ยนจาก mcp.run_stdio() เป็น mcp.run()
    mcp.run()