# service_pod

## installation
```pip install poetry```  
```poetry init```  
```poetry env use python3.10```  
```poetry add fastapi[all]```  
To add interpreter to IDE use command:  
``` poetry env info --path```  
and add path to IDE.  

Documentation page   
```http://127.0.0.1:8000/api/openapi```  

### Redis
download image:
```docker pull redis```
run image:
```docker run --name redis -d redis```
redis-cli:
```docker exec -it redis redis-cli ```
redis-ip to connect from host:
- docker inspect redis
- "NetworkSettings": {
        "Gateway": "172.17.0.1",
        "IPAddress": "172.17.0.2"
    }
### Celery
#### No schedule tasks
In a separate terminal:  
```poetry shell```  
```celery -A tasks.tasks:celery worker --loglevel=INFO```  
In second separate terminal:  
```celery -A tasks.tasks:celery flower --loglevel=INFO```  
Enter flower:  
```localhost:5555```   

### PostgreSQL
```sudo docker run  --rm  --name postgres  -p 5432:5432   -e POSTGRES_USER=postgres   -e POSTGRES_PASSWORD=postgres  -e POSTGRES_DB=collection   -d postgres:14.5```  
enter password(localhost):  
```sudo -i -u postgres```  
```psql -h localhost```  
