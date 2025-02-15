# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserGulliverShip(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserGulliverShip()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserGulliverShip(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserGulliverShip
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserGulliverShip
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserGulliverShip
    def Progress(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserGulliverShip
    def NormalDestinationUpdateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserGulliverShip
    def NormalDestinationIdList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserGulliverShip
    def NormalDestinationIdListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserGulliverShip
    def NormalDestinationIdListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserGulliverShip
    def NormalDestinationIdListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # UserGulliverShip
    def HighlightRefreshEndedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserGulliverShip
    def IsSeenNewDestination(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserGulliverShipStart(builder):
    builder.StartObject(6)

def Start(builder):
    UserGulliverShipStart(builder)

def UserGulliverShipAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserGulliverShipAddId(builder, id)

def UserGulliverShipAddProgress(builder, progress):
    builder.PrependUint8Slot(1, progress, 0)

def AddProgress(builder, progress):
    UserGulliverShipAddProgress(builder, progress)

def UserGulliverShipAddNormalDestinationUpdateTime(builder, normalDestinationUpdateTime):
    builder.PrependInt64Slot(2, normalDestinationUpdateTime, 0)

def AddNormalDestinationUpdateTime(builder, normalDestinationUpdateTime):
    UserGulliverShipAddNormalDestinationUpdateTime(builder, normalDestinationUpdateTime)

def UserGulliverShipAddNormalDestinationIdList(builder, normalDestinationIdList):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(normalDestinationIdList), 0)

def AddNormalDestinationIdList(builder, normalDestinationIdList):
    UserGulliverShipAddNormalDestinationIdList(builder, normalDestinationIdList)

def UserGulliverShipStartNormalDestinationIdListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartNormalDestinationIdListVector(builder, numElems):
    return UserGulliverShipStartNormalDestinationIdListVector(builder, numElems)

def UserGulliverShipAddHighlightRefreshEndedAt(builder, highlightRefreshEndedAt):
    builder.PrependInt64Slot(4, highlightRefreshEndedAt, 0)

def AddHighlightRefreshEndedAt(builder, highlightRefreshEndedAt):
    UserGulliverShipAddHighlightRefreshEndedAt(builder, highlightRefreshEndedAt)

def UserGulliverShipAddIsSeenNewDestination(builder, isSeenNewDestination):
    builder.PrependBoolSlot(5, isSeenNewDestination, 0)

def AddIsSeenNewDestination(builder, isSeenNewDestination):
    UserGulliverShipAddIsSeenNewDestination(builder, isSeenNewDestination)

def UserGulliverShipEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserGulliverShipEnd(builder)
