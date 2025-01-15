# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserGardeningQuestProgress(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserGardeningQuestProgress()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserGardeningQuestProgress(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserGardeningQuestProgress
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserGardeningQuestProgress
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserGardeningQuestProgress
    def QuestInfoId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserGardeningQuestProgress
    def Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def UserGardeningQuestProgressStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserGardeningQuestProgressStart(builder)

def UserGardeningQuestProgressAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserGardeningQuestProgressAddId(builder, id)

def UserGardeningQuestProgressAddQuestInfoId(builder, questInfoId):
    builder.PrependUint32Slot(1, questInfoId, 0)

def AddQuestInfoId(builder, questInfoId):
    UserGardeningQuestProgressAddQuestInfoId(builder, questInfoId)

def UserGardeningQuestProgressAddCount(builder, count):
    builder.PrependInt16Slot(2, count, 0)

def AddCount(builder, count):
    UserGardeningQuestProgressAddCount(builder, count)

def UserGardeningQuestProgressEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserGardeningQuestProgressEnd(builder)
