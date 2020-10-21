class UserNotFoundError(Exception):
    pass

class User():
    """User representation class
    """ 
    def __init__(self, name: str = '', age: int = 0):
      self.name = name
      self.age = age
    
    def select(self) -> str:
        if self.name == 'Rogerio':
            return f'Nome: {self.name}, Idade: {self.age}'

def get_user_bad(name: str, age: int):
    """Má implementação, existe 2 retornos 
    pois se usuário nao existe vai retornar none

    :Args:
        name (str): Nome do usuário
        age (int): idade do usuário

    :Returns:
        UserType: retorna usuário
    """
    user = User(name, age).select()
    if user:
        return user


def get_user_good(name: str, age: int):
    """Boa implementacao pos utiliza boas praticas de retorno

    Args:
        name (str): Nome do usuario
        age (int): Idade do usuario

    Returns:
        UserType: retorna usuario
    """

    user = User(name, age).select()
    if not user:
        raise UserNotFoundError(f"{name} does not exist.")
    return user


get = get_user_bad('Rogerio', 10) # Corrects
get_bad_user = get_user_bad('jose', 20) # Forced error
print(get)
print(get_bad_user)
print("#" * 20)
getCorrect = get_user_good('Rogerio', 10)
getCorrect_error = get_user_good('jose', 20)
print(getCorrect)
print(getCorrect_error)