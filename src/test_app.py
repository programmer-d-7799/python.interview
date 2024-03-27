import pytest
from app import *


def test_popularity_tracker_no_popular_content():
    # arrange
    popularityTracker = MostPopular()

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == -1


def test_popularity_tracker_one_popular_content():
    # arrange
    popularityTracker = MostPopular()
    popularityTracker.increase_popularity(7)

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == 7


def test_popularity_tracker_popular_then_no_popular():
    # arrange
    popularityTracker = MostPopular()
    popularityTracker.increase_popularity(7)
    popularityTracker.decrease_popularity(7)

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == -1


def test_popularity_tracker_two_popular_content():
    # arrange
    popularityTracker = MostPopular()
    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(8)
    popularityTracker.increase_popularity(8)

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == 8


def test_popularity_tracker_two_popular_content_one_decreased():
    # arrange
    popularityTracker = MostPopular()
    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(8)
    popularityTracker.increase_popularity(8)
    popularityTracker.decrease_popularity(8)
    popularityTracker.decrease_popularity(8)

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == 7


def test_popularity_tracker_two_popular_content_same_popularity():
    # arrange
    popularityTracker = MostPopular()
    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(8)
    popularityTracker.increase_popularity(8)

    # action
    result = popularityTracker.most_popular()

    # assert
    assert result == 8


def test_popularity_tracker_wrong_input_type():
    # arrange
    popularityTracker = MostPopular()

    # action
    with pytest.raises(ValueError):
        popularityTracker.increase_popularity("string")


def test_popularity_tracker_negative_content_id():
    # arrange
    popularityTracker = MostPopular()

    # action
    with pytest.raises(ValueError):
        popularityTracker.increase_popularity(-1)
