from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap_case():
    large = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    short = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00", 2, 60)
    expected = [] 
    assert compute_overlap_time(large, short) == expected



def test_multiple_intervals_overlap_case():
    large = time_range("2010-01-12 09:00:00", "2010-01-12 11:00:00", 3, 0) 
    short = time_range("2010-01-12 09:00:00", "2010-01-12 11:00:00", 4, 0) 
    expected = [
        ("2010-01-12 09:00:00", "2010-01-12 09:30:00"),
        ("2010-01-12 09:30:00", "2010-01-12 09:40:00"),
        ("2010-01-12 09:40:00", "2010-01-12 10:00:00"),
        ("2010-01-12 10:00:00", "2010-01-12 10:20:00"),
        ("2010-01-12 10:20:00", "2010-01-12 10:30:00"),
        ("2010-01-12 10:30:00", "2010-01-12 11:00:00")
    ]
    assert compute_overlap_time(large, short) == expected


def test_exact_end_start_case():
    large = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")  
    short = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")  
    expected = []  
    assert compute_overlap_time(large, short) == expected

if __name__ == "__main__":
    test_generic_case()
    test_no_overlap_case()
    test_multiple_intervals_overlap_case()
    test_exact_end_start_case()
    print("All tests passed!")