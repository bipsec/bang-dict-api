from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WordMeaning(Base):
    __tablename__ = "word_meaning"

    id = Column(Integer, primary_key=True, index=True)
    pageNo = Column(String, unique=True, index=True)
    words = Column(String, unique=True, index=True)
    number = Column(String, unique=True, index=True)
    spelling = Column(String, index=True)
    meaning = Column(String, index=True)
    pos = Column(String, unique=True, index=True)
    ipa = Column(String, unique=True, index=True)
    root_lang = Column(String, index=True)
    type = Column(String, unique=True, index=True)
    sentence = Column(String, unique=True, index=True)
    source = Column(String, index=True)

#     ipa = relationship("IPA", back_populates="word_meaning")
#     sentences = relationship("Sentence", back_populates="word_meaning")
#     pos_taggers = relationship("PosTagger", back_populates="word_meaning")
#
#
# class IPA(Base):
#     __tablename__ = "ipa"
#
#     id = Column(Integer, primary_key=True, index=True)
#     ipa = Column(String, index=True)
#     words_id = Column(String, ForeignKey("word_meaning.words"))
#
#     word_meaning = relationship("WordMeaning", back_populates="ipa")
#
#
# class PosTagger(Base):
#     __tablename__ = "parts_of_speech"
#
#     id = Column(Integer, primary_key=True, index=True)
#     pos = Column(String, index=True)
#     words_id = Column(String, ForeignKey('word_meaning.words'))
#
#     word_meaning = relationship("WordMeaning", back_populates="pos_taggers")
#
#
# class Sentence(Base):
#     __tablename__ = "sentence"
#
#     id = Column(Integer, primary_key=True, index=True)
#     sentence = Column(String, index=True)
#     words_id = Column(String, ForeignKey("word_meaning.words"))
#
#     word_meaning = relationship("WordMeaning", back_populates="sentences")
