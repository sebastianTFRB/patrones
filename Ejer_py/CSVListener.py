# Generated from CSV.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete listener for a parse tree produced by CSVParser.
class CSVListener(ParseTreeListener):

    # Enter a parse tree produced by CSVParser#csvFile.
    def enterCsvFile(self, ctx:CSVParser.CsvFileContext):
        pass

    # Exit a parse tree produced by CSVParser#csvFile.
    def exitCsvFile(self, ctx:CSVParser.CsvFileContext):
        pass


    # Enter a parse tree produced by CSVParser#header.
    def enterHeader(self, ctx:CSVParser.HeaderContext):
        pass

    # Exit a parse tree produced by CSVParser#header.
    def exitHeader(self, ctx:CSVParser.HeaderContext):
        pass


    # Enter a parse tree produced by CSVParser#row.
    def enterRow(self, ctx:CSVParser.RowContext):
        pass

    # Exit a parse tree produced by CSVParser#row.
    def exitRow(self, ctx:CSVParser.RowContext):
        pass


    # Enter a parse tree produced by CSVParser#text.
    def enterText(self, ctx:CSVParser.TextContext):
        pass

    # Exit a parse tree produced by CSVParser#text.
    def exitText(self, ctx:CSVParser.TextContext):
        pass


    # Enter a parse tree produced by CSVParser#string.
    def enterString(self, ctx:CSVParser.StringContext):
        pass

    # Exit a parse tree produced by CSVParser#string.
    def exitString(self, ctx:CSVParser.StringContext):
        pass


    # Enter a parse tree produced by CSVParser#empty.
    def enterEmpty(self, ctx:CSVParser.EmptyContext):
        pass

    # Exit a parse tree produced by CSVParser#empty.
    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        pass



del CSVParser