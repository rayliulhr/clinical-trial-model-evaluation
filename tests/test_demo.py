"""Hand-calculated cases and invariants; no real patient data."""
import math
import unittest
from demo import Observation, simulate, summarize


class CalibrationTests(unittest.TestCase):
    def test_hand_calculation_and_horizon(self):
        rows = [Observation(2, True, .1), Observation(6, False, .2)]
        result = summarize(rows, 4)
        self.assertEqual(result['events'], 1)
        self.assertAlmostEqual(result['expected'], 1.0)
        self.assertAlmostEqual(result['oe'], 1.0)
        self.assertEqual(result['at_risk'], 1)
        self.assertEqual(result['censored_before'], 0)

    def test_future_event_does_not_enter_numerator(self):
        result = summarize([Observation(5, True, .1)], 4)
        self.assertEqual(result['events'], 0)
        self.assertAlmostEqual(result['expected'], .4)
        self.assertEqual(result['oe'], 0)

    def test_event_and_censor_ties(self):
        result = summarize([Observation(4, True, .1),
                            Observation(4, False, .1)], 4)
        self.assertEqual(result['events'], 1)
        self.assertEqual(result['at_risk'], 2)
        self.assertEqual(result['censored_before'], 0)

    def test_zero_exposure_and_empty(self):
        for rows in [[], [Observation(0, False, .1)],
                     [Observation(2, True, 0)]]:
            self.assertIsNone(summarize(rows, 4)['oe'])

    def test_scaling_invariant(self):
        rows = [Observation(2, True, .1), Observation(6, False, .2)]
        self.assertAlmostEqual(summarize(rows, 4, .5)['oe'], 2)
        self.assertAlmostEqual(summarize(rows, 4, 2)['oe'], .5)

    def test_unsupported_tail_can_have_identical_score(self):
        rows = [Observation(2, True, .1), Observation(12, False, .1)]
        a, b = summarize(rows, 12), summarize(rows, 24)
        self.assertEqual(a['oe'], b['oe'])
        self.assertEqual(b['at_risk'], 0)
        self.assertEqual(b['illustrative_support'], 'low_or_absent_followup')

    def test_seed_reproducibility_and_administrative_limit(self):
        rows = simulate(n=50, administrative_months=12)
        self.assertEqual(rows, simulate(n=50, administrative_months=12))
        self.assertTrue(all(r.time <= 12 for r in rows))

    def test_invalid_values_rejected(self):
        for row in [Observation(-1, True, .1), Observation(math.nan, True, .1),
                    Observation(1, True, -1), Observation(1, 1, .1)]:
            with self.assertRaises(ValueError):
                summarize([row], 4)
        for value in [0, -1, math.nan, math.inf]:
            with self.assertRaises(ValueError):
                summarize([], value)
            with self.assertRaises(ValueError):
                summarize([], 4, value)


if __name__ == '__main__':
    unittest.main()
