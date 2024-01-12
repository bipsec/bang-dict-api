from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class WordMeaning(Base):
#     __tablename__ = "word_meaning"
#
#     id = Column(Integer, primary_key=True, index=True)
#     pageNo = Column(String, unique=True, index=True)
#     words = Column(String, unique=False, index=True)
#     number = Column(String, nullable=True, index=True)
#     spelling = Column(String, nullable=True, index=True)
#     meaning = Column(String, nullable=True, index=True)
#     pos = Column(String, nullable=True, unique=False, index=True)
#     ipa = Column(String, unique=False, nullable=True, index=True)
#     root_lang = Column(String, nullable=True, index=True)
#     type = Column(String, unique=False, nullable=True, index=True)
#     sentence = Column(String, unique=False, nullable=True,index=True)
#     source = Column(String, index=True)
#     audio = Column(String, nullable=True, index=True)

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
