      ******************************************************************
      * Author: Maxfx                                                  *
      * Date: 11/9/2017                                                *
      * Program demonstration while loop
      * Revision: Maxfx 18/2/2018
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. WHILE.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 W-I PIC 99 VALUE 20.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

           PERFORM WHILE-LOOP.
           GOBACK.

           WHILE-LOOP SECTION.
           PERFORM UNTIL W-I <= 0
             DISPLAY W-I
             COMPUTE W-I = W-I - 1
           END-PERFORM.


000000* Quelle: https://github.com/Martinfx/Cobol/blob/master/OpenCobol/Loops/While.cbl

000000* Beschreibung: Dieses COBOL-Programm verwendet eine While-Schleife, um eine absteigende Zählung von 20 bis 1 durchzuführen und die Werte auf dem Bildschirm anzuzeigen.