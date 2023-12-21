from redis import Redis


def main():
    redis_client = Redis(host="localhost", port=6379, password=None)
    redis_client.set("Hello", "world")
    result = redis_client.get("Hello")
    print(f"Response from redis: {result}")


if __name__ == "__main__":
    main()
