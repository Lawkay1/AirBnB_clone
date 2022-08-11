#!/usr/bin/python3
"test file base model"


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os


class TestAirbnbProjects(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del(self.model)
        if os.path.exists("file.json"):
            os.remove("file.json")
        models.storage.reset()
        return super().tearDown()

    def test_create_istance(self):
        """case init instance"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        self.model.save()

        file = 'file.json'
        with open(file, mode="r+", encoding="utf-8") as f:
            file_string = f.read()
            data = json.loads(file_string)

        self.assertTrue(
                '{}.{}'.format(type(self.model).__name__, self.model.id) in data
            )

        self.assertDictEqual(
            self.model.to_dict(),
            data['{}.{}'.format(type(self.model).__name__, self.model.id)]
            )

    def test_assign_attribute(self):
        """ new attribute"""
        self.model.name = "John"
        self.model.my_number = 89
        self.assertIs(self.model.name, "John")
