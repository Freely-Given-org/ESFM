# ESFM

- **Enhanced Standard Format Markers** for modern digital Bibles with advanced features

This is the home of ESFM: A community-enhanced version of the United Bible Societies Institute for Computer Assisted Publishing ([UBSICAP](https://github.com/ubsicap))-controlled [USFM](https://github.com/ubsicap/usfm) standard. See more USFM/USX info [here](https://docs.usfm.bible) also.

It should be noted that USFM already allows for [user extensions](https://ubsicap.github.io/usfm/about/syntax.html#z-namespace) and [user-defined attributes](https://ubsicap.github.io/usfm/attributes/index.html#user-defined-attributes). ESFM will likely make use of those (for USFM compatibility reasons -- see [below]()).

## Expected Goals

1. To allow optional phrasing within a USFM source file e.g., if you want one set of files for two Bible variants that have either "Yahweh" or "the LORD" to be selectable on a website or before printing
  - having the variants inside the ESFM files enables the translator to easily check both/all variants in their Bible editor(provided that there’s not so many variants that the text becomes very difficult to decipher)
  - the [OEB project](https://github.com/openenglishbible/Open-English-Bible) was using braces to mark options in their USFM files
  - note that some variants might be better handled by the [Scripted Bible Editor](https://github.com/Freely-Given-org/ScriptedBibleEditor) which is BCV-aware and hence allows changes to specify certain books or verses to be included or excluded from particular changes
2. To allow alignment (called "tagging" by some) of translated words with original language words, e.g., "_In the beginning_" is the translation of the first word in the Hebrew Scriptures
3. To allow pronoun referent tagging, e.g., to specify who "_he_" is in "He said,"
3. To allow semantic tagging, e.g., to specify that "_Israel_" is a "person" in one instance, but referring to "a nation" in another
4. To allow utterance tagging, e.g., to mark ALL utterances with info about the speaker(s), i.e., the next step past "red letter" Bibles (which use the existing USFM \wj character markers)
5. To allow connection graphs, e.g., who is the father of this person; who is the father of this house; who did this action to whom.
1. To allow parsing of translated words, e.g., noting that English "_ran_" is a form of the verb "_run_" which might assist searching
7. To define an [interlink format](https://ubsicap.github.io/usfm/linking/index.html) between different Bible versions that’s not simply [Paratext](https://paratext.org/)-only (see our [Bible Publication Details](https://github.com/Freely-Given-org/BiblePublicationsDetails) project also)
8. To allow for categories to be marked in footnotes and cross-references, but not necessarily printed (e.g., manuscript/critical footnote, translation footnote, cultural footnote, and OT reference, synoptic reference) -- this is different from [\fk](https://github.com/Freely-Given-org/BiblePublicationsDetails) which is a printed keyword and part of the main footnote text
9. To not rely on a [stylesheet](https://ubsicap.github.io/usfm/about/index.html#paratext-stylesheet) that was only designed for Paratext
10. To be able to encode commentaries well (i.e., not just for Bibles)
11. To have goals, discussions, and decision-making in the open, so that new versions can be released as necessary and also aren’t just imposed unexpectedly -- please feel free to start a new [discussion thread](https://github.com/Freely-Given-org/ESFM/discussions)

## Changes from USFM

1. No paragraph marker is required after a chapter marker -- this is because original language (Heb/Grk) Bibles may not even have paragraph markers. Requiring a paragraph marker after a chapter marker in any version that doesn’t mark paragraphs with USFM markers (perhaps the version has no concept of paragraph, or perhaps uses ¶ pilcrow instead of USFM paragraph markers) seems counterintuitive. We don’t expect that this change will break many USFM editor flows, although it might require updates to anything that checks or validates, prints or displays, formatted USFM.

## Restrictions (tighter than USFM)

ESFM will be more restricted or defined than USFM, or in other words, ESFM is generally a subset of valid USFM. This means that existing USFM files will not be valid ESFM, but that’s not expected to be a problem as ESFM is intended for new (or updated) works. For example:

1. File encoding must be UTF-8 (and only UTF-8)
2. Specially formatted \rem lines give extra ESFM metadata
2. Unnumbered versions of [numbered markers](https://ubsicap.github.io/usfm/about/syntax.html#numbered-markers) like [\s](https://ubsicap.github.io/usfm/titles_headings/index.html#s) will not be allowed -- this must be encoded as \s1
3. [\ie](https://ubsicap.github.io/usfm/introductions/index.html#ie) marker will be compulsory
4. Use of [whitespace](https://ubsicap.github.io/usfm/about/syntax.html#whitespace) will be more rigidly defined (in order to better capture the translator’s intentions)
5. File extensions will be specified, including case
6. File naming conventions will be specified, including case -- no inconsistent and confusing 2-digit/character numbering systems (i.e., book ordering is specified elsewhere, not in filenames)
7. Folder naming conventions will be recommended

## Compiled Version

At least one compiled version will be defined. This will be even more tightly defined and only intended for computers to read. (It’s not decided yet whether or not it will be human readable, bit-compressed, or both.)

## Indexes

Indexes to the source ESFM files and to the compiled files will be defined. This is indexes _plural_ because it includes at least:

1. Book/chapter/verse (BCV) indexes
2. Book/section/paragraph (BSP) indexes
3. A word-form dictionary which lists all verses or verse ranges that include that word-form

Note that book headers and introductions will have *pseudo-verses* (based on line numbers) so that they can scroll more intelligently in a Bible editor, e.g., [Biblelator](https://Freely-Given.org/Software/Biblelator/) cf. Paratext where the book introduction can be difficult to work on.

## Scripts

Scripts will be provided to do the following:

1. Convert ESFM files to stock USFM 3 (perhaps by selecting the desired phrasing options and other details at the time -- of course this will usually be a lossy conversion)
2. Compile the ESFM files and create the indexes
3. Package an ESFM folder into a [Scripture Burrito](https://docs.burrito.bible)
4. Rapidly load compiled ESFM and associated indexes

It is expected that Python scripts will definitely be provided and probably Rust modules (crates), but possibly sample code in other languages (such as JS and Go) as well.

## USFM Compatibility

ESFM will be designed so that the files can be easily loaded into a stock USFM editor, even if certain fields display strangely and do not have any special formatting support.

We are aware that other well-funded organisations have other (and probably better designed) systems,
but of course, if they’re not available to us, then they’re effectively irrelevant.
However, if the opportunities arise, we’re definitely interested in networking.

## History

ESFM was first conceived in 2014 (back in USFM 2 days). You can still read about the very early work [here](https://Freely-Given.org/Software/BibleDropBox/ESFMBibles.html).

## Involvement

Freely-Given welcomes the involvement of other interested parties.
And we especially welcome better ideas than our own -- please feel free to start a new [discussion thread](https://github.com/Freely-Given-org/ESFM/discussions).

## Proof of concept

In the [uWAlignmentTest](uWAlignmentTest/) folder, we took an unfoldingWord, aligned English translation (English ULT aligned to UGNT) and tried converting it to our proposed ESFM/TSV combined format (Feb 2023).

Taking these files, we plan to attempt realigning the ULT text to the SR GNT.

Finally, we plan to write an ESFM/TSV back to uW aligned USFM converter, thus completing the round trip as a further test that our initial conversion is not losing any important data.

### Obsolete proof of concept

In the now-obsolete [uWAlignmentTest.w](uWAlignmentTest.w/) folder, we took an unfoldingWord, aligned English translation (English ULT aligned to UGNT) and tried converting it to our earlier ESFM/TSV combined format that had each word wrapped in \w ...\w* markers.
