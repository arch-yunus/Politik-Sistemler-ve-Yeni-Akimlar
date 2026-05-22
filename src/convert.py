"""Simple Markdown -> HTML converter CLI.

Usage:
    python -m src.convert input.md -o output.html

Provides `convert_markdown(text)` for testing.
"""
import argparse
from pathlib import Path

try:
    import markdown
except Exception:  # pragma: no cover - user installs dependencies
    markdown = None


def convert_markdown(text: str) -> str:
    if markdown is None:
        raise RuntimeError("Missing 'markdown' package. Install with requirements.txt")
    return markdown.markdown(text, extensions=["fenced_code", "tables"])


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("-o", "--output", help="Output HTML file (optional)")
    args = parser.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        raise SystemExit(f"Input file not found: {inp}")

    text = inp.read_text(encoding="utf-8", errors="replace")
    html = convert_markdown(text)

    if args.output:
        outp = Path(args.output)
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(html, encoding="utf-8")
        print(f"Wrote: {outp}")
    else:
        print(html)


if __name__ == "__main__":
    main()
