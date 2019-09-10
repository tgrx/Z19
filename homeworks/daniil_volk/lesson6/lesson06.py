class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        if type(self) == type(other):
            return self.email == other.email
        else:
            raise TypeError


# class UserForm(User):
#     def validate_name(self):
#         if isinstance(self.name[0], int):
#             return ValueError
#         if self.name[0] == '.' or self.name[-1] == '.':
#             return ValueError
#         a = (not any(c.islower() for c in self.name))
#         b = (not self.name.isnumeric())
#         c = (self.name != '_')
#         d = ('.' not in self.name)
#         if a and b and c and d:
#             return ValueError
#
#     def validate_email(self):
#         em = self.email.split("@")
#         log = em[0]
#         dom = em[1]
#
#         if log[0] == '+' or log[-1] == '+':
#             return ValueError
#         if isinstance(log[0], int):
#             return ValueError
#         if log[0] == '.' or log[-1] == '.':
#             return ValueError
#         a = (not any(c.islower() for c in log))
#         b = (not log.isnumeric())
#         c = (log != '_')
#         d = ('.' not in log)
#         e = ('+' not in log)
#         if a and b and c and d and e:
#             return ValueError
#
#         if isinstance(dom[0], int):
#             return ValueError
#         if dom[0] == '.' or dom[-1] == '.':
#             return ValueError
#         a = (not any(c.islower() for c in dom))
#         b = (not dom.isnumeric())
#         c = (dom != '_')
#         d = ('.' not in dom)
#         if a and b and c and d:
#             return ValueError
