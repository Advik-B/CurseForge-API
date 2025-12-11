#!/usr/bin/env python3
"""
CurseForge API CLI Examples

This script shows examples of using the CLI tool.
"""

import subprocess
import os

def run_cli_example(command, description):
    """Run a CLI command and display the output"""
    print(f"\n=== {description} ===")
    print(f"Command: python -m curseforge {command}")
    
    # Check if API key is available
    if not os.getenv('CURSEFORGE_API_KEY'):
        print("❌ CURSEFORGE_API_KEY environment variable not set")
        print("   Set it with: export CURSEFORGE_API_KEY='your-api-key'")
        return
    
    try:
        result = subprocess.run(
            f"python -m curseforge {command}".split(),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ Success:")
            print(result.stdout)
        else:
            print("❌ Error:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("❌ Command timed out")
    except Exception as e:
        print(f"❌ Error running command: {e}")

def main():
    print("CurseForge API CLI Examples")
    print("=" * 50)
    
    examples = [
        ("--help", "Show help"),
        ("game 432", "Get Minecraft game info"),
        ("search 432 'journeymap' --limit 3", "Search for JourneyMap in Minecraft"),
        ("mod 32274", "Get JourneyMap mod details"),
    ]
    
    for command, description in examples:
        run_cli_example(command, description)
    
    print("\n" + "=" * 50)
    print("CLI Examples Complete!")
    print("\nFor more commands, run: python -m curseforge --help")

if __name__ == '__main__':
    main()