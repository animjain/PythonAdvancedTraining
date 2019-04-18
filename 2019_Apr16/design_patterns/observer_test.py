from observers import observe, notify


@observe(on="connect")
def handle_connection(v):
    print("handle_connection() called (connect): v =", v)


@observe(on="connect")
def handle_connection_secure(v):
    print("Handling a secure connection: v =", v)


@observe(on="timeout")
def handle_timeout(v):
    print("handle_timeout() called (timeout): v =", v)


@observe(on="login")
def authenticate_user(v):
    print("authenticate_user() called (connect) v =", v)


from time import sleep
notify("connect", 10)
sleep(2)
notify("login", "john")
sleep(1)
notify("timeout", 10)
