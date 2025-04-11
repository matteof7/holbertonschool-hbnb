from app import create_app, db
from app.models.user import User
from app.extensions import bcrypt
import sqlalchemy

app = create_app()

with app.app_context():
    try:
        # Supprimer l'utilisateur s'il existe déjà
        db.session.query(User).filter_by(email="admin@hbnb.io").delete()
        db.session.commit()
        
        # Créer un admin en laissant le modèle gérer le hachage
        admin = User(
            first_name="Admin",
            last_name="User",
            email="admin@hbnb.io",
            password="admin123",  # Le modèle hashe lui-même
            is_admin=True
        )
        
        db.session.add(admin)
        db.session.commit()
        
        # Vérifier que l'utilisateur a été créé
        user_check = db.session.query(User).filter_by(email="admin@hbnb.io").first()
        if user_check:
            print(f"Utilisateur admin créé avec succès: {user_check.email}")
            # Essayer la vérification du mot de passe
            test_password = "admin123"
            # Vérifier avec bcrypt directement
            password_matches = bcrypt.check_password_hash(user_check.password, test_password)
            print(f"Vérification du mot de passe avec bcrypt: {'Succès' if password_matches else 'Échec'}")
            
            # Essayer également avec la méthode du modèle si elle existe
            if hasattr(user_check, 'check_password'):
                model_check = user_check.check_password(test_password)
                print(f"Vérification avec la méthode du modèle: {'Succès' if model_check else 'Échec'}")
        else:
            print("ERREUR: L'utilisateur n'a pas été créé correctement")
    
    except Exception as e:
        print(f"Erreur: {e}")
        db.session.rollback()