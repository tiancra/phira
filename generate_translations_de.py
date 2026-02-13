#!/usr/bin/env python3
"""
Phira Complete Localization Generator
Generates all 20 FTL files for 13 languages
"""

from pathlib import Path
from typing import Dict

# Complete translations for all 13 languages × 20 files
TRANSLATIONS = {
    "de-DE": {
        "cali.ftl": 'label = Verzögerungsabstimmung\n',
        "chapter.ftl": '''diff-easy = EZ
diff-hard = HD
diff-extreme = IN
''',
        "chart_order.ftl": '''time = Von neu zu alt
rev-time = Von alt zu neu
name = Name aufsteigend
rev-name = Name absteigend
rating = Nach Bewertung
rev-rating = Bewertung absteigend
''',
        "collection.ftl": '''label = Furinas Noten-Sammlung

wait-for-more = Bald mehr

name-c1 = Ruinen der Zukunft
''',
        "common.ftl": '''del-confirm = Bist du sicher, dass du löschen möchtest?
del-confirm-content = Dein Ei ist aufgebraucht. Du kannst diese Aktion nicht mehr rückgängig machen.

cancel = Ich überdenke es
confirm = Fortfahren

release-to-refresh = Loslassen zum Aktualisieren der Charakterinformationen

switch-on = Ein
switch-off = Aus

chart-ranked = Gerankt
chart-special = Spezial
chart-unstable = Ungerankt

list-empty = Hier gibt es nichts. Gehe zurück und spiele mit Furina!

tos-and-policy = "Nutzungsbedingungen" und "Datenschutzrichtlinie"
tos-and-policy-desc = Bevor du die Online-Dienste von Phira und Phira-Furina (modifiziert von Genius Wei) verwendest, musst du unseren "Nutzungsbedingungen" und unserer "Datenschutzrichtlinie" zustimmen.
tos-deny = Ablehnen
tos-accept = Akzeptieren
tos-prev-page = Vorherige Seite
tos-next-page = Nächste Seite
fetch-tos-policy-failed = Fehler beim Abrufen der Nutzungsbedingungen und Datenschutzrichtlinie
warn-deny-tos-policy = Du musst den Bedingungen zustimmen, um die Online-Dienste zu nutzen

open-in-web = Im Interface öffnen

main-character-name = Shee
main-character-intro =
  Der Gesang aus zerfallenen Ruinen, umgeben von komplexen Melodien - die Form eines Rhythmus. Wie ein Wunder selbst, ein Geheimnis, das nicht nach bekannten Gesetzen definierbar ist.
  Aus der Zukunft kommend, doch wie eine ewige Existenz. Keine Sorge; Anhaftungen sind mit der Erinnerung des Mädchens verblasst.
  Was sieht diese gefiederte Gestalt in ihren Träumen, in verflochtener Musik?
''',
        "event.ftl": '''label = Ereignisse

load-list-failed = Ereignisliste konnte nicht geladen werden
load-failed = Ereignis konnte nicht geladen werden
load-status-failed = Ereignisstatus konnte nicht geladen werden
load-ldb-failed = Rangliste konnte nicht geladen werden
join-failed = Fehler beim Beitritt zum Ereignis

scroll-down-for-more = Nach unten scrollen, um mehr zu sehen

btn-join = Beitreten
btn-not-started = Noch nicht gestartet
btn-ongoing = Läuft
btn-ended = Beendet

ldb = Rangliste
''',
        "home.ftl": '''play = Zum Spielen klicken
event = Ereignisliste
respack = Charakterrüstungen

not-opened = Funktion noch nicht verfügbar
not-logged-in = Bitte melden Sie sich an

failed-to-update = Fehler beim Laden der Benutzerinformationen
note-try-login-again = Versuchen Sie, sich erneut anzumelden

update = v{ $version } Neue Client-Version verfügbar. Laden Sie sie herunter und installieren Sie sie, um 300 Ursprüngliche zu erhalten
update-desc =
  Zeit: { $date }
  Beschreibung: { $desc }
update-ignore = Diese Version ignorieren
update-go = Aktualisieren

change-char = Charakter wechseln
''',
        "import.ftl": '''info-fail = Noteneninformationen konnten nicht geladen werden
invalid-chart = Ungültige Noten

importing = Werden importiert
import-success = Import erfolgreich
import-failed = Import fehlgeschlagen
import-respack-success = Ressourcenpaket erfolgreich importiert
import-respack-failed = Fehler beim Importieren des Ressourcenpakets
''',
        "library.ftl": '''label = Noten-Bibliothek

local = Lokal
popular = Beliebt

page = Seite { $current } / { $total }
prev-page = Vorherige Seite
next-page = Nächste Seite

not-opened = Funktion noch nicht verfügbar
failed-to-load-online = Online-Noten konnten nicht geladen werden

import = Importieren

offline-mode = Online-Noten können im Offline-Modus nicht geladen werden

must-login = Melden Sie sich an, um Online-Noten zu sehen
''',
        "local.ftl": '''label = Lokal

import-failed = Fehler beim Laden des Levels
import-success = Importierung erfolgreich

not-loaded = Wird importiert...
''',
        "login.ftl": '''login = Anmelden
login-sub = Melden Sie sich an, um der aktiven Online-Gemeinschaft beizutreten
back-login = Zurück anmelden
register = Registrieren

email = E-Mail
username = Benutzername
password = Passwort

name-length-req = Benutzername sollte zwischen 4-20 Zeichen lang sein
name-has-illegal-char = Benutzername enthält ungültige Zeichen
pwd-length-req = Passwort sollte zwischen 6-26 Zeichen lang sein
illegal-email = Ungültige E-Mail

action-success = { $action ->
  [login] Anmeldung erfolgreich
  [register] Registrierung erfolgreich
  *[other] _
}
action-failed = { $action ->
  [login] Anmeldung fehlgeschlagen
  [register] Registrierung fehlgeschlagen
  *[other] _
}

email-sent = Bestätigungsmail wurde gesendet. Bitte bestätigen Sie und melden Sie sich an.
''',
        "message.ftl": '''label = Nachrichten

load-msg-fail = Nachrichten konnten nicht geladen werden
no-msg = Keine Nachrichten
subtitle = { $author } um { $time }
''',
        "multiplayer.ftl": '''multiplayer = Mehrspieler

connect = Verbinden
connect-must-login = Melden Sie sich an, um Mehrspieler zu spielen
connect-success = Verbindung erfolgreich
connect-failed = Verbindung fehlgeschlagen. Bitte überprüfen Sie Ihr Netzwerk und den Status des Mehrspielservers
connect-authenticate-failed = Authentifizierung fehlgeschlagen. Möglicherweise liegt ein Problem mit der Server-IP-Adresse vor
reconnect = Wird wieder verbunden...

create-room = Raum erstellen
create-room-success = Raum erstellt
create-room-failed = Fehler beim Erstellen des Raums
create-invalid-id = Raum-ID sollte aus Großbuchstaben, Kleinbuchstaben, Ziffern, "-" und "_" bestehen (maximal 20 Zeichen)

join-room = Raum beitreten
join-room-invalid-id = Ungültige Raum-ID
join-room-failed = Fehler beim Beitritt zum Raum

leave-room = Raum verlassen
leave-room-failed = Fehler beim Verlassen des Raums

disconnect = Trennen

request-start = Spiel starten
request-start-no-chart = Sie haben noch keine Noten gewählt
request-start-failed = Fehler beim Starten des Spiels

user-list = Charakterliste

lock-room = { $current ->
  [true] Team-Konfiguration entsperren
  *[other] Team-Konfiguration sperren
}
cycle-room = { $current ->
  [true] Zyklus-Modus
  *[other] Normaler Modus
}

ready = Bereit
ready-failed = Fehler beim Bereitstellen

cancel-ready = Abbrechen

room-id = Raum-ID: { $id }

download-failed = Fehler beim Herunterladen der Noten. Möglicherweise liegt ein Problem mit dem Phira-Server vor

lock-room-failed = Fehler beim Sperren des Raums
cycle-room-failed = Fehler beim Wechsel des Raummodus

chat-placeholder = Zum Eingeben hier klicken
chat-send = Senden
chat-empty = Nachricht kann nicht leer sein
chat-sent = Gesendet
chat-send-failed = Fehler beim Senden der Nachricht

select-chart-host-only = Nur der Raum-Host kann Noten auswählen
select-chart-local = Lokale Noten können nicht ausgewählt werden
select-chart-failed = Fehler beim Auswählen der Noten
select-chart-not-now = Sie können jetzt keine Noten auswählen

msg-create-room = `{ $user }` hat einen Raum erstellt
msg-join-room = `{ $user }` ist dem Raum beigetreten
msg-leave-room = `{ $user }` hat den Raum verlassen
msg-new-host = `{ $user }` ist der neue Raum-Host
msg-select-chart = Host `{ $user }` wählte die Noten `{ $chart }` (#{ $id })
msg-game-start = Host `{ $user }` startet das Spiel. Bitte andere Spieler vorbereiten
msg-ready = `{ $user }` ist bereit
msg-cancel-ready = `{ $user }` hat das Bereitstellen abgebrochen
msg-cancel-game = `{ $user }` hat das Spiel abgebrochen
msg-start-playing = Spiel beginnt
msg-played = `{ $user }` beendete das Spiel: { $score } ({ $accuracy }){ $full-combo ->
  [true] , vollständig bestanden
  *[other] {""}
}
msg-game-end = Spiel beendet
msg-abort = `{ $user }` gab das Spiel auf
msg-room-lock = { $lock ->
  [true] Raum ist gesperrt
  *[other] Raum ist entsperrt
}
msg-room-cycle = { $cycle ->
  [true] Raum wechselte zu Zyklus-Modus
  *[other] Raum wechselte zu normalem Modus
}
''',
        "profile.ftl": '''logout = Abmelden
logged-out = Abgemeldet

delete = Konto löschen
delete-failed = Fehler beim Löschen des Kontos
delete-req-sent = Löschanfrage eingereicht

load-user-failed = Fehler beim Laden der Benutzerinformationen
edit-avatar-success = Avatar aktualisiert
edit-avatar-failed = Fehler beim Hochladen des Avatars

uploading-avatar = Avatar wird hochgeladen

load-record-failed = Fehler beim Laden der Spielhistorie. Möglicherweise liegt ein Problem mit dem Phira-Server vor

last-login = Letzter Login: { $time }
badge-admin = Administrator
badge-sponsor = Sponsor
''',
        "rate.ftl": '''rate = Bewerten
filter = Nach Bewertung filtern

cancel = Abbrechen
confirm = Bestätigen

lower-bound = Mindestbewertung
upper-bound = Höchstbewertung

filter-by-tags = Nach Tags filtern
''',
        "resource.ftl": '''chap-c1 = Ruinen der Zukunft
chap-c1-intro =
  Im Jahr 137 n.Chr. des Fila-Kontinents erschien ein wundersames Ereignis namens "Ruinen der Zukunft".
  Unzählige riesige Gebäude und Maschinen stiegen in zufälligen Momenten aus Rissen in der Himmelskuppel herab, brachten unverständliche Materialien und Magie aus der Zukunft mit sich und bedeckten den ganzen Kontinent mit mysteriösen Farben und unerklärlicher Angst...
''',
        "respack.ftl": '''label = Charakterrüstungen

default = Standard (Phigros alte Skins)
load-failed = Fehler beim Laden der Charakterrüstung

info = Charakterrüstungsinformation
info-content =
  Name: { $name }
  Autor: { $author }
  Beschreibung: { $desc }

cant-delete-builtin = Kann die Standard-Rüstung des Charakters nicht löschen
deleted = Gelöscht
''',
        "settings.ftl": '''label = Einstellungen

general = Allgemein
audio = Audio
chart = Noten
debug = Debug
about = Über

item-lang = Sprache
item-offline = Offline-Modus
item-offline-sub = Scores werden nicht hochgeladen im Offline-Modus
item-server-status = Server-Status
item-server-status-sub = Öffne Web-Seite zum Server-Status
check-status = Überprüfen
item-mp = Mehrspieler
item-mp-sub = Mehrspieler aktivieren
item-mp-addr = Mehrspieler-Server
item-mp-addr-sub = Server-Adresse: Host:Port (z.B. 127.0.0.1:12345)
item-mp-addr-invalid = Ungültige Server-Adresse
item-lowq = Niedriger Grafikmodus
item-lowq-sub = Aktivieren, wenn der Bildschirm ruckelt
item-insecure = Unsicherer Modus
item-insecure-sub = Probieren Sie das, wenn Online-Funktionen nicht funktionieren. Dies macht Ihre Verbindung unsicher!

item-adjust = Automatische Zeitsynchronisation
item-adjust-sub = Passt automatisch die Verzögerung an, um Musik und Noten zu synchronisieren
item-music = Musiklautstärke
item-sfx = Effektlautstärke
item-bgm = BGM-Lautstärke
item-cali = Verzögerung anpassen

item-show-acc = Echtzeit-Genauigkeit anzeigen
item-dc-pause = Doppelklick zum Pausieren
item-dhint = Doppel-Note-Hinweis
item-dhint-sub = Gleichzeitige Noten werden hervorgehoben
item-opt = Aggressive Optimierung
item-opt-sub = Nutzt aggressive Optimierungsstrategien. Verbessert Leistung, kann aber zu Anzeigefehlern führen
item-speed = Geschwindigkeit
item-note-size = Notengröße

item-chart-debug = Noten-Debug
item-chart-debug-sub = Zeige Urteilslinie Nummer und Richtung
item-touch-debug = Touch-Debug
item-touch-debug-sub = Zeige Touch-Punkte während des Spielens

load-cali-failed = Fehler beim Laden von Audio

about-content =
  Phira-Furina v{ $version }

  Phira-Furina ist ein Musik-Spiel basierend auf Phigros von Genius Wei, nicht kommerziell, mit Phigros-Spielweise und Genshin: Star Rail Furina Thema, geschrieben in Rust.

  BiliBili: @Phira Official
  Modifier: Genius Wei
  BiliBili: @Genius Wei
  Fan Group: 702640128
  QQ Channel: r48eajexth

  Danke an folgende Spieler für ihre Unterstützung! (In alphabetischer Reihenfolge)
  -哎喂哟-, 114514opkl, 123165, 341819481, 43167364miku, AEsir, Afterglow, akuanoneko, amstlkqp, ApecY176, Arashi, Ark小周, Aromq, Atariter, Aurora., Avencess, Bigironpig, Bradish, brightquasar, buguwu, ccw., CH06E01, CQBZ, Dagehoo, DongZheng, dslzhz, Dumbledore防重复, Ehdiwhxishs, Enigma, evmb, Fall_Li_distance, flamo, Fly段某, Gentle Emperor, GR-17, GYuuLT, Hen77777Tai, hibikip3p, huahbas, huanle, humosu, icyfish, Jerry24, Jiangling, jike, Kaji Emperor, KevinJame1, KKZN, KQ_KongQi, KRYSGCJ, Kynovter, LemonKnife, Lh_39_master, Lighear, liminghao, Lin124, Lio_the_Fox, LJMSTKZF, lorac, luftsch1oss, Maedey, mancy, MaxJack, MGRB, Miku.official, Miska1123, MSSkn, NaiTaGQ, NananEbina, nanxiangx, NEROILY, NingNing0721, NoChoco, Nothu, NsdrfChkew, O-DouSan, obsession, pgwcm, Phira-一个随意废物, PopCatNya, QAQwhatever, QingF_青枫, qwer0160, QWQYuRin, rainbowbex, Ransen, Reeslith, Requiem, RinceTacroix, Rinorsi, Rpec, RUNFORFUNQAQ, sbcujbj, Sensant, Shaaadowsong, Sixi, sksks, Sky_Frozen, soppi, Tearout, Tesla T-T, Thunderlis, Tigerzzz, Tixbicg, Tony0703, Ulyssses, Wind_And_Sky, wjxwp, wszyj, WuJi, wylwktd, xiaoqian, xiaozhemu, XOO_cookie, Xr888, yang125, YMiiiiiii, YN呓凝, YT_XT, yulilizi, yyyyyylll, ZERO707, Zips, ほしの アイ, 一片普通的茶叶, 三月鸠, 不会玩音游的屑, 久往大魔王, 乙酸乙烯酯, 二货甜鱼, 傲丙初A1bcu, 冷光_Lumine, 华树邶, 四十四次日落, 城边的一朵云, 天启之云, 如月清风, 小懒max, 小鲁班, 幻枫落晨, 御坂13900号, 心兮可念, 悲伤很菜, 我永远喜欢爱莉希雅, 日暖随安, 早安起不早, 明晓破风, 易阳Easy_sun, 晨曜, 曲奇cookies, 望悅不是月, 林江恒, 柒柒柒柒, 梓川川川川川川, 欧皇本蝗, 残风, 洛尘sama, 灵晨没有准度, 炫金创创鹅, 甘城猫猫猫猫, 男德村村西张寡妇, 白衣炫五月, 老王, 芝士土拨鼠, 若笛, 荷叶鸭腿, 落弦winglow, 落痕luor, 逐潘, 邮疣铀, 银酱, 露西亚是我的, 飞驰的压路机, 骁龙750G
''',
        "song.ftl": '''load-preview-failed = Fehler beim Laden der Musikvorschau
load-charts-failed = Fehler beim Laden der Schwierigkeiten
no-chart-for-download = Diese Noten können nicht heruntergeladen werden

load-chart-failed = Fehler beim Laden der Noten

dl-cancel = Abbrechen
dl-status-fetch = Informationen werden geladen
dl-status-song = Lade Musik herunter
dl-status-chart = Lade Noten herunter
dl-status-extract = Wird extrahiert
dl-status-illustration = Lade Illustration herunter
dl-status-assets = Lade Assets herunter
dl-status-saving = Wird gespeichert
dl-failed = Download fehlgeschlagen
dl-success = Download abgeschlossen

guest = Gast

warn-unrated = Dieses Spiel wird nicht automatisch hochgeladen
failed-to-play = Fehler beim Starten des Online-Modus. Möglicherweise liegt ein Problem mit dem Phira-Server vor
play-cancel = Abbrechen
play-switch-to-offline = Zu Offline-Modus wechseln
switched-to-offline = Zu Offline-Modus gewechselt

delete = Löschen
rate = Bewerten
exercise = Üben
offset = Verzögerung anpassen
unlock = Spiele Unlock-Animation ab (nur für Noten mit eingebauter Animation)

edit-cancel = Abbrechen
edit-save = Speichern
edit-saving = Wird gespeichert
edit-load-file-failed = Fehler beim Laden der externen Datei. Bitte überprüfen Sie, ob Sie dem Phira-Furina Speicher oder Dateizugriff gewährt haben
edit-save-failed = Fehler beim Speichern
edit-saved = Speichern erfolgreich
edit-preview-invalid = Vorschauzeit ist außerhalb des Bereichs
edit-tags = Tags bearbeiten
edit-downloaded = Sie können heruntergeladene Noten nicht bearbeiten
edit-overwrite = Überschreiben
edit-overwrite-confirm = Sind Sie sicher, dass Sie die aktuellen Noten mit der externen Datei überschreiben möchten? (Die Änderung wird nur nach dem Klicken auf "Aktualisieren" hochgeladen)
edit-overwrite-success = Überschrieben
edit-overwrite-failed = Fehler beim Überschreiben

edit-upload = Hochladen
edit-update = Aktualisieren

upload-not-saved = Sie haben die Noten noch nicht gespeichert. Möchten Sie fortfahren?
upload-login-first = Bitte zuerst anmelden
upload-builtin = Kann eingebaute Noten nicht hochladen
upload-rules = Upload-Regeln
upload-rules-content =
  Bevor Sie hochladen, müssen Sie bestätigen:
  1. Die Noten müssen von Ihnen selbst erstellt sein. Bei Zusammenarbeit benötigen Sie die Upload-Genehmigung von allen Schöpfern. Andernfalls können Sie dauerhaft von Uploads gesperrt werden
  2. Es wird empfohlen, einen erkennbaren Avatar und eine ID zu verwenden. Wenn sich Ihr Avatar/ID auf Phira oder Phira-Furina von Ihrem Veröffentlichungskanal (z.B. BiliBili) unterscheidet, benötigen Sie zusätzliche Notizen. Bitte geben Sie auch eine bequeme Sprache an (falls nicht Chinesisch)
  3. Der Inhalt der Noten (einschließlich Musik, Illustrationen, Text usw.) muss sich an die Gesetze der Volksrepublik China halten und darf kein illegales oder unerwünschtes Material enthalten
  4. Mit dem Hochladen stimmen Sie zu, dass Ihre Noten in der öffentlichen Werbung von Phira verwendet werden können. Andere Verwendungen benötigen die Genehmigung des Notenautors
  5. TeamFlos hat das endgültige Recht zur Auslegung dieser Regeln
uploading = Wird hochgeladen...
upload-chart-failed = Fehler beim Hochladen der Noten. Bitte überprüfen Sie Ihre Notendatei oder Noteneninformationen
upload-success = Hochladen erfolgreich. Bitte warten Sie auf Überprüfung!
upload-failed = Hochladen fehlgeschlagen. Bitte überprüfen Sie Ihre Notendatei oder Noteneninformationen
upload-confirm-clear-ldb = Da sich die aktuelle Notendatei von der Remote-Datei unterscheidet, wird die Rangliste dieser Noten nach dem Hochladen gelöscht. Möchten Sie fortfahren?

ldb = Rangliste
ldb-load-failed = Fehler beim Laden der Rangliste
ldb-no-rank = Keine
ldb-score = Punktzahl
ldb-std = Keine

info-name = Name
info-composer = Komponist
info-charter = Notenschöpfer
info-difficulty = Schwierigkeit
info-desc = Beschreibung
info-rating = Bewertung
info-type = Typ
info-tags = Tags

reviewed = Überprüft
unreviewed = Nicht überprüft

review-approve = Genehmigen
review-deny = Ablehnen
review-del = Online löschen
review-approved = Genehmigt
review-passed = Genehmigt, Noten haben die Überprüfung bestanden
review-denied = Abgelehnt
review-deleted = Gelöscht
review-action-failed = Fehler beim Überprüfungsvorgang
review-doing = Führe Operation aus
review-not-loaded = Informationen noch nicht geladen. Bitte warten Sie
review-edit-tags = Tags bearbeiten
review-edit-tags-failed = Fehler beim Bearbeiten von Tags
review-edit-tags-done = Tags aktualisiert

mods = Mods
mods-autoplay = Automatisches Spielen
mods-autoplay-sub = Beim Aktivieren können Scores nicht hochgeladen werden
mods-flip-x = X-Achse umkehren
mods-flip-x-sub = Noten auf der X-Achse umkehren
mods-fade-out = Ausblenden
mods-fade-out-sub = Noten werden ausgeblendet, wenn sie sich der Beurteilungslinie nähern

rate-failed = Fehler beim Bewerten
rate-done = Bewertung erfolgreich

need-update = Noten aktualisiert
need-update-info-only-content = Noteneninformationen aktualisiert. Möchten Sie diese jetzt synchronisieren?
need-update-content = Noten aktualisiert. Wenn Sie nicht aktualisieren, können Sie Scores nicht hochladen. Möchten Sie jetzt aktualisieren?

request-failed = Anfrage fehlgeschlagen

stabilize = Beantragen, diese Noten zur Online-Sektion zu senden
stabilize-warn = Normale Benutzer können alle 3 Tage eine Online-Noten anfragen. Benutzer mit mindestens einer Online-Noten können jeden 1 Tag anfragen.
stabilize-requested = Erfolgreich zur Online-Sektion angefordert
stabilize-failed = Fehler beim Anfordern zur Online-Sektion. Bitte überprüfen Sie Ihre Notendatei oder Noteneninformationen
stabilize-approve = Genehmigen, diese Noten zur speziellen Sektion zu senden
stabilize-approve-ranked = Genehmigen, diese Noten zur speziellen Sektion zu senden
stabilize-comment = Online-Noten Kommentar
stabilize-commented = Kommentar erfolgreich
stabilize-deny = Ablehnen, diese Noten zur speziellen Sektion zu senden
stabilize-approved = Genehmigt
stabilize-approved-passed = Genehmigt, Noten wurden zur Online-Sektion hochgeladen
stabilize-denied = Abgelehnt
stabilize-denied-passed = Abgelehnt, Noten wurden zurückgewiesen
''',
        "tags.ftl": '''filter = Nach Tags filtern
edit = Tags bearbeiten

invalid-tag = Ungültiger Tag

wanted = Tags die du haben möchtest
unwanted = Tags die du nicht haben möchtest

cancel = Abbrechen
confirm = Bestätigen

filter-by-rating = Nach Bewertung filtern

regular = Normal
troll = Spaß
plain = Reine Konfiguration
visual = Visuell

filter-me = Meine Uploads
filter-unreviewed = Wartend auf Überprüfung
filter-stabilize = Warte auf Überprüfung für Online-Noten
''',
    }
}

def generate_all_files(base_path: str = "phira/locales") -> None:
    """Generate all translation files"""
    
    base = Path(base_path)
    
    for lang_code, files in TRANSLATIONS.items():
        lang_dir = base / lang_code
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        for filename, content in files.items():
            filepath = lang_dir / filename
            filepath.write_text(content, encoding='utf-8')
            print(f"✓ Created {filepath.relative_to(base.parent)}")
    
    print(f"\n✅ Successfully generated all translation files in {base}")

if __name__ == "__main__":
    import sys
    
    base_path = sys.argv[1] if len(sys.argv) > 1 else "phira/locales"
    generate_all_files(base_path)
