from typing import Any

import pytest

from scr.processing import filter_by_state, sort_by_date


def test_filter_by_executed(filter_state: list[dict[str, Any]]) -> None:
    assert filter_by_state(filter_state, state="EXECUTED") == [
        {"id": 816976472, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 765799246, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_canceled(filter_state: list[dict[str, Any]]) -> None:
    assert filter_by_state(filter_state, state="CANCELED") == [
        {"id": 123812831, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 809385983, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "received_data, expected_data",
    [
        ([{"date": "2019-05-22"}, {"date": "2021-08-06"}], [{"date": "2021-08-06"}, {"date": "2019-05-22"}]),
        ([{"date": "2022-09-01"}, {"date": "2021-09-16"}], [{"date": "2022-09-01"}, {"date": "2021-09-16"}]),
        ([{"date": "2020-07-01"}, {"date": "2020-07-01"}], [{"date": "2020-07-01"}, {"date": "2020-07-01"}]),
    ],
)
def test_sort_by_date(received_data: list[dict], expected_data: list[dict]) -> None:
    assert sort_by_date(received_data) == expected_data


def test_sort_by_date_incorrect(incorrect_sort_date: list[dict]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(incorrect_sort_date)
