from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base model class."""

    def __init__(self, *args, **kwargs):
        """Initialize the model."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        for key, value in kwargs.items():
            setattr(self, key, value)

            def to_dict(self):
                """Return dictionary representation"""
                return {
                    'id': self.id,
                    'created_at': self.created_at.isoformat(),
                    'updated_at': self.updated_at.isoformat()
                }
