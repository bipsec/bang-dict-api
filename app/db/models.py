from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, LargeBinary, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class WordMeaning(Base):
    __tablename__ = "word_meaning"

    id = Column(Integer, primary_key=True, index=True)
    pageNo = Column(String, unique=False, index=True)
    words = Column(String, unique=False, index=True)
    number = Column(String, unique=False, nullable=True, index=True)
    spelling = Column(String, nullable=True, index=True)
    meaning = Column(String, nullable=True, index=True)
    pos = Column(String, nullable=True, unique=False, index=True)
    ipa = Column(String, unique=False, nullable=True, index=True)
    root_lang = Column(String, nullable=True, index=True)
    type = Column(String, unique=False, nullable=True, index=True)
    sentence = Column(String, unique=False, nullable=True, index=True)
    source = Column(String, index=True)

    sentences = relationship("Sentence", back_populates="word_meaning")
    pos_taggers = relationship("PosTagger", back_populates="word_meaning")
    ipas = relationship("IPA", back_populates="word_meaning")
    audio_data = relationship("AudioData", back_populates="word_meaning")


class Sentence(Base):
    __tablename__ = "word_sentence"

    id = Column(Integer, primary_key=True, index=True)
    words = Column(String, unique=False, index=True)
    sentence = Column(String, unique=False, nullable=True, index=True)
    word_meaning_id = Column(Integer, ForeignKey("word_meaning.id"))

    word_meaning = relationship("WordMeaning", back_populates="sentences")


class PosTagger(Base):
    __tablename__ = "word_pos"

    id = Column(Integer, primary_key=True, index=True)
    words = Column(String, unique=False, index=True)
    pos = Column(String, unique=False, nullable=True, index=True)
    word_meaning_id = Column(Integer, ForeignKey("word_meaning.id"))

    word_meaning = relationship("WordMeaning", back_populates="pos_taggers")


class IPA(Base):
    __tablename__ = "ipa"

    id = Column(Integer, primary_key=True, index=True)
    words = Column(String, unique=False, index=True)
    ipa = Column(String, unique=False, nullable=True, index=True)
    word_meaning_id = Column(Integer, ForeignKey("word_meaning.id"))

    word_meaning = relationship("WordMeaning", back_populates="ipas")



class AudioData(Base):
    __tablename__ = "word_audio"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=False, nullable=True)
    duration = Column(Float, unique=False, nullable=True)
    audio_file = Column(LargeBinary, unique=False, nullable=True)
    audio_type = Column(String, unique=False, nullable=True)
    word_meaning_id = Column(Integer, ForeignKey("word_meaning.id"))

    word_meaning = relationship("WordMeaning", back_populates="audio_data")
