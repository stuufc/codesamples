      ******************************************************************
      * Author: Maxfx                                                  *
      * Revision: 31/08/2017                                           *
      * Revision: Maxfx 27/12/2017                                     *
      * Example work with string                                       *
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. WORK-WITH-STRING.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           01 W-COUNT     PIC 999.
           01 W-STRING    PIC X(10) VALUE "HOHOHOHOHO".

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

           PERFORM VARYING W-COUNT FROM 1 BY 1 UNTIL W-COUNT > 10
             DISPLAY W-STRING(W-COUNT:1)
           END-PERFORM

           GOBACK.

000000*Quelle: https://github.com/Martinfx/Cobol/blob/master/OpenCobol/String/String.cbl

000000*Beschreibung: Zusammenfassend zeigt dieses Programm, wie man mit Zeichenketten in COBOL arbeitet, indem es die einzelnen Zeichen einer Zeichenkette durch eine Schleife durchläuft und sie anzeigt. Es dient als Beispiel für die Verwendung von Schleifen und Zeichenkettenoperationen in COBOL.




