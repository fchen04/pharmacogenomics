from flask import Flask
import os
from dotenv import load_dotenv

# Import blueprints for your project
from backend.doctor.doctor_routes import doctor_bp
from backend.patient.patient_routes import patient_bp
from backend.analyst.analyst_routes import analyst_bp
from backend.admin.admin_routes import admin_bp

# Load environment variables
load_dotenv()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Register blueprints for each role/persona
    app.register_blueprint(doctor_bp, url_prefix='/api/doctor')
    app.logger.info("Doctor blueprint registered")

    app.register_blueprint(patient_bp, url_prefix='/api/patient')
    app.logger.info("Patient blueprint registered")

    app.register_blueprint(analyst_bp, url_prefix='/api/analyst')
    app.logger.info("Analyst blueprint registered")

    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.logger.info("Admin blueprint registered")

    # Register optional system admin blueprint
    app.register_blueprint(admin_bp, url_prefix='/api/system_admin')
    app.logger.info("System Admin blueprint registered")
    
    # Default route
    @app.route('/')
    def index():
        return {'message': 'Welcome to the Pharmacogenetics API server!'}

    return app

if __name__ == '__main__':
    # We want to run in debug mode (for hot reloading). 
    # The app will be bound to port 4000 (this may vary depending on your Docker setup).
    # Check docker-compose.yml to see what port this might be mapped to.
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 4000)))
