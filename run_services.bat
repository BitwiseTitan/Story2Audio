@echo off
set "VENV_PATH=venv\Scripts\activate"

:: Start gRPC server
start cmd /k "call %VENV_PATH% && python grpc_server.py"

:: Start Gradio UI
start cmd /k "call %VENV_PATH% && python gradio_ui.py"
