# MCP 서버 템플릿

이 템플릿을 사용하여 새로운 MCP 서버를 빠르게 시작할 수 있습니다.

## 사용 방법

### 1. 파일 복사

```bash
cp -r assets/mcp-server-template/ ~/my-mcp-server/
cd ~/my-mcp-server/
```

### 2. 서버 이름 변경

`server.py`에서 서버 이름 변경:

```python
app = Server("my-server-name")  # 원하는 이름으로 변경
```

### 3. 도구 구현

`execute_example_tool()` 함수를 수정하여 실제 로직 구현:

```python
async def execute_example_tool(query: str, limit: int) -> dict:
    # 실제 API 호출 또는 데이터 처리
    response = await api_client.search(query, limit=limit)
    return response
```

### 4. MCP 설정 추가

`.claude/mcp_settings.json`에 서버 등록:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["-m", "server"],
      "cwd": "/path/to/my-mcp-server",
      "env": {
        "MY_API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

### 5. 환경 변수 설정

```bash
export MY_API_KEY="your-api-key-here"
```

### 6. Claude Code 재시작

MCP 설정을 로드하기 위해 Claude Code를 재시작합니다.

## 커스터마이징

### 새 도구 추가

1. `list_tools()`에 도구 정의 추가:

```python
Tool(
    name="my_new_tool",
    description="새 도구 설명",
    inputSchema={
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "파라미터 설명"}
        },
        "required": ["param1"]
    }
)
```

2. `call_tool()`에 실행 로직 추가:

```python
elif name == "my_new_tool":
    param1 = arguments["param1"]
    result = await execute_my_new_tool(param1)
    return [TextContent(type="text", text=str(result))]
```

3. 헬퍼 함수 구현:

```python
async def execute_my_new_tool(param1: str) -> dict:
    # 로직 구현
    return {"result": "success"}
```

### 리소스 추가 (선택)

```python
@app.list_resources()
async def list_resources() -> list:
    return [
        {
            "uri": "my-resource://item/123",
            "name": "예시 리소스",
            "description": "리소스 설명"
        }
    ]

@app.read_resource()
async def read_resource(uri: str) -> str:
    # 리소스 내용 반환
    return "리소스 데이터"
```

## 테스트

### 로컬 테스트

```bash
python server.py
```

### Claude Code에서 테스트

Claude Code를 열고 MCP 도구가 제대로 로드되었는지 확인:

```
사용 가능한 도구를 보여줘
```

도구 실행 테스트:

```
example_tool을 사용해서 "테스트" 검색해줘
```

## 디버깅

### 로그 레벨 변경

```python
logging.basicConfig(level=logging.DEBUG)
```

### 에러 추적

```python
logger.error(f"Error details: {e}", exc_info=True)
```

## 참고

- MCP 공식 문서: https://modelcontextprotocol.io
- `.claude/skills/0-claude-code-expert/references/mcp_development.md`
