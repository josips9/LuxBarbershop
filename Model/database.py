from __future__ import annotations

import os
from dotenv import load_dotenv
import socket

import firebase_admin
import requests
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db


def get_connect(func, host="8.8.8.8", port=53, timeout=3):
    """Checks for an active Internet connection."""

    def wrapped(*args):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port)
            )
            return func(*args)
        except Exception:
            return False

    return wrapped


def add_barber(barber_id: object, barber: object) -> object:
    """
    Adds a new barber to the database.

    Args:
        barber_id (str): The ID of the barber.
        barber (Barber): The barber object containing the details.

    Returns:
        bool: True if the barber is added successfully, False otherwise.
    """
    try:
        # Get a reference to the "barbers" node in the database
        barbers_ref = db.reference('barbers')

        # Create a new child node with the provided barber_id
        barber_ref = barbers_ref.child(barber_id)

        # Set the barber details as the value of the child node
        barber_ref.set({
            'id': barber.id,
            'name': barber.name,
            'specialty': barber.service
        })

        return True
    except Exception as e:
        print("Error adding barber:", str(e))
        return False


def generate_id() -> object:
    """
    Generates a unique ID for a new barber in the database.
    Returns:
        str: The unique ID generated for the new barber.
    """

    # Get a reference to the "barbers" node in the database
    barbers_ref = db.reference('barbers')

    # Use push() to generate a new child node with a unique ID
    new_barber_ref = barbers_ref.push()

    # Get the generated ID from the new child node's key
    unique_id = new_barber_ref.key

    return unique_id


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    name = "Firebase"

    def __init__(self):
        load_dotenv()

        # Get the path to the service account key file
        key_file = os.path.join(os.path.dirname(__file__), 'firebase-adminsdk.json')

        # Initialize Firebase
        cred = credentials.Certificate(key_file)

        self.DATABASE_URL = os.getenv('DATABASE_URL')
        firebase_admin.initialize_app(cred, {
            'databaseURL': self.DATABASE_URL
        })

        # Address for users collections.
        self.USER_DATA = "Userdata"

        # Address for barbers collections
        self.BARBERS = "barbers"

        # RealTime Database attribute.
        self.real_time_firebase = firebase.FirebaseApplication(
            self.DATABASE_URL, None
        )

    def get_all_barbers(self) -> object:
        """
        Retrieves all barbers from the database.
        Returns a list of barbers.
        """

        barbers = self.get_data_from_collection("Barbers")

        if barbers:
            return list(barbers.values())
        else:
            return []

    @get_connect
    def get_data_from_collection(self, name_collection: str) -> dict | bool:
        """Returns data of the selected collection from the database."""

        try:
            data = self.real_time_firebase.get(
                self.DATABASE_URL, name_collection
            )
        except requests.exceptions.ConnectionError:
            return False

        return data

