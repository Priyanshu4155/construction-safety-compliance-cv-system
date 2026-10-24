from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def status(name: str, ok: bool) -> None:
    print(f"{'OK' if ok else 'FAIL'} - {name}")


def main() -> None:
    print("=" * 70)
    print("PROJECT HEALTHCHECK")
    print("=" * 70)

    required_files = [
        "app/streamlit_app.py",
        "src/detection.py",
        "src/train.py",
        "src/evaluate.py",
        "src/risk_scoring.py",
        "src/compliance_rules.py",
        "configs/ppe_yolov8.yaml",
        "configs/risk_rules.yaml",
        "scripts/train_reasonable_gpu.sh",
        "scripts/gpu_preflight.py",
    ]

    failed = False
    for rel in required_files:
        exists = (ROOT / rel).exists()
        status(rel, exists)
        failed = failed or not exists

    print("\nPython package availability:")
    for package in ["torch", "ultralytics", "cv2", "streamlit", "pandas", "yaml"]:
        ok = importlib.util.find_spec(package) is not None
        status(package, ok)
        failed = failed or not ok

    print("\nSyntax check:")
    files_to_compile = [
        "app/streamlit_app.py",
        "src/detection.py",
        "src/train.py",
        "src/evaluate.py",
        "scripts/gpu_preflight.py",
        "scripts/regenerate_visible_samples.py",
    ]
    result = subprocess.run([sys.executable, "-m", "py_compile", *files_to_compile], cwd=ROOT)
    status("py_compile", result.returncode == 0)
    failed = failed or result.returncode != 0

    print("\nDataset check:")
    dataset = subprocess.run([sys.executable, "scripts/check_dataset.py"], cwd=ROOT)
    status("dataset", dataset.returncode == 0)
    failed = failed or dataset.returncode != 0

    print("\nTest suite:")
    pytest = subprocess.run([sys.executable, "-m", "pytest", "tests", "-q"], cwd=ROOT)
    status("pytest", pytest.returncode == 0)
    failed = failed or pytest.returncode != 0

    print("=" * 70)
    if failed:
        raise SystemExit(1)
    print("Project healthcheck passed.")


if __name__ == "__main__":
    main()
