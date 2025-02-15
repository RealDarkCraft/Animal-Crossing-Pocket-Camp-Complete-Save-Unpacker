# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserOmakaseLayoutData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserOmakaseLayoutData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserOmakaseLayoutData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserOmakaseLayoutData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserOmakaseLayoutData
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOmakaseLayoutData
    def LayoutRecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOmakaseLayoutData
    def LayoutRecipeCampaignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserOmakaseLayoutData
    def RecommendFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserOmakaseLayoutData
    def MoyougaeNotificationFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserOmakaseLayoutData
    def TutorialNotificationFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserOmakaseLayoutData
    def PutNotificationFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def UserOmakaseLayoutDataStart(builder):
    builder.StartObject(7)

def Start(builder):
    UserOmakaseLayoutDataStart(builder)

def UserOmakaseLayoutDataAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserOmakaseLayoutDataAddId(builder, id)

def UserOmakaseLayoutDataAddLayoutRecipeId(builder, layoutRecipeId):
    builder.PrependUint32Slot(1, layoutRecipeId, 0)

def AddLayoutRecipeId(builder, layoutRecipeId):
    UserOmakaseLayoutDataAddLayoutRecipeId(builder, layoutRecipeId)

def UserOmakaseLayoutDataAddLayoutRecipeCampaignId(builder, layoutRecipeCampaignId):
    builder.PrependUint32Slot(2, layoutRecipeCampaignId, 0)

def AddLayoutRecipeCampaignId(builder, layoutRecipeCampaignId):
    UserOmakaseLayoutDataAddLayoutRecipeCampaignId(builder, layoutRecipeCampaignId)

def UserOmakaseLayoutDataAddRecommendFlag(builder, recommendFlag):
    builder.PrependBoolSlot(3, recommendFlag, 0)

def AddRecommendFlag(builder, recommendFlag):
    UserOmakaseLayoutDataAddRecommendFlag(builder, recommendFlag)

def UserOmakaseLayoutDataAddMoyougaeNotificationFlag(builder, moyougaeNotificationFlag):
    builder.PrependBoolSlot(4, moyougaeNotificationFlag, 0)

def AddMoyougaeNotificationFlag(builder, moyougaeNotificationFlag):
    UserOmakaseLayoutDataAddMoyougaeNotificationFlag(builder, moyougaeNotificationFlag)

def UserOmakaseLayoutDataAddTutorialNotificationFlag(builder, tutorialNotificationFlag):
    builder.PrependBoolSlot(5, tutorialNotificationFlag, 0)

def AddTutorialNotificationFlag(builder, tutorialNotificationFlag):
    UserOmakaseLayoutDataAddTutorialNotificationFlag(builder, tutorialNotificationFlag)

def UserOmakaseLayoutDataAddPutNotificationFlag(builder, putNotificationFlag):
    builder.PrependBoolSlot(6, putNotificationFlag, 0)

def AddPutNotificationFlag(builder, putNotificationFlag):
    UserOmakaseLayoutDataAddPutNotificationFlag(builder, putNotificationFlag)

def UserOmakaseLayoutDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserOmakaseLayoutDataEnd(builder)
