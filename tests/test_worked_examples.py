import unittest
from statistics import mean

from control_subsets import ALIGNED, CONTROL_EVENTS, REVERSED, TREATED_EVENTS, replay, rmse
from landmark import CASES, Lab, Timeline, landmark_row


class LandmarkTests(unittest.TestCase):
    def test_retained_cases_include_missing_labs_and_unknown_status(self):
        rows = [landmark_row(person) for person in CASES]
        self.assertEqual([r for r in rows if r is not None], [
            ("A", 4.0, "alive"), ("B", None, "died"),
            ("C", None, "unknown"), ("F", 6.0, "alive")])

    def test_boundary_and_late_death(self):
        self.assertIsNone(landmark_row(Timeline("D", 10, death=10)))
        self.assertEqual(landmark_row(Timeline("X", 7, death=20)), ("X", None, "died"))
        self.assertEqual(landmark_row(Timeline("Y", 7, death=21)), ("Y", None, "alive"))

    def test_unreleased_results_cannot_replace_available_results(self):
        p = Timeline("X", 10, labs=(Lab(9, None, 19), Lab(5, 8, 11), Lab(9, 12, 17)))
        self.assertEqual(landmark_row(p), ("X", 11, "unknown"))


class SubsetTests(unittest.TestCase):
    def test_hand_calculation_on_first_subset(self):
        reference, pairs = replay(CONTROL_EVENTS, TREATED_EVENTS, ALIGNED, 3)
        self.assertEqual(reference, -0.25)
        self.assertEqual(len(pairs), 56)
        self.assertEqual(pairs[0], (0.25, 0.0))
        for estimates in zip(*pairs):
            self.assertAlmostEqual(mean(estimates), reference)

    def test_effect_of_reversing_score(self):
        reference, aligned = replay(CONTROL_EVENTS, TREATED_EVENTS, ALIGNED, 3)
        _, reversed_scores = replay(CONTROL_EVENTS, TREATED_EVENTS, REVERSED, 3)
        plain, good = zip(*aligned)
        plain_again, bad = zip(*reversed_scores)
        self.assertEqual(plain, plain_again)
        self.assertLess(rmse(good, reference), rmse(plain, reference))
        self.assertGreater(rmse(bad, reference), rmse(plain, reference))

    def test_constant_score_and_full_sample(self):
        _, pairs = replay(CONTROL_EVENTS, TREATED_EVENTS, [0.5] * 8, 3)
        for a, b in pairs:
            self.assertEqual(a, b)
        reference, full = replay(CONTROL_EVENTS, TREATED_EVENTS, REVERSED, 8)
        self.assertEqual(full, [(reference, reference)])

    def test_invalid_inputs(self):
        for scores, size in [(ALIGNED, 0), (ALIGNED, 9), ([0.5], 3)]:
            with self.assertRaises(ValueError):
                replay(CONTROL_EVENTS, TREATED_EVENTS, scores, size)


if __name__ == "__main__":
    unittest.main()
