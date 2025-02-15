# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserStorehouseName(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserStorehouseName()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserStorehouseName(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserStorehouseName
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserStorehouseName
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserStorehouseName
    def StorehouseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserStorehouseName
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def UserStorehouseNameStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserStorehouseNameStart(builder)

def UserStorehouseNameAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserStorehouseNameAddId(builder, id)

def UserStorehouseNameAddStorehouseId(builder, storehouseId):
    builder.PrependInt32Slot(1, storehouseId, 0)

def AddStorehouseId(builder, storehouseId):
    UserStorehouseNameAddStorehouseId(builder, storehouseId)

def UserStorehouseNameAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    UserStorehouseNameAddName(builder, name)

def UserStorehouseNameEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserStorehouseNameEnd(builder)
