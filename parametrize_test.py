import pytest
from times import compute_overlap_time, time_range

@pytest.mark.parametrize(
    "time_range_1, time_range_2, expected",
    [
        # Test case 1: generic overlap case
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
        ),
        # Test case 2: no overlap
        (
            time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00"),
            time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00", 2, 60),
            []
        ),
        # Test case 3: multiple intervals overlap
        (
            time_range("2010-01-12 09:00:00", "2010-01-12 11:00:00", 3, 0),
            time_range("2010-01-12 09:00:00", "2010-01-12 11:00:00", 4, 0),
            [
                ("2010-01-12 09:00:00", "2010-01-12 09:30:00"),
                ("2010-01-12 09:30:00", "2010-01-12 09:40:00"),
                ("2010-01-12 09:40:00", "2010-01-12 10:00:00"),
                ("2010-01-12 10:00:00", "2010-01-12 10:20:00"),
                ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
                ("2010-01-12 10:30:00", "2010-01-12 11:00:00")
            ]
        ),
        # Test case 4: exact end-start overlap
        (
            time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00"),
            time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
            []
        ),
    ]
)
def test_compute_overlap(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected


def test_time_range_backwards():
    # 使用 pytest.raises 来检查是否抛出 ValueError
    with pytest.raises(ValueError, match="End time must be after start time."):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


if __name__ == "__main__":
    test_compute_overlap()
    test_time_range_backwards()
    print("All tests passed!")
