# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserFortuneCookieAnalysisLotterySetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserFortuneCookieAnalysisLotterySetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserFortuneCookieAnalysisLotterySetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserFortuneCookieAnalysisLotterySetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserFortuneCookieAnalysisLotterySetElement
    def SerialNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def ItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def ItemAppearanceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def BonusId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def Purchase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def Route(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # UserFortuneCookieAnalysisLotterySetElement
    def Time(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserFortuneCookieAnalysisLotterySetElementStart(builder):
    builder.StartObject(7)

def Start(builder):
    UserFortuneCookieAnalysisLotterySetElementStart(builder)

def UserFortuneCookieAnalysisLotterySetElementAddSerialNumber(builder, serialNumber):
    builder.PrependUint32Slot(0, serialNumber, 0)

def AddSerialNumber(builder, serialNumber):
    UserFortuneCookieAnalysisLotterySetElementAddSerialNumber(builder, serialNumber)

def UserFortuneCookieAnalysisLotterySetElementAddItemId(builder, itemId):
    builder.PrependUint32Slot(1, itemId, 0)

def AddItemId(builder, itemId):
    UserFortuneCookieAnalysisLotterySetElementAddItemId(builder, itemId)

def UserFortuneCookieAnalysisLotterySetElementAddItemAppearanceId(builder, itemAppearanceId):
    builder.PrependUint32Slot(2, itemAppearanceId, 0)

def AddItemAppearanceId(builder, itemAppearanceId):
    UserFortuneCookieAnalysisLotterySetElementAddItemAppearanceId(builder, itemAppearanceId)

def UserFortuneCookieAnalysisLotterySetElementAddBonusId(builder, bonusId):
    builder.PrependUint32Slot(3, bonusId, 0)

def AddBonusId(builder, bonusId):
    UserFortuneCookieAnalysisLotterySetElementAddBonusId(builder, bonusId)

def UserFortuneCookieAnalysisLotterySetElementAddPurchase(builder, purchase):
    builder.PrependUint8Slot(4, purchase, 0)

def AddPurchase(builder, purchase):
    UserFortuneCookieAnalysisLotterySetElementAddPurchase(builder, purchase)

def UserFortuneCookieAnalysisLotterySetElementAddRoute(builder, route):
    builder.PrependInt16Slot(5, route, 0)

def AddRoute(builder, route):
    UserFortuneCookieAnalysisLotterySetElementAddRoute(builder, route)

def UserFortuneCookieAnalysisLotterySetElementAddTime(builder, time):
    builder.PrependInt64Slot(6, time, 0)

def AddTime(builder, time):
    UserFortuneCookieAnalysisLotterySetElementAddTime(builder, time)

def UserFortuneCookieAnalysisLotterySetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserFortuneCookieAnalysisLotterySetElementEnd(builder)
