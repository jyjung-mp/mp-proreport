#!/usr/bin/env python3
"""
MCP 서버 템플릿

이 템플릿을 사용하여 새로운 MCP 서버를 빠르게 시작할 수 있습니다.
"""

import os
import logging
from typing import Optional
from mcp.server import Server
from mcp.types import Tool, TextContent

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP 서버 인스턴스 생성
app = Server("my-mcp-server")

# 환경 변수에서 API 키 로드
API_KEY = os.getenv("MY_API_KEY")

# ============================================================================
# Tools (도구)
# ============================================================================

@app.list_tools()
async def list_tools() -> list[Tool]:
    """사용 가능한 도구 목록 반환"""
    return [
        Tool(
            name="example_tool",
            description="예시 도구입니다. 파라미터를 받아 결과를 반환합니다.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "검색 쿼리"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "결과 개수 제한 (기본값: 10)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="another_tool",
            description="또 다른 예시 도구입니다.",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "아이템 ID"
                    }
                },
                "required": ["id"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """도구 실행"""

    if name == "example_tool":
        query = arguments["query"]
        limit = arguments.get("limit", 10)

        logger.info(f"Executing example_tool: query={query}, limit={limit}")

        try:
            # 실제 API 호출 또는 로직 구현
            result = await execute_example_tool(query, limit)

            return [TextContent(
                type="text",
                text=f"검색 결과: {result}"
            )]

        except Exception as e:
            logger.error(f"Error in example_tool: {e}")
            return [TextContent(
                type="text",
                text=f"오류 발생: {str(e)}"
            )]

    elif name == "another_tool":
        item_id = arguments["id"]

        logger.info(f"Executing another_tool: id={item_id}")

        try:
            result = await execute_another_tool(item_id)

            return [TextContent(
                type="text",
                text=f"아이템 정보: {result}"
            )]

        except Exception as e:
            logger.error(f"Error in another_tool: {e}")
            return [TextContent(
                type="text",
                text=f"오류 발생: {str(e)}"
            )]

    else:
        raise ValueError(f"Unknown tool: {name}")


# ============================================================================
# Helper Functions
# ============================================================================

async def execute_example_tool(query: str, limit: int) -> dict:
    """
    예시 도구 실행 로직

    실제 구현 시 이 함수를 수정하여 API 호출, 데이터 처리 등을 수행
    """
    # TODO: 실제 로직 구현
    return {
        "query": query,
        "results": [
            {"id": 1, "title": "결과 1"},
            {"id": 2, "title": "결과 2"}
        ][:limit]
    }


async def execute_another_tool(item_id: str) -> dict:
    """
    또 다른 도구 실행 로직
    """
    # TODO: 실제 로직 구현
    return {
        "id": item_id,
        "name": "예시 아이템",
        "status": "active"
    }


# ============================================================================
# Resources (선택사항)
# ============================================================================

@app.list_resources()
async def list_resources() -> list:
    """사용 가능한 리소스 목록 (선택사항)"""
    return []


# ============================================================================
# Main
# ============================================================================

async def main():
    """MCP 서버 시작"""
    from mcp.server.stdio import stdio_server

    # API 키 확인
    if not API_KEY:
        logger.warning("API_KEY not set in environment variables")

    async with stdio_server() as (read_stream, write_stream):
        logger.info("MCP server starting...")
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
