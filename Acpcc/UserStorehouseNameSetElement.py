# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserStorehouseNameSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserStorehouseNameSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserStorehouseNameSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserStorehouseNameSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserStorehouseNameSetElement
    def StorehouseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserStorehouseNameSetElement
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def UserStorehouseNameSetElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserStorehouseNameSetElementStart(builder)

def UserStorehouseNameSetElementAddStorehouseId(builder, storehouseId):
    builder.PrependInt32Slot(0, storehouseId, 0)

def AddStorehouseId(builder, storehouseId):
    UserStorehouseNameSetElementAddStorehouseId(builder, storehouseId)

def UserStorehouseNameSetElementAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    UserStorehouseNameSetElementAddName(builder, name)

def UserStorehouseNameSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserStorehouseNameSetElementEnd(builder)
