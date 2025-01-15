# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftObjectOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftObjectOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftObjectOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftObjectOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftObjectOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftObjectOneSlot
    def ItemLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserCraftObjectOneSlot
    def IsUnlocked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCraftObjectOneSlot
    def IsNew(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCraftObjectOneSlot
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserCraftObjectOneSlotStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserCraftObjectOneSlotStart(builder)

def UserCraftObjectOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserCraftObjectOneSlotAddId(builder, id)

def UserCraftObjectOneSlotAddItemLabel(builder, itemLabel):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(itemLabel), 0)

def AddItemLabel(builder, itemLabel):
    UserCraftObjectOneSlotAddItemLabel(builder, itemLabel)

def UserCraftObjectOneSlotAddIsUnlocked(builder, isUnlocked):
    builder.PrependBoolSlot(2, isUnlocked, 0)

def AddIsUnlocked(builder, isUnlocked):
    UserCraftObjectOneSlotAddIsUnlocked(builder, isUnlocked)

def UserCraftObjectOneSlotAddIsNew(builder, isNew):
    builder.PrependBoolSlot(3, isNew, 0)

def AddIsNew(builder, isNew):
    UserCraftObjectOneSlotAddIsNew(builder, isNew)

def UserCraftObjectOneSlotAddLevel(builder, level):
    builder.PrependInt32Slot(4, level, 0)

def AddLevel(builder, level):
    UserCraftObjectOneSlotAddLevel(builder, level)

def UserCraftObjectOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftObjectOneSlotEnd(builder)
