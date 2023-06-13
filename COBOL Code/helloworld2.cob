       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD2.
     
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.


       DATA DIVISION.

       FILE SECTION.

       WORKING-STORAGE SECTION.
       77  W-NOME    PIC A(15) VALUE "Stefan Banzer".


       PROCEDURE DIVISION.

       MAIN-PROCEDURE.
            DISPLAY "Hello world!".
            DISPLAY W-NOME.
            STOP RUN.

       END PROGRAM HELLO-WORLD2.

000000* Quelle: https://github.com/victordomingos/Learning_COBOL/blob/master/02_variable.cbl -> angepasst