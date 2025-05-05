@echo off
setlocal

REM Activate virtual environment
call venv\Scripts\activate

REM Start gRPC server in background
start "gRPC Server" cmd /c "python grpc_server.py"
echo Started gRPC server...

REM Start FastAPI server in background
start "FastAPI Server" cmd /c "uvicorn app.main:app --port 8000"
echo Started FastAPI server...

REM Wait for servers to start
timeout /t 10 > nul

REM Run combined tests
python test_all_services.py

REM Wait before shutting down
timeout /t 2

REM Kill background servers
taskkill /FI "WINDOWTITLE eq gRPC Server"
taskkill /FI "WINDOWTITLE eq FastAPI Server"

echo All done.
pause
