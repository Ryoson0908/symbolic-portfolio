"""One-off: copy chat-attached logo into assets/ (run from any cwd)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(
    r"C:\Users\ryoso\.cursor\projects\c-Users-ryoso-OneDrive-Ryoshun-Ssite-symbolic-portfolio\assets\c__Users_ryoso_AppData_Roaming_Cursor_User_workspaceStorage_faf4bd11f399cc19758a384f08f6feeb_images_Ryoshun-3e8fa098-56fc-4eb7-bc45-4e237f1ec99f.png"
)
DST = ROOT / "assets" / "ryoshun-orbit-logo.png"


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"Source missing: {SRC}")
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC, DST)
    print("OK", DST, DST.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
