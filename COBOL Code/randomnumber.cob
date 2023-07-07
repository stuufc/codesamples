      ******************************************************************
      * Author: Maxfx
      * Date: 30.7.2017
      * Example of generating random numbers.
      * Revision: Maxfx 18/2/2018
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RANDOM-NUMBERS.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
           01 W-RESULT PIC 999.
           01 SEED     PIC 9V999999999.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

            PERFORM GET-SEED.
            PERFORM GENERATE-NUMBER.
            GOBACK.

           GET-SEED SECTION.

           MOVE FUNCTION RANDOM(FUNCTION SECONDS-PAST-MIDNIGHT) TO SEED.

           GENERATE-NUMBER SECTION.

            PERFORM 10 TIMES
              COMPUTE W-RESULT = (FUNCTION RANDOM * 100) + 1
              DISPLAY "Random number: " W-RESULT
            END-PERFORM.


000000* Quelle: https://github.com/Martinfx/Cobol/blob/master/OpenCobol/Random/RandomNumbers.cbl

000000* Beschreibung: Zusammenfassend erzeugt dieses Programm eine Reihe von zufälligen Zahlen und gibt sie aus. Es kann als Beispiel für die Verwendung des RANDOM-Befehls dienen.




