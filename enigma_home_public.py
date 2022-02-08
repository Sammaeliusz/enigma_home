global lu
import time
import os
import sys 
menut = '''
Witaj w grze Enigma home.
1 - Nowa gra
2 - kontynuuj
3 - Wyjdź
'''
podaj = '''Podaj kod, kod i hasło lub hasło do poziomu do którego chcesz wejść
(poziom 2 i 3 kod, poziomy 4 i 6 hasło, poziom 5 kod i hasło).
'''
wpt = '''
Wybierz poziom
1 - wróć
2 - poziom 2
3 - poziom 3
4 - poziom 4
5 - poziom 5
6 - poziom 6
'''
tytuł = '''
-----------------------------------------------
|               enigma house                  |
|---------------------------------------------|
|                  coding :                   |
|                  Michal                     |   
|---------------------------------------------|
|                  story:                     |
|                  Michal                     |
|---------------------------------------------|'''
fabuła = '''Budzisz się w pokoju z jednymi drzwiami zabezpieczonymi kodem trzymając w ręku okulary z dziwnym przyciskiem. Wstajesz i rozglądasz się po pokoju.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do kodołamacza
3 - podejdź do drzwi.
'''
przyciskt = '''Gdy wciskasz przycisk to widzisz że na ścianach coś się świeci.
Możliwe akcje to:
1 - przyjrzyj się świecącym obiektom
2 - podejdź do drzwi.
'''
świece1 = '''Podchdzisz do świecących obiektów które okazują się liczbami: 35819 i 25348.
Możliwe akcje to:
1 - back.
'''
drzwiczki = '''Drzwi są zabezpieczone 5 cyfrowym kodem.
Możliwe akcje to:
1 - wpisz kod
2 - back
'''
codebraker1 = '''Gdy podchodzisz do kodołamacza okazuje się on zabezpieczony 5 cyfrowym kodem.
Możliwe akcje to:
1 - zlam kod
2 - back
'''
wracaszt = '''Wracasz na środek pokoju.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do kodołamacza
3 - podejdź do drzwi.
'''
kpt = '''złamany kod to: 43796
Możliwe akcje to:
1 - back
'''
def menu():
    manu = input(menut)
    if manu == '1':
        os.system("cls")
        fabula1()
    elif manu == '2':
        os.system("cls")
        wp()
    elif manu == '3':
        sys.exit(0)
    else:
        print('Nie ma takiej opcji, spróbój jeszcze raz.')
        menu2()
def menu2():
    manu = input(menut)
    if manu == '1':
        os.system("cls")
        fabula1()
    elif manu == '2':
        os.system("cls")
        wp()
    elif manu == '3':
        sys.exit(0)
    else:
        print('Nie ma takiej opcji, spróbój jeszcze raz.')
        menu()
def wp():
        wpw = input(wpt)
        if wpw == '1':
            os.system("cls")
            menu()
        elif wpw == '2':
            kd = input(podaj)
            if kd == '43796':
                os.system("cls")
                fabula2()
        elif wpw == '3':
            kd = input(podaj)
            if kd == '54273':
                os.system("cls")
                fabula3()
        elif wpw == '4':
            kd = input(podaj)
            if kd == 'dzik i opos':
                os.system("cls")
                fabula4()
        elif wpw == '5':
            print(podaj)
            kd = input('Podaj kod')
            kd2 = input('Podaj hasło')
            if kd == '76248' and kd2 == 'byk':
                os.system("cls")
                fabula5()
        elif wpw == '6':
            kd = input(podaj)
            if kd == 'zeus posejdon i hades':
                os.system("cls")
                fabula6()
        else:
            print('Nie ma takiej opcji, spróbój jeszcze raz.')
            wp2()
def wp2():
        wpw = input(wpt)
        if wpw == '1':
            os.system("cls")
            menu()
        elif wpw == '2':
            kd = input(podaj)
            if kd == '43796':
                os.system("cls")
                fabula2()
        elif wpw == '3':
            kd = input(podaj)
            if kd == '54273':
                os.system("cls")
                fabula3()
        elif wpw == '4':
            kd = input(podaj)
            if kd == 'dzik i opos':
                os.system("cls")
                fabula4()
        elif wpw == '5':
            print(podaj)
            kd = input('Podaj kod ')
            kd2 = input('Podaj hasło ')
            if kd == '76248' and kd2 == 'byk':
                os.system("cls")
                fabula5()
        elif wpw == '6':
            kd = input(podaj)
            if kd == 'zeus posejdon i hades':
                os.system("cls")
                fabula6()
        else:
            print('Nie ma takiej opcji, spróbój jeszcze raz.')
            wp()    
def wracasz12():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk()
    elif wraodp == '2':
        kod1()
    elif wraodp == '3':
        drzwi()
    else:
        wracasz()

def kod1 ():
    kododp1 = input(codebraker1)
    if kododp1 == '1':
        kodkod1 = input( 'Podaj kod:')
        if kodkod1 == '35819':
            kod1 = input( 'Odblokowałeś kodołamacz podaj kod do złamania: ')
            if kod1 == '25348':
                kp = input (kpt)
                if kp == 1:
                    wracasz()
                else:
                    wracasz()
                
            else:
                print ('Spróbuj jeszcze raz')
                wracasz()
        else:
            print ('Spróbuj jeszcze raz')
            wracasz()
    elif kododp1 == '2':
        wracasz()
    else:
        wracasz()
def drzwi():
    odpdrz = input (drzwiczki)
    if odpdrz == '1':
        koddrz = input('Podaj kod: ')
        if koddrz == '43796':
            os.system("cls")
            fabula2()
        else:
            print ('Spróbuj jeszcze raz')
            wracasz()
    else:
        wracasz()
def swiece():
    swiodp = input(świece1)
    if swiodp == 1:
        wracasz12()
    else:
        wracasz12()
def przycisk():
    przodp = input(przyciskt)
    if przodp == '1':
        swiece()
    elif przodp == '2':
        drzwi()
def fabula1():
    print(tytuł)
    time.sleep(5)
    fabodp = input(fabuła)
    if fabodp == '1':
        przycisk()
    elif fabodp == '2':
        kod1()
    elif fabodp == '3':
        drzwi()
    else:
        wracasz()
def wracasz():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk()
    elif wraodp == '2':
        kod1()
    elif wraodp == '3':
        drzwi()
    else:
        wracasz12()

fabuła2 = '''Przechodisz do kolejnego pokoju z jednymi drzwiami zabezpieczonymi kodem i rozglądasz się po nim.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do kodołamacza
3 - podejdź do drzwi.
'''
świece2 = '''Podchdzisz do świecących obiektów które okazują się liczbami: []2[]7[] i 3[]8[]9.
Możliwe akcje to:
1 - back.
'''
kpt2 = '''złamany kod to: 54273
Możliwe akcje to:
1 - back
'''
def wracasz22():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk2()
    elif wraodp == '2':
        kod2()
    elif wraodp == '3':
        drzwi2()
    else:
        wracasz2()

def kod2 ():
        kod1 = input( 'Podaj kod do złamania: ')
        if kod1 == '32879':
            kp2 = input (kpt2)
            if kp2 == 1:
                wracasz2()
            else:
                wracasz2()
        else:
            print ('Spróbuj jeszcze raz')
            wracasz2()
def drzwi2():
    odpdrz = input (drzwiczki)
    if odpdrz == '1':
        koddrz = input('Podaj kod: ')
        if koddrz == '54273':
            os.system("cls")
            fabula3()
        else:
            print ('Spróbuj jeszcze raz')
            wracasz2()
    else:
        wracasz2()
def swiece2():
    swiodp = input(świece2)
    if swiodp == 1:
        wracasz2()
    else:
        wracasz2()
def przycisk2():
    przodp = input(przyciskt)
    if przodp == '1':
        swiece2()
    elif przodp == '2':
        drzwi2()
def fabula2():
    fabodp = input(fabuła2)
    if fabodp == '1':
        przycisk2()
    elif fabodp == '2':
        kod2()
    elif fabodp == '3':
        drzwi2()
    else:
        wracasz2()
def wracasz2():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk2()
    elif wraodp == '2':
        kod2()
    elif wraodp == '3':
        drzwi2()
    else:
        wracasz22()

świece3 = '''Podchdzisz do świecących obiektów które okazują się tekstami:

Dawno dawno temu w królewskim
zamku miezkał król Błażej i królowa
Izabela, uwielbiali oni polowanie dlatego często wyruszali zapolować na
kuropatwy, głuszce, sarny, i kanie.
i
W pewnej ubogiej wsi żył rzemieślnik Hugo
który wyrabiał narzędzia rolnicze po które często przychodził chłop
Hieronim, czasami wychodzili razem na piwo
do leżącej nieopodal karczmy w której podawali świetny sos.

Możliwe akcje to:
1 - back.
'''
fabuła3 = '''Przechodisz do kolejnego pokoju z jednymi drzwiami zabezpieczonymi hasłem i rozglądasz się po nim.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do drzwi.
'''
wracaszt3 = '''Wracasz na środek pokoju.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do drzwi.
'''
drzwiczki3 = '''Drzwi są zabezpieczone hasłem.
Możliwe akcje to:
1 - wpisz hasło
2 - back
'''
def wracasz32():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk3()
    elif wraodp == '2':
        drzwi3()
    else:
        wracasz2()
def drzwi3():
    odpdrz = input (drzwiczki3)
    if odpdrz == '1':
        koddrz = input('Podaj hasło: ')
        if koddrz == 'dzik i opos':
            os.system("cls")
            fabula4()
        else:
            wracasz3()
            print ('Spróbuj jeszcze raz')
    else:
        wracasz3()
def swiece3():
    swiodp = input(świece3)
    if swiodp == 1:
        wracasz3()
    else:
        wracasz3()
def przycisk3():
    przodp = input(przyciskt)
    if przodp == '1':
        swiece3()
    elif przodp == '2':
        drzwi3()
def fabula3():
    fabodp = input(fabuła3)
    if fabodp == '1':
        przycisk3()
    elif fabodp == '2':
        drzwi3()
    else:
        wracasz32()
def wracasz3():
    wraodp = input (wracaszt3)
    if wraodp == '1':
        przycisk3()
    elif wraodp == '2':
        drzwi3()
    else:
        wracasz32()
fabuła4 = '''Przechodisz do kolejnego pokoju z jednymi drzwiami zabezpieczonymi kodem i hasłem. Rozglądasz się po pokoju.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do kodołamacza
3 - podejdź do drzwi.
'''
świece4 = '''Na jednej ścianie widzisz duży znak lupy a na drugiej mały znak lupy i jakiś mały tekst.
Możliwe akcje to:
1 - podejdź do dużej lupy
2 - podejdź do małej lupy ze znaczkami
3 - back
'''
mate4 = '''Małe znaczki okazują się słowem byk i liczbą 31524. Możliwe akcje to:
1 - back
'''
kpt4 = '''złamany kod to: 76248
Możliwe akcje to:
1 - back
'''
dl = '''Gdy podchodzisz do dużej lupy wysuwa się szuflada na której jest lupa.'''
ml = '''Gdy podchodziszdo małej lupy okazuje się że nie umiesz rozczytać małych znaczków napisanych na ścianie. Możliwe akcje to:
1 - back '''
mll = '''
2 - odczytaj znaczki
'''
drzwiczki4 = '''Drzwi są zabezpieczone hasłem i 5 cyfrowym kodem.
Możliwe akcje to:
1 - wpisz kod
2 - back
'''
def wracasz42():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk4()
    elif wraodp == '2':
        kod4()
    elif wraodp == '3':
        drzwi4()
    else:
        wracasz4()

def kod4 ():
        kod1 = input( 'Podaj kod do złamania: ')
        if kod1 == '31524':
            kp2 = input(kpt4)
            if kp2 == 1:
                wracasz4()
            else:
                wracasz4()
        else:
            print ('Spróbuj jeszcze raz')
            wracasz4()
def drzwi4():
    odpdrz = input (drzwiczki4)
    if odpdrz == '1':
        koddrz = input('Podaj kod: ')
        hasdrz = input('Podaj hasło: ')
        if koddrz == '76248' and hasdrz == 'byk':
            os.system("cls")
            print('Gdy wpisujesz hasło i kod odwiera się winda na której kładziesz lupe. Potem drzwi się otwierają a ty prechodzisz do kolejnego pokoju.')
            fabula5()
        else:
            wracasz4()
            print('Spróbuj jeszcze raz')
    else:
        wracasz4()
def swiece4():
    global lu
    swiodp = input(świece4)
    if swiodp == '1':
        print (dl)
        lu = '1'
        wracasz4()
    elif swiodp == '2':
        if lu == '1':
            mle = ml + mll
            odpmle = input (mle)
            if odpmle == '1':
                wracasz4()
            elif odpmle == '2':
                odpmate = input(mate4)
                if odpmate == '1':
                    wracasz4()
                else:
                    wracasz4()
            else:
                wracasz4()
        else:
            odpml = input(ml)
    elif swiodp == '3':    
        wracasz4()
    else:
        wracasz4()
def przycisk4():
    przodp = input(przyciskt)
    if przodp == '1':
        swiece4()
    elif przodp == '2':
        drzwi4()
def fabula4():
    fabodp = input(fabuła4)
    if fabodp == '1':
        przycisk4()
    elif fabodp == '2':
        kod4()
    elif fabodp == '3':
        drzwi4()
    else:
        wracasz4()
def wracasz4():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk4()
    elif wraodp == '2':
        kod4()
    elif wraodp == '3':
        drzwi4()
    else:
        wracasz42()
świece5 = '''Podchdzisz do świecącego obiektu który okazuje się tekstem:
sedah i nodjesop suez
Możliwe akcje to:
1 - back.
'''
fabuła5 = '''Przechodisz do kolejnego pokoju z jednymi drzwiami zabezpieczonymi hasłem i rozglądasz się po nim.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do drzwi.
'''
wracaszt5 = '''Wracasz na środek pokoju.
Możliwe akcje to:
1 - kliknij przycisk w okularach
2 - podejdź do drzwi.
'''
koniec = '''Dziękujemy za przejście naszej pierwszej gry.'''
def wracasz52():
    wraodp = input (wracaszt)
    if wraodp == '1':
        przycisk5()
    elif wraodp == '2':
        drzwi5()
    else:
        wracasz52()
def drzwi5():
    odpdrz = input (drzwiczki3)
    if odpdrz == '1':
        koddrz = input('Podaj hasło: ')
        if koddrz == 'zeus posejdon i hades':
            os.system("cls")
            fabula6()
        else:
            wracasz5()
    else:
        wracasz5()
def swiece5():
    swiodp = input(świece5)
    if swiodp == 1:
        wracasz5()
    else:
        wracasz5()
def przycisk5():
    przodp = input(przyciskt)
    if przodp == '1':
        swiece5()
    elif przodp == '2':
        drzwi5()
def fabula5():
    fabodp = input(fabuła5)
    if fabodp == '1':
        przycisk5()
    elif fabodp == '2':
        drzwi5()
    else:
        wracasz52()
def wracasz5():
    wraodp = input (wracaszt5)
    if wraodp == '1':
        przycisk5()
    elif wraodp == '2':
        drzwi5()
    else:
        wracasz52()
fabuła6 = '''Przechodisz do kolejnego pokoju bez drzwi i widzisz półkę nad którą widać napis:
na półkę połóż okulary.
Możliwe akcje to:
1 - połórz okulary na półkę
'''
wracaszt6 = '''Wracasz na środek pokoju.
Możliwe akcje to:
1 - połórz okulary na półkę
'''
półka = '''Gdy kładziesz okulary na półce odsuwa się fragment ściany. Gdy wychodzisz na zewnątrz widzisz ogród a na środku tego ogrodu stoi stary dom z wierzyczką.'''
koniec = '''Dziękujemy za przejście naszej pierwszej gry.'''
def wracasz62():
    wraodp = input (wracaszt)
    if wraodp == '1':
        półka6()
    else:
        wracasz62()
def półka6():
    print(półka)
    print(koniec)
    i=input()
def fabula6():
    fabodp = input(fabuła6)
    if fabodp == '1':
        półka6()
    else:
        wracasz62()
def wracasz6():
    wraodp = input (wracaszt)
    if wraodp == '1':
        półka6()
    else:
        wracasz6()
menu()


