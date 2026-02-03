@echo off
echo Starting Pintu Application...

:: Start Backend
echo Starting Django Backend...
start "Django Backend" cmd /k "cd backend && venv\Scripts\python.exe -m daphne -b 127.0.0.1 -p 8000 service_market.asgi:application"

:: Start Frontend
echo Starting Next.js Frontend...
start "Next.js Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo Application started!
echo Frontend: http://localhost:3000
echo Backend: http://localhost:8000
echo.
echo Waiting for servers to initialize (10 seconds)...
timeout /t 10
echo Opening Browser...
start http://localhost:3000
pause
