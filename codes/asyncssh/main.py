# pip install asyncssh

import asyncio, asyncssh, sys

async def run_client():
    async with asyncssh.connect('your-hostname') as conn:
        result = await conn.run('ls -l', check=True)
        print(result.stdout, end='')

try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))