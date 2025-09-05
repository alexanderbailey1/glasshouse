from typing import List, Dict

async def get_answers(question: str) -> List[Dict]:
    return [
        {
            "model": "mock-primary",
            "text": f"Primary answer to '{question}'",
            "citations": ["https://example.com/primary"]
        },
        {
            "model": "mock-secondary",
            "text": f"Secondary answer to '{question}'",
            "citations": ["https://example.com/secondary"]
        }
    ]
