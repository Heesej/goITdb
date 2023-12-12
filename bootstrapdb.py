from faker import Faker
from models import Base, User
from session import Session


def main():
    Base.metadata.create_all()

    session = Session()

    fake = Faker()
    for _ in range(10):
        user = User(
            username=fake.user_name(),
            email=fake.email()
        )
        session.add(user)
    session.commit()

    query = session.query(User)
    for user in query.all():
        user.username = user.username.title()
        session.add(user)
        print(user)
    
    bob = session.query(User).filter_by(username="Bob").first()
    if bob is not None:
        bob.username = "John"
        session.add(bob)
    
    sam = session.query(User).filter_by(username="Sam").first()
    if sam is not None:
        session.delete(sam)
    
    session.commit()


if __name__ == "__main__":
    main()
