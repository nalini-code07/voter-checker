import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "voter_check.py")


def run_script():
    result = subprocess.run(
        [sys.executable, SCRIPT],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.splitlines()


class TestVoterCheck(unittest.TestCase):

    def setUp(self):
        self.code, self.lines = run_script()

    def test_script_runs_without_error(self):
        self.assertEqual(self.code, 0)

    def test_single_voter_aged_17_cannot_vote(self):
        self.assertEqual(
            self.lines[0:4],
            ["Voter ID: 1001", "Age: 17", "Not eligible", "Cannot vote"],
        )

    def test_for_loop_checks_three_voters_in_order(self):
        self.assertEqual(
            self.lines[5:14],
            [
                "Age: 17", "Not eligible", "Cannot vote",
                "Age: 18", "Eligible", "General",
                "Age: 70", "Eligible", "Senior",
            ],
        )

    def test_age_18_is_the_first_general_age(self):
        index = self.lines.index("Age: 18", 5)
        self.assertEqual(self.lines[index + 1], "Eligible")
        self.assertEqual(self.lines[index + 2], "General")

    def test_while_loop_counts_down_from_5_to_1(self):
        self.assertEqual(
            self.lines[15:20],
            [
                "Polling station closes in 5 minutes",
                "Polling station closes in 4 minutes",
                "Polling station closes in 3 minutes",
                "Polling station closes in 2 minutes",
                "Polling station closes in 1 minutes",
            ],
        )

    def test_ends_with_closed(self):
        self.assertEqual(self.lines[-1], "Closed")
        self.assertEqual(len(self.lines), 21)


if __name__ == "__main__":
    unittest.main()

