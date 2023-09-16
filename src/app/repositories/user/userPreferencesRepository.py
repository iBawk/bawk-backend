from sqlalchemy.orm import Session

from db.models import UserPreferencesModel


class UserPreferencesRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user_preferences(self, userPreferences):
        try:
            self.db.add(userPreferences)
            self.db.commit()
            self.db.refresh(userPreferences)

            return userPreferences
        except Exception as e:
            print(e)
            raise e

    def get_user_preferences(self, id: str):
        try:
            userPreferences = self.db.query(UserPreferencesModel).filter(
                UserPreferencesModel.id == id).first()
            return userPreferences
        except Exception as e:
            print(e)
            raise e
