from pydantic import BaseModel


class WordMeaningBase(BaseModel):
    words: str
    meaning: str
    spelling: str
    similar_spelling: str
    root_lang: str
    source: str


class WordMeaningCreate(WordMeaningBase):
    pass


class WordMeaning(WordMeaningBase):
    id: int

    class Config:
        orm_mode = True


# class IPABase(BaseModel):
#     ipa: str
#     words_id: str
#
#
# class IPACreate(IPABase):
#     pass
#
#
# class IPA(IPABase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
#
# class PosTaggerBase(BaseModel):
#     pos: str
#     words_id: str
#
#
# class PosTaggerCreate(PosTaggerBase):
#     pass
#
#
# class PosTagger(PosTaggerBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
#
# class SentenceBase(BaseModel):
#     sentence: str
#     words_id: str
#
#
# class SentenceCreate(SentenceBase):
#     pass
#
#
# class Sentence(SentenceBase):
#     id: int
#
#     class Config:
#         orm_mode = True
