from fastapi import FastAPI, BackgroundTasks
import redis

app = FastAPI()

# Configuración de Redis
redis_client = redis.StrictRedis(host="redis", port=6379, db=0, decode_responses=True)

def process_event(event: str):
    """
    Procesa el evento recibido.
    """
    print(f"Procesando evento: {event}")

@app.on_event("startup")
def listen_to_events():
    """
    Inicia un listener para eventos del canal 'events'.
    """
    def redis_listener():
        pubsub = redis_client.pubsub()
        pubsub.subscribe("events")
        for message in pubsub.listen():
            if message["type"] == "message":
                process_event(message["data"])

    import threading
    listener_thread = threading.Thread(target=redis_listener)
    listener_thread.daemon = True
    listener_thread.start()
