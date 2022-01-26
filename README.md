# ESFM

- **Enhanced Standard Format Markers** for modern digital Bibles with advanced features

This is the home of ESFM: A community-enhanced version of the United Bible Societies Institute for Computer Assisted Publishing ([UBSICAP](https://github.com/ubsicap))-controlled [USFM](https://github.com/ubsicap/usfm) standard.

It should be noted that USFM already allows for [user extensions](https://ubsicap.github.io/usfm/about/syntax.html#z-namespace) and [user-defined attributes](https://ubsicap.github.io/usfm/attributes/index.html#user-defined-attributes). ESFM will likely make use of those (for USFM compatibility reasons -- see [below]()).

## Expected Goals

1. To allow optional phrasing within a USFM source file e.g., if you want one set of files for two Bible variants that have either "Yahweh" or "the LORD" to be selectable on a website or before printing
2. To allow pronoun referent tagging, e.g., to specify who "_he_" is in "He said,"
3. To allow semantic tagging, e.g., to specify that "_Israel_" is a "person" in one instance, but referring to "a nation" in another
4. To allow utterance tagging, e.g., to mark ALL utterances with info about the speaker(s), i.e., the next step past "red letter" Bibles 
5. To allow connection graphs, e.g., who is the father of this person; who is the father of this house; who did this action to whom.
6. To allow alignment of translated words with original language words, e.g., "_In the beginning_" is the translation of the first word in the Hebrew Scriptures
7. To define an [interlink format](https://ubsicap.github.io/usfm/linking/index.html) that's not simply [Paratext](https://paratext.org/)-only
8. To allow for categories to be marked in footnotes and cross-references (e.g., manuscript footnote, translation footnote, cultural footnote, and OT reference, synoptic reference)
9. To not rely on a [stylesheet](https://ubsicap.github.io/usfm/about/index.html#paratext-stylesheet) that was only designed for Paratext
10. To be able to encode commentaries as well as Bibles
11. To have decision-making in the open, so new versions can be released as necessary and also aren't just imposed unexpectedly

## Changes

1. No paragraph marker is required after a chapter marker -- this is because original language (Heb/Grk) Bibles don't have chapter numbers and may not even have paragraph markers.

## Restrictions

ESFM will be more restricted or defined than USFM. This will mean that existing USFM files will not likely be valid ESFM, but that's not expected to be a problem as ESFM is intended for new (or updated) works. For example:

1. UTF-8 will always be assumed
2. Unnumbered versions of [numbered markers](https://ubsicap.github.io/usfm/about/syntax.html#numbered-markers) like [\s](https://ubsicap.github.io/usfm/titles_headings/index.html#s) will not be allowed -- this must be encoded as \s1
3. [\ie](https://ubsicap.github.io/usfm/introductions/index.html#ie) marker will be compulsory
4. Use of [whitespace](https://ubsicap.github.io/usfm/about/syntax.html#whitespace) will be more rigidly defined (in order to better capture the translator's intentions)
5. File extensions will be specified, including case
6. File naming conventions will be specified, including case
7. Folder naming conventions will be recommended

## Compiled Version

At least one compiled version will be defined. This will be even more tightly defined and only intended for computers to read. (It's not decided yet whether or not it will be human readable, bit-compressed, or both.)

## Indexes

Indexes to the source ESFM files and to the compiled files will be defined. This is indexes _plural_ because it includes at least:

1. Book/chapter/verse (BCV) indexes
2. Book/section/paragraph (BSP) indexes
3. A word-form dictionary which lists all verses or verse ranges that include that word-form

Note that book introductions will have pseudo-verses so that they can scroll more intelligently in a Bible editor, e.g., [Biblelator](https://freely-given.org/Software/Biblelator/) cf. Paratext where the book introduction can be difficult to work on.

## Scripts

Scripts will be provided to do the following:

1. Convert ESFM files to stock USFM 3 (perhaps by selecting the desired phrasing options and other details at the time -- of course this will usually be a lossy conversion)
2. Compile the ESFM files and create the indexes
3. Package an ESFM folder into a [Scripture Burrito](https://docs.burrito.bible)
4. Rapidly load compiled ESFM and associated indexes

It is expected that Python scripts and Rust modules (crates) will definitely be provided, but possibly others as well.

## USFM Compatibility

ESFM will be designed so that the files can be easily loaded into a stock USFM editor, even if certain fields display strangely and do not have any special formatting support.

## History

ESFM was first conceived in 2014 (back in USFM 2 days). You can still read about the very early work [here](https://freely-given.org/Software/BibleDropBox/ESFMBibles.html).

## Involvement

Freely-Given welcomes the involvement of other interested parties.
