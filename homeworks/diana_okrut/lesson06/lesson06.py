# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __eq__(self, other):
#         return self.email == other.email


# class UserForm(User):
#     def validate_name(self):
#         try:
#             a = 'qwertyuiopasdfghjklzxcvbnm_'
#             b = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
#             c = 'qwertyuiopasdfghjklzxcvbnm0123456789_.'
#             if self.name[0] not in a:
#             elif self.name[-1] not in b:
#                 return ValueError
#             for x in self.name[1:-1]:
#                 if x not in c:
#                     return ValueError
#
#     def validate_email(self):
#         a = 'qwertyuiopasdfghjklzxcvbnm_'
#         b = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
#         c = 'qwertyuiopasdfghjklzxcvbnm0123456789_.'
#         d = 'qwertyuiopasdfghjklzxcvbnm0123456789_+.'
#         try:
#             lisemail = self.email.split("@")
#             login = lisemail[0]
#             domain = lisemail[1]
#             if login[0] not in a:
#                 return ValueError
#             if login[-1] not in b:
#                 return ValueError
#             for x in login[1,-1]:
#                 if x not in d:
#                     return ValueError
#
#             if domain[0] not in a:
#                 return ValueError
#             if domain[-1] not in b:
#                 return ValueError
#             for x in domain[1, -1]:
#                 if x not in c:
#                     return ValueError
