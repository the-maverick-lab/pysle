from praatio import tgio
from pysle import isletool
from pysle import praattools

def createSyllabifiedTextgrid(names_audio, text_grid):

  isleDict = isletool.LexicalTool()

  tg = tgio.openTextgrid(text_grid)
  syllableTG = praattools.syllabifyTextgrid(isleDict, tg, "words", "phones", skipLabelList=["", ])
  tg.addTier(syllableTG.tierDict["syllable"])
  tg.addTier(syllableTG.tierDict["tonicSyllable"])
  tg.addTier(syllableTG.tierDict["tonicVowel"])

  tg.save('../mavid-scripts/files/wav_recordedNames_syllables_test.TextGrid')

  return

if __name__ == "__main__":
  createSyllabifiedTextgrid('../mavid-scripts/files/recordedNames.wav', '../mavid-scripts/files/wav_recordedNames.TextGrid')