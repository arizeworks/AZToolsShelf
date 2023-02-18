# pyright: reportShadowedImports=false
import bpy

from .Operators import operator_shelf

operatorclasses = ()
operatorclasses += operator_shelf.shelfclasses