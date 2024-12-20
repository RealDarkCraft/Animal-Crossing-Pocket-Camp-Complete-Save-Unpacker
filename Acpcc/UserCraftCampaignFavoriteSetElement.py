# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftCampaignFavoriteSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftCampaignFavoriteSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftCampaignFavoriteSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftCampaignFavoriteSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftCampaignFavoriteSetElement
    def ItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftCampaignFavoriteSetElement
    def CampaignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftCampaignFavoriteSetElement
    def SubType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserCraftCampaignFavoriteSetElementStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserCraftCampaignFavoriteSetElementStart(builder)

def UserCraftCampaignFavoriteSetElementAddItemId(builder, itemId):
    builder.PrependUint32Slot(0, itemId, 0)

def AddItemId(builder, itemId):
    UserCraftCampaignFavoriteSetElementAddItemId(builder, itemId)

def UserCraftCampaignFavoriteSetElementAddCampaignId(builder, campaignId):
    builder.PrependUint32Slot(1, campaignId, 0)

def AddCampaignId(builder, campaignId):
    UserCraftCampaignFavoriteSetElementAddCampaignId(builder, campaignId)

def UserCraftCampaignFavoriteSetElementAddSubType(builder, subType):
    builder.PrependInt32Slot(2, subType, 0)

def AddSubType(builder, subType):
    UserCraftCampaignFavoriteSetElementAddSubType(builder, subType)

def UserCraftCampaignFavoriteSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftCampaignFavoriteSetElementEnd(builder)
