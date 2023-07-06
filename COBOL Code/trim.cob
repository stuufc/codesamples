       identification division.
       program-id. trim-function-test.

       data division.
       file section.

       working-storage section.

       01  ws-test-string-1    pic x(30) value "    hello world       ".

       01  ws-test-string-2    pic x(30).

       procedure division.
       main-procedure.
           display "--" ws-test-string-1 "--"
           display "--" function trim(ws-test-string-1) "--"
           display "--" function trim(ws-test-string-1 leading) "--"
           display "--" function trim(ws-test-string-1 trailing) "--"

           move "******************************" to ws-test-string-2
           display ws-test-string-2
           move ws-test-string-1 to ws-test-string-2
           display ws-test-string-2

           move "******************************" to ws-test-string-2
           display ws-test-string-2
           move function trim(ws-test-string-1) to ws-test-string-2
           display ws-test-string-2

           move "******************************" to ws-test-string-2
           display ws-test-string-2
           move function trim(ws-test-string-1 leading)
               to ws-test-string-2
           display ws-test-string-2

           move "******************************" to ws-test-string-2
           display ws-test-string-2
           move function trim(ws-test-string-1 trailing)
               to ws-test-string-2
           display ws-test-string-2


           display "--" "    String literal    " "--"
           display "--" function trim("   String literal    ") "--"
           display
               "--" function trim("     String literal   " leading) "--"
           end-display
           display
               "--" function trim("   String literal    " trailing) "--"
           end-display


           stop run.

       end program trim-function-test.


000000*Quelle: https://github.com/shamrice/COBOL-Examples/blob/main/trim/trim.cbl -> angepasst

000000* Beschreibung: Dieser Code demonstriert die Verwendung der TRIM-Funktion in COBOL. Er enthält Beispiele, wie man einen Zeichenstring mit führenden und abschließenden Leerzeichen trimmt 
000000* sowie die Verwendung der TRIM-Funktion mit Zeichenliteralen. Die Ergebnisse werden mit Hilfe von DISPLAY-Anweisungen angezeigt.




