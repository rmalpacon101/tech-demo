class ConnectionContextManager:
    def __init__(self):
        print('connection open')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exit - {exc_type} {exc_val} {exc_tb}')
        return True

    def __del__(self):
        print('closing connection')


if __name__ == "__main__":
    with ConnectionContextManager() as c:
        print('inside')