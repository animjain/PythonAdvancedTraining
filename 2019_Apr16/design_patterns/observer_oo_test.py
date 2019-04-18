from observers_oo import PubSub

pubsub = PubSub()


@pubsub.subscribe(on="connect")
def handle_connection(v):
    print("handle_connection() called (connect): v =", v)
    pubsub.publish("secure_connect", v)


@pubsub.subscribe(on="secure_connect")
def handle_connection_secure(v):
    print("Handling a secure connection: v =", v)
    pubsub.publish("login", v)


@pubsub.subscribe(on="timeout")
def handle_timeout(v):
    print("handle_timeout() called (timeout): v =", v)


@pubsub.subscribe(on="login")
def authenticate_user(v):
    print("authenticate_user() called (connect) v =", v)
    pubsub.publish("timeout", v)


if __name__ == '__main__':
    pubsub.publish("connect", "localhost")
