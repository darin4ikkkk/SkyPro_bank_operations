import pytest

from src.processing import filter_by_state, sort_by_date, sort_key


def test_filter_by_state():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                                                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    assert filter_by_state([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == []

    assert filter_by_state([]) == []


@pytest.mark.parametrize("dates_list, expected", [([{'date': '2019-07-03T18:35:29.512364'},
                                                    {'date': '2019-03-03T18:35:29.512364'},
                                                    {'date': '2018-07-03T18:35:29.512364'}], [{'date': '2019-07-03T18:35:29.512364'},
                                                                                              {'date': '2019-03-03T18:35:29.512364'},
                                                                                              {'date': '2018-07-03T18:35:29.512364'}]), ([{'date': '2019-07-03T18:35:29.512364'},
                                                                                                                                          {'date': '2020-07-03T18:35:29.512364'},
                                                                                                                                          {'date': '2019-07-07T18:35:29.512364'}], [{'date': '2020-07-03T18:35:29.512364'},
                                                                                                                                                                                    {'date': '2019-07-07T18:35:29.512364'},
                                                                                                                                                                                    {'date': '2019-07-03T18:35:29.512364'}]), ([{'date': '2019-07-03T18:35:29.512364'},
                                                                                                                                                                                                                                {'date': '2019-09-03T18:35:29.512364'},
                                                                                                                                                                                                                                {'date': '2019-11-04T18:35:29.512364'}], [{'date': '2019-11-04T18:35:29.512364'},
                                                                                                                                                                                                                                                                          {'date': '2019-09-03T18:35:29.512364'},
                                                                                                                                                                                                                                                                          {'date': '2019-07-03T18:35:29.512364'}])])

def test_sort_by_date(dates_list, expected):
    assert sort_by_date(dates_list) == expected


def test_sort_by_date_reverse():
    assert sort_by_date([{'date': '2018-08-03'}, {'date': '2018-06-03'}, {'date': '2018-07-03'}], False) == [{'date': '2018-06-03'}, {'date': '2018-07-03'}, {'date': '2018-08-03'}]


def test_sort_by_date_repeat():
        assert sort_by_date([{'date': '2018-07-03'}, {'date': '2018-07-03'}, {'date': '2018-07-03'}]) == [{'date': '2018-07-03'}, {'date': '2018-07-03'}, {'date': '2018-07-03'}]


@pytest.fixture
def clear_list():
    return []


def test_sort_by_date_clear(clear_list):
    assert sort_by_date(clear_list) == []
