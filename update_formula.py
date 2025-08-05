#!/usr/bin/env python3
"""
Script to update the Homebrew formula for CODX with new version and SHA256 hashes.
"""

import sys
import re
import requests
import hashlib
from pathlib import Path

def get_sha256_from_url(url):
    """Download file from URL and calculate SHA256 hash."""
    print(f"Downloading {url}...")
    response = requests.get(url)
    response.raise_for_status()
    return hashlib.sha256(response.content).hexdigest()

def update_formula(version):
    """Update the Homebrew formula with new version and SHA256 hashes."""
    # Remove 'v' prefix if present
    clean_version = version.lstrip('v')
    
    # URLs for the binaries
    base_url = f"https://github.com/LalwaniPalash/codx/releases/download/{version}"
    linux_url = f"{base_url}/codx-linux-amd64"
    macos_url = f"{base_url}/codx-macos-arm64"
    
    # Get SHA256 hashes
    print("Calculating SHA256 hashes...")
    linux_sha = get_sha256_from_url(linux_url)
    macos_sha = get_sha256_from_url(macos_url)
    
    print(f"Linux SHA256: {linux_sha}")
    print(f"macOS SHA256: {macos_sha}")
    
    # Read current formula
    formula_path = Path("Formula/codx.rb")
    content = formula_path.read_text()
    
    # Update version
    content = re.sub(
        r'version "[^"]+"',
        f'version "{clean_version}"',
        content
    )
    
    # Update Linux URL and SHA
    content = re.sub(
        r'url "[^"]+/codx-linux-amd64"',
        f'url "{linux_url}"',
        content
    )
    content = re.sub(
        r'sha256 "[a-f0-9]{64}"  # Linux',
        f'sha256 "{linux_sha}"  # Linux',
        content
    )
    
    # Update macOS URL and SHA
    content = re.sub(
        r'url "[^"]+/codx-macos-arm64"',
        f'url "{macos_url}"',
        content
    )
    content = re.sub(
        r'sha256 "[a-f0-9]{64}"  # macOS',
        f'sha256 "{macos_sha}"  # macOS',
        content
    )
    
    # Write updated formula
    formula_path.write_text(content)
    print(f"Updated formula to version {clean_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_formula.py <version>")
        sys.exit(1)
    
    version = sys.argv[1]
    update_formula(version)