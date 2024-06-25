#!/usr/bin/python3
""" python module intialization """
from models.engine.file_storage  import FileStorage
from models.base_model import Basemodel
storage = FileStorage()

storage.reload()
