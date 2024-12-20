# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserPaymentRecommendData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserPaymentRecommendData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserPaymentRecommendData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserPaymentRecommendData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserPaymentRecommendData
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserPaymentRecommendData
    def ShowCountToday(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def UserPaymentRecommendDataStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserPaymentRecommendDataStart(builder)

def UserPaymentRecommendDataAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserPaymentRecommendDataAddId(builder, id)

def UserPaymentRecommendDataAddShowCountToday(builder, showCountToday):
    builder.PrependUint8Slot(1, showCountToday, 0)

def AddShowCountToday(builder, showCountToday):
    UserPaymentRecommendDataAddShowCountToday(builder, showCountToday)

def UserPaymentRecommendDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserPaymentRecommendDataEnd(builder)
