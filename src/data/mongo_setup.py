import mongoengine


def mongo_setup():
    mongoengine.register_connection(
        alias='core',
        name="Gateru_Bank"

    )
