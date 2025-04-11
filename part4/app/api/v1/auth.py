from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
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
        
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])
        
        if user:
            print(f"Utilisateur trouvé: {user.email}")
            print(f"Méthodes disponibles : {dir(user)}")
            # Trouvez la méthode qui commence par 'check_' ou 'verify_'
            print(f"Tentative de vérification du mot de passe")
            password_correct = user.verify_password(credentials['password'])
            print(f"Mot de passe correct: {password_correct}")
        else:
            print(f"Aucun utilisateur trouvé avec cet email")
            
        # Step 2: Check if the user exists and the password is correct
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        # Step 3: Create a JWT token with the user's id as identity
        # and is_admin as additional claim
        access_token = create_access_token(
            identity=str(user.id),  # L'identité doit être une chaîne
            additional_claims={'is_admin': user.is_admin}  # Ajoutez is_admin comme claim additionnel
        )
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200