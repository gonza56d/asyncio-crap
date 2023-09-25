from http_requests import sync


def main():
    return sync.run(10, 'https://google.com')


if __name__ == '__main__':
    result = main()
    print(result)
