import pytest
from app.app import summarize, parse_input

@pytest.fixture
def sample_lists():
    return {
        "empty": [],
        "123": [1, 2, 3],
        "invalid": [1, "a", 3]
    }

def test_summarize_empty_list(sample_lists):
    assert summarize(sample_lists["empty"]) == {"count": 0, "sum": 0, "avg": None}

def test_summarize_123(sample_lists):
    nums = sample_lists["123"]
    result = summarize(nums)
    assert result["count"] == 3
    assert result["sum"] == 6
    assert result["avg"] == 2


def test_summarize_invalid_list(sample_lists):
    with pytest.raises(ValueError):
        summarize(sample_lists["invalid"])
