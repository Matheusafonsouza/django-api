def validate_cpf(cpf):
    """
    Method for validate cpf conditions.
    :param cpf: Client instance cpf
    :returnts: The true if validation is ok or false if validation fails
    """
    return len(cpf) == 11


def validate_rg(rg):
    """
    Method for validate rg conditions.
    :param rg: Client instance rg
    :returnts: The true if validation is ok or false if validation fails
    """
    return len(rg) == 9


def validate_phone(phone):
    """
    Method for validate phone conditions.
    :param phone: Client instance phone
    :returnts: The true if validation is ok or false if validation fails
    """
    return len(phone) == 11


def validate_name(name):
    """
    Method for validate name conditions.
    :param name: Client instance name
    :returnts: The true if validation is ok or false if validation fails
    """
    return name.isalpha()
