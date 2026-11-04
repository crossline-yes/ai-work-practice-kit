"""Copy empty practice templates without overwriting existing work. Python 3, no dependencies."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="빈 작업 기록 양식을 복사합니다. 기존 파일은 건너뜁니다.")
    parser.add_argument("destination", type=Path, help="현재 과제 안의 기록 폴더, 예: work-notes")
    parser.add_argument("--dry-run", action="store_true", help="파일을 만들지 않고 대상만 확인")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent / "templates"
    target = args.destination.absolute()
    if any(p.is_symlink() for p in [target, *target.parents]):
        parser.error("연결된 폴더 대신 실제 작업 폴더를 지정하세요.")
    if target.exists() and not target.is_dir():
        parser.error("대상이 폴더가 아닙니다.")
    for item in sorted(source.glob("*.md")):
        dest = target / item.name
        if dest.exists() or dest.is_symlink():
            print(f"SKIP {dest.name} (이미 있음)")
            continue
        if args.dry_run:
            print(f"WOULD CREATE {dest}")
            continue
        target.mkdir(parents=True, exist_ok=True)
        with dest.open("x", encoding="utf-8") as handle:
            handle.write(item.read_text(encoding="utf-8"))
        print(f"CREATED {dest.name}")


if __name__ == "__main__":
    main()
