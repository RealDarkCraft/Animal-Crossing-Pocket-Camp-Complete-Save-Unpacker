# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserTapEventSpFurnitureNpcTalkParam(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserTapEventSpFurnitureNpcTalkParam()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserTapEventSpFurnitureNpcTalkParam(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserTapEventSpFurnitureNpcTalkParam
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserTapEventSpFurnitureNpcTalkParam
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventSpFurnitureNpcTalkParam
    def NpcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserTapEventSpFurnitureNpcTalkParam
    def LongParam01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserTapEventSpFurnitureNpcTalkParamStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserTapEventSpFurnitureNpcTalkParamStart(builder)

def UserTapEventSpFurnitureNpcTalkParamAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserTapEventSpFurnitureNpcTalkParamAddId(builder, id)

def UserTapEventSpFurnitureNpcTalkParamAddNpcId(builder, npcId):
    builder.PrependUint32Slot(1, npcId, 0)

def AddNpcId(builder, npcId):
    UserTapEventSpFurnitureNpcTalkParamAddNpcId(builder, npcId)

def UserTapEventSpFurnitureNpcTalkParamAddLongParam01(builder, longParam01):
    builder.PrependInt64Slot(2, longParam01, 0)

def AddLongParam01(builder, longParam01):
    UserTapEventSpFurnitureNpcTalkParamAddLongParam01(builder, longParam01)

def UserTapEventSpFurnitureNpcTalkParamEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserTapEventSpFurnitureNpcTalkParamEnd(builder)
