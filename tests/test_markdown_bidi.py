from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "markdown_bidi", ROOT / "scripts" / "markdown_bidi.py"
)
assert SPEC and SPEC.loader
MARKDOWN_BIDI = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MARKDOWN_BIDI)


class MarkdownBidiTest(unittest.TestCase):
    def test_terms_and_link_labels_use_github_allowed_span(self) -> None:
        source = (
            "# نمونه\n\n"
            "[NPCI](https://www.npci.org.in/) سازمان پرداخت هند است و UPI را "
            "در یک App عرضه می‌کند.\n"
        )

        formatted = MARKDOWN_BIDI.format_markdown(source)

        self.assertIn(
            '[<span dir="ltr">NPCI</span>](https://www.npci.org.in/)',
            formatted,
        )
        self.assertIn('<span dir="ltr">UPI</span>', formatted)
        self.assertIn('<span dir="ltr">App</span>', formatted)
        self.assertNotIn('<bdi dir="ltr">', formatted)
        self.assertEqual([], MARKDOWN_BIDI.validate_markdown(formatted))

    def test_existing_bdi_document_is_migrated_without_changing_words(self) -> None:
        legacy = (
            f"{MARKDOWN_BIDI.MARKER}\n"
            f"{MARKDOWN_BIDI.RTL_OPEN}\n\n"
            'مرز <bdi dir="ltr">Bounded Context</bdi> روشن است.\n\n'
            f"{MARKDOWN_BIDI.DIV_CLOSE}\n"
        )

        migrated = MARKDOWN_BIDI.format_markdown(legacy)

        self.assertIn('<span dir="ltr">Bounded Context</span>', migrated)
        self.assertNotIn('<bdi dir="ltr">', migrated)
        self.assertIn('مرز <span dir="ltr">Bounded Context</span> روشن است.', migrated)
        self.assertEqual([], MARKDOWN_BIDI.validate_markdown(migrated))

    def test_fenced_code_is_not_rewritten(self) -> None:
        code = 'System.out.println("متن فارسی and English");'
        source = f"# نمونه\n\n```java\n{code}\n```\n"

        formatted = MARKDOWN_BIDI.format_markdown(source)

        self.assertIn(f"```java\n{code}\n```", formatted)
        self.assertNotIn(f'<span dir="ltr">{code}</span>', formatted)
        self.assertEqual([], MARKDOWN_BIDI.validate_markdown(formatted))

    def test_validator_rejects_legacy_bdi_outside_code(self) -> None:
        formatted = MARKDOWN_BIDI.format_markdown("# نمونه\n\nواژه API معتبر است.\n")
        legacy = formatted.replace(
            '<span dir="ltr">API</span>', '<bdi dir="ltr">API</bdi>'
        )

        errors = MARKDOWN_BIDI.validate_markdown(legacy)

        self.assertTrue(any("bdi is stripped by GitHub" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
