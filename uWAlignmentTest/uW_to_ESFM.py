#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# uW_to_ESFM.py
#
# Module handling uW_to_ESFM functions
#
# Copyright (C) 2023 Robert Hunt
# Author: Robert Hunt <Freely.Given.org+BOS@gmail.com>
# License: See gpl-3.0.txt
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Module handling uW_to_ESFM functions.
"""
from gettext import gettext as _
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import os
import shutil
import glob
import logging

import sys
sys.path.append( '../../BibleOrgSys/' )
import BibleOrgSys.BibleOrgSysGlobals as BibleOrgSysGlobals
from BibleOrgSys.BibleOrgSysGlobals import fnPrint, vPrint, dPrint


LAST_MODIFIED_DATE = '2023-02-09' # by RJH
SHORT_PROGRAM_NAME = "uW_to_ESFM"
PROGRAM_NAME = "uW Aligned Bible to ESFM"
PROGRAM_VERSION = '0.02'
PROGRAM_NAME_VERSION = f'{SHORT_PROGRAM_NAME} v{PROGRAM_VERSION}'

DEBUGGING_THIS_MODULE = False
ALL_PRODUCTION_BOOKS = True # Set to False for a faster test build

# UW_SOURCE_FOLDER = Path( 'uWSourceFiles/' )
UGNT_USFM_SOURCE_FOLDER = Path( '../../OpenBibleData/copiedBibles/Original/unfoldingWord.org/UGNT/' )
ULT_USFM_SOURCE_FOLDER = Path( '../../OpenBibleData/copiedBibles/English/unfoldingWord.org/ULT/' )
ESFM_DESTINATION_FOLDER = Path( 'ESFMFiles/' )
UGNT_ESFM_DESTINATION_FOLDER = ESFM_DESTINATION_FOLDER.joinpath( 'UGNT/' )
ULT_ESFM_DESTINATION_FOLDER = ESFM_DESTINATION_FOLDER.joinpath( 'ULT/' )
DEBUG_DESTINATION_FOLDER = Path( 'Test/')
BOOK_LIST = ['TIT','JN3']


class State:
    pass
# end of State class

state = State()


def uW_to_ESFM() -> bool:
    """
    """
    fnPrint( DEBUGGING_THIS_MODULE, "uW_to_ESFM()")

    for BBB in BOOK_LIST:
        UGNTWordList = UGNT_to_ESFM( BBB )
        ULT_to_ESFM( BBB, UGNTWordList )
# end of uW_to_ESFM.uW_to_ESFM


def UGNT_to_ESFM( BBB:str ) -> bool:
    """
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"UGNT_to_TSV( {BBB} )" )

    grkWordFilename, grkWordList = UGNT_to_TSV( BBB )

    UUU = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMAbbreviation( BBB ).upper()
    bookNumberStr = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMNumStr( BBB )
    inputFilepath = UGNT_USFM_SOURCE_FOLDER.joinpath( f'{bookNumberStr}-{UUU}.usfm' )
    outputFilepath = UGNT_ESFM_DESTINATION_FOLDER.joinpath( f'{BBB}.ESFM' )
    with open( inputFilepath, 'rt', encoding='utf-8' ) as ugnt_input_file:
        usfm_text = ugnt_input_file.read()

    lines = adjustOriginalWords( BBB, usfm_text.split('\n'), grkWordList )
    with open( outputFilepath, 'wt', encoding='utf-8' ) as esfm_output_file:
        esfm_output_file.write( f'{USFM_to_ESFM( BBB, lines, grkWordFilename )}\n' )

    return grkWordList
# end of uW_to_ESFM.UGNT_to_ESFM


def UGNT_to_TSV( BBB:str ) -> Tuple[str,List[Tuple[str,str,str]]]:
    """
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"UGNT_to_TSV( {BBB} )" )

    UUU = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMAbbreviation( BBB ).upper()
    bookNumberStr = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMNumStr( BBB )
    inputFilepath = UGNT_USFM_SOURCE_FOLDER.joinpath( f'{bookNumberStr}-{UUU}.usfm' )
    filename = f'{BBB}.tsv'
    outputFilepath = UGNT_ESFM_DESTINATION_FOLDER.joinpath( filename )
    with open( inputFilepath, 'rt', encoding='utf-8' ) as ugnt_input_file, open( outputFilepath, 'wt', encoding='utf-8' ) as tsv_output_file:
        tsv_output_file.write( 'C\tV\tWord\tPrevious\tNext\tLemma\tESN\tRole\tMorphology\n')
        word_list = []
        for usfm_line in ugnt_input_file:
            usfm_line = usfm_line.rstrip( '\n' )
            if not usfm_line: continue
            assert usfm_line.startswith( '\\' )
            usfm_line = usfm_line[1:] # Remove the leading backslash
            try: marker, rest = usfm_line.split( ' ', 1 )
            except ValueError: marker, rest = usfm_line, ''
            # print( f"{marker=} {rest=}")
            if marker in ('id','usfm','ide', 'h', 'toc1','toc2','toc3'):
                assert rest
                continue # We don't need these
            elif marker in ('mt','mt1','mt2', 'rem'):
                assert rest
                continue # We don't need these
            elif marker == 'c':
                assert rest
                V = '0'
                C = rest
                # if C=='2': halt
                assert C.isdigit()
            elif marker == 'v':
                assert rest
                try: V, rest = rest.split( ' ', 1 )
                except ValueError: V, rest = rest, ''
                assert V.isdigit(), f"Expected a verse number digit with '{V=}' '{rest=}'"
                assert not rest # UGNT has nothing else on v lines
            elif marker == 'p':
                assert not rest
                prev = '¶'
            elif marker == 'w':
                # print( f"{BBB} {C}:{V} Got word '{rest}'")
                assert rest
                assert rest.count( '|' ) == 1
                assert rest.count( '\\w*' ) == 1
                word, rest = rest.split( '|', 1 )
                if rest[-1] == '*': next = ''
                else:
                    assert rest[-2] == '*'
                    next, rest = rest[-1], rest[:-1]
                assert next in ',.?!;:—', f"{BBB} {C}:{V} {next=}"
                bits = rest.replace( '\\w*', '', 1 ).split( ' ' )
                assert len( bits ) == 3
                lemma = bits[0].replace( 'lemma="' , '', 1 ).replace( '"' , '', 1 )
                assert '"' not in lemma
                esn = bits[1].replace( 'strong="' , '', 1 ).replace( '"' , '', 1 )
                assert '"' not in esn # extended Strongs number
                morph = bits[2].replace( 'x-morph="' , '', 1 ).replace( '"' , '', 1 )
                assert '"' not in morph
                assert morph.startswith( 'Gr,' )
                morph = morph[3:] # We know that it's Greek
                role, morph = morph.split( ',', 1 )
                # print( f"{BBB} {C}:{V} {word=} {next=} {lemma=} {esn=} {role=} {morph=}")
                tsv_output_file.write( f'{C}\t{V}\t{word}\t{prev}\t{next}\t{lemma}\t{esn}\t{role}\t{morph}\n')
                word_list.append( (C,V,word) )
                prev = ''
            else:
                logging.critical( f"{BBB} {C}:{V} UGNT has unexpected USFM marker: \\{marker}='{rest}'" )
                raise Exception( f"Unexpected UGNT USFM marker {BBB} {C}:{V} \\{marker}='{rest}'" )
    assert next != ' ' # Book should end with punctuation
    vPrint( 'Normal', DEBUGGING_THIS_MODULE, f"  Wrote {len(word_list):,} {BBB} UGNT words to {outputFilepath}." )
    return filename, word_list
# end of uW_to_ESFM.UGNT_to_TSV


def ULT_to_ESFM( BBB:str, grkWordList:List[Tuple[str,str,str]] ) -> bool:
    """
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"ULT_to_ESFM( {BBB} )" )

    alignmentList = ULT_to_TSV( BBB, grkWordList )

    UUU = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMAbbreviation( BBB ).upper()
    bookNumberStr = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMNumStr( BBB )
    inputFilepath = ULT_USFM_SOURCE_FOLDER.joinpath( f'{bookNumberStr}-{UUU}.usfm' )
    outputFilepath = ULT_ESFM_DESTINATION_FOLDER.joinpath( f'{BBB}.ESFM' )
    with open( inputFilepath, 'rt', encoding='utf-8' ) as aligned_translation_usfm_input_file:
        usfm_text = aligned_translation_usfm_input_file.read()

    lines = adjustAlignedWords( BBB, usfm_text.split('\n'), alignmentList )
    with open( outputFilepath, 'wt', encoding='utf-8' ) as esfm_output_file:
        esfm_output_file.write( f'{USFM_to_ESFM( BBB, lines )}\n' )
# end of uW_to_ESFM.ULT_to_ESFM


def ULT_to_TSV( BBB:str, originalLgBookWordList:List[Tuple[str,str,str]] ) -> List[Tuple[str,str,str,List[Tuple[List[Tuple[str,str,str]],List[Tuple[str,str,str]]]]]]:
    """
    originalLgBookWordList contains a list of 3-tuples: C,V,grkWord
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"ULT_to_TSV( {BBB} )" )

    # First load of all the alignment data for the book into a large list
    UUU = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMAbbreviation( BBB ).upper()
    bookNumberStr = BibleOrgSysGlobals.loadedBibleBooksCodes.getUSFMNumStr( BBB )
    inputFilepath = ULT_USFM_SOURCE_FOLDER.joinpath( f'{bookNumberStr}-{UUU}.usfm' )
    with open( inputFilepath, 'rt', encoding='utf-8' ) as ult_input_file:
        # TODO: What about unaligned words
        bookAlignments = []
        C = V = '0'
        word_fields = ''
        for usfm_line in ult_input_file:
            usfm_line = usfm_line.rstrip( '\n' )
            if not usfm_line: continue
            # print( f"{BBB} {C}:{V} {usfm_line=}" )
            assert usfm_line.startswith( '\\' )
            usfm_line = usfm_line[1:] # Remove the leading backslash
            try: marker, rest = usfm_line.split( ' ', 1 )
            except ValueError: marker, rest = usfm_line, ''
            # print( f"{marker=} {rest=}")
            if marker in ('id','usfm','ide', 'h', 'toc1','toc2','toc3'):
                assert rest
                continue # We don't need these
            elif marker in ('mt','mt1','mt2', 'rem'):
                assert rest
                continue # We don't need these
            elif marker == 'c':
                if word_fields:
                    # print( f"At c: need to process {word_fields}")
                    bookAlignments.append( (C,V,parse_aligned_word_fields( f'{BBB}_{C}:{V}', word_fields)) )
                    word_fields = ''
                assert rest
                V = '0'
                C = rest
                # if C=='2': halt
                assert C.isdigit()
            elif marker == 'v':
                if word_fields:
                    # print( f"At v: need to process {word_fields}")
                    bookAlignments.append( (C,V,parse_aligned_word_fields( f'{BBB}_{C}:{V}', word_fields)) )
                    word_fields = ''
                assert rest
                try: V, rest = rest.split( ' ', 1 )
                except ValueError: V, rest = rest, ''
                assert V.isdigit(), f"Expected a verse number digit with '{V=}' '{rest=}'"
                if rest:
                    word_fields = f'{word_fields} {rest}'
            elif marker == 'ts\\*':
                assert not rest
                continue # We don't need these here
            elif marker == 'p':
                prev = '¶'
            elif marker in ('w','zaln-s'):
                # print( f"{BBB} {C}:{V} Got word '{rest}'")
                assert rest
                word_fields = f'{word_fields} \\{marker} {rest}'
            else:
                logging.critical( f"{BBB} {C}:{V} ULT has unexpected USFM marker: \\{marker}='{rest}'" )
    bookAlignments.append( (C,V,parse_aligned_word_fields( f'{BBB}_{C}:{V}', word_fields)) )
    assert next != ' ' # Book should end with punctuation
    # print( f"{bookAlignments[-2:]=}" )

    # Now normalise the alignments -- seems uW alignments can unnecessarily repeat a zaln field
    #   for the same Greek word
    normalisedAlignments = []
    normalisedCount = 0
    for c,v,verseAlignments in bookAlignments:
        normalisedVerseAlignments = []
        lastOriginalWordTuple = None
        for verseOriginalWordList,verseTranslatedWordList in verseAlignments:
            if len(verseOriginalWordList) == 1:
                originalWordTuple = verseOriginalWordList[0]
                if originalWordTuple == lastOriginalWordTuple:
                    lastTranslatedWordList += verseTranslatedWordList
                    normalisedCount += 1
                else:
                    normalisedVerseAlignments.append( (verseOriginalWordList,verseTranslatedWordList) )
                lastOriginalWordTuple = originalWordTuple
                lastTranslatedWordList = verseTranslatedWordList
            else: # not sure if we need to do any normalising here ???
                lastOriginalWordTuple = None
                normalisedVerseAlignments.append( (verseOriginalWordList,verseTranslatedWordList) )
        # print( c, v, ([],None) in normalisedVerseAlignments, len(normalisedVerseAlignments), normalisedVerseAlignments )
        if ([],None) in normalisedVerseAlignments: halt
        normalisedAlignments.append( (c,v,normalisedVerseAlignments) )
    vPrint( 'Normal', DEBUGGING_THIS_MODULE, f"  {BBB} {normalisedCount:,} alignment pairs combined")
    # print( f"({len(normalisedAlignments)}) {normalisedAlignments[0]}" ); halt
    # print( ([],None) in normalisedAlignments, len(normalisedAlignments), normalisedAlignments )
    if ([],None) in normalisedAlignments: halt
    # print( f"{normalisedAlignments[-2:]=}" )

    # Now write the alignment data for the book into a TSV file
    outputFilepath = ULT_ESFM_DESTINATION_FOLDER.joinpath( f'{BBB}.tsv' )
    with open( outputFilepath, 'wt', encoding='utf-8' ) as tsv_output_file:
        tsv_output_file.write( 'C\tV\tWord\tOrigRows\tPrevious\tNext\tLemma\tESN\tRole\tMorphology\n')
        # print( len(normalisedAlignments[0]), normalisedAlignments[0] )
        # We want a line for each English word (even unaligned ones)
        originalLgStartIndex = 0
        for c,v,verseAlignments in normalisedAlignments:
            # print( f"\n\n\n{BBB} {c}:{v} ({len(verseAlignments)}) {verseAlignments}")
            # Find the original language words for this verse
            for n,(oC,oV,oWrd) in enumerate( originalLgBookWordList[originalLgStartIndex:] ):
                if n == 0: assert oC==c and oV==v
                if oC!=c or oV!=v: break # gone on to the next verse
            else: # at end of book
                n += 1 # Ensure that we get the final entry
                assert originalLgStartIndex + n == len(originalLgBookWordList)
            originalLgEndIndex = originalLgStartIndex + n
            for verseOriginalWordList,verseTranslatedWordList in verseAlignments:
                # print( f"\n   {verseOriginalWordList}   {verseTranslatedWordList} {originalLgBookWordList[originalLgStartIndex:originalLgEndIndex]}" )
                # grkEntry = grkWordList[originalIndex]
                # print( f"   {originalWordList}   {translatedWordList}   {grkEntry}")
                originalWordIndexes = []
                for originalLgWord,occurrence,numOccurrences in verseOriginalWordList:
                    # print( f"        {originalLgWord=} {occurrence}/{numOccurrences}")

                    # Find the TSV row number of this original language word
                    foundOccurrence = 0
                    for n,(oC,oV,oWrd) in enumerate( originalLgBookWordList[originalLgStartIndex:originalLgEndIndex] ):
                        # print( f"  {originalLgWord=} {oC=} {oV=} {oWrd=} {occurrence=} {numOccurrences=}")
                        if oWrd == originalLgWord:
                            foundOccurrence += 1
                            assert foundOccurrence <= numOccurrences
                            # print( f"    {originalLgWord=} {oWrd=} {foundOccurrence=} {occurrence=} {numOccurrences=}")
                            if foundOccurrence == occurrence:
                                break
                    else:
                        print( f"{originalLgStartIndex=} {originalLgEndIndex=} {len(originalLgBookWordList)=}" )
                        failed
                    originalWordIndexes.append( str( originalLgStartIndex + n + 1 ) )
                originalWordIndexesStr = ';'.join( originalWordIndexes )
                # print( f"        Got {verseOriginalWordList=} -> {originalWordIndexesStr=}")

                for translatedWordEntry in verseTranslatedWordList:
                    tsvEntry = f'{c}\t{v}\t{translatedWordEntry[0]}\t{originalWordIndexesStr}\t\t\t\t\t\t\n'
                    # print( f"    {tsvEntry=}" )
                    tsv_output_file.write( f'{c}\t{v}\t{translatedWordEntry[0]}\t{originalWordIndexesStr}\t\t\t\t\t\t\n' )
            originalLgStartIndex = originalLgEndIndex
    vPrint( 'Normal', DEBUGGING_THIS_MODULE, f"  Wrote {len(normalisedAlignments):,} {BBB} ULT aligned words to {outputFilepath}." )
    return normalisedAlignments
# end of uW_to_ESFM.ULT_to_TSV


def parse_aligned_word_fields( ref:str, fields:str ) -> List[Tuple[List[Tuple[str,str,str]],List[Tuple[str,str,str]]]]:
    """
    Parse a chunk that might contain zaln milestones and w fields
        and produce a table

    e.g., \\zaln-s |x-strong="G39720" x-lemma="Παῦλος" x-morph="Gr,N,,,,,NMS," x-occurrence="1" x-occurrences="1" x-content="Παῦλος"\\*\\w Paul|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\*, \\zaln-s |x-strong="G14010" x-lemma="δοῦλος" x-morph="Gr,N,,,,,NMS," x-occurrence="1" x-occurrences="1" x-content="δοῦλος"\\*\\w a|x-occurrence="1" x-occurrences="1"\\w* \\w servant|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G23160" x-lemma="θεός" x-morph="Gr,N,,,,,GMS," x-occurrence="1" x-occurrences="2" x-content="Θεοῦ"\\*\\w of|x-occurrence="1" x-occurrences="5"\\w* \\w God|x-occurrence="1" x-occurrences="2"\\w*\\zaln-e\\* \\zaln-s |x-strong="G11610" x-lemma="δέ" x-morph="Gr,CC,,,,,,,," x-occurrence="1" x-occurrences="1" x-content="δὲ"\\*\\w and|x-occurrence="1" x-occurrences="2"\\w*\\zaln-e\\* \\zaln-s |x-strong="G06520" x-lemma="ἀπόστολος" x-morph="Gr,N,,,,,NMS," x-occurrence="1" x-occurrences="1" x-content="ἀπόστολος"\\*\\w an|x-occurrence="1" x-occurrences="1"\\w* \\w apostle|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G24240" x-lemma="Ἰησοῦς" x-morph="Gr,N,,,,,GMS," x-occurrence="1" x-occurrences="1" x-content="Ἰησοῦ"\\*\\w of|x-occurrence="2" x-occurrences="5"\\w* \\w Jesus|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G55470" x-lemma="χριστός" x-morph="Gr,N,,,,,GMS," x-occurrence="1" x-occurrences="1" x-content="Χριστοῦ"\\*\\w Christ|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\*, \\zaln-s |x-strong="G25960" x-lemma="κατά" x-morph="Gr,P,,,,,A,,," x-occurrence="1" x-occurrences="1" x-content="κατὰ"\\*\\w for|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G41020" x-lemma="πίστις" x-morph="Gr,N,,,,,AFS," x-occurrence="1" x-occurrences="1" x-content="πίστιν"\\*\\w the|x-occurrence="1" x-occurrences="3"\\w* \\w faith|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G15880" x-lemma="ἐκλεκτός" x-morph="Gr,NS,,,,GMP," x-occurrence="1" x-occurrences="1" x-content="ἐκλεκτῶν"\\*\\w of|x-occurrence="3" x-occurrences="5"\\w*\\zaln-e\\* \\zaln-s |x-strong="G15880" x-lemma="ἐκλεκτός" x-morph="Gr,NS,,,,GMP," x-occurrence="1" x-occurrences="1" x-content="ἐκλεκτῶν"\\*\\w the|x-occurrence="2" x-occurrences="3"\\w* \\w chosen|x-occurrence="1" x-occurrences="1"\\w* \\w people|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G23160" x-lemma="θεός" x-morph="Gr,N,,,,,GMS," x-occurrence="2" x-occurrences="2" x-content="Θεοῦ"\\*\\w of|x-occurrence="4" x-occurrences="5"\\w* \\w God|x-occurrence="2" x-occurrences="2"\\w*\\zaln-e\\* \\zaln-s |x-strong="G25320" x-lemma="καί" x-morph="Gr,CC,,,,,,,," x-occurrence="1" x-occurrences="1" x-content="καὶ"\\*\\w and|x-occurrence="2" x-occurrences="2"\\w*\\zaln-e\\* \\zaln-s |x-strong="G19220" x-lemma="ἐπίγνωσις" x-morph="Gr,N,,,,,AFS," x-occurrence="1" x-occurrences="1" x-content="ἐπίγνωσιν"\\*\\w knowledge|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G02250" x-lemma="ἀλήθεια" x-morph="Gr,N,,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="ἀληθείας"\\*\\w of|x-occurrence="5" x-occurrences="5"\\w*\\zaln-e\\* \\zaln-s |x-strong="G02250" x-lemma="ἀλήθεια" x-morph="Gr,N,,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="ἀληθείας"\\*\\w the|x-occurrence="3" x-occurrences="3"\\w* \\w truth|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G35880" x-lemma="ὁ" x-morph="Gr,EA,,,,GFS," x-occurrence="1" x-occurrences="1" x-content="τῆς"\\*\\w that|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G25960" x-lemma="κατά" x-morph="Gr,P,,,,,A,,," x-occurrence="1" x-occurrences="1" x-content="κατ’"\\*\\w agrees|x-occurrence="1" x-occurrences="1"\\w* \\w with|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\* \\zaln-s |x-strong="G21500" x-lemma="εὐσέβεια" x-morph="Gr,N,,,,,AFS," x-occurrence="1" x-occurrences="1" x-content="εὐσέβειαν"\\*\\w godliness|x-occurrence="1" x-occurrences="1"\\w*\\zaln-e\\*,
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"parse_aligned_word_fields( {ref} {len(fields)} {fields[:300]}... )" )

    zsCount, zeCount, zEndCount = fields.count('\\zaln-s '), fields.count('\\zaln-e'), fields.count('\\*')
    assert zsCount == zeCount, f"{ref} {zsCount=} {zeCount=} {zEndCount=}"
    assert (zsCount + zeCount) == zEndCount
    wCount, wEndCount = fields.count('\\w '), fields.count('\\w*')
    assert wCount == wEndCount
    # print( f"zaln={zsCount} Greek words, w={wCount} English words in '{fields}'")

    # Work our way along the line
    startSearchIndex = 0
    grkWord = engWord = engWords = None
    grkWords, alignList = [], []
    while True:
        ixBS = fields.find( '\\', startSearchIndex )
        if ixBS == -1: break
        if fields[ixBS:].startswith( '\\zaln-s |' ):
            ixEnd = fields.find( '\\*', ixBS+9 )
            assert ixEnd != -1
            grkField = fields[ixBS+9:ixEnd]
            assert '\\' not in grkField and '|' not in grkField and '*' not in grkField
            grkBits = grkField.split( ' ' )
            # print( f"  {len(grkBits)} {grkBits}")
            assert len(grkBits) == 6
            assert grkBits[3].startswith( 'x-occurrence="' ) and grkBits[3][-1] == '"'
            assert grkBits[4].startswith( 'x-occurrences="' ) and grkBits[4][-1] == '"'
            grkOccurrence, grkOccurrences = grkBits[3][14:-1], grkBits[4][15:-1]
            assert grkBits[5].startswith( 'x-content="' ) and grkBits[5][-1] == '"'
            # We ignore ESN([0]), lemma([1]), morph([2]) which are all duplicated information
            grkWord = grkBits[5][11:-1]
            # print( f"    {grkWord=}" )
            grkWords.append( (grkWord,int(grkOccurrence),int(grkOccurrences)) )
            # print( f"    {grkWords=}" )
            engWords = []
            startSearchIndex = ixEnd + 2
        elif fields[ixBS:].startswith( '\\w ' ):
            engWord = ''
            ixEnd = fields.find( '\\w*', ixBS+3 )
            assert ixEnd != -1
            engField = fields[ixBS+3:ixEnd]
            assert '\\' not in engField and '*' not in engField and engField.count('|')==1
            engWord, engField = engField.split( '|', 1 )
            engBits = engField.split( ' ' )
            # print( f"  {len(engBits)} {engBits}")
            assert len(engBits) == 2
            assert engBits[0].startswith( 'x-occurrence="' ) and engBits[0][-1] == '"'
            assert engBits[1].startswith( 'x-occurrences="' ) and engBits[1][-1] == '"'
            engOccurrence, engOccurrences = engBits[0][14:-1], engBits[1][15:-1]
            # print( f"    {engWord=} {engOcurrence=} {engOccurrences=}" )
            engWords.append( (engWord,engOccurrence,engOccurrences))
            # print( f"    {engWords=}" )
            startSearchIndex = ixEnd + 3
        elif fields[ixBS:].startswith( '\\zaln-e\\*' ):
            if grkWords:
                alignList.append( (grkWords,engWords) )
            else: assert not engWords
            # if len(grkWords) > 1: halt
            grkWord = engWord = engWords = None
            grkWords = []
            startSearchIndex = ixBS + 9
        # For these footnote fields, just note then ignore them
        elif fields[ixBS:].startswith( '\\f ' ):
            ixEnd = fields.find( '\\f*', ixBS+3 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 3
        elif fields[ixBS:].startswith( '\\ft ' ):
            ixEnd = fields.find( '\\f*', ixBS+4 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 4
        elif fields[ixBS:].startswith( '\\fq ' ):
            ixEnd = fields.find( '\\f*', ixBS+4 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 4
        elif fields[ixBS:].startswith( '\\fq*' ):
            ixEnd = fields.find( '\\f*', ixBS+4 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 4
        elif fields[ixBS:].startswith( '\\fqa ' ):
            ixEnd = fields.find( '\\f*', ixBS+5 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 5
        elif fields[ixBS:].startswith( '\\fqa*' ):
            ixEnd = fields.find( '\\f*', ixBS+5 )
            assert ixEnd != -1
            startSearchIndex = ixBS + 5
        elif fields[ixBS:].startswith( '\\f*' ):
            startSearchIndex = ixBS + 3
        else:
            assert False, f"unexpected field {ref} {fields[ixBS:]}"
    assert ([],None) not in alignList
    return alignList
# end of uW_to_ESFM.parse_aligned_word_fields


def USFM_to_ESFM( BBB:str, lines:List[str], wordFilename:Optional[str]=None ) -> str:
    """
    Takes an entire USFM book contents and returns a normalised ESFM version.
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"USFM_to_ESFM( {BBB} {len(lines)} {lines[0]} )" )

    assert lines[0].startswith( '\\id ' )
    usfm_book_code = lines[0][4:7]
    fileBBBFromIdLine = BibleOrgSysGlobals.loadedBibleBooksCodes.getBBBFromUSFMAbbreviation( usfm_book_code )
    assert fileBBBFromIdLine == BBB
    assert fileBBBFromIdLine in BibleOrgSysGlobals.loadedBibleBooksCodes, f"{BBB=} {usfm_book_code=} {fileBBBFromIdLine=}"

    assumedWorkName = lines[0][8:].strip()
    # print( f"{usfm_book_code} {assumedWorkName=}" )
    # Rebuild the id line
    lines[0] = f'\\id {usfm_book_code} - {assumedWorkName}' if assumedWorkName else f'\\id {usfm_book_code}'
    ix = lines[0].find( ' v' )
    if ix==-1 or not lines[0][ix+2].isdigit(): # Seems no version number field
        lines[0] = f'{lines[0].rstrip()} v0.0.0'

    assert lines[1].startswith( '\\usfm ' )
    assert lines[1] == '\\usfm 3.0'
    assert lines[2].startswith( '\\ide ' )
    assert lines[2] == '\\ide UTF-8'
    assert lines[3].startswith( '\\h ' )

    lines.insert( 3, f'\\rem ESFM v0.5 {BBB}' )
    if wordFilename:
        lines.insert( 4, f'\\rem WORDTABLE {wordFilename}' )

    return normalise_USFM_markers_to_ESFM( '\n'.join( lines ) )
# end of uW_to_ESFM.USFM_to_ESFM


def adjustOriginalWords( BBB:str, usfmLines:List[str], wordList:List[Tuple[str,str,str]] ) -> str:
    """
    Adjust \\w fields in an original language book to point to the TSV rows.
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"adjustOriginalWords( {len(usfmLines)} {len(wordList)} )" )

    C = V = '0'
    wordListIndex = 0
    newList = []
    for usfm_line in usfmLines:
        if not usfm_line: continue
        assert usfm_line.startswith( '\\' )
        usfm_line = usfm_line[1:] # Remove the leading backslash
        try: marker, rest = usfm_line.split( ' ', 1 )
        except ValueError: marker, rest = usfm_line, ''
        # print( f"{marker=} {rest=}")
        if marker in ('id','usfm','ide', 'h', 'toc1','toc2','toc3',
                    'mt','mt1','mt2', 'rem'):
            assert rest
            newList.append( f'\\{marker} {rest}' )
        elif marker == 'c':
            assert rest
            V = '0'
            C = rest
            # if C=='2': halt
            assert C.isdigit()
            newList.append( f'\\c {rest}' )
        elif marker == 'v':
            assert rest
            try: V, rest = rest.split( ' ', 1 )
            except ValueError: V, rest = rest, ''
            assert V.isdigit(), f"Expected a verse number digit with '{V=}' '{rest=}'"
            newList.append( f'\\v {V} {rest}' )
        elif marker in ('p',):
            newList.append( f'\\{marker} {rest}' if rest else f'\\{marker}' )
        elif marker == 'w':
            # print( f"{BBB} {C}:{V} Got word '{rest}'")
            assert rest
            assert rest.count( '|' ) == 1
            assert rest.count( '\\w*' ) == 1
            word, rest = rest.split( '|', 1 )
            if rest[-1] == '*': next = ''
            else:
                assert rest[-2] == '*'
                next, rest = rest[-1], rest[:-1]
            assert next in ',.?!;:—', f"{BBB} {C}:{V} {next=}"
            bits = rest.replace( '\\w*', '', 1 ).split( ' ' )
            assert len( bits ) == 3, f"{bits=}"
            lemma = bits[0].replace( 'lemma="' , '', 1 ).replace( '"' , '', 1 )
            assert '"' not in lemma
            esn = bits[1].replace( 'strong="' , '', 1 ).replace( '"' , '', 1 )
            assert '"' not in esn # extended Strongs number
            morph = bits[2].replace( 'x-morph="' , '', 1 ).replace( '"' , '', 1 )
            assert '"' not in morph
            assert morph.startswith( 'Gr,' )
            morph = morph[3:] # We know that it's Greek
            role, morph = morph.split( ',', 1 )
            # print( f"{BBB} {C}:{V} {word=} {next=} {lemma=} {esn=} {role=} {morph=}")
            wordListIndex += 1
            newList[-1] = f"{newList[-1]}{'' if newList[-1][-1]==' ' else ' '}\\w {word}|{wordListIndex}\\w*{next}"
        else:
            logging.critical( f"{BBB} {C}:{V} original has unexpected USFM marker: \\{marker}='{rest}'" )
    assert wordListIndex == len(wordList)
    return newList
# end of uW_to_ESFM.adjustOriginalWords


def adjustAlignedWords( BBB:str, usfmLines:List[str], alignmentList:List[Tuple[str,str,str,List[Tuple[List[Tuple[str,str,str]],List[Tuple[str,str,str]]]]]] ) -> str:
    """
    Adjust \\w fields in a translated book to point to the TSV rows.
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"adjustAlignedWords( {len(usfmLines)} {len(alignmentList)} )" )
    # print( f"\nadjustAlignedWords( {BBB} ({len(usfmLines)}) ) alignment keys =", [f'{l[0]}_{l[1]}:{l[2]}' for l in alignmentList] )

    # Check for duplicate CV entries
    lastBCV = None
    for alignmentEntry in alignmentList:
        BCV = f'{alignmentEntry[0]}_{alignmentEntry[1]}:{alignmentEntry[2]}'
        assert BCV != lastBCV # Pretty sure this could happen
        lastBCV = BCV
    # print( f'{alignmentList[0]=}' )

    C = V = '0'
    rowNum = 1
    alignmentListIndex = 0
    currentVerseAlignments = alignmentList[alignmentListIndex]
    newLineList = []
    for usfm_line in usfmLines:
        if not usfm_line: continue
        assert usfm_line.startswith( '\\' )
        usfm_line = usfm_line[1:] # Remove the leading backslash
        try: marker, rest = usfm_line.split( ' ', 1 )
        except ValueError: marker, rest = usfm_line, ''
        # print( f"\nLine Loop {marker=} {rest=}")
        if marker in ('id','usfm','ide', 'h', 'toc1','toc2','toc3',
                    'mt','mt1','mt2', 'rem'):
            assert rest
            newLineList.append( f'\\{marker} {rest}' )
        elif marker == 'c':
            assert rest
            V = '0'
            C = rest
            # if C=='2': halt
            assert C.isdigit()
            newLineList.append( f'\\c {rest}' )
        elif marker == 'v':
            assert rest
            try: V, rest = rest.split( ' ', 1 )
            except ValueError: V, rest = rest, ''
            assert V.isdigit(), f"Expected a verse number digit with '{V=}' '{rest=}'"
            if currentVerseAlignments[0] != C or currentVerseAlignments[1] != V:
                alignmentListIndex += 1 # Try the next alignment
                currentVerseAlignments = alignmentList[alignmentListIndex]
                assert currentVerseAlignments[0] == C and currentVerseAlignments[1] == V
            if rest:
                marker, rest, rowNum = convertLineAlignments( BBB, C, V, marker, rest, rowNum) #, currentVerseAlignments )
                assert '\\zaln' not in rest
                assert 'x-occurrence' not in rest
                newLineList.append( f'\\v {V} {rest}' )
            else:
                newLineList.append( f'\\v {V}' )
        elif marker in ('p',):
            newLineList.append( f'\\{marker} {rest}' if rest else f'\\{marker}' )
        elif marker == 'w':
            # print( f"{BBB} {C}:{V} Got word '{rest}'")
            assert rest
            marker, rest, rowNum = convertLineAlignments( BBB, C, V, marker, rest, rowNum) #, currentVerseAlignments )
            if marker and rest:
                newLineList.append( f'\\{marker} {rest}' )
            elif rest:
                newLineList[-1] += f' {rest}'
            else: halt
        elif marker == 'zaln-s':
            # print( f"{BBB} {C}:{V} Got word '{rest}'")
            assert rest
            marker, rest, rowNum = convertLineAlignments( BBB, C, V, marker, rest, rowNum) #, currentVerseAlignments )
            if marker and rest:
                newLineList.append( f'\\{marker} {rest}' )
            elif rest:
                newLineList[-1] += f' {rest}'
            else: halt
        elif marker == 'ts\\*':
            assert not rest
            newLineList.append( '\\ts\\*' )
        else:
            logging.critical( f"{BBB} {C}:{V} aligned has unexpected USFM marker: \\{marker}='{rest}'" )
    assert alignmentListIndex == len(alignmentList)-1, f"adjustAlignedWords( {BBB} ) {alignmentListIndex=} {len(alignmentList)=}"
    # print( f"  adjustAlignedWords() returning ({len(newLineList)}) {newLineList}")
    return newLineList
# end of uW_to_ESFM.adjustAlignedWords


def convertLineAlignments( BBB:str, c:str, v:str, marker:str, rest:str, translatedWordNum:int): #, alignments:Tuple[str,str,str,List[Tuple[List[Tuple[str,str,str]],List[Tuple[str,str,str]]]]] ) -> Tuple[str,str]:
    """
    Takes a USFM line and updates \zaln and \w fields to ESFM.
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"convertLineAlignments( {marker}={rest} {translatedWordNum=} )" )
    # assert len(alignments) == 4
    # assert alignments[0]==BBB and alignments[1]==c and alignments[2]==v
    # alignments = alignments[3] # Now List[Tuple[List[Tuple[str,str,str]],List[Tuple[str,str,str]]]]

    if marker in ('w','zaln-s','zaln-e'):
        marker, rest = '', f'\\{marker} {rest}'
    # print( f"\nconvertLineAlignments( {BBB} {c}:{v} {marker}='{rest}' {translatedWordNum=}" ) # {alignments[translatedWordNum-1:]=} )" )

    # Work our way along the line
    alignmentIndex = 0
    startSearchIndex = 0
    grkWords = []
    while True:
        # print( f"  Loop {alignmentIndex=} {translatedWordNum=} {startSearchIndex=} {rest=}" )
        ixBS = rest.find( '\\', startSearchIndex )
        if ixBS == -1: break
        if rest[ixBS:].startswith( '\\zaln-s |' ):
            ixEnd = rest.find( '\\*', ixBS+9)
            assert ixEnd != -1
            grkField = rest[ixBS+9:ixEnd]
            assert '\\' not in grkField and '|' not in grkField and '*' not in grkField
            grkBits = grkField.split( ' ' )
            # print( f"  {len(grkBits)} {grkBits}")
            assert len(grkBits) == 6
            assert grkBits[3].startswith( 'x-occurrence="' ) and grkBits[3][-1] == '"'
            assert grkBits[4].startswith( 'x-occurrences="' ) and grkBits[4][-1] == '"'
            grkOccurrence, grkOccurrences = grkBits[3][14:-1], grkBits[4][15:-1]
            assert grkBits[5].startswith( 'x-content="' ) and grkBits[5][-1] == '"'
            # We ignore ESN([0]), lemma([1]), morph([2]) which are all duplicated information
            grkWord = grkBits[5][10:-1]
            grkTuple = grkWord,grkOccurrence,grkOccurrences
            # print( f"    {grkTuple=} {alignmentIndex=}" )
            # if alignmentIndex == 0: # we probably have to find the correct place in the (verse) list to start this line from
            #     for alignmentIndex,alightmentTwoTuple in enumerate( alignments):
            #         print( alignmentIndex, alightmentTwoTuple )
            #         if grkTuple in alightmentTwoTuple[0]: # found the right Greek word
            #             break
            # currentAlignment = alignments[alignmentIndex]
            # assert len(currentAlignment)==2 and len(currentAlignment[0])==1 and currentAlignment[0][0][0]==grkWord # Might be wrong at some point
            rest = f'{rest[:ixBS]}{rest[ixEnd+2:]}' # Completely remove the zaln-s field
        elif rest[ixBS:].startswith( '\\w ' ):
            engWord = ''
            ixEnd = rest.find( '\\w*', ixBS+3)
            assert ixEnd != -1
            engField = rest[ixBS+3:ixEnd]
            assert '\\' not in engField and '*' not in engField and engField.count('|')==1
            engWord, engField = engField.split( '|', 1 )
            engBits = engField.split( ' ' )
            # print( f"  {len(engBits)} {engBits}")
            assert len(engBits) == 2
            assert engBits[0].startswith( 'x-occurrence="' ) and engBits[0][-1] == '"'
            assert engBits[1].startswith( 'x-occurrences="' ) and engBits[1][-1] == '"'
            engOccurrence, engOccurrences = engBits[0][14:-1], engBits[1][15:-1]
            # print( f"    {engWord=} {engOccurrence=} {engOccurrences=}" )
            thisTuple = engWord,engOccurrence,engOccurrences
            # for foundIndex,alignedWordTuple in enumerate( currentAlignment[1] ):
            #     # print( alignedWordTuple)
            #     if alignedWordTuple == thisTuple:
            #         break
            # else:
            #     print( f"No match found for {BBB} {c}:{v} {thisTuple} in {currentAlignment[1]=}" ); halt
            #     foundIndex = -1
            newField = f'\\w {engWord}|{translatedWordNum}\\w*'
            # if foundIndex == len(currentAlignment[1]) - 1: # it was the last translated word in the alignment
            translatedWordNum += 1
            rest = f'{rest[:ixBS]}{newField}{rest[ixEnd+3:]}' # Adjust the w field
            startSearchIndex = ixBS + len(newField)
        elif rest[ixBS:].startswith( '\\zaln-e\\*' ):
            grkWord = engWord = engWords = None
            grkWords = []
            rest = f'{rest[:ixBS]}{rest[ixBS+9:]}' # Completely remove the zaln-e field
        else:
            assert False, f"unexpected field {BBB} {c}:{v} {rest[ixBS:]}"

    # print( f"  convertLineAlignments() returning {marker}={rest} {translatedWordNum=}" )
    return marker,rest,translatedWordNum
# end of uW_to_ESFM.convertLineAlignments


def normalise_USFM_markers_to_ESFM( usfm:str ) -> str:
    """
    Takes an entire USFM book contents and returns a normalised ESFM version.
    """
    fnPrint( DEBUGGING_THIS_MODULE, f"normalise_USFM_markers_to_ESFM( {len(usfm)} {usfm[:300]}... )" )

    for usfm_marker in ('mt','imt', 'mte','imte', 's','is', 'ms',
                        'q','iq', 'qm', 'pi','ph', 'io',
                        'li','ili', 'lim', 'liv',
                        'th','thr','tc','tcr',
                        'sd',):
        usfm = usfm.replace( f'\\{usfm_marker} ', f'\\{usfm_marker}1 ' ) # change to explicitly numbered marker

    return usfm
# end of uW_to_ESFM.normalise_USFM_markers_to_ESFM


def briefDemo() -> None:
    """
    Main program to handle command line parameters and then run what they want.
    """
    BibleOrgSysGlobals.introduceProgram( __name__, PROGRAM_NAME_VERSION, LAST_MODIFIED_DATE )

    # Demo the uW_to_ESFM object
    uW_to_ESFM()
# end of uW_to_ESFM.briefDemo

def fullDemo() -> None:
    """
    Full demo to check class is working
    """
    BibleOrgSysGlobals.introduceProgram( __name__, PROGRAM_NAME_VERSION, LAST_MODIFIED_DATE )

    # Demo the uW_to_ESFM object
    uW_to_ESFM()
# end of uW_to_ESFM.fullDemo

if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support() # Multiprocessing support for frozen Windows executables

    # Configure basic Bible Organisational System (BOS) set-up
    parser = BibleOrgSysGlobals.setup( SHORT_PROGRAM_NAME, PROGRAM_VERSION, LAST_MODIFIED_DATE )
    BibleOrgSysGlobals.addStandardOptionsAndProcess( parser )

    fullDemo()

    BibleOrgSysGlobals.closedown( PROGRAM_NAME, PROGRAM_VERSION )
# end of uW_to_ESFM.py
