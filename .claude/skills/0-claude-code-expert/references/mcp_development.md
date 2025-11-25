# MCP 서버 개발 가이드

## MCP (Model Context Protocol) 개요

MCP는 Claude Code와 외부 서비스를 연동하기 위한 프로토콜입니다. MCP 서버를 통해 Claude가 다양한 도구와 리소스에 접근할 수 있습니다.

## MCP 서버 구조

### 기본 구성 요소

```python
from mcp import MCPServer, Tool

server = MCPServer("server-name")

@server.tool()
async def my_tool(param: str) -> str:
    """도구 설명"""
    # 구현
    return result
```

### 필수 구성 요소

1. **Tools (도구)**: Claude가 호출할 수 있는 함수
2. **Resources (리소스)**: Claude가 읽을 수 있는 데이터
3. **Prompts (프롬프트)**: 재사용 가능한 프롬프트 템플릿

## MCP 서버 개발 단계

### 1단계: 요구사항 정의

**질문 체크리스트:**
- 어떤 외부 서비스와 연동할 것인가?
- 어떤 데이터를 제공해야 하는가?
- 어떤 작업을 수행해야 하는가?
- 인증이 필요한가?

### 2단계: 도구(Tool) 설계

**도구 설계 원칙:**
- 하나의 도구는 하나의 작업만 수행
- 파라미터는 명확하고 검증 가능해야 함
- 에러 처리는 명확하게
- 설명(description)은 구체적으로

**예시: Jira 검색 도구**

```python
@server.tool()
async def jira_search_by_key(jira_key: str) -> dict:
    """
    Jira 이슈를 키로 검색하고 상세 정보를 반환합니다.

    Parameters:
        jira_key: Jira 이슈 키 (예: PROJ-123)

    Returns:
        이슈 상세 정보 (제목, 상태, 담당자, 설명 등)
    """
    # 구현
    pass
```

### 3단계: 리소스(Resource) 설계

**리소스 사용 시나리오:**
- 자주 참조하는 문서
- 설정 정보
- 스키마 정의
- API 응답 캐시

**예시: Wiki 페이지 리소스**

```python
@server.resource("wiki://page/{page_id}")
async def get_wiki_page(page_id: str) -> str:
    """Wiki 페이지 내용 조회"""
    # 구현
    pass
```

### 4단계: 인증 구현

**인증 방식:**
- API 키 (환경 변수)
- OAuth 토큰
- 세션 쿠키

**예시: API 키 인증**

```python
import os

API_KEY = os.getenv("SERVICE_API_KEY")

async def call_api(endpoint: str):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    # API 호출
```

### 5단계: 에러 처리

**에러 처리 원칙:**
- 사용자에게 이해 가능한 에러 메시지
- 재시도 가능한 에러는 구분
- 로그 남기기

**예시:**

```python
from mcp.exceptions import MCPError

@server.tool()
async def search_item(query: str) -> dict:
    try:
        result = await api_call(query)
        return result
    except APIError as e:
        raise MCPError(f"API 호출 실패: {e.message}")
    except NetworkError as e:
        raise MCPError(f"네트워크 오류: 재시도 필요")
```

## MCP 서버 설정 (.claude/mcp_settings.json)

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

## 실전 예시: Cafe24 Meeting MCP 서버

### 구조

```
cafe24-meeting/
├── __init__.py
├── server.py          # MCP 서버 메인
├── api/
│   ├── meeting.py     # 미팅 API 클라이언트
│   ├── employee.py    # 직원 API 클라이언트
│   └── room.py        # 회의실 API 클라이언트
├── models/
│   └── types.py       # 데이터 타입 정의
└── utils/
    └── auth.py        # 인증 헬퍼
```

### 주요 도구

1. **미팅 조회**: `meeting_list(startDate, endDate)`
2. **미팅 생성**: `meeting_create(subject, startDate, endDate, participants)`
3. **회의실 검색**: `room_availability(floor, startDate, endDate)`
4. **직원 검색**: `employee_search(name)`

### 설계 포인트

- **날짜 형식 통일**: `YYYY-MM-DD HH:mm` 형식 사용
- **에러 응답 표준화**: 모든 에러는 `{error: string, code: string}` 형식
- **파라미터 검증**: Pydantic 모델 사용
- **캐싱**: 자주 조회되는 데이터(직원 정보 등)는 캐싱

## 테스트

### 단위 테스트

```python
import pytest
from my_mcp_server import server

@pytest.mark.asyncio
async def test_search_tool():
    result = await server.call_tool("search_item", {"query": "test"})
    assert result is not None
```

### 통합 테스트

```bash
# MCP 서버 실행
python -m my_mcp_server

# Claude Code에서 테스트
# .claude/mcp_settings.json에 서버 등록 후
# Claude Code 재시작
```

## 디버깅

### 로그 확인

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@server.tool()
async def my_tool(param: str):
    logger.debug(f"Tool called with param: {param}")
    # 구현
```

### 일반적인 문제

1. **도구가 호출되지 않음**
   - description이 명확한가?
   - 파라미터 타입이 정확한가?
   - MCP 서버가 제대로 시작되었는가?

2. **인증 실패**
   - 환경 변수가 설정되었는가?
   - API 키가 유효한가?

3. **타임아웃**
   - API 호출이 너무 오래 걸리는가?
   - 비동기 처리가 제대로 되어 있는가?

## 베스트 프랙티스

1. **도구는 단순하게**: 복잡한 로직은 분리
2. **설명은 구체적으로**: Claude가 언제 사용할지 알 수 있도록
3. **에러는 명확하게**: 사용자가 이해할 수 있는 메시지
4. **캐싱 활용**: 반복 호출되는 데이터는 캐싱
5. **타입 힌트 사용**: Python type hints로 파라미터 명확화
6. **문서화**: README와 주석으로 사용법 설명

## 참고 자료

- MCP 공식 문서: https://modelcontextprotocol.io
- Claude Code MCP 가이드: `.claude/README.md`
- 예시 서버: `.claude/skills/0-claude-code-expert/assets/mcp-server-template/`
