      ******************************************************************
      * Author: Maxfx                                                  *
      * Date: 27/8/2017                                                *
      * Program demonstration for loop in cobol program.               *
      * Revision: Maxfx 18/2/2018                                      *
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. FOR-LOOP.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 W-I PIC 999 VALUE 0.
       01 W-J PIC 999 VALUE 0.
       01 W-K PIC 999 VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

           PERFORM FOR-UNTIL-LOOP.
           PERFORM FOR-VAIRING-LOOP.
           GOBACK.

           FOR-UNTIL-LOOP SECTION.

           PERFORM UNTIL W-I > 20
             MOVE W-I TO W-J
             ADD 1 TO W-I

             PERFORM UNTIL W-J > 20
               COMPUTE W-K = W-J * W-I
               DISPLAY "UNTIL: " W-I  " W-K: " W-K " = " W-J " * " W-I
               ADD 1 TO W-J

             END-PERFORM
           END-PERFORM.


           FOR-VAIRING-LOOP SECTION.

           ADD 0 TO W-I
           ADD 0 TO W-J
           ADD 0 TO W-K

           PERFORM VARYING W-I FROM 1 BY 1 UNTIL W-I > 20
             MOVE W-I TO W-J
             ADD 1 TO W-I

             PERFORM VARYING W-J FROM 1 BY 1 UNTIL W-J > 20
               COMPUTE W-K = W-J * W-I
               DISPLAY "VARYING: " W-I  " W-K: " W-K " = " W-J " * " W-I
               ADD 1 TO W-J
             END-PERFORM

           END-PERFORM.


000000* Quelle: https://github.com/Martinfx/Cobol/blob/master/OpenCobol/Loops/ForLoop.cbl

000000* Beschreibung: Dieses COBOL-Programm führt im Wesentlichen zwei verschiedene Schleifenstrukturen aus, um die Ergebnisse der Multiplikation von zwei Zahlen zu berechnen und anzuzeigen. Die zwei Schleifenstrukturen sind die "UNTIL"-Schleife und die "VARYING"-Schleife.
000000* Im Grunde genommen verwendet dieses Programm zwei verschiedene Methoden, um das gleiche Ergebnis zu erzielen: Es berechnet und zeigt das Produkt aller Paare von Zahlen von 1 bis 20.



000000* Die "FOR-UNTIL-LOOP" Sektion führt eine Schleife aus, die die Werte von W-I und W-J erhöht, bis sie größer als 20 sind. Innerhalb dieser Schleife wird eine weitere Schleife ausgeführt, die W-J erhöht und das Produkt von W-I und W-J in W-K speichert. Für jeden Schleifendurchlauf wird die Berechnung "UNTIL: " W-I " W-K: " W-K " = " W-J " * " W-I ausgegeben.

000000* Nachdem die "FOR-UNTIL-LOOP" Sektion abgeschlossen ist, werden W-I, W-J und W-K zurückgesetzt, und die "FOR-VARYING-LOOP" Sektion wird ausgeführt. Diese Sektion verwendet die "PERFORM VARYING"-Struktur, die ähnlich funktioniert wie die "FOR"-Schleife in anderen Programmiersprachen. Diese Struktur erhöht die Werte von W-I und W-J bei jedem Schleifendurchlauf, bis sie größer als 20 sind. Innerhalb dieser Schleife wird eine ähnliche zweite Schleife ausgeführt. Das Produkt von W-I und W-J wird in W-K gespeichert und die gleiche Berechnung wie oben wird ausgegeben.