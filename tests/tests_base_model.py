#!/usr/bin/python3
""" test moduel """
import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """ unittest for the base class """
    def setUp(self):
        """set up class """
        pass

    def tearDown(self):
        """tear down class """
        pass

    def test_base(self):
        """ test Base class """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """ test id """
        self.assertEqual(type(BaseModel().id), str)
        self.assertIsNotNone(BaseModel().id)

    def test_created_t(self):
        """ test created_at attribute"""
        cr = BaseModel()
        self.assertIsNotNone(BaseModel().created_at)
        self.assertNotEqual(cr.created_at, BaseModel().created_at)

    def test_updated_t(self):
        """ test updated_at attribute"""
        up = BaseModel()
        self.assertIsNotNone(BaseModel().created_at)
        self.assertNotEqual(up.updated_at, BaseModel().updated_at)

    def test_to_dict(self):
        """ test to_dict() method for the class BaseModel """
        dic = BaseModel().to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIn("created_at", dic)
        self.assertIn("updated_at", dic)
        self.assertIn("__class__", dic)
        self.assertIn("id", dic)

    def test_save(self):
        """ test save method for the class BaseModel """
        sv = BaseModel()
        sv_n = sv.to_dict()
        sv.save()
        self.assertNotEqual(sv_n['updated_at'], sv.updated_at)
        self.assertEqual(sv_n['created_at'], sv.created_at.isoformat())
        self.assertEqual(sv_n['id'], sv.id)
        self.assertIsInstance(sv, BaseModel)

    def test_new(self):
        """ test new """
        pass
