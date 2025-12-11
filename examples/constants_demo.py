#!/usr/bin/env python3
"""
Example demonstrating the user-requested constants functionality.

This example shows exactly how to use the CurseForge API wrapper with the
new constants as requested in the GitHub comment.
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from curseforge import CurseClient, Games, SORT_FIELDS

def main():
    """
    Demonstrate the exact usage pattern requested by the user:
    
    client = CurseClient("api-key")
    results = client.search_mods(
        game_id=Games.MINECRAFT,  # Minecraft
        search_filter="journeymap",
        sort_field=SORT_FIELDS.TOTAL_DOWNLOADS,  # Total downloads
        page_size=10
    )
    """
    
    # For demo purposes, we'll use a placeholder API key
    # In real usage, you'd get this from environment or config
    api_key = os.getenv('CURSEFORGE_API_KEY', 'demo-key')
    
    # Initialize client exactly as requested
    client = CurseClient(api_key)
    
    # This is the exact usage pattern the user requested
    print("=== User-Requested Usage Pattern ===")
    print("client = CurseClient('api-key')")
    print("results = client.search_mods(")
    print(f"    game_id=Games.MINECRAFT,  # {Games.MINECRAFT}")
    print("    search_filter='journeymap',")  
    print(f"    sort_field=SORT_FIELDS.TOTAL_DOWNLOADS,  # {SORT_FIELDS.TOTAL_DOWNLOADS}")
    print("    page_size=10")
    print(")")
    print()
    
    # Show all available constants
    print("=== Available Game Constants ===")
    game_attrs = [attr for attr in dir(Games) if not attr.startswith('_')]
    for attr in game_attrs:
        value = getattr(Games, attr)
        print(f"Games.{attr} = {value}")
    print()
    
    print("=== Available Sort Field Constants ===") 
    sort_attrs = [attr for attr in dir(SORT_FIELDS) if not attr.startswith('_')]
    for attr in sort_attrs:
        value = getattr(SORT_FIELDS, attr)
        print(f"SORT_FIELDS.{attr} = {value}")
    print()
    
    # Demonstrate the functionality (without making actual API calls)
    print("✅ Constants are working perfectly!")
    print("The API can now be used exactly as requested in the GitHub comment.")


if __name__ == '__main__':
    main()