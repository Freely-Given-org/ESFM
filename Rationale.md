# Rationale

## Introduction

### USFM (Unified Standard Format Markers)

USFM is the most common Bible interchange format,
editable by UBS/SIL Paratext and open-source Bibledit
as well as our own Biblelator,
and used by the Digital Bible Library -- a collection of mostly tightly-restricted Bible translations.

Here's an example of some USFM text:

```
\id 1JN Matigsalug Version
\usfm 3.0
\ide UTF-8
\h 1 Huwan
\toc1 1 Huwan
\toc2 1 Huwan
\toc3 1Huw
\mt2 Ka an-anayan ne sulat ni
\mt1 Huwan
\is1 Igpewun‑a
\ip Due daruwa ne katuyuan te seini se \bk An-anayan ne sulat ni Huwan\bk*: 1.) ka pegbagget te me talagbasa te pegnengneng meyitenged te Manama wey te Anak din ne si Hisu Kristu; wey 2.) ka pegpaney-paney kandan te keilangan ne kene eg-ikul te kene ne malehet ne pegpanulu ne egpakadereet de te pegsabeka ran diye te Magbebaye. Migkahi seeye se kene ne malehet ne talagpanulu te si Hisus kun ne Anak te Manama kene egkeyitabu ne etew sikandin ne iling kanta. Migpanulu man‑e sikandan ne ka kaluwasan, ware kun kalabetan te peg-ugpe ne matareng wey te peggeyinawa te duma.
\ip Na, te pegsupak te sika ne pegpanulu, mig-ayad-ayad migpangguhud si Huwan, ne si Hisu Kristu malehet iya ne etew, wey amana rin man‑e ipasabut ne ka langun ne migpalintutuu ki Hisus wey ka miggeyinawa te Manama, keilangan ne egpaheyinaweey degma ka tagse sabeka.
\iot Ka nenasulat te seini ne baseen
\io1 Igpewun‑a \ior 1:1-4\ior*
\io1 Ka marusilem wey ka malayag \ior 1:5–2:29\ior*
\io1 Ka me anak te Manama wey ka me anak ni Meibulan \ior 3:1-24\ior*
\io1 Ka kamalehetan wey ka seyyup \ior 4:1-6\ior*
\io1 Ka geyinawa \ior 4:7-21\ior*
\io1 Ka pegpalintutuu ki Hisu Kristu \ior 5:1-21\ior*
\c 1
\s1 Ka lalag ne migbehey te umul
\p
\v 1 \x + \xo 1:1: \xt Huw 1:1.\x*Duen e sikandin dengan te an-anayan, ne narineg ney e kuntee wey nakita ney e mismu wey nahen-genan ney pad iya, sikandin ka egngaranan te Lalag ne egbehey te umul.
\v 2 \x + \xo 1:2: \xt Huw 1:14.\x*Ne hengkayi te nekeuma kayi te kanta ka sika ne umul, nakita ney en iya sika, wey migpamalehet key kayi wey migpangguhud key kaniyu meyitenged te umul ne ware egtamanan. Ne duma sika te Amey, ne kuntee migpakite e kanami.\f + \fr 1:2 \ft Pangunggilingan de seini.\f*
\v 3 Igpangguhud ney degma kaniyu ke nekey ka nakita ney wey ke nekey ka narineg ney, eyew egpekegduma kew duma kanami diye te Amey wey te Anak din ne si \nd Hisu Kristu\nd*.
\v 4 Ne insulat ney seini eyew egkahale-gale ki.
```

You can see header fields at the beginning of the field,
there's an introduction (most of the backslash markers followed by an i),
and a small segment of the translated Bible text with paragraph and character formatting,
a section heading, and cross-references and a footnote.

### USX

USX is USFM plonked inside XML fields. Hence the above roughly comes out as:

```
<?xml version="1.0" encoding="utf-8"?>
<usx>
  <book code="1JN" style="id">Matigsalug Version </book>
  <para style="ide">UTF-8 </para>
  <para style="h">1 Huwan </para>
  <para style="toc1">1 Huwan </para>
  <para style="toc2">1 Huwan </para>
  <para style="toc3">1Huw </para>
  <para style="mt2">Ka an-anayan ne sulat ni </para>
  <para style="mt1">Huwan </para>
  <para style="is">Igpewun-a </para>
  <para style="ip">Due daruwa ne katuyuan te seini se <char style="bk">An-anayan ne sulat ni Huwan</char>: 1) ka pegbagget te me talagbasa te pegnengneng meyitenged te Manama wey te Anak din ne si Hisu Kristu; wey 2) ka pegpaney-paney kandan te keilangan ne kene eg-ikul te kene ne malehet ne pegpanulu ne egpakadereet de te pegsabeka ran diye te Magbebaye. Migkahi seeye se kene ne malehet ne talagpanulu te si Hisus kun ne Anak te Manama kene egkeyitabu ne etew sikandin ne iling kanta. Migpanulu man-e sikandan ne ka kaluwasan, ware kun kalabetan te peg-ugpe ne matareng wey te peggeyinawa te duma. </para>
  <para style="ip">Na, te pegsupak te sika ne pegpanulu, mig-ayad-ayad migpangguhud si Huwan, ne si Hisu Kristu malehet iya ne etew, wey amana rin man-e ipasabut ne ka langun ne migpalintutuu ki Hisus wey ka miggeyinawa te Manama, keilangan ne egpaheyinaweey degma ka tagse sabeka. </para>
  <para style="iot">Ka nenasulat te seini ne baseen </para>
  <para style="io1">Igpewun-a 1:1-4 </para>
  <para style="io1">Ka marusilem wey ka malayag 1:5–2:29 </para>
  <para style="io1">Ka me anak te Manama wey ka me anak ni Meibulan 3:1-24 </para>
  <para style="io1">Ka kamalehetan wey ka seyyup 4:1-6 </para>
  <para style="io1">Ka geyinawa 4:7-21 </para>
  <para style="io1">Ka pegpalintutuu ki Hisu Kristu 5:1-21 </para>
  <chapter number="1" style="c" />
  <para style="s">Ka lalag ne migbehey te umul </para>
  <para style="p">
    <verse number="1" style="v" /><note style="x" caller="-"><char style="xo" closed="false">1:1: </char><char style="xt" closed="false">Huw 1:1.</char></note> Duen e sikandin dengan te an-anayan, ne narineg ney e kuntee wey nakita ney e mismu wey nahen-genan ney pad iya, sikandin ka egngaranan te Lalag ne egbehey te umul. <verse number="2" style="v" /><note style="x" caller="-"><char style="xo" closed="false">1:2: </char><char style="xt" closed="false">Huw 1:14.</char></note> Ne hengkayi te nekeuma kayi te kanta ka sika ne umul, nakita ney en iya sika, wey migpamalehet key kayi wey migpangguhud key kaniyu meyitenged te umul ne ware egtamanan. Ne duma sika te Amey, ne kuntee migpakite e kanami. <verse number="3" style="v" />Igpangguhud ney degma kaniyu ke nekey ka nakita ney wey ke nekey ka narineg ney, eyew egpekegduma kew duma kanami diye te Amey wey te Anak din ne si Hisu Kristu. <verse number="4" style="v" />Ne insulat ney seini eyew egkahale-gale ki. </para>
...
</usx>
```

Some software might find the XML easier to validate and/or to parse.

### Aligned USFM (called Tagged by some)

Here is how a verse from a Greek New Testament is encoded in USFM:

```
\id 1JN unfoldingWord® Greek New Testament
\usfm 3.0
\ide UTF-8
\h 1 John
\toc1 The First Letter of John
\toc2 First John
\toc3 1Jn
\mt1 First John

\c 1
\p
\v 1
\w ὃ|lemma="ὅς" strong="G37390" x-morph="Gr,RR,,,,NNS,"\w*
\w ἦν|lemma="εἰμί" strong="G15100" x-morph="Gr,V,IIA3,,S,"\w*
\w ἀπ’|lemma="ἀπό" strong="G05750" x-morph="Gr,P,,,,,G,,,"\w*
\w ἀρχῆς|lemma="ἀρχή" strong="G07460" x-morph="Gr,N,,,,,GFS,"\w*,
\w ὃ|lemma="ὅς" strong="G37390" x-morph="Gr,RR,,,,ANS,"\w*
\w ἀκηκόαμεν|lemma="ἀκούω" strong="G01910" x-morph="Gr,V,IEA1,,P,"\w*,
\w ὃ|lemma="ὅς" strong="G37390" x-morph="Gr,RR,,,,ANS,"\w*
\w ἑωράκαμεν|lemma="ὁράω" strong="G37080" x-morph="Gr,V,IEA1,,P,"\w*
\w τοῖς|lemma="ὁ" strong="G35880" x-morph="Gr,EA,,,,DMP,"\w*
\w ὀφθαλμοῖς|lemma="ὀφθαλμός" strong="G37880" x-morph="Gr,N,,,,,DMP,"\w*
\w ἡμῶν|lemma="ἐγώ" strong="G14730" x-morph="Gr,RP,,,1G,P,"\w*,
\w ὃ|lemma="ὅς" strong="G37390" x-morph="Gr,RR,,,,ANS,"\w*
\w ἐθεασάμεθα|lemma="θεάομαι" strong="G23000" x-morph="Gr,V,IAM1,,P,"\w*,
\w καὶ|lemma="καί" strong="G25320" x-morph="Gr,CC,,,,,,,,"\w*
\w αἱ|lemma="ὁ" strong="G35880" x-morph="Gr,EA,,,,NFP,"\w*
\w χεῖρες|lemma="χείρ" strong="G54950" x-morph="Gr,N,,,,,NFP,"\w*
\w ἡμῶν|lemma="ἐγώ" strong="G14730" x-morph="Gr,RP,,,1G,P,"\w*
\w ἐψηλάφησαν|lemma="ψηλαφάω" strong="G55840" x-morph="Gr,V,IAA3,,P,"\w*,
\w περὶ|lemma="περί" strong="G40120" x-morph="Gr,P,,,,,G,,,"\w*
\w τοῦ|lemma="ὁ" strong="G35880" x-morph="Gr,EA,,,,GMS,"\w*
\w λόγου|lemma="λόγος" strong="G30560" x-morph="Gr,N,,,,,GMS,"\w*
\w τῆς|lemma="ὁ" strong="G35880" x-morph="Gr,EA,,,,GFS,"\w*
\w ζωῆς|lemma="ζωή" strong="G22220" x-morph="Gr,N,,,,,GFS,"\w*—
```

And here is a literal English translation that maps to that UGNT:

```
\id 1JN EN_ULT en_English_ltr Tue Aug 16 2022 11:47:12 GMT-0400 (Eastern Daylight Time) tc
\usfm 3.0
\ide UTF-8
\h 1 John
\toc1 The First Letter of John
\toc2 First John
\toc3 1Jn
\mt First John
\c 1
\p
\v 1 \zaln-s |x-strong="G37390" x-lemma="ὅς" x-morph="Gr,RR,,,,NNS," x-occurrence="1" x-occurrences="4" x-content="ὃ"\*\w What|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G15100" x-lemma="εἰμί" x-morph="Gr,V,IIA3,,S," x-occurrence="1" x-occurrences="1" x-content="ἦν"\*\w was|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G05750" x-lemma="ἀπό" x-morph="Gr,P,,,,,G,,," x-occurrence="1" x-occurrences="1" x-content="ἀπ’"\*\w from|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G07460" x-lemma="ἀρχή" x-morph="Gr,N,,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="ἀρχῆς"\*\w the|x-occurrence="1" x-occurrences="2"\w*
\w beginning|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*,
\zaln-s |x-strong="G37390" x-lemma="ὅς" x-morph="Gr,RR,,,,ANS," x-occurrence="2" x-occurrences="4" x-content="ὃ"\*\w which|x-occurrence="1" x-occurrences="3"\w*\zaln-e\*
\zaln-s |x-strong="G01910" x-lemma="ἀκούω" x-morph="Gr,V,IEA1,,P," x-occurrence="1" x-occurrences="1" x-content="ἀκηκόαμεν"\*\w we|x-occurrence="1" x-occurrences="3"\w*
\w have|x-occurrence="1" x-occurrences="4"\w*
\w heard|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*,
\zaln-s |x-strong="G37390" x-lemma="ὅς" x-morph="Gr,RR,,,,ANS," x-occurrence="3" x-occurrences="4" x-content="ὃ"\*\w which|x-occurrence="2" x-occurrences="3"\w*\zaln-e\*
\zaln-s |x-strong="G37080" x-lemma="ὁράω" x-morph="Gr,V,IEA1,,P," x-occurrence="1" x-occurrences="1" x-content="ἑωράκαμεν"\*\w we|x-occurrence="2" x-occurrences="3"\w*
\w have|x-occurrence="2" x-occurrences="4"\w*
\w seen|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,DMP," x-occurrence="1" x-occurrences="1" x-content="τοῖς"\*\zaln-s |x-strong="G37880" x-lemma="ὀφθαλμός" x-morph="Gr,N,,,,,DMP," x-occurrence="1" x-occurrences="1" x-content="ὀφθαλμοῖς"\*\w with|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*\zaln-e\*
\zaln-s |x-strong="G14730" x-lemma="ἐγώ" x-morph="Gr,RP,,,1G,P," x-occurrence="1" x-occurrences="2" x-content="ἡμῶν"\*\w our|x-occurrence="1" x-occurrences="2"\w*\zaln-e\*
\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,DMP," x-occurrence="1" x-occurrences="1" x-content="τοῖς"\*\zaln-s |x-strong="G37880" x-lemma="ὀφθαλμός" x-morph="Gr,N,,,,,DMP," x-occurrence="1" x-occurrences="1" x-content="ὀφθαλμοῖς"\*\w eyes|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*\zaln-e\*,
\zaln-s |x-strong="G37390" x-lemma="ὅς" x-morph="Gr,RR,,,,ANS," x-occurrence="4" x-occurrences="4" x-content="ὃ"\*\w which|x-occurrence="3" x-occurrences="3"\w*\zaln-e\*
\zaln-s |x-strong="G23000" x-lemma="θεάομαι" x-morph="Gr,V,IAM1,,P," x-occurrence="1" x-occurrences="1" x-content="ἐθεασάμεθα"\*\w we|x-occurrence="3" x-occurrences="3"\w*
\w have|x-occurrence="3" x-occurrences="4"\w*
\w looked|x-occurrence="1" x-occurrences="1"\w*
\w at|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G25320" x-lemma="καί" x-morph="Gr,CC,,,,,,,," x-occurrence="1" x-occurrences="1" x-content="καὶ"\*\w and|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G14730" x-lemma="ἐγώ" x-morph="Gr,RP,,,1G,P," x-occurrence="2" x-occurrences="2" x-content="ἡμῶν"\*\w our|x-occurrence="2" x-occurrences="2"\w*\zaln-e\*
\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,NFP," x-occurrence="1" x-occurrences="1" x-content="αἱ"\*\zaln-s |x-strong="G54950" x-lemma="χείρ" x-morph="Gr,N,,,,,NFP," x-occurrence="1" x-occurrences="1" x-content="χεῖρες"\*\w hands|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*\zaln-e\*
\zaln-s |x-strong="G55840" x-lemma="ψηλαφάω" x-morph="Gr,V,IAA3,,P," x-occurrence="1" x-occurrences="1" x-content="ἐψηλάφησαν"\*\w have|x-occurrence="4" x-occurrences="4"\w*
\w touched|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*,
\zaln-s |x-strong="G40120" x-lemma="περί" x-morph="Gr,P,,,,,G,,," x-occurrence="1" x-occurrences="1" x-content="περὶ"\*\w regarding|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,GMS," x-occurrence="1" x-occurrences="1" x-content="τοῦ"\*\w the|x-occurrence="2" x-occurrences="2"\w*\zaln-e\*
\zaln-s |x-strong="G30560" x-lemma="λόγος" x-morph="Gr,N,,,,,GMS," x-occurrence="1" x-occurrences="1" x-content="λόγου"\*\w Word|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*
\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="τῆς"\*\zaln-s |x-strong="G22220" x-lemma="ζωή" x-morph="Gr,N,,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="ζωῆς"\*\w of|x-occurrence="1" x-occurrences="1"\w*
\w life|x-occurrence="1" x-occurrences="1"\w*\zaln-e\*\zaln-e\*—
```

That one verse says "What was from the beginning, which we have heard, which we have seen with our eyes, which we have looked at and our hands have touched, regarding the Word of life—",
although you might have struggled to see that above.
However, it has the advantage that each English word can be linked to a Strongs lexicon,
and also directly linked to the word or words that it's translated from.

So in the age of hyperlinks and interactive displays,
USFM has moved from human-readable to unreadable.
But that's not the biggest problem, because we can use software
(as I did) to display the readable text.
(In this case, the plain text is viewable [here](https://door43.org/u/unfoldingWord/en_ult/master/63-1JN.html#062-ch-001).)

The bigger problem is that the USFM is now very bulky and takes too much time
to transport across the internet,
and worse still, too much computer power (whether in the server or in the client) to parse that file
ready to display it to the user.
Those alignment fields (zaln) are quite complex, because sometimes one Greek word
translates to multiple English words (which might not be contiguous in the fluent English text),
and sometimes one English word comes from multiple Greek words
(and it's not uncommon for those Greek words to also be non-contiguous).

Note also that this aligned/tagged USFM required the use of user-extensions to the
[USFM spec](https://ubsicap.github.io/usfm/)
with custom z markers (\zaln milestones) and several custom x- atttributes.
Note also that the original text files (Greek above) uses the _strong_ attribute
but the field is not a standard Strongs number (it has an additional digit appended at the end).

Even though it's loadable in traditional Bible editors,
the use of custom USFM extensions also makes _editing_ of these aligned/tagged texts
VERY complex.

## Summary and Conclusion

So in summary, aligned/tagged USFM is currently too complex to be human-readable
(so we might as well forget trying?), and too long and complex to be performant
to download and parse quickly on client computers (which might be an old phone).

Hence we propose a need for another look at aligned/tagged Bible formats
where we must consider verbosity and performance factors.
