#!/usr/bin/env python3
"""
CurseForge API Wrapper - Example Usage

This script demonstrates how to use the CurseForge API wrapper.
You'll need to set your API key as an environment variable or pass it directly.

To run this example:
1. Get a CurseForge API key from https://docs.curseforge.com/
2. Set environment variable: export CURSEFORGE_API_KEY="your-api-key"
3. Run: python examples/basic_usage.py
"""

import os
import sys
from curseforge import CurseClient, Games, SORT_FIELDS


def main():
    # Get API key from environment variable
    api_key = os.getenv('CURSEFORGE_API_KEY')
    
    if not api_key:
        print("Error: Please set CURSEFORGE_API_KEY environment variable")
        print("Get your API key from: https://docs.curseforge.com/")
        sys.exit(1)
    
    # Initialize the client with caching enabled
    client = CurseClient(api_key, cache=True)
    
    try:
        print("=== CurseForge API Wrapper Example ===\n")
        
        # Example 1: Get game information
        print("1. Getting Minecraft game info...")
        minecraft = client.game(Games.MINECRAFT)  # Using the constant instead of 432
        print(f"   Game: {minecraft.name} (ID: {minecraft.id})")
        print(f"   Slug: {minecraft.slug}")
        print(f"   Status: {minecraft.status}\n")
        
        # Example 2: Search for mods
        print("2. Searching for JourneyMap...")
        search_results = list(client.search_mods(
            game_id=Games.MINECRAFT,  # Using the constant instead of 432
            search_filter="journeymap",
            sort_field=SORT_FIELDS.TOTAL_DOWNLOADS,  # Sort by total downloads
            page_size=5
        ))
        
        for mod in search_results:
            print(f"   Found: {mod.name} ({mod.download_count:,} downloads)")
        print()
        
        # Example 3: Get specific mod details
        if search_results:
            mod = search_results[0]
            print(f"3. Getting details for {mod.name}...")
            print(f"   Summary: {mod.summary}")
            print(f"   Featured: {mod.is_featured}")
            print(f"   Available: {mod.is_available}")
            
            # Get mod files
            print(f"   Latest files:")
            files = list(client.get_mod_files(mod.id))
            for file in files[:3]:  # Show first 3 files
                print(f"     - {file.display_name}")
                if file.download_url:
                    print(f"       URL: {file.download_url}")
        print()
        
        # Example 4: List game categories
        print("4. Getting Minecraft categories...")
        categories = list(client.categories(Games.MINECRAFT))  # Using the constant
        for category in categories[:5]:  # Show first 5 categories
            print(f"   Category: {category.name}")
        print()
        
        print("✅ Example completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Clean up
        client.close_cache()


if __name__ == '__main__':
    main()