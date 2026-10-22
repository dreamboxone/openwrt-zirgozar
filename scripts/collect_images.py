#!/usr/bin/env python3
"""Validate the Google WiFi build outputs and stage release files."""

import hashlib
import os
from pathlib import Path
import shutil


REQUIRED_PACKAGES = {
    "zirgozar", "luci-app-zirgozar", "mwan3", "luci-app-mwan3",
    "kmod-nft-tproxy", "kmod-nft-socket",
}


def one_file(directory: Path, pattern: str) -> Path:
    matches = sorted(path for path in directory.glob(pattern) if path.is_file())
    if len(matches) != 1 or matches[0].stat().st_size == 0:
        available = ", ".join(path.name for path in sorted(directory.iterdir()))
        raise RuntimeError(
            f"Expected one nonempty {pattern}, found {len(matches)}. Files: {available}"
        )
    return matches[0]


def collect(source: Path, destination: Path, version: str, tag: str) -> None:
    target = source / "bin/targets/ipq40xx/chromium"
    # OpenWrt manifests omit the release version in their filename.
    manifest = one_file(target, "*google_wifi*.manifest")
    packages = {line.split()[0] for line in manifest.read_text().splitlines() if line.strip()}
    missing = REQUIRED_PACKAGES - packages
    if missing:
        raise RuntimeError(f"Required packages missing from {manifest.name}: {sorted(missing)}")
    images = {
        kind: one_file(target, f"*google_wifi-squashfs-{kind}.bin")
        for kind in ("factory", "sysupgrade")
    }
    destination.mkdir(parents=True, exist_ok=True)
    checksums = []
    for kind, image in images.items():
        name = f"openwrt-google-wifi-ac1304-{version}-zirgozar-{tag}-{kind}.bin"
        shutil.copy2(image, destination / name)
        checksums.append(f"{hashlib.sha256(image.read_bytes()).hexdigest()}  {name}\n")
    shutil.copy2(manifest, destination / manifest.name)
    shutil.copy2(source / ".config", destination / "build.config")
    (destination / "sha256sums").write_text("".join(checksums), encoding="utf-8")


if __name__ == "__main__":
    collect(Path("openwrt"), Path("artifacts"), os.environ["OPENWRT_VERSION"],
            os.environ["ZIRGOZAR_TAG"])
