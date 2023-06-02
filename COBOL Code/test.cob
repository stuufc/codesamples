IDENTIFICATION DIVISION.
PROGRAM-ID. LoopExample.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 COUNTER PIC 9 VALUE 0.

PROCEDURE DIVISION.
PERFORM UNTIL COUNTER = 10
    ADD 1 TO COUNTER
    DISPLAY "Counter is: " COUNTER
END-PERFORM.

STOP RUN.