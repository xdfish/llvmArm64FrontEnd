from enum import Enum
from source.irtypes import linkage_types


a: linkage_types = linkage_types.external

print(type(a.value))