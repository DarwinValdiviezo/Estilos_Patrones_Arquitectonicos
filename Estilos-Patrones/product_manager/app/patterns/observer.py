class OrderNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def unsubscribe(self, user):
        self.subscribers.remove(user)

    def notify(self, message):
        for user in self.subscribers:
            user.update(message)

class User:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received notification: {message}")
