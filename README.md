# ESFM
Enhanced Standard Format Markers for Biblical resources

This is the home of ESFM: A community-enhanced version of the United Bible Societies Institute for Computer Assisted Publishing ([UBSICAP](https://github.com/ubsicap)) controlled [USFM](https://github.com/ubsicap/usfm) standard.

## Goals

1. To allow optional phrasing within a USFM source file. For example, if you want one set of files for two Bible variants that have either "Yahweh" or "the LORD" to be selectable on a website or before printing
2. To allow pronoun referent tagging, e.g., to specify who "he" is in "He said,"
3. To allow semantic tagging, e.g., to specify that "Israel" is a "person" in one instance, but referring to "a nation" in another
4. To allow alignment of translated words with original language words, e.g., "In the beginning" is the translation of the first word in the Hebrew Scriptures

## Restrictions

ESFM will be more restricted or defined than USFM. This will mean that existing USFM files will not likely be valid ESFM, but that's not expected to be a problem as ESFM is intended for new (or updated) works. For example:

1. Unnumbered fields like \s will not be allowed -- this must be encoded as \s1
2. Use of whitespace will be tightly defined
3. File extensions will be specified, including case
4. File naming conventions will be specified, including case
5. Folder naming conventions will be recommended

## Compiled Version

At least one compiled version will be defined. This will be even more tightly defined and only intended for computers to read. (It's not decided yet whether or not it will be human readable, bit-compressed, or both.)

## Indexes

Indexes to the source ESFM files and to the compiled files will be defined. This is indexes plural because it includes at least:

1. Book/chapter/verse (BCV) indexes
2. Book/section/paragraph (BSP) indexes

## Scripts

Scripts will be provided to do the following:

1. Convert ESFM files to stock USFM 3 (perhaps by selecting the desired phrasing options and other details at the time)
2. Compile the ESFM files and create the indexes
3. Package an ESFM folder into a [Scripture Burrito]()
4. Rapidly load compiled ESFM and associated indexes

It is expected that Python scripts and Rust modules (crates) will definitely be provided, but possibly others as well.

## History

ESFM was first conceived in 2014 (back in USFM 2 days). You can still read about the very early work [here](https://freely-given.org/Software/BibleDropBox/ESFMBibles.html).

## Involvement

Freely-Given welcomes the involvement of other interested parties.
