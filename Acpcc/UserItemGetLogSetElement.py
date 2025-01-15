# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserItemGetLogSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserItemGetLogSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserItemGetLogSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserItemGetLogSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserItemGetLogSetElement
    def DateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserItemGetLogSetElement
    def RouteId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserItemGetLogSetElement
    def ItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserItemGetLogSetElement
    def Amount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserItemGetLogSetElement
    def OptionData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserItemGetLogSetElement
    def ItemType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserItemGetLogSetElementStart(builder):
    builder.StartObject(6)

def Start(builder):
    UserItemGetLogSetElementStart(builder)

def UserItemGetLogSetElementAddDateTime(builder, dateTime):
    builder.PrependInt64Slot(0, dateTime, 0)

def AddDateTime(builder, dateTime):
    UserItemGetLogSetElementAddDateTime(builder, dateTime)

def UserItemGetLogSetElementAddRouteId(builder, routeId):
    builder.PrependInt32Slot(1, routeId, 0)

def AddRouteId(builder, routeId):
    UserItemGetLogSetElementAddRouteId(builder, routeId)

def UserItemGetLogSetElementAddItemId(builder, itemId):
    builder.PrependUint32Slot(2, itemId, 0)

def AddItemId(builder, itemId):
    UserItemGetLogSetElementAddItemId(builder, itemId)

def UserItemGetLogSetElementAddAmount(builder, amount):
    builder.PrependInt32Slot(3, amount, 0)

def AddAmount(builder, amount):
    UserItemGetLogSetElementAddAmount(builder, amount)

def UserItemGetLogSetElementAddOptionData(builder, optionData):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(optionData), 0)

def AddOptionData(builder, optionData):
    UserItemGetLogSetElementAddOptionData(builder, optionData)

def UserItemGetLogSetElementAddItemType(builder, itemType):
    builder.PrependInt32Slot(5, itemType, 0)

def AddItemType(builder, itemType):
    UserItemGetLogSetElementAddItemType(builder, itemType)

def UserItemGetLogSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserItemGetLogSetElementEnd(builder)
