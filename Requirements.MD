|||
|---|---|
|Identyfikator|Temperatura1|
|Priorytet|M|
|Nazwa|Stan temperatury|
|Opis|badamy temperature i zwracamy 1 z 3 stanów do układu|
|Dane wejściowe|temperatura|
|Warunki początkowe|podłączony czujnik temperatury|
|Warunki końcowe|określony stan temperatury|
|Sytuacje wyjątkowe|brak temperatury|
|Efekty uboczne|brak|
|Czynności równoczesne|brak|
|Udziałowiec|dioda|
|Powiązania z innymi wymaganiami|diody(Dioda1,Dioda2,Dioda3)|<br>

|||
|---|---|
|Identyfikator|Alarm1|
|Priorytet|S|
|Nazwa | alarm|
|Opis|alarm wydaje dzwięk jeśli jest uzbrojony i przycisk został wciśnięty|
|Dane wejściowe|stan uzbrojenia, stan wciśnięcia|
|Warunki początkowe|alarm nie wydaje dzwieku, przycisk nie jest wcisniety|
|Warunki końcowe|alarm wydaje dzwiek, przycisk jest wcisniety|
|Sytuacje wyjątkowe|alarm nie jest uzbrojony|
|Efekty uboczne|migrena|
|Czynności równoczesne:|brak|
|Udziałowiec|użytkownik systemu|
|Powiązania z innymi wymaganiami|przycisk(4)|

|||
|---|---|
|Identyfikator|Przycisk1|
|Priorytet|S|
|Nazwa|Przycisk|
|Opis| przycisk włączający syrenę|
|Dane wejściowe|stan wciśnięcia przycisku|
|Warunki początkowe|przycisk nie jest wciśnięty|
|Warunki końcowe|przycisk jest wciśnięty|
|Sytuacje wyjątkowe|moze zle dzialac przy duzych lub malych temperaturach, uszkodzony przycisk|
|Efekty uboczne|brak|
|Czynności równoczesne|brak|
|Udziałowiec|buzzer|
|Powiązania z innymi wymaganiami|alarm(Alarm1)|

|||
|---|---|
|Identyfikator|Dotyk1|
|Priorytet| C|
|Nazwa|czujnik dotykowy|
|Opis|przy dotknieciu czujnika dotykowego alarm zostaje uzbrojony|
|Dane wejściowe|czujnik dotykowy|
|Warunki początkowe|cisza|
|Warunki końcowe|uzbrojony alarm|
|Sytuacje wyjątkowe|różnie|
|Efekty uboczne|brak|
|Czynności równoczesne|brak|
|Udziałowiec|buzzer|
|Powiązania z innymi wymaganiami|brak|

|||
|---|---|
|Identyfikator|Dioda1|
|Priorytet| M|
|Nazwa|Dioda niebeiska- zimna|
|Opis|dioda pali sie dopoki temperatura nie jest powyzej n|
|Dane wejściowe| stan temperatury|
|Warunki początkowe|temperatura ponizej n|
|Warunki końcowe|dioda odpowiedzialna za dany stan się świeci(sygnal high), a reszta nie|
|Sytuacje wyjątkowe|przerwany drucik wolframowy|
|Efekty uboczne|brak|
|Czynności równoczesne|definiowanie stau temperatury|
|Udziałowiec|użytkownik systemu|
|Powiązania z innymi wymaganiami|Stan temperatury(Temperatura1)|

|||
|---|---|
|Identyfikator|Dioda2|
|Priorytet|M|
|Nazwa|Dioda biala- neutralna|
|Opis|dioda pali sie dopoki temperatura jest poiedzy x a y|
|Dane wejściowe|stan temperatury|
|Warunki początkowe|temperatura pomiedzy x a y|
|Warunki końcowe|dioda odpowiedzialna za dany stan się świeci(sygnal high), a reszta nie|
|Sytuacje wyjątkowe|przerwany drucik wolframowy|
|Efekty uboczne|brak|
|Czynności równoczesne|definiowanie stau temperatury|
|Udziałowiec|użytkownik systemu|
|Powiązania z innymi wymaganiami|Stan temperatury(Temperatura1)|

|||
|---|---|
|Identyfikator|Dioda3|
|Priorytet|M|
|Nazwa|Dioda czerwona- ciepla|
|Opis|dioda pali sie dopoki temperatura jest powyzej n|
|Dane wejściowe|stan temperatury|
|Warunki początkowe|temperatura n|
|Warunki końcowe|dioda odpowiedzialna za dany stan się świeci(sygnal high), a reszta nie|
|Sytuacje wyjątkowe|przerwany drucik wolframowy|
|Efekty uboczne|brak|
|Czynności równoczesne|definiowanie stau temperatury|
|Udziałowiec|użytkownik systemu|
|Powiązania z innymi wymaganiami|Stan temperatury(Temperatura1)|
