from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        """Initializes base model with common attributes"""
    self.id = str(uuid.uuid4())
    self.created_at = datetime.utcnow()
    self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Convert instance to dictionary"""
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
    
    def update(self, data):
        """Update instance attributes"""
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
