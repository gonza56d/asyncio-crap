import requests
from time import perf_counter


def run(requests_amount: int, url: str, assert_success: bool = True) -> float:
    start_time = perf_counter()
    for i in range(requests_amount):
        result = requests.get(url)
        if assert_success and not 200 <= result.status_code <= 299:
            raise ValueError(
                f'Call number {i+1} did not succeed with a {result.status_code} status code.\n'
                f'Elapsed time: {perf_counter() - start_time} seconds.'
            )
    end_time = perf_counter()
    return end_time - start_time
