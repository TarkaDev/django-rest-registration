from django.dispatch import Signal

account_verified = Signal(providing_args=['user'])
account_verified.__doc__ = """
This signal should be called when user has succesfully verified (e.g. he activated account via e-mail activation).
"""
