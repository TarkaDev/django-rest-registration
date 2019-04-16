from django.dispatch import Signal

verified_account = Signal(providing_args=['user'])
verified_account.__doc__ = """
This signal should be called when user has succesfully verified (e.g. he activated account via e-mail activation).
"""
