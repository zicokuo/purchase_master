import dataclasses


@dataclasses
class ConstVarsDB:
    field_len_xs: int = 32
    field_len_base: int = 64
    field_len_xl: int = 128
    field_len_bool: int = 1
