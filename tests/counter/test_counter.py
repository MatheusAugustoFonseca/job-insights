# from src.pre_built.counter import count_ocurrences
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "agriculture") == 24
    assert count_ocurrences("data/jobs.csv", "backend") == 55
    assert count_ocurrences("data/jobs.csv", "back-end") == 20
    assert count_ocurrences("data/jobs.csv", "back end") == 8
