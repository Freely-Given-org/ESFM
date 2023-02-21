# unfoldingWord Bible Alignment Test folder

unfoldingWord has a scheme for connecting/aligning/tagging translated words to the original languages words which they're translated from.
This data is stored in the USFM files of the translated Bible books, but it's verbose and somewhat complex to parse,
and hence it takes quite a reasonable amount of processing to extract the raw Bible text.
To edit the translated text is even more complex.

Part of the reason for complexity is (using Greek and English as examples):

- sometimes one Greek word is translated into one English word (1:1)
- sometimes one Greek word requires two or more English words to translate it (1:n)
- sometimes two or more Greek words are translated with only one English word (n:1)
- it's conceivable that two ore more Greek words are translated with two or more English words (n:n) ???
- sometimes the two or more Greek words are not contiguous
- sometimes the two or more English words are not contiguous
- we also want to add additional information about the Greek words (such as lemma, Strongs number, morphology, etc.)
- we also want to add additional information about the English words

In these subfolders, we have some test files converted from unfoldingWord USFM files.

These were produced by the Python script uW_to_ESFM.w.py

(We also hope to write a script that does the reverse to prove the concept of round-tripping
without losing information.)
