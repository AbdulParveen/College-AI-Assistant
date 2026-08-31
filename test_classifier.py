from __future__ import annotations

import unittest

from src.classifier import classify_query


class ClassifierTests(unittest.TestCase):
    def test_academic_question(self) -> None:
        self.assertEqual(
            classify_query("What attendance is needed for the semester exam?"),
            "academic",
        )

    def test_fee_question(self) -> None:
        self.assertEqual(classify_query("Can I pay my tuition fee late?"), "fee")

    def test_fee_wins_when_payment_language_is_stronger(self) -> None:
        self.assertEqual(
            classify_query("How do I pay the examination fee and get a receipt?"),
            "fee",
        )

    def test_general_question(self) -> None:
        self.assertEqual(classify_query("Hello, what can you help me with?"), "general")


if __name__ == "__main__":
    unittest.main()

