from fastapi import FastAPI
import redis

app = FastAPI()

# Configuración de Redis
redis_client = redis.StrictRedis(host="redis", port=6379, db=0, decode_responses=True)

@app.post("/event")
def publish_event(event: str):
    """
    Publica un evento en el canal 'events'.
    """
    redis_client.publish("events", event)
    return {"message": f"Evento '{event}' publicado"}
