# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserActivityEventSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserActivityEventSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserActivityEventSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserActivityEventSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserActivityEventSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def CampaignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def Progress(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def GetCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def TotalPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def SetToolItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def RewardGetList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserActivityEventSlot
    def RewardGetListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserActivityEventSlot
    def RewardGetListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserActivityEventSlot
    def RewardGetListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # UserActivityEventSlot
    def KeepCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def KeepPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserActivityEventSlot
    def KeepItemIdList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserActivityEventSlot
    def KeepItemIdListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserActivityEventSlot
    def KeepItemIdListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserActivityEventSlot
    def KeepItemIdListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # UserActivityEventSlot
    def DeleteItemIdList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserActivityEventSlot
    def DeleteItemIdListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserActivityEventSlot
    def DeleteItemIdListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserActivityEventSlot
    def DeleteItemIdListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # UserActivityEventSlot
    def MatItemIdList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserActivityEventSlot
    def MatItemIdListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserActivityEventSlot
    def MatItemIdListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserActivityEventSlot
    def MatItemIdListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

def UserActivityEventSlotStart(builder):
    builder.StartObject(12)

def Start(builder):
    UserActivityEventSlotStart(builder)

def UserActivityEventSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserActivityEventSlotAddId(builder, id)

def UserActivityEventSlotAddCampaignId(builder, campaignId):
    builder.PrependUint32Slot(1, campaignId, 0)

def AddCampaignId(builder, campaignId):
    UserActivityEventSlotAddCampaignId(builder, campaignId)

def UserActivityEventSlotAddProgress(builder, progress):
    builder.PrependInt32Slot(2, progress, 0)

def AddProgress(builder, progress):
    UserActivityEventSlotAddProgress(builder, progress)

def UserActivityEventSlotAddGetCount(builder, getCount):
    builder.PrependInt32Slot(3, getCount, 0)

def AddGetCount(builder, getCount):
    UserActivityEventSlotAddGetCount(builder, getCount)

def UserActivityEventSlotAddTotalPoint(builder, totalPoint):
    builder.PrependInt64Slot(4, totalPoint, 0)

def AddTotalPoint(builder, totalPoint):
    UserActivityEventSlotAddTotalPoint(builder, totalPoint)

def UserActivityEventSlotAddSetToolItemId(builder, setToolItemId):
    builder.PrependUint32Slot(5, setToolItemId, 0)

def AddSetToolItemId(builder, setToolItemId):
    UserActivityEventSlotAddSetToolItemId(builder, setToolItemId)

def UserActivityEventSlotAddRewardGetList(builder, rewardGetList):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(rewardGetList), 0)

def AddRewardGetList(builder, rewardGetList):
    UserActivityEventSlotAddRewardGetList(builder, rewardGetList)

def UserActivityEventSlotStartRewardGetListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartRewardGetListVector(builder, numElems):
    return UserActivityEventSlotStartRewardGetListVector(builder, numElems)

def UserActivityEventSlotAddKeepCount(builder, keepCount):
    builder.PrependInt32Slot(7, keepCount, 0)

def AddKeepCount(builder, keepCount):
    UserActivityEventSlotAddKeepCount(builder, keepCount)

def UserActivityEventSlotAddKeepPoint(builder, keepPoint):
    builder.PrependInt64Slot(8, keepPoint, 0)

def AddKeepPoint(builder, keepPoint):
    UserActivityEventSlotAddKeepPoint(builder, keepPoint)

def UserActivityEventSlotAddKeepItemIdList(builder, keepItemIdList):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(keepItemIdList), 0)

def AddKeepItemIdList(builder, keepItemIdList):
    UserActivityEventSlotAddKeepItemIdList(builder, keepItemIdList)

def UserActivityEventSlotStartKeepItemIdListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartKeepItemIdListVector(builder, numElems):
    return UserActivityEventSlotStartKeepItemIdListVector(builder, numElems)

def UserActivityEventSlotAddDeleteItemIdList(builder, deleteItemIdList):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(deleteItemIdList), 0)

def AddDeleteItemIdList(builder, deleteItemIdList):
    UserActivityEventSlotAddDeleteItemIdList(builder, deleteItemIdList)

def UserActivityEventSlotStartDeleteItemIdListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartDeleteItemIdListVector(builder, numElems):
    return UserActivityEventSlotStartDeleteItemIdListVector(builder, numElems)

def UserActivityEventSlotAddMatItemIdList(builder, matItemIdList):
    builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(matItemIdList), 0)

def AddMatItemIdList(builder, matItemIdList):
    UserActivityEventSlotAddMatItemIdList(builder, matItemIdList)

def UserActivityEventSlotStartMatItemIdListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMatItemIdListVector(builder, numElems):
    return UserActivityEventSlotStartMatItemIdListVector(builder, numElems)

def UserActivityEventSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserActivityEventSlotEnd(builder)
