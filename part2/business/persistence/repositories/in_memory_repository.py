class  InMemoryRepository:
    """In-memory resopitory implementation"""

    def __init__(self):
        """Initialize the repository"""
        self._objects = {}

    def all (self):
        """Return all objects"""
        return list  (self._objects.values())
    
    def get (self, obj_id):
        """Get obnject by id"""
        return self._objects.get(obj_id)
    
    def save (self,obj):
        """Save object"""
        self._objects[obj.id] = obj
        return obj
    
    def delete (self, obj_id):
        """Delete object by id"""
        if obj_id in self._objects:
            del self._objects[obj_id]

