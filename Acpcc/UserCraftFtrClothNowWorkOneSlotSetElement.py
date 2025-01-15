# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftFtrClothNowWorkOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftFtrClothNowWorkOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftFtrClothNowWorkOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftFtrClothNowWorkOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def CompleteDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def ItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def RecipeTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def BonusType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothNowWorkOneSlotSetElement
    def PeddlerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserCraftFtrClothNowWorkOneSlotSetElementStart(builder):
    builder.StartObject(6)

def Start(builder):
    UserCraftFtrClothNowWorkOneSlotSetElementStart(builder)

def UserCraftFtrClothNowWorkOneSlotSetElementAddCompleteDate(builder, completeDate):
    builder.PrependInt64Slot(0, completeDate, 0)

def AddCompleteDate(builder, completeDate):
    UserCraftFtrClothNowWorkOneSlotSetElementAddCompleteDate(builder, completeDate)

def UserCraftFtrClothNowWorkOneSlotSetElementAddIndex(builder, index):
    builder.PrependInt32Slot(1, index, 0)

def AddIndex(builder, index):
    UserCraftFtrClothNowWorkOneSlotSetElementAddIndex(builder, index)

def UserCraftFtrClothNowWorkOneSlotSetElementAddItemId(builder, itemId):
    builder.PrependUint32Slot(2, itemId, 0)

def AddItemId(builder, itemId):
    UserCraftFtrClothNowWorkOneSlotSetElementAddItemId(builder, itemId)

def UserCraftFtrClothNowWorkOneSlotSetElementAddRecipeTime(builder, recipeTime):
    builder.PrependInt32Slot(3, recipeTime, 0)

def AddRecipeTime(builder, recipeTime):
    UserCraftFtrClothNowWorkOneSlotSetElementAddRecipeTime(builder, recipeTime)

def UserCraftFtrClothNowWorkOneSlotSetElementAddBonusType(builder, bonusType):
    builder.PrependInt32Slot(4, bonusType, 0)

def AddBonusType(builder, bonusType):
    UserCraftFtrClothNowWorkOneSlotSetElementAddBonusType(builder, bonusType)

def UserCraftFtrClothNowWorkOneSlotSetElementAddPeddlerId(builder, peddlerId):
    builder.PrependUint32Slot(5, peddlerId, 0)

def AddPeddlerId(builder, peddlerId):
    UserCraftFtrClothNowWorkOneSlotSetElementAddPeddlerId(builder, peddlerId)

def UserCraftFtrClothNowWorkOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftFtrClothNowWorkOneSlotSetElementEnd(builder)
