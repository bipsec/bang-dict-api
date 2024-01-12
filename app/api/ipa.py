import pathlib
from fastapi import APIRouter, HTTPException
from app.scripts.ipa_converter import BanglaIPATranslator

router = APIRouter()

# need to use this to give path
model_path = pathlib.Path(__file__).absolute().parents[1] / "model" / "ipa_model.pth"


@router.get("/get_ipa/")
async def get_ipa_for_word(word: str):
    try:
        ipa = BanglaIPATranslator(model_path)

        ipa_translated = ipa.translate(word)

        return ipa_translated

    except IndexError:
        return "IPA is not generated from the model"
