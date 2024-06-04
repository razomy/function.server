def app():
    from razomy.function.server import app_module
    return app_module.app


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
