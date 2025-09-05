import asyncio
import hashlib
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=False)

async def compute_root():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT hash FROM event ORDER BY id DESC LIMIT 100"))
        hashes = [row[0] for row in res]
    if not hashes:
        return None
    concat = ''.join(sorted(hashes)).encode()
    return hashlib.sha256(concat).hexdigest()

async def main():
    while True:
        root = await compute_root()
        if root:
            print("Computed Merkle root", root)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
