#!/usr/bin/env python
# encoding: utf-8
"""
test_searcher.py
"""

import os
import testcase
from core.sherlock import indexer, searcher
from core.utils import debug


class TestSearcher(testcase.BaseTestCase):
    def setUp(self):
        """ Called before each test """
        testcase.BaseTestCase.setUp(self)
        pass
        
    def tearDown(self):
        """ Called after each test """
        pass
        
    def test_simple_search(self):
        """Tests simple search logic
        """
        # index a file for the search
        path = os.path.join(self.test_dir, 'text/objc_example.m')
        idxr = indexer.get_indexer(name='test', rebuild_index=True)
        idxr.index_text(path)
        # test values
        self.assertTrue(idxr.doc_count() == 1, 'bad doc count')
        
        idx = idxr.get_index()
        # find something in the file
        results = idx.search('key')
        self.assertTrue(len(results) == 1, 'wrong hit count')
        pass

    def test_search(self):
        """Tests searching against more than one document
        """
        # index directory
        idxr = indexer.get_indexer(name='test', rebuild_index=True)
        path = os.path.join(self.test_dir, 'text')
        idxr.index_text(path)
        self.assertTrue(idxr.doc_count() == 7, "no documents indexed")
        # search
        idx = idxr.get_index()
        search_text = 'value'
        results = idx.search(search_text)
        self.assertTrue(len(results), 'no results from the search')
        # search by path
        results = idx.search_path(os.path.join(path, 'objc_example.m'))
        self.assertTrue(len(results) == 1, 'wrong number of results: %d' % len(results))
        pass


def run():
    testcase.run_all(TestSearcher)
    pass
