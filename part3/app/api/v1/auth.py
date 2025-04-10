from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Modèle de requête pour la connexion
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload
        
        print(f"Tentative de connexion avec email: {credentials['email']}")
        
        # Vérifier si l'utilisateur existe
        user = facade.get_user_by_email(credentials['email'])
        
        if not user:
            print(f"Aucun utilisateur trouvé avec l'email: {credentials['email']}")
            return {'error': 'Invalid credentials'}, 401
            
        print(f"Utilisateur trouvé: {user.email}, vérification du mot de passe...")
        
        if not user.verify_password(credentials['password']):
            print(f"Mot de passe incorrect pour: {user.email}")
            return {'error': 'Invalid credentials'}, 401
            
        print(f"Authentification réussie pour: {user.email}")
        
        # Générer un token JWT
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        return {'access_token': access_token}, 200
