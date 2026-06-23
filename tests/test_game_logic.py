import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess


#FIX: Added pytests using agent and had it redo the directory structure to fit the testing names

def test_guess_too_high_string_secret():
    # Bug: secret passed as str caused lexicographic compare — "15" > "9" is False,
    # so guess=15 would wrongly return "Too Low" instead of "Too High"
    outcome, _ = check_guess(15, "9")
    assert outcome == "Too High"


def test_guess_too_low_string_secret():
    outcome, _ = check_guess(3, "9")
    assert outcome == "Too Low"


def test_exact_match_string_secret():
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"
