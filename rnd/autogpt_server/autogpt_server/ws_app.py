import os
import uvicorn

from autogpt_server.server.ws_api import app


def main():
    uvicorn.run(
        app,
        host=os.getenv("WS_SERVER_HOST", "0.0.0.0"),
        port=int(os.getenv("WS_SERVER_PORT", "8001"))
    )


if __name__ == "__main__":
    main()
