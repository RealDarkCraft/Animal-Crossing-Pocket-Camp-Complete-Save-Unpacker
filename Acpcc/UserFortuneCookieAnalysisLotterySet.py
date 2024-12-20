# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFortuneCookieAnalysisLotterySet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFortuneCookieAnalysisLotterySet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFortuneCookieAnalysisLotterySet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFortuneCookieAnalysisLotterySet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFortuneCookieAnalysisLotterySet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySet
    def TotalCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserFortuneCookieAnalysisLotterySetElement import UserFortuneCookieAnalysisLotterySetElement
            obj = UserFortuneCookieAnalysisLotterySetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserFortuneCookieAnalysisLotterySet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserFortuneCookieAnalysisLotterySet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def UserFortuneCookieAnalysisLotterySetStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserFortuneCookieAnalysisLotterySetStart(builder)

def UserFortuneCookieAnalysisLotterySetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserFortuneCookieAnalysisLotterySetAddId(builder, id)

def UserFortuneCookieAnalysisLotterySetAddTotalCount(builder, totalCount):
    builder.PrependUint32Slot(1, totalCount, 0)

def AddTotalCount(builder, totalCount):
    UserFortuneCookieAnalysisLotterySetAddTotalCount(builder, totalCount)

def UserFortuneCookieAnalysisLotterySetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserFortuneCookieAnalysisLotterySetAddElements(builder, elements)

def UserFortuneCookieAnalysisLotterySetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserFortuneCookieAnalysisLotterySetStartElementsVector(builder, numElems)

def UserFortuneCookieAnalysisLotterySetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFortuneCookieAnalysisLotterySetEnd(builder)
