# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCottageFurnitureOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCottageFurnitureOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCottageFurnitureOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCottageFurnitureOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCottageFurnitureOneSlotSetElement
    def CottageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def Floor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def PosX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def PosY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def PosZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def RotY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCottageFurnitureOneSlotSetElement
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserCottageFurnitureOneSlotSetElement
    def Guid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserCottageFurnitureOneSlotSetElement
    def Swicth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserCottageFurnitureOneSlotSetElementStart(builder):
    builder.StartObject(9)

def Start(builder):
    UserCottageFurnitureOneSlotSetElementStart(builder)

def UserCottageFurnitureOneSlotSetElementAddCottageId(builder, cottageId):
    builder.PrependInt32Slot(0, cottageId, 0)

def AddCottageId(builder, cottageId):
    UserCottageFurnitureOneSlotSetElementAddCottageId(builder, cottageId)

def UserCottageFurnitureOneSlotSetElementAddFloor(builder, floor):
    builder.PrependInt32Slot(1, floor, 0)

def AddFloor(builder, floor):
    UserCottageFurnitureOneSlotSetElementAddFloor(builder, floor)

def UserCottageFurnitureOneSlotSetElementAddPosX(builder, posX):
    builder.PrependInt32Slot(2, posX, 0)

def AddPosX(builder, posX):
    UserCottageFurnitureOneSlotSetElementAddPosX(builder, posX)

def UserCottageFurnitureOneSlotSetElementAddPosY(builder, posY):
    builder.PrependInt32Slot(3, posY, 0)

def AddPosY(builder, posY):
    UserCottageFurnitureOneSlotSetElementAddPosY(builder, posY)

def UserCottageFurnitureOneSlotSetElementAddPosZ(builder, posZ):
    builder.PrependInt32Slot(4, posZ, 0)

def AddPosZ(builder, posZ):
    UserCottageFurnitureOneSlotSetElementAddPosZ(builder, posZ)

def UserCottageFurnitureOneSlotSetElementAddRotY(builder, rotY):
    builder.PrependInt32Slot(5, rotY, 0)

def AddRotY(builder, rotY):
    UserCottageFurnitureOneSlotSetElementAddRotY(builder, rotY)

def UserCottageFurnitureOneSlotSetElementAddLabel(builder, label):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)

def AddLabel(builder, label):
    UserCottageFurnitureOneSlotSetElementAddLabel(builder, label)

def UserCottageFurnitureOneSlotSetElementAddGuid(builder, guid):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(guid), 0)

def AddGuid(builder, guid):
    UserCottageFurnitureOneSlotSetElementAddGuid(builder, guid)

def UserCottageFurnitureOneSlotSetElementAddSwicth(builder, swicth):
    builder.PrependBoolSlot(8, swicth, 0)

def AddSwicth(builder, swicth):
    UserCottageFurnitureOneSlotSetElementAddSwicth(builder, swicth)

def UserCottageFurnitureOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCottageFurnitureOneSlotSetElementEnd(builder)
