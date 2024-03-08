#!/usr/bin/python3
"""review
"""

class Review(BaseModel):
    """reveiw class added
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        super().__init__()
