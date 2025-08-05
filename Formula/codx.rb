# Formula/codx.rb

class Codx < Formula
  # 1. METADATA: Basic information about your formula.
  desc "A powerful, local-first code snippet manager for the command line"
  homepage "https://github.com/LalwaniPalash/codx"
  version "1.0.1" # This should match the version of your GitHub Release.

  # 2. BINARY DEFINITIONS: This is the core logic.
  # We define different URLs and checksums for each OS/CPU combination.
  on_macos do
    if Hardware::CPU.intel?
      # For Intel Macs
      url "https://github.com/LalwaniPalash/codx/releases/download/v1.0.1/codx-macos-x86_64"
      sha256 "PASTE_THE_SHA256_HASH_OF_THE_INTEL_MAC_BINARY_HERE"
    elsif Hardware::CPU.arm?
      # For Apple Silicon (M1/M2/M3) Macs
      url "https://github.com/LalwaniPalash/codx/releases/download/v1.0.1/codx-macos-arm64"
      sha256 "PASTE_THE_SHA256_HASH_OF_THE_ARM_MAC_BINARY_HERE"
    end
  end

  on_linux do
    if Hardware::CPU.intel?
      # For Intel/AMD Linux
      url "https://github.com/LalwaniPalash/codx/releases/download/v1.0.1/codx-linux-amd64"
      sha256 "PASTE_THE_SHA256_HASH_OF_THE_LINUX_BINARY_HERE"
    end
    # You could add an arm64 block for Linux on ARM (e.g., Raspberry Pi) if you build for it.
  end

  # 3. INSTALLATION METHOD: This tells Homebrew what to do with the downloaded file.
  def install
    # This line takes the downloaded file (e.g., "codx-macos-arm64") and
    # copies it into the Homebrew binary directory, renaming it to "codx".
    bin.install Dir["*"].first => "codx"
  end

  # 4. TEST BLOCK: A simple, automated test to run after installation.
  test do
    # This command runs `codx --version` and checks if it executes successfully.
    # It's a basic sanity check to ensure the binary is not corrupted and works.
    system "#{bin}/codx", "--version"
  end
end