import pymysql
import os
from dotenv import load_dotenv

# Load environment variables if not already loaded
load_dotenv()

def get_db_connection():
    """
    Create and return a connection to the MySQL database for the PharmacogeneticAppDB.
    """
    connection = pymysql.connect(
        host=os.getenv('DB_HOST', 'db'),  
        user=os.getenv('DB_USER', 'root'),  
        password=os.getenv('MYSQL_ROOT_PASSWORD', ''),  
        database=os.getenv('DB_NAME', 'PharmacogeneticAppDB'),  #
        cursorclass=pymysql.cursors.DictCursor 
    )
    return connection