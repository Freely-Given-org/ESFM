# ESFM Specifications

## Introduction

This spec is based on the [USFM spec](https://ubsicap.github.io/usfm/),
and our files have been checked that they can be edited in UBS/SIL Paratext 9
(even though it doesn't recognise what the fields mean).
Our own [Biblelator](https://github.com/Freely-Given-org/Biblelator) will eventually be updated to support this format natively.

In this document, we use the term _original language_ to
refer any of Hebrew or Aramaic, or Koine Greek.
(In translation books, that might also be called the _source language_.)

## USFM Headers

Looking at the start of a traditional USFM file for a Bible translation:

```
\id 1JN
\usfm 3.0
\ide UTF-8
\h 1 Huwan
\toc1 1 Huwan
\toc2 1 Huwan
\toc3 1Huw
\mt2 Ka an-anayan ne sulat ni
\mt1 Huwan
```

we add the following [\rem](https://ubsicap.github.io/usfm/identification/index.html#rem) fields:

```
\id 1JN - Matigsalug Translation v1.0.17
\usfm 3.0
\ide UTF-8
\rem ESFM v0.6 JN1
\rem WORKDATA Matigsalug.txt
\rem FILEDATA Matigsalug.JN1.txt
\rem WORDTABLE Matigsalug.words.tsv
\h 1 Huwan
\toc1 1 Huwan
\toc2 1 Huwan
\toc3 1Huw
\mt2 Ka an-anayan ne sulat ni
\mt1 Huwan
```

Please note the following:

1. After the USFM book code on the Id line, the work name can be specified
after ' - ' (space, hyphen, space).
However, this work name is mostly for human readers of the file
(as a full metadata file can be specified below).
1. The [Id line](https://ubsicap.github.io/usfm/identification/index.html#index-1)
should end with the version number of that book.
This should be detectable with ' v' (space, lowercase v)
and a version number similar to a [SemVer number](https://semver.org/)
except that the three sets of digits (if they all exist) would be
Major Revision Number, Minor Revision Number, Minor Fixes Number.
1. The USFM line must refer to the
[USFM version](https://ubsicap.github.io/usfm/identification/index.html#usfm)
that this standard is based on, currently 3.0 as per [here](https://github.com/Freely-Given-org/Biblelator)
1. The [IDE line](https://ubsicap.github.io/usfm/identification/index.html#index-3)
can only contain 'UTF-8' for valid ESFM.
1. ESFM does NOT use or expect the optional USFM [Status line](https://ubsicap.github.io/usfm/identification/index.html#sts).
1. The first [REM line](https://ubsicap.github.io/usfm/identification/index.html#rem)
MUST contain 'ESFM' followed by a space and the ESFM format version number,
and then another space and the three-character UPPERCASE
[BibleOrgSys book code](https://freely-given.org/Software/BibleOrganisationalSystem/BOSBooksCodes.html).
Note that unlike USFM books codes, BibleOrgSys books codes
all start with an UPPERCASE letter, and hence can also be used as variable names
in most computer languages.
1. All of the above is compulsory for an ESFM Bible book file.
1. The REM WORKDATA line points to a file which contains
metadata for the work.
This can include any field from the
[DublinCore Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms)
and much of the data can be packaged into a
[Scripture Burrito](https://docs.burrito.bible) for interchange.
1. The REM FILEDATA line points to a file which contains
metadata for the file.
As well as listing the translators, editors, and checkers for this book,
it can even include the edit history for each change.
1. The REM WORDTABLE line points to a
[TSV](https://en.wikipedia.org/wiki/Tab-separated_values) file
which contains reference information for the words in the text.
1. The above three (optional) files described below also
form part of this specification.

## Words

Instead of a traditional USFM file something like the following:

```
\c 1
\p
\v 1 The scroll of the birth of \add the\add* \nd Lord\nd* Jesus Christ, son of David.
```

we might now have in ESFM:

```
\c 1
\p
\v 1
The¦1 scroll¦2 of¦3 the¦4 birth¦5 of¦6
\add the¦587\add* \nd Lord¦588\nd*
Jesus¦7 Christ¦8, son¦9 of¦10 David¦11.
```

Note that we use a [Unicode broken bar](https://www.compart.com/en/unicode/U+00A6)
rather than a pipe character, for three reasons:

1. Pipe is used in USFM 3.0 inside \w and \fig and other fields
2. We have encountered USFM Bibles where the translators (wrongly?) use double pipe characters for a line break
3. We have encountered original texts in the USFM where the editor uses a pipe character to mean "or" (i.e., for alternatives)
4: The broken bar is not on standard PC keyboards so MUCH less likely to be entered as part of any Bible text.

In a previous test we had:

```
\c 1
\p
\v 1
\w The|1\w* \w scroll|2\w* \w of|3\w* \w the|4\w* \w birth|5\w* \w of|6\w*
\add \w the|587\w*\add* \nd \w Lord|588\w*\nd*
\w Jesus|7\w* \w Christ|8\w*, \w son|9\w* \w of|10\w* \w David|11\w*.
```

Yes, considerably more difficult to read
with no real advantages.
You will have noticed that this style abused the
[USFM w default field](https://ubsicap.github.io/usfm/attributes/index.html#default-attribute).

However, again, Paratext will load and save ESFM without complaint.
(That doesn't mean that the Paratext Basic Checks won't complain.)

The numbers associated with each word are LINE NUMBERS
of a row in the TSV file referred to by WORDTABLE.
A TSV file is a table -- much like a spreadsheet.
Line #1 is the first line after the column headers.
As seen above, if you add some words later,
there's nothing to suggest that the ESFM words
must have consecutive row numbers -- just UNIQUE row numbers.

Words in headings, introductions and footnotes, etc.
can all contain these line numbers.

If a translation is edited, it's recommended that
new line numbers are created (and new rows added to the end of the TSV table.)
The now-unused word rows can be marked as deprecated.
Once the translation is published,
the deprecated rows can be deleted and all the words renumbered,
but we're not recommending that that happen during normal editing.

# Why have word numbers?

Initially we were planning to add information into USFM files.
Here are three words ("we have heard") from an unfoldingWord English translation
that are aligned/tagged to a single word ("ἀκηκόαμεν") in the unfoldingWord Greek New Testament:

```
\zaln-s |x-strong="G01910" x-lemma="ἀκούω" x-morph="Gr,V,IEA1,,P," x-occurrence="1" x-occurrences="1" x-content="ἀκηκόαμεν"\*\w we|x-occurrence="1" x-occurrences="3"\w*
\w have|x-occurrence="1" x-occurrences="4"\w*
\w heard|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*,
```

The ESFM snippet might be:

```
we¦15345 have¦15346 heard¦15347
```

which I think you'll agree is a little more human-readable (FWIW).

But we now want to add even more information to the text:

* We want to know who the writer/speaker is and a link to their biography.
* We want to know who the pronouns refer to and a link to their biography.
* We want links to maps and GPS coordinates of locations.
* We want links to cultural notes and a URL of an interesting online article.
* We want links to some variant spellings in the Greek.
* And so on...

Imagine how the USFM would look with all that added!
And then we want to load the USFM into a simple online text editor.
So we have to first download, parse, and then filter out all of that extra information
just to discover what the translated text actually says.

## Why link to TSV files and not the very popular JSON

Here is a snippet of the
[Open Scriptures Hebrew Bible](https://hb.openscriptures.org/)
extracted from their
[OSIS files](https://github.com/openscriptures/morphhb/tree/master/wlc/)
and converted into a table/TSV:

```
Ref     RowType Special Strongs CantillationHierarchy   Morphology      OSHBid  WordOrMorpheme
GEN_1:1w1a      m               b       1.0     HR      01xeNa  בְּ
GEN_1:1w1b      m               7225    1.0     Ncfsa   01xeNb  רֵאשִׁית
GEN_1:1w2       w               1254 a          HVqp3ms 01Nvk   בָּרָ֣א
GEN_1:1w3       w               430     1       HNcmpa  01TyA   אֱלֹהִ֑ים
GEN_1:1w4       w               853             HTo     01vuQ   אֵ֥ת
GEN_1:1w5a      m               d       0.0     HTd     01TSca  הַ
GEN_1:1w5b      m               8064    0.0     Ncmpa   01TScb  שּׁמַ֖יִם
GEN_1:1w6a      m               c               HC      01k5Pa  וְ
GEN_1:1w6b      m               853             To      01k5Pb  אֵ֥ת
GEN_1:1w7a      m               d       0       HTd     01nPha  הָ
GEN_1:1w7b      m               776     0       Ncbsa   01nPhb  אָֽרֶץ
GEN_1:1 seg                             x-sof-pasuq             ׃
```

Here is exactly the same info (Gen 1:1) in JSON:

```
[
  [
    "GEN_1:1w1a",
    "m",
    "",
    "b",
    "1.0",
    "HR",
    "01xeNa",
    "\u05d1\u05bc\u05b0"
  ],
  [
    "GEN_1:1w1b",
    "m",
    "",
    "7225",
    "1.0",
    "Ncfsa",
    "01xeNb",
    "\u05e8\u05b5\u05d0\u05e9\u05c1\u05b4\u0596\u05d9\u05ea"
  ],
  [
    "GEN_1:1w2",
    "w",
    "",
    "1254 a",
    null,
    "HVqp3ms",
    "01Nvk",
    "\u05d1\u05bc\u05b8\u05e8\u05b8\u05a3\u05d0"
  ],
  [
    "GEN_1:1w3",
    "w",
    "",
    "430",
    "1",
    "HNcmpa",
    "01TyA",
    "\u05d0\u05b1\u05dc\u05b9\u05d4\u05b4\u0591\u05d9\u05dd"
  ],
  [
    "GEN_1:1w4",
    "w",
    "",
    "853",
    null,
    "HTo",
    "01vuQ",
    "\u05d0\u05b5\u05a5\u05ea"
  ],
  [
    "GEN_1:1w5a",
    "m",
    "",
    "d",
    "0.0",
    "HTd",
    "01TSca",
    "\u05d4\u05b7"
  ],
  [
    "GEN_1:1w5b",
    "m",
    "",
    "8064",
    "0.0",
    "Ncmpa",
    "01TScb",
    "\u05e9\u05c1\u05bc\u05b8\u05de\u05b7\u0596\u05d9\u05b4\u05dd"
  ],
  [
    "GEN_1:1w6a",
    "m",
    "",
    "c",
    null,
    "HC",
    "01k5Pa",
    "\u05d5\u05b0"
  ],
  [
    "GEN_1:1w6b",
    "m",
    "",
    "853",
    null,
    "To",
    "01k5Pb",
    "\u05d0\u05b5\u05a5\u05ea"
  ],
  [
    "GEN_1:1w7a",
    "m",
    "",
    "d",
    "0",
    "HTd",
    "01nPha",
    "\u05d4\u05b8"
  ],
  [
    "GEN_1:1w7b",
    "m",
    "",
    "776",
    "0",
    "Ncbsa",
    "01nPhb",
    "\u05d0\u05b8\u05bd\u05e8\u05b6\u05e5"
  ],
  [
    "GEN_1:1",
    "seg",
    "",
    "",
    "",
    "x-sof-pasuq",
    "",
    "\u05c3"
  ],
]
```

Compared to the JSON (and it is indeed possible to remove mich of the whitespace from the JSON),
the TSV is so much more concise and quicker to parse.
Especially when the OSHB has over half-a-million rows (split by morpheme).
The GNT has almost 170,000 rows (including variants).

JSON dictionaries/maps (compared to the above _lists_) are even more wordy,
as the name of each field is repeated for each instance,
whereas in TSV, the column names only appear once at the top of the file.

Again, due to its popularity JSON is a good interchange format,
but not always suitable for fast, efficient parsing of long and complex texts.

### Other formats

CSV is less useful than TSV for Bible applications, because
so many Bible fields contain commas, and hence a lot more escaping is required.
(There's no normal reason to have a TAB character in a Bible text.)

Note also that [Parquet](https://parquet.apache.org/docs/file-format/)
may also be used as a replacement for TSV if those additional compression and efficiency
improvements are important for your application.

## Using row numbers for linking

Our first thought was to use an Id field --
something like those five-character OSHB IDs that are shown
in the above TSV snippet.
(The first one is 01xeNa -- we appended the suffix a,b,c,d,e for morphemes.)
Those OSHB Ids
(which we understand were suggested by the
[Bible Tagging project](https://github.com/educational-resources-and-services/bibletags-usfm) --
although unfortunately they went on to define their own set of WLC Ids which are different from the OSHB ones)
consist of a two-digit book number
followed by three random alphanumeric characters.
(With 66 books, this allows for 66 * (26+26+10)^3 = 15,729,648 combinations.)

But ID fields don't offer many advantages over row numbers.
The main advantage is permanence,
i.e., if you commit at some point in time to never change them again,
then after that, they can always be used to refer to that particular word.
If you need to change the word, then you create a new ID
and check to never reuse the old one.
But actually if you want,
you can make those same commitments with row numbers.

One advantage of row numbers is that you can index
directly into an array,
without having to go through a dictionary/map.

Creating a new row number is also easier and less expensive.
You simply need to know the number of existing rows and add one,
whereas creating a Id field requires checking all existing
Id fields to ensure that it's not a repeat.

One potential disadvantage of row numbers is the pyschological
pressure to ensure that 57 comes after 56,
i.e., to assign significance to them and always be wanting to reorder.
It's more difficult to get through to your brain
that they don't carry semantic information -- they're only for linking.

## Word tables (TSV)

TSV tables should always contain a header line/row, imagined at row #0.
So row #1 indexes to the first data line after the header row.

We recommend for performance reasons, that the word tables are stored by Bible book,
similar to how most translators use USFM files,
so the first word in each Bible book could link to row #1.

[Note that it is also quite possible (via the WORDTABLE entry in the file),
to have a single word table used for all books.
This would lead to larger tables, and larger numbers in the ESFM files,
but there might be some applications where this is desirable.]

It is quite possible to have very wide tables
containing a lot of data for each word.
But it's also quite easy to create a smaller file
with only the columns needed for a particular app.
For example, if you don't have a Strongs lexicon in your app,
there's no need to include a column of Strongs numbers in your custom table.


## Many to many alignment

The unfoldingWord aligned text snippet above and reproduced below:

```
\zaln-s |x-strong="G01910" x-lemma="ἀκούω" x-morph="Gr,V,IEA1,,P," x-occurrence="1" x-occurrences="1" x-content="ἀκηκόαμεν"\*\w we|x-occurrence="1" x-occurrences="3"\w*
\w have|x-occurrence="1" x-occurrences="4"\w*
\w heard|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*,
```

(see more in the files [here](https://git.door43.org/unfoldingWord/en_ult/))

with ESFM as

```
we¦15345 have¦15346 heard¦15347
```

can be expressed in table columns as follows:

```
(RowNum) OrigRows
 (15,345)   7610
 (15,346)   7610
 (15,347)   7610
```

thus pointing three English words to one Greek word.
There's absolutely no need (in fact, it's a big advantage not)
to repeat all that parsing and other info from the Greek table
(although also nothing to stop you combining info from the Greek table
into additional columns in the English translation table
if you really need that information more quickly in your app).
And of course, discontinuities are easily handled --
the middle Greek link would simply be pointing to a different Greek word.

The unfoldingWord _occurrence_ field tells the USFM which particular
Greek word in the verse is linked.
Using row numbers links directly to the word so there's no need for that.
The _occurrences_ fields are presumably there to allow the underlying
Greek text to change a little and for this to be detected.
I'm not aware of when this has ever been used in practice???

If you need to know what English words translate one Greek word,
you would want to do a reverse pivot of that table
(or else scan up and down to see if the same OrigLine number is reused).
The ESFM method also allows words to be connected to other verses,
e.g., if a word appears in v6,
but is elided in the original language in v7 yet is necessary in the translation,
it doesn't matter to this system that the OrigLine number
links to a word in the previous verse.
(It's up to the UI whether or not to display that information.)

The above example shows one original language word being translated as three words.
Of course, the one-to-one example is trivial.
What about multiple original words translated as a single word?
If your language had a word _asara_ for "wild honey"
(John the Baptist's food from Mark 1:6), then ESFM:

```
\w asara¦12345\w*
```

might point to:

```
(RowNum) OrigRows
 (12,345)  492;493
```

Note that we use a semi-colon instead of a comma
so that CSV parsers are less likely to become confused.

Again, they need not be consecutive original language words.

Apart from the _OrigLines_ columns, none of the other column names
are yet specified by this ESFM spec.
(Nor is the order of columns specified.)
Instead, the columns may be customised by the server
according to the needs/expectations of the app that is using them.

## Additional observations

1. This spec neither forces nor discourages tagging words outside of Bible verse text, i.e., in titles, introductions, section headings, and footnotes, etc. It just depends on what you want/need.
2. If every word in a ESFM text is tagged and the numbers are consecutive, and if the linked table contains information about what punctuation & whitespace and paragraph & character markers precede and/or follow the word, it's conceivable that a text could be constructed from the table alone (i.e., just from walking through the table without requiring any ESFM file). This was not a design goal, but a side-effect, and it probably makes more sense for an original language (Heb/Grk) text than for a translation (because it tends to have less additional fields like section headings as well as less character markup).

## Discarded ideas

The 5-character OSHB ID includes a base-62 portion --
the final three characters can be a digit or an UPPERCASE or lowercase letter,
so 10+26+26 = 62 options.
On the other hand, standard line numbers are only base-10,
so six digits are required to express numbers up to a million (OSHB morphemes).

We considered using more characters to encode the line number.
But this would require more processing if we just used alphanumeric characters,
and more USFM boilerplate if we also used punctuation characters.
So instead of:

```
the¦135876
```

we could have had the shorter:

```
the¦a2P
```

but if also using punctuation, we would have needed something like:

```
\w the|x-e="-.F"\w* \w temple|x-e="7q<"\w*```

which then gave no advantage at all.
(Might as well just have the extra line-number digits.)
