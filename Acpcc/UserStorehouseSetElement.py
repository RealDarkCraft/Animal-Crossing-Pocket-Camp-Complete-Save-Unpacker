# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserStorehouseSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserStorehouseSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserStorehouseSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserStorehouseSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserStorehouseSetElement
    def ItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserStorehouseSetElement
    def Quantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserStorehouseSetElement
    def StorehouseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserStorehouseSetElementStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserStorehouseSetElementStart(builder)

def UserStorehouseSetElementAddItemId(builder, itemId):
    builder.PrependUint32Slot(0, itemId, 0)

def AddItemId(builder, itemId):
    UserStorehouseSetElementAddItemId(builder, itemId)

def UserStorehouseSetElementAddQuantity(builder, quantity):
    builder.PrependInt32Slot(1, quantity, 0)

def AddQuantity(builder, quantity):
    UserStorehouseSetElementAddQuantity(builder, quantity)

def UserStorehouseSetElementAddStorehouseId(builder, storehouseId):
    builder.PrependInt32Slot(2, storehouseId, 0)

def AddStorehouseId(builder, storehouseId):
    UserStorehouseSetElementAddStorehouseId(builder, storehouseId)

def UserStorehouseSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserStorehouseSetElementEnd(builder)
