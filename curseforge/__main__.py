#!/usr/bin/env python3
"""
CurseForge API CLI Tool

A simple command-line interface for the CurseForge API wrapper.
"""

import argparse
import json
import os
import sys
from .base import CurseClient
from .util.manifest_parser import parse_manifest


def main():
    parser = argparse.ArgumentParser(description='CurseForge API CLI Tool')
    parser.add_argument('--api-key', type=str, help='CurseForge API key (or set CURSEFORGE_API_KEY env var)')
    parser.add_argument('--no-cache', action='store_true', help='Disable caching')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Game command
    game_parser = subparsers.add_parser('game', help='Get game information')
    game_parser.add_argument('game_id', type=int, help='Game ID')
    
    # Games command
    games_parser = subparsers.add_parser('games', help='List all games')
    
    # Mod command
    mod_parser = subparsers.add_parser('mod', help='Get mod information')
    mod_parser.add_argument('mod_id', type=int, help='Mod ID')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for mods')
    search_parser.add_argument('game_id', type=int, help='Game ID to search in')
    search_parser.add_argument('query', type=str, help='Search query')
    search_parser.add_argument('--limit', type=int, default=10, help='Limit results (default: 10)')
    
    # Manifest command
    manifest_parser = subparsers.add_parser('manifest', help='Parse manifest file')
    manifest_parser.add_argument('file', type=str, help='Path to manifest.json file')
    manifest_parser.add_argument('--download-urls', action='store_true', help='Get download URLs for all mods')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Get API key
    api_key = args.api_key or os.getenv('CURSEFORGE_API_KEY')
    if not api_key:
        print("Error: API key required. Use --api-key or set CURSEFORGE_API_KEY environment variable.")
        sys.exit(1)
    
    # Initialize client
    client = CurseClient(api_key, cache=not args.no_cache)
    
    try:
        if args.command == 'game':
            game = client.game(args.game_id)
            print(json.dumps({
                'id': game.id,
                'name': game.name,
                'slug': game.slug,
                'status': game.status
            }, indent=2))
            
        elif args.command == 'games':
            games = list(client.games())
            print(json.dumps([{
                'id': game.id,
                'name': game.name,
                'slug': game.slug
            } for game in games], indent=2))
            
        elif args.command == 'mod':
            mod = client.mod(args.mod_id)
            print(json.dumps({
                'id': mod.id,
                'name': mod.name,
                'slug': mod.slug,
                'summary': mod.summary,
                'download_count': mod.download_count,
                'is_featured': mod.is_featured
            }, indent=2))
            
        elif args.command == 'search':
            results = list(client.search_mods(
                game_id=args.game_id,
                search_filter=args.query,
                page_size=args.limit
            ))
            print(json.dumps([{
                'id': mod.id,
                'name': mod.name,
                'slug': mod.slug,
                'download_count': mod.download_count
            } for mod in results], indent=2))
            
        elif args.command == 'manifest':
            if not os.path.exists(args.file):
                print(f"Error: File {args.file} not found.")
                sys.exit(1)
                
            with open(args.file, 'r') as f:
                manifest_data = json.load(f)
                
            manifest = parse_manifest(manifest_data)
            result = {
                'name': manifest.name,
                'version': manifest.version,
                'author': manifest.author,
                'files': []
            }
            
            for file_manifest in manifest.files:
                file_info = {
                    'project_id': file_manifest.project_id,
                    'file_id': file_manifest.file_id,
                    'required': file_manifest.required
                }
                
                if args.download_urls:
                    try:
                        mod_file = client.manifest_to_modfile(file_manifest)
                        file_info['download_url'] = mod_file.download_url
                        file_info['file_name'] = mod_file.file_name
                    except Exception as e:
                        file_info['error'] = str(e)
                
                result['files'].append(file_info)
            
            print(json.dumps(result, indent=2))
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        client.close_cache()


if __name__ == '__main__':
    main()
