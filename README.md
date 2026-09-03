https://www.kaggle.com/datasets/nasa/solar-eclipses?select=solar.csv

uv init --no-package                    
uv init --package backend               
uv init --package frontend  

```bash
uv add --package backend fastapi "uvicorn[standard]" pandas
uv add --package frontend streamlit requests pandas
uv add kagglehub
uv add jupyter ipykernel

uv sync                                  
```

```bash
# Backend FastAPI
uv run --package backend uvicorn backend.main:app --reload --port 8000

# Frontend Streamlit
uv run --package frontend streamlit run frontend/src/frontend/main.py

```

```bash
docker build -t eclipseboard-backend -f backend/Dockerfile .
docker build -t eclipseboard-frontend -f frontend/Dockerfile .

docker run -p 8000:8000 eclipseboard-backend
docker run -p 8501:8501 eclipseboard-frontend

docker compose up --build      # run both together with the dck compose.yml file
```

```bash
az login                                    
az acr login --name <name>           

docker compose build                        
docker compose push      
                   
az acr repository list --name <name> --output table  #verify

az resource list --resource-group <RG name> --output table  # list all resources in RG
```


