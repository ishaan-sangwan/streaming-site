from rest_framework_simplejwt.tokens import AccessToken

def GetUserId(token):
    decoded = AccessToken(token)
    return decoded['user_id']