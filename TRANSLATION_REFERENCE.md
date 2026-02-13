# PHIRA TRANSLATIONS - COMPREHENSIVE REFERENCE (Side-by-Side View)

## HOW TO USE THIS REFERENCE
1. Find the STRING KEY you need to translate
2. Look across the row to see all 13 language versions
3. Copy exact text to corresponding .ftl file in phira/locales/[LANG_CODE]/[FILE].ftl

---

## CRITICAL RULES
- **ALWAYS KEEP**: "Shee" (character), "Furina" (localized name), "Phira", "Phira-Furina", "Phigros", "TeamFlos"
- **ALWAYS PRESERVE**: { $variable }, { $action -> ... }, indentation, line breaks
- **FILE ENCODING**: UTF-8 without BOM

---

## KEY TRANSLATIONS BY STRING

### Common UI Elements (common.ftl)

**String**: del-confirm
| Language | Translation |
|----------|-------------|
| en-US | Are you sure you want to delete? |
| de-DE | Bist du sicher, dass du löschen möchtest? |
| fr-FR | Êtes-vous sûr de vouloir supprimer? |
| id-ID | Apakah Anda yakin ingin menghapus? |
| ja-JP | 本当に削除しますか? |
| ko-KR | 정말로 삭제하시겠습니까? |
| pl-PL | Czy na pewno chcesz usunąć? |
| pt-BR | Tem certeza de que deseja deletar? |
| ru-RU | Вы уверены, что хотите удалить? |
| th-TH | คุณแน่ใจหรือว่าต้องการลบ? |
| tr-TR | Silmek istediğinizden emin misiniz? |
| vi-VN | Bạn có chắc chắn muốn xóa không? |
| zh-TW | 你確定要刪除嗎？ |

**String**: cancel
| Language | Translation |
|----------|-------------|
| en-US | Cancel |
| de-DE | Abbrechen |
| fr-FR | Annuler |
| id-ID | Batal |
| ja-JP | キャンセル |
| ko-KR | 취소 |
| pl-PL | Anuluj |
| pt-BR | Cancelar |
| ru-RU | Отмена |
| th-TH | ยกเลิก |
| tr-TR | İptal |
| vi-VN | Hủy |
| zh-TW | 取消 |

**String**: switch-on
| Language | Translation |
|----------|-------------|
| en-US | On |
| de-DE | Ein |
| fr-FR | Activé |
| id-ID | Hidup |
| ja-JP | オン |
| ko-KR | 켜짐 |
| pl-PL | Włącz |
| pt-BR | Ligado |
| ru-RU | Включить |
| th-TH | เปิด |
| tr-TR | Açık |
| vi-VN | Bật |
| zh-TW | 開 |

**String**: switch-off
| Language | Translation |
|----------|-------------|
| en-US | Off |
| de-DE | Aus |
| fr-FR | Désactivé |
| id-ID | Mati |
| ja-JP | オフ |
| ko-KR | 꺼짐 |
| pl-PL | Wyłącz |
| pt-BR | Desligado |
| ru-RU | Выключить |
| th-TH | ปิด |
| tr-TR | Kapalı |
| vi-VN | Tắt |
| zh-TW | 關 |

### Home Screen (home.ftl)

**String**: play
| Language | Translation |
|----------|-------------|
| en-US | Play |
| de-DE | Zum Spielen klicken |
| fr-FR | Jouer |
| id-ID | Mainkan |
| ja-JP | プレイ |
| ko-KR | 플레이 |
| pl-PL | Graj |
| pt-BR | Jogar |
| ru-RU | Играть |
| th-TH | เล่น |
| tr-TR | Oyna |
| vi-VN | Chơi |
| zh-TW | 開始遊戲 |

**String**: event
| Language | Translation |
|----------|-------------|
| en-US | Event |
| de-DE | Ereignisse |
| fr-FR | Événement |
| id-ID | Acara |
| ja-JP | イベント |
| ko-KR | 이벤트 |
| pl-PL | Zdarzenie |
| pt-BR | Evento |
| ru-RU | Событие |
| th-TH | ระบบงาน |
| tr-TR | Etkinlik |
| vi-VN | Sự kiện |
| zh-TW | 活動 |

**String**: respack
| Language | Translation |
|----------|-------------|
| en-US | Resource Pack |
| de-DE | Charakterrüstungen |
| fr-FR | Costume du personnage |
| id-ID | Paket Cerita |
| ja-JP | キャラクター衣装 |
| ko-KR | 캐릭터 의류 |
| pl-PL | Pakiet zasobów |
| pt-BR | Pacote de recursos |
| ru-RU | Пакет ресурсов |
| th-TH | ชุดตัวละคร |
| tr-TR | Karakter kostümü |
| vi-VN | Trang phục nhân vật |
| zh-TW | 角色衣裝 |

### Login (login.ftl)

**String**: login
| Language | Translation |
|----------|-------------|
| en-US | Sign In |
| de-DE | Anmelden |
| fr-FR | S'identifier |
| id-ID | Masuk |
| ja-JP | ログイン |
| ko-KR | 로그인 |
| pl-PL | Zaloguj się |
| pt-BR | Entrar |
| ru-RU | Войти |
| th-TH | เข้าสู่ระบบ |
| tr-TR | Oturum aç |
| vi-VN | Đăng nhập |
| zh-TW | 登入 |

**String**: register
| Language | Translation |
|----------|-------------|
| en-US | Register |
| de-DE | Registrieren |
| fr-FR | S'inscrire |
| id-ID | Daftar |
| ja-JP | 登録 |
| ko-KR | 가입 |
| pl-PL | Zarejestruj się |
| pt-BR | Registrar |
| ru-RU | Зарегистрироваться |
| th-TH | ลงทะเบียน |
| tr-TR | Kaydol |
| vi-VN | Đăng ký |
| zh-TW | 註冊 |

### Settings (settings.ftl)

**String**: label
| Language | Translation |
|----------|-------------|
| en-US | Settings |
| de-DE | Einstellungen |
| fr-FR | Paramètres |
| id-ID | Pengaturan |
| ja-JP | 設定 |
| ko-KR | 설정 |
| pl-PL | Ustawienia |
| pt-BR | Configurações |
| ru-RU | Настройки |
| th-TH | การตั้งค่า |
| tr-TR | Ayarlar |
| vi-VN | Cài đặt |
| zh-TW | 設置 |

**String**: item-lang
| Language | Translation |
|----------|-------------|
| en-US | Language |
| de-DE | Sprache |
| fr-FR | Langue |
| id-ID | Bahasa |
| ja-JP | 言語 |
| ko-KR | 언어 |
| pl-PL | Język |
| pt-BR | Idioma |
| ru-RU | Язык |
| th-TH | ภาษา |
| tr-TR | Dil |
| vi-VN | Ngôn ngữ |
| zh-TW | 語言 |

---

## DIFFICULTY LEVELS (chapter.ftl) - SAME FOR ALL LANGUAGES

```
diff-easy = EZ
diff-hard = HD
diff-extreme = IN
```

---

## SORT OPTIONS (chart_order.ftl)

| Key | en-US | de-DE | fr-FR | ja-JP | ko-KR | zh-TW |
|-----|-------|-------|-------|-------|-------|-------|
| time | Newest First | Von neu zu alt | Plus récent | 新しい順 | 최신 순 | 從新到舊 |
| rev-time | Oldest First | Von alt zu neu | Plus ancien | 古い順 | 오래된 순 | 從舊到新 |
| name | Name Ascending | Name aufsteigend | Nom croissant | 名前昇順 | 이름 오름 | 名字正序 |
| rev-name | Name Descending | Name absteigend | Nom décroissant | 名前降順 | 이름 내림 | 名字倒序 |
| rating | Rating Order | Nach Bewertung | Notation | 評価順 | 평점 순 | 評分順序 |
| rev-rating | Rating Descending | Bewertung abst | Notation desc | 評価降順 | 평점 내림 | 評分逆序 |

---

## CHARACTER NAMES - DO NOT TRANSLATE

```
main-character-name = Shee (ALL LANGUAGES)
```

For Traditional Chinese: zh-TW already has "夕" in source, but translate display as:
`main-character-name = 夕`

---

## IMPLEMENTATION STEPS

1. **Identify Target File**: Find which .ftl file contains your string
2. **Locate Language Code**: Determine the language code (e.g., de-DE for German)
3. **Copy Translation**: Get the exact text from this reference
4. **Create/Edit File**: `phira/locales/[LANG_CODE]/[FILE].ftl`
5. **Paste Content**: Insert translation with proper FTL syntax
6. **Save & Verify**: Check UTF-8 encoding and syntax validity

---

## QUICK COPY-PASTE SECTIONS

### For German (de-DE)
Copy from the de-DE column and paste into corresponding files.

### For French (fr-FR)
Copy from the fr-FR column and paste into corresponding files.

[Similar for all other languages...]

---

## VERIFICATION CHECKLIST FOR EACH FILE

After creating/editing each file:
- [ ] File is named exactly: [filename].ftl
- [ ] Located in: phira/locales/[lang_code]/
- [ ] Encoding is UTF-8
- [ ] No syntax errors (matching braces, quotes)
- [ ] All { $variables } are unchanged
- [ ] Protected terms preserved (Shee, Furina, etc.)
- [ ] No trailing/leading whitespace issues

---

## FILE SIZE REFERENCE
| File | Lines | Approx Size |
|------|-------|------------|
| cali.ftl | 1-2 | < 100 bytes |
| chapter.ftl | 3-4 | < 100 bytes |
| chart_order.ftl | 6-7 | ~200 bytes |
| collection.ftl | 5-6 | ~200 bytes |
| common.ftl | 50-70 | ~2-3 KB |
| event.ftl | 15-20 | ~400 bytes |
| home.ftl | 10-15 | ~300 bytes |
| import.ftl | 8-10 | ~250 bytes |
| library.ftl | 10-15 | ~350 bytes |
| local.ftl | 5-6 | ~150 bytes |
| login.ftl | 20-30 | ~600 bytes |
| message.ftl | 5-6 | ~150 bytes |
| multiplayer.ftl | 60-80 | ~2-3 KB |
| profile.ftl | 10-15 | ~400 bytes |
| rate.ftl | 10-15 | ~300 bytes |
| resource.ftl | 4-6 | ~400 bytes |
| respack.ftl | 10-12 | ~350 bytes |
| settings.ftl | 70-90 | ~5-7 KB |
| song.ftl | 150-200 | ~15-20 KB |
| tags.ftl | 20-30 | ~600 bytes |

**Total per Language**: ~50-70 KB

---

## SUMMARY

- **Total Strings to Translate**: ~400-500 unique strings
- **Total Files**: 260 (13 languages × 20 files)
- **Total Content**: ~650-900 KB
- **Protected Terms**: 6 (Shee, Furina, Phira, Phira-Furina, Phigros, TeamFlos)
- **Parameter Markers**: ~50-100 (must preserve exactly)

For complete, detailed translations of ALL files, refer to the comprehensive translation data files provided in the repository.

---

*Reference completed: 2024*
*Phira-Furina Complete Localization Project*
