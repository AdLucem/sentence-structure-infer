# sentence-structure-infer

NLP Applications course project. Record of the project so far:

## Initial Discussion

Each 'data point' in this project was three-faceted:

	- The original english sentence
	- The machine translation of the original english sentence
	- The post-edited version of the machine translated sentence

## Diff

## Initial Data

## Okay So We Have A Lot Of Diff(erence)

## Observations About Initial Dataset

	- Very different: rather than being _postedited_, it was more appropriate to say that the sentences had been _rewritten_ by the posteditors. (This was later found to be a flaw in the data- see next point)
	- Most technical words- which, in this document, were most words- had been **translated** in the MT data, but **transliterated** by the post-editors in the post-edited data. (This was an observation that persisted when we fetched original data from Anusaaraka)

## Initial Data: Questionable

Major differences observed between the machine-translated data that was provided and the data that was translated by the newly up-and-running Anusaaraka machine translator website. It was concluded that the data provided by Rashid was a melange of several systems, and would not tell us anything about any particular system- thus negating the purpose of working on it.

The concept learnt from this point was that the data given should be closely looked at before embarking on an NLP task- to test for factors like overfitting, provenance and whether the data fits the task (eg: one should not take data from system A to test flaws in system B).

Fortunately, at the next meeting, the team was informed that Anusaaraka was up and working, and we were able to fetch data from it and compare to the english-postedited sentence pairs.

## Data Collection From Anusaaraka

Manually feeding data to Anusaaraka and taking the translated data.

## Automatic Chunk Alignment

	- Instead of a traditional chunker, a chunking method based on StanfordNLP's dependency parser was used. This is because [...]

## Going Back To Diff

## TODOs and Further Work

This code is in desperate need of refactoring if you want to run it on a large- or even a medium- database of sentences.
