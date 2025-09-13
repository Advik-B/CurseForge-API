#!/usr/bin/env python3
"""
Test suite for CurseForge API wrapper
Note: These tests require a valid CurseForge API key to run properly.
For unit tests, we test the object creation and serialization without API calls.
"""

import unittest
from curseforge.classes import (
    CurseMod, CurseModFile, CurseGame, CurseCategory, 
    CurseImage, CurseHash, CurseModFileManifest
)
from curseforge import CurseClient


class TestCurseForgeClasses(unittest.TestCase):
    """Test CurseForge data classes"""

    def test_curse_mod_from_dict(self):
        """Test CurseMod.from_dict with sample data"""
        test_data = {
            'id': 238222,
            'gameId': 432,
            'name': 'JourneyMap',
            'slug': 'journeymap',
            'summary': 'Real-time mapping in-game or your browser',
            'status': 4,
            'downloadCount': 50000000,
            'isFeatured': True,
            'primaryCategoryId': 423,
            'categories': [],
            'classId': 6,
            'authors': [
                {'id': 1, 'name': 'TestAuthor', 'url': 'https://example.com'}
            ],
            'logo': {
                'id': 1,
                'modId': 238222,
                'title': 'JourneyMap Logo',
                'description': '',
                'thumbnailUrl': 'https://example.com/thumb.png',
                'url': 'https://example.com/logo.png'
            },
            'screenshots': [],
            'mainFileId': 1234567,
            'latestFiles': [],
            'latestFilesIndexes': [],
            'dateCreated': '2023-01-01T00:00:00.000Z',
            'dateModified': '2023-01-01T00:00:00.000Z',
            'dateReleased': '2023-01-01T00:00:00.000Z',
            'allowModDistribution': True,
            'gamePopularityRank': 1,
            'isAvailable': True,
            'thumbsUpCount': 100
        }
        
        mod = CurseMod.from_dict(test_data)
        self.assertIsInstance(mod, CurseMod)
        self.assertEqual(mod.id, 238222)
        self.assertEqual(mod.name, 'JourneyMap')
        self.assertEqual(mod.slug, 'journeymap')
        self.assertEqual(mod.download_count, 50000000)
        self.assertTrue(mod.is_featured)

    def test_curse_game_from_dict(self):
        """Test CurseGame.from_dict with sample data"""
        test_data = {
            'id': 432,
            'name': 'Minecraft',
            'slug': 'minecraft',
            'assets': {
                'iconUrl': 'https://example.com/icon.png',
                'tileUrl': 'https://example.com/tile.png',
                'coverUrl': 'https://example.com/cover.png'
            },
            'status': 1,
            'apiStatus': 1,
            'dateModified': '2023-01-01T00:00:00.000Z'
        }
        
        game = CurseGame.from_dict(test_data)
        self.assertIsInstance(game, CurseGame)
        self.assertEqual(game.id, 432)
        self.assertEqual(game.name, 'Minecraft')
        self.assertEqual(game.slug, 'minecraft')

    def test_curse_image_from_dict(self):
        """Test CurseImage.from_dict with sample data"""
        test_data = {
            'id': 123,
            'modId': 456,
            'title': 'Test Image',
            'description': 'A test image',
            'thumbnailUrl': 'https://example.com/thumb.png',
            'url': 'https://example.com/image.png'
        }
        
        image = CurseImage.from_dict(test_data)
        self.assertIsInstance(image, CurseImage)
        self.assertEqual(image.id, 123)
        self.assertEqual(image.modId, 456)
        self.assertEqual(image.title, 'Test Image')

    def test_curse_hash_from_dict(self):
        """Test CurseHash.from_dict with sample data"""
        test_data = {
            'value': 'abc123def456',
            'algo': 1
        }
        
        hash_obj = CurseHash.from_dict(test_data)
        self.assertIsInstance(hash_obj, CurseHash)
        self.assertEqual(hash_obj.value, 'abc123def456')
        self.assertEqual(hash_obj.algo, 1)

    def test_curse_category_from_dict(self):
        """Test CurseCategory.from_dict with sample data"""
        test_data = {
            'id': 423,
            'gameId': 432,
            'name': 'Map and Information',
            'slug': 'map-information',
            'url': 'https://example.com',
            'iconUrl': 'https://example.com/icon.png',
            'dateModified': '2023-01-01T00:00:00.000Z',
            'isClass': False,
            'classId': 6,
            'parentCategoryId': 0,
            'displayIndex': 1
        }
        
        category = CurseCategory.from_dict(test_data)
        self.assertIsInstance(category, CurseCategory)
        self.assertEqual(category.id, 423)
        self.assertEqual(category.name, 'Map and Information')

    def test_curse_mod_file_manifest_from_dict(self):
        """Test CurseModFileManifest.from_dict with sample data"""
        test_data = {
            'projectID': 238222,
            'fileID': 1234567,
            'required': True
        }
        
        manifest = CurseModFileManifest.from_dict(test_data)
        self.assertIsInstance(manifest, CurseModFileManifest)
        self.assertEqual(manifest.project_id, 238222)
        self.assertEqual(manifest.file_id, 1234567)
        self.assertTrue(manifest.required)


class TestCurseClient(unittest.TestCase):
    """Test CurseClient functionality that doesn't require API calls"""

    def test_client_initialization(self):
        """Test CurseClient initialization"""
        client = CurseClient("test-api-key", cache=False)
        self.assertEqual(client.api_key, "test-api-key")
        self.assertEqual(client.version, "v1")
        self.assertFalse(client.cache)

    def test_client_with_cache(self):
        """Test CurseClient initialization with cache"""
        client = CurseClient("test-api-key", cache=True, cache_dir="/tmp/test_cache")
        self.assertEqual(client.api_key, "test-api-key")
        self.assertTrue(client.cache)
        self.assertEqual(client.cache_dir, "/tmp/test_cache")
        client.close_cache()  # Clean up


if __name__ == '__main__':
    print("Running CurseForge API wrapper tests...")
    print("Note: These are unit tests that don't require an API key.")
    print("For integration tests with actual API calls, you'll need a valid CurseForge API key.")
    unittest.main()