import argparse
from taxonomic_report_studio.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Studio-style report builder for taxonomic abundance summaries.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
