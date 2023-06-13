
       identification division.
       program-id. json-generate-example.
       data division.
       file section.
       working-storage section.

       01  ws-json-output                       pic x(256).

       01  ws-json-char-count                   pic 9(4).

       01  ws-record.
           05  ws-record-name                  pic x(10).
           05  ws-record-value                 pic x(10).
           05  ws-record-blank                 pic x(10).
           05  ws-record-flag                  pic x(5) value "false".
               88  ws-record-flag-enabled      value "true".
               88  ws-record-flag-disabled     value "false".

       procedure division.
       main-procedure.

           move "Test Name" to ws-record-name
           move "Test Value" to ws-record-value
           set ws-record-flag-enabled to true

           json generate ws-json-output
               from ws-record
               count in ws-json-char-count
               name of
                   ws-record-name is "name",
                   ws-record-value is "value",
                   ws-record-flag is "enabled"
               on exception
                   display "Error generating JSON error " JSON-CODE
                   stop run
               not on exception
                   display "JSON document successfully generated."
           end-json

           display "Generated JSON for record: " ws-record
           display "----------------------------"
           display function trim(ws-json-output)
           display "----------------------------"
           display "JSON output character count: " ws-json-char-count
           display "Done."
           stop run.


       end program json-generate-example.


000000*Quelle: json_generate/json_generate.cbl -> angepasst

000000*Beschreibung: Dieses COBOL-Programm erzeugt ein JSON-Dokument aus einem Datensatz. Das erzeugte JSON-Dokument wird in der Variable ws-json-output gespeichert und seine Zeichenanzahl wird in ws-json-char-count gespeichert. Beide Variablen werden am Ende des Programms ausgegeben.