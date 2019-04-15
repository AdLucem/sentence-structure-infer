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

	- Instead of a traditional chunker, a chunking method based on StanfordNLP's dependency parser was used. This is because of [... factors. write]
	- Align dependents:

## Results So Far 

	- In studying the data of this project, we've learnt one major thing: a general-purpose machine translatiion system may, in fact, be inadequate for translation into a particular register of the language. In this case, our dataset was a technical manual for building codes- thus, the register of English contained highly technical and scientific words, and precision was needed in the translated material as well.

	- Another thing that was leant is that the Anusaaraka system tends to translate to highbrow, 'formal' Hindi, while the post-editors have simplified it to a mixture of transliteration and simpler hindi terms that nonetheless match the terms used in the English document. This informs that Anusaaraka's lexicon needs to be upgraded to correspond to a more casual, readable register of Hindi.

	- The postedited data is actually code-mixed, since there is a fair amount of English mixed in and even replacing certain Hindi terms in postedited data.

	- Nonetheless, stanfordnlp can extract some decent amount of head-similarity between the machine translated and the postedited data. It's noticed that the head of the MT sentence and the head of the postedited sentence are semantically similar, suggesting that the post-editor did simple word replacement. Thus, we infer that the MT system identifies the head verb in the english sentence correctly, but translates it in too "high-brow" a fashion, requiring the post-editor to transliterate the original head verb (english), or replace it. Sample data comparing heads is shown:

	```
	समिति  कमिटी (translit)
    प्राक्कथन  फॉरवॉर्ड (translit)
    करता  बताया (change)
    किया  किया 
    गया  किया (change)
    बढाया  बढ़ा (simplify)
    गया  की (change)
    परखा  की (simplify)
    पर्मिसबल  किया (change)
    ```

## TODOs and Further Work

This code is in desperate need of refactoring if you want to run it on a large- or even a medium- database of sentences.
