from core.server.modify import app, run_server
import uvicorn
import asyncio
from core.utils.utils import config_data


async def main():
    await run_server()
    config = uvicorn.Config(
        app=app,
        host=config_data["app"]["host"],
        port=config_data["app"]["port"]
    )
    server = uvicorn.Server(config)
    await server.serve()
    


if __name__ == "__main__":
    asyncio.run(main())
