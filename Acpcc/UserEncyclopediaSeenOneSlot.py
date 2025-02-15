# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserEncyclopediaSeenOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserEncyclopediaSeenOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserEncyclopediaSeenOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserEncyclopediaSeenOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserEncyclopediaSeenOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserEncyclopediaSeenOneSlot
    def KeyName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserEncyclopediaSeenOneSlot
    def IsCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserEncyclopediaSeenOneSlot
    def KeyId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserEncyclopediaSeenOneSlotStart(builder):
    builder.StartObject(4)

def Start(builder):
    UserEncyclopediaSeenOneSlotStart(builder)

def UserEncyclopediaSeenOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserEncyclopediaSeenOneSlotAddId(builder, id)

def UserEncyclopediaSeenOneSlotAddKeyName(builder, keyName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(keyName), 0)

def AddKeyName(builder, keyName):
    UserEncyclopediaSeenOneSlotAddKeyName(builder, keyName)

def UserEncyclopediaSeenOneSlotAddIsCheck(builder, isCheck):
    builder.PrependBoolSlot(2, isCheck, 0)

def AddIsCheck(builder, isCheck):
    UserEncyclopediaSeenOneSlotAddIsCheck(builder, isCheck)

def UserEncyclopediaSeenOneSlotAddKeyId(builder, keyId):
    builder.PrependUint32Slot(3, keyId, 0)

def AddKeyId(builder, keyId):
    UserEncyclopediaSeenOneSlotAddKeyId(builder, keyId)

def UserEncyclopediaSeenOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserEncyclopediaSeenOneSlotEnd(builder)
